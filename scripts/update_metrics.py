#!/usr/bin/env python3
"""Refresh GitHub star counts, activity dates, and repository health in README.md."""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request

LINE_PATTERN = re.compile(
    r"^(- \[[^\]]+\]\(https://github\.com/([^/\s\)]+/[^/\s\)]+)\) - .+ \()([^,]+),\s*(?:[^,]+,\s*)?(\d{4}-\d{2})(\))$"
)
STALE_DAYS_THRESHOLD = 548  # ~18 months


def format_stars(count: int) -> str:
    """Format GitHub star count compactly (e.g., 14.9k stars or 558 stars)."""
    if count >= 1000:
        return f"{count / 1000:.1f}k stars"
    return f"{count} stars"


def fetch_repo_metadata(slug: str, token: str | None) -> dict[str, object] | None:
    """Query GitHub REST API for repository stargazers_count, pushed_at, and archived status."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-autonomous-agent-resilience-updater",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(f"https://api.github.com/repos/{slug}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        print(f"WARNING: Failed to fetch {slug}: {exc}", file=sys.stderr)
        return None


def classify_repo_health(
    slug: str,
    meta: dict[str, object],
    now_utc: datetime | None = None,
) -> dict[str, object]:
    """Evaluate archived, renamed, and stale (>18 months) signals for one repository."""
    now = now_utc or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=STALE_DAYS_THRESHOLD)

    full_name = str(meta.get("full_name", slug))
    pushed_raw = str(meta.get("pushed_at", ""))
    pushed_date = pushed_raw[:10]
    is_archived = bool(meta.get("archived"))
    is_renamed = bool(full_name and full_name.lower() != slug.lower())

    is_stale = False
    if len(pushed_date) == 10:
        try:
            pushed_dt = datetime.strptime(pushed_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
            is_stale = pushed_dt < cutoff
        except ValueError:
            is_stale = False

    return {
        "slug": slug,
        "canonical_full_name": full_name,
        "url": f"https://github.com/{slug}",
        "archived": is_archived,
        "renamed": is_renamed,
        "stale": is_stale,
        "pushed_at": pushed_date,
    }


def refresh_readme(
    readme_path: Path,
    write: bool,
    report_json: Path | None = None,
) -> int:
    """Update metrics lines in README.md; optionally emit a JSON health summary."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    original_lines = readme_path.read_text(encoding="utf-8").splitlines(keepends=True)
    updated_lines: list[str] = []
    changes = 0
    warnings = 0

    now_utc = datetime.now(timezone.utc)
    health_report: dict[str, list[dict[str, str]]] = {
        "archived": [],
        "renamed": [],
        "stale": [],
    }

    for raw_line in original_lines:
        ending = "\n" if raw_line.endswith("\n") else ""
        stripped = raw_line.rstrip("\r\n")
        match = LINE_PATTERN.match(stripped)
        if not match:
            updated_lines.append(raw_line)
            continue

        prefix, slug, maturity, _old_date, suffix = match.groups()
        meta = fetch_repo_metadata(slug, token)
        if meta is None:
            updated_lines.append(raw_line)
            warnings += 1
            continue

        status = classify_repo_health(slug, meta, now_utc=now_utc)
        if status["archived"]:
            print(f"WARNING: Repository {slug} is now archived!", file=sys.stderr)
            health_report["archived"].append({"slug": slug, "url": f"https://github.com/{slug}"})
            warnings += 1
        if status["renamed"]:
            canonical = str(status["canonical_full_name"])
            print(f"WARNING: Repository {slug} moved/renamed to {canonical}", file=sys.stderr)
            health_report["renamed"].append({"slug": slug, "canonical_full_name": canonical})
            warnings += 1
        if status["stale"]:
            pushed_at = str(status["pushed_at"])
            health_report["stale"].append({"slug": slug, "pushed_at": pushed_at})

        pushed_month = str(meta.get("pushed_at", ""))[:7] or _old_date
        if slug.lower().startswith("pokushko/") or maturity == "maintainer's project":
            new_line = f"{prefix}{maturity}, {pushed_month}{suffix}{ending}"
        else:
            stars = int(meta.get("stargazers_count", 0))
            new_line = f"{prefix}{maturity}, {format_stars(stars)}, {pushed_month}{suffix}{ending}"

        if new_line != raw_line:
            changes += 1
        updated_lines.append(new_line)

    if write and changes > 0:
        readme_path.write_text("".join(updated_lines), encoding="utf-8")

    if report_json is not None:
        report_json.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "generated_at": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "checked_lines": sum(1 for ln in original_lines if LINE_PATTERN.match(ln.rstrip("\r\n"))),
            "changed_lines": changes,
            **health_report,
        }
        report_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    mode = "updated" if write else "would update"
    print(f"Checked README.md: {changes} line(s) {mode}, {warnings} warning(s).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Update GitHub star and activity metrics in README.md.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="Dry-run without modifying README.md.")
    group.add_argument("--write", action="store_true", help="Write updated metrics back to README.md.")
    parser.add_argument(
        "--report-json",
        type=Path,
        default=None,
        help="Optional path to write archived/renamed/stale repository JSON report.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    return refresh_readme(repo_root / "README.md", write=args.write, report_json=args.report_json)


if __name__ == "__main__":
    raise SystemExit(main())
