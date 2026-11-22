#!/usr/bin/env python3
"""Weekly Freshness Radar: discovers new agent-resilience repos/papers and checks catalog health."""

from __future__ import annotations

import argparse
import concurrent.futures
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from update_metrics import LINE_PATTERN, classify_repo_health, fetch_repo_metadata, format_stars  # noqa: E402

REPO_SLUG = "pokushko/awesome-autonomous-agent-resilience"
RADAR_LABEL = "weekly-radar"

GITHUB_SEARCH_TERMS = [
    '"ai agent" resilience OR fault-tolerant OR durable',
    '"prompt injection" agent OR llm defense OR firewall',
    "mcp security OR sandbox agent",
    'opentelemetry llm OR "agent observability" OR "agent evaluation"',
]

ARXIV_SEARCH_QUERY = (
    'all:("multi-agent" OR "LLM agent") AND '
    'all:("failure" OR "prompt injection" OR "resilience" OR "sandbox" OR "fault")'
)


def extract_existing_identifiers(readme_text: str) -> tuple[set[str], list[str], set[str]]:
    """Return existing GitHub slugs (lowercase set & ordered list) and arXiv IDs in README.md."""
    slugs_seen: set[str] = set()
    for match in re.finditer(r"https://github\.com/([^/\s\)\"']+/[^/\s\)\"']+)", readme_text):
        slug = match.group(1).rstrip(".,;:")
        slugs_seen.add(slug.lower())

    tracked_slugs: list[str] = []
    for raw_line in readme_text.splitlines():
        m = LINE_PATTERN.match(raw_line.rstrip("\r\n"))
        if m:
            tracked_slugs.append(m.group(2))

    arxiv_ids = set(re.findall(r"https://arxiv\.org/abs/(\d{4}\.\d{4,5})", readme_text))
    return slugs_seen, tracked_slugs, arxiv_ids


def clean_sentence(raw_text: str | None, item_name: str = "", max_len: int = 135) -> str:
    """Normalize a candidate description into a clean one-line sentence."""
    text = " ".join((raw_text or "").split()).strip()
    text = re.sub(r"https?://\S+", "", text).strip()
    text = re.sub(r"^[^\w]+", "", text).strip()
    if not text:
        return "Open-source project supporting autonomous AI agent reliability and safety workflows."

    # Avoid starting description with the item name (awesome-lint no-repeat-item-in-description)
    if item_name and text.lower().startswith(item_name.lower()):
        remainder = text[len(item_name):].lstrip(" :-—–,.")
        if remainder:
            text = remainder

    if len(text) > max_len:
        cut = text[: max_len - 3].rsplit(" ", 1)[0].rstrip(",;:- ")
        text = cut if len(cut) >= 30 else text[: max_len - 3].strip()

    text = text.rstrip(".!? ")
    if text:
        text = text[0].upper() + text[1:]
    return f"{text}."


def github_api_json(url: str, token: str | None, method: str = "GET", payload: dict | None = None) -> object:
    """Perform a JSON request against the GitHub REST API."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-autonomous-agent-resilience-radar",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    body = None
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=20) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def scan_existing_repo_health(tracked_slugs: list[str], token: str | None) -> dict[str, list[dict[str, str]]]:
    """Concurrently inspect tracked README GitHub repos for archived, renamed, or stale (>18m) status."""
    now_utc = datetime.now(timezone.utc)
    report: dict[str, list[dict[str, str]]] = {"archived": [], "renamed": [], "stale": []}

    def _inspect(slug: str) -> dict[str, object] | None:
        meta = fetch_repo_metadata(slug, token)
        if meta is None:
            return None
        return classify_repo_health(slug, meta, now_utc=now_utc)

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for res in pool.map(_inspect, tracked_slugs):
            if res is None:
                continue
            slug = str(res["slug"])
            if res["archived"]:
                report["archived"].append({"slug": slug, "url": f"https://github.com/{slug}"})
            if res["renamed"]:
                report["renamed"].append(
                    {"slug": slug, "canonical_full_name": str(res["canonical_full_name"])}
                )
            if res["stale"]:
                report["stale"].append({"slug": slug, "pushed_at": str(res["pushed_at"])})

    return report


def discover_github_candidates(
    existing_slugs: set[str],
    token: str | None,
    limit: int = 8,
) -> list[dict[str, object]]:
    """Query GitHub Search API for active, high-signal repositories missing from README.md."""
    since_date = (datetime.now(timezone.utc) - timedelta(days=90)).strftime("%Y-%m-%d")
    candidates_by_slug: dict[str, dict[str, object]] = {}

    for term in GITHUB_SEARCH_TERMS:
        query = f"{term} pushed:>={since_date} archived:false stars:>=300"
        url = (
            "https://api.github.com/search/repositories?q="
            + urllib.parse.quote(query, safe="")
            + "&sort=stars&order=desc&per_page=15"
        )
        try:
            data = github_api_json(url, token)
        except Exception as exc:
            print(f"WARNING: GitHub search failed for term '{term}': {exc}", file=sys.stderr)
            continue

        items = data.get("items", []) if isinstance(data, dict) else []
        for item in items:
            full_name = str(item.get("full_name", ""))
            lower_slug = full_name.lower()
            topics = [str(t).lower() for t in (item.get("topics") or [])]
            if not full_name or lower_slug in existing_slugs:
                continue
            if item.get("fork") or item.get("archived"):
                continue
            if "awesome" in lower_slug or "awesome" in topics or "awesome-list" in topics:
                continue
            if "interview" in lower_slug or "guide" in str(item.get("name", "")).lower():
                continue
            raw_desc = str(item.get("description") or "")
            # Filter out predominantly CJK descriptions for an English-indexed list
            if sum(1 for ch in raw_desc if "\u4e00" <= ch <= "\u9fff") > 3:
                continue

            stars = int(item.get("stargazers_count", 0))
            if lower_slug not in candidates_by_slug or stars > int(candidates_by_slug[lower_slug]["stars"]):
                candidates_by_slug[lower_slug] = {
                    "name": str(item.get("name", full_name.split("/")[-1])),
                    "full_name": full_name,
                    "url": str(item.get("html_url", f"https://github.com/{full_name}")),
                    "description": clean_sentence(item.get("description"), str(item.get("name", ""))),
                    "stars": stars,
                    "pushed_month": str(item.get("pushed_at", ""))[:7] or datetime.now(timezone.utc).strftime("%Y-%m"),
                }

    ranked = sorted(candidates_by_slug.values(), key=lambda x: int(x["stars"]), reverse=True)
    return ranked[:limit]


def discover_arxiv_candidates(existing_arxiv_ids: set[str], limit: int = 6) -> list[dict[str, str]]:
    """Query arXiv API for recent papers on agent failures, prompt injection, and resilience."""
    url = (
        "https://export.arxiv.org/api/query?search_query="
        + urllib.parse.quote(ARXIV_SEARCH_QUERY, safe="")
        + "&sortBy=submittedDate&sortOrder=descending&max_results=20"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "awesome-autonomous-agent-resilience-radar"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            xml_bytes = resp.read()
    except Exception as exc:
        print(f"WARNING: arXiv search failed: {exc}", file=sys.stderr)
        return []

    root = ET.fromstring(xml_bytes)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    results: list[dict[str, str]] = []

    for entry in root.findall("a:entry", ns):
        id_node = entry.find("a:id", ns)
        title_node = entry.find("a:title", ns)
        summary_node = entry.find("a:summary", ns)
        pub_node = entry.find("a:published", ns)
        if id_node is None or title_node is None:
            continue

        aid = (id_node.text or "").split("/abs/")[-1].split("v")[0].strip()
        if not aid or aid in existing_arxiv_ids:
            continue

        title = " ".join((title_node.text or "").split())
        year = (pub_node.text or "")[:4] if pub_node is not None else datetime.now(timezone.utc).strftime("%Y")
        authors = [a.findtext("a:name", default="", namespaces=ns) for a in entry.findall("a:author", ns)]
        first_last = authors[0].split()[-1] if authors and authors[0].strip() else "Authors"
        label = f"{title} ({first_last} et al., {year})"

        summary_text = " ".join((summary_node.text if summary_node is not None else "").split())
        sentences = re.split(r"(?<=[.!?])\s+", summary_text, maxsplit=1)
        desc = clean_sentence(sentences[0] if sentences else summary_text, title, max_len=155)

        results.append(
            {
                "id": aid,
                "url": f"https://arxiv.org/abs/{aid}",
                "label": label,
                "description": desc,
            }
        )
        if len(results) >= limit:
            break

    return results


def build_issue_markdown(
    health: dict[str, list[dict[str, str]]],
    gh_candidates: list[dict[str, object]],
    arxiv_candidates: list[dict[str, str]],
) -> str:
    """Build the Markdown body for the Weekly Freshness Radar issue."""
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines: list[str] = [
        f"Automated weekly scan executed on **{today_str} (UTC)**.",
        "",
        "## Repository Health Alerts",
        "",
    ]

    has_alerts = any(health[k] for k in ("archived", "renamed", "stale"))
    if not has_alerts:
        lines.append("All listed repositories are active and healthy.")
    else:
        if health["archived"]:
            lines.append("### Archived Repositories")
            for item in health["archived"]:
                lines.append(f"- `{item['slug']}` ({item['url']}) is archived.")
            lines.append("")
        if health["renamed"]:
            lines.append("### Renamed or Redirected Repositories")
            for item in health["renamed"]:
                lines.append(f"- `{item['slug']}` now resolves to `{item['canonical_full_name']}`.")
            lines.append("")
        if health["stale"]:
            lines.append("### Repositories Inactive Over 18 Months")
            for item in health["stale"]:
                lines.append(f"- `{item['slug']}` (last pushed `{item['pushed_at']}`).")
            lines.append("")

    lines.extend(["", "## New High-Signal GitHub Candidates", ""])
    if not gh_candidates:
        lines.append("No new qualifying repositories discovered this week.")
    else:
        for cand in gh_candidates:
            stars_fmt = format_stars(int(cand["stars"]))
            lines.append(
                f"- [{cand['name']}]({cand['url']}) - {cand['description']} "
                f"(research, {stars_fmt}, {cand['pushed_month']})"
            )

    lines.extend(["", "## Recent arXiv Papers", ""])
    if not arxiv_candidates:
        lines.append("No new qualifying arXiv papers discovered this week.")
    else:
        for paper in arxiv_candidates:
            lines.append(f"- [{paper['label']}]({paper['url']}) - {paper['description']} (research)")

    lines.extend(
        [
            "",
            "## Maintainer Checklist",
            "",
            "- [ ] Verify relevance, primary sources, and accurate descriptions before adding any candidate.",
            "- [ ] Run `npx awesome-lint README.md` locally and ensure 0 errors / 0 warnings.",
            "- [ ] Open a PR against `main` so CI (`awesome-lint` + `lychee`) validates all changes before merge.",
            "",
        ]
    )
    return "\n".join(lines)


def ensure_radar_label(token: str) -> None:
    """Create the weekly-radar label if it does not yet exist."""
    url = f"https://api.github.com/repos/{REPO_SLUG}/labels"
    payload = {
        "name": RADAR_LABEL,
        "color": "00F0FF",
        "description": "Automated weekly scan of new agent resilience tools, papers, and catalog health",
    }
    try:
        github_api_json(url, token, method="POST", payload=payload)
    except urllib.error.HTTPError as exc:
        if exc.code != 422:
            raise


def open_weekly_issue(title: str, body: str, token: str) -> str | None:
    """Open a weekly-radar Issue unless an open one already exists from the last 6 days."""
    issues_url = f"https://api.github.com/repos/{REPO_SLUG}/issues?labels={RADAR_LABEL}&state=open&per_page=5"
    existing = github_api_json(issues_url, token)
    now_utc = datetime.now(timezone.utc)
    if isinstance(existing, list):
        for issue in existing:
            created = str(issue.get("created_at", ""))
            if created:
                try:
                    dt = datetime.strptime(created[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
                    if (now_utc - dt) < timedelta(days=6):
                        print(f"Skipping issue creation: open radar issue #{issue.get('number')} created on {created[:10]}.")
                        return None
                except ValueError:
                    pass

    ensure_radar_label(token)
    created_issue = github_api_json(
        f"https://api.github.com/repos/{REPO_SLUG}/issues",
        token,
        method="POST",
        payload={"title": title, "body": body, "labels": [RADAR_LABEL]},
    )
    if isinstance(created_issue, dict):
        return str(created_issue.get("html_url", ""))
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Weekly Freshness Radar for Awesome Autonomous Agent Resilience.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Print Markdown report without opening a GitHub Issue.")
    mode.add_argument("--open-issue", action="store_true", help="Open a weekly GitHub Issue with the scan report.")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if args.open_issue and not token:
        print("ERROR: GITHUB_TOKEN environment variable is required with --open-issue.", file=sys.stderr)
        return 1

    readme_path = SCRIPT_DIR.parent / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")
    existing_slugs, tracked_slugs, existing_arxiv_ids = extract_existing_identifiers(readme_text)

    health = scan_existing_repo_health(tracked_slugs, token)
    gh_candidates = discover_github_candidates(existing_slugs, token)
    arxiv_candidates = discover_arxiv_candidates(existing_arxiv_ids)
    report_md = build_issue_markdown(health, gh_candidates, arxiv_candidates)

    if args.dry_run:
        print(report_md)
        return 0

    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    title = f"Weekly Freshness Radar — {today_str}"
    issue_url = open_weekly_issue(title, report_md, str(token))
    if issue_url:
        print(f"Opened Weekly Freshness Radar issue: {issue_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
