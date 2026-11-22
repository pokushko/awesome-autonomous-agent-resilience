#!/usr/bin/env python3
"""Refresh GitHub star counts and latest push dates in README.md."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

LINE_PATTERN = re.compile(
    r"^(- \[[^\]]+\]\(https://github\.com/([^/\s\)]+/[^/\s\)]+)\) - .+ \()([^,]+),\s*(?:[^,]+,\s*)?(\d{4}-\d{2})(\))$"
)


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


def refresh_readme(readme_path: Path, write: bool) -> int:
    """Update metrics lines in README.md; return count of changed lines."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    original_lines = readme_path.read_text(encoding="utf-8").splitlines(keepends=True)
    updated_lines: list[str] = []
    changes = 0
    warnings = 0

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

        if meta.get("archived"):
            print(f"WARNING: Repository {slug} is now archived!", file=sys.stderr)
            warnings += 1

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

    mode = "updated" if write else "would update"
    print(f"Checked README.md: {changes} line(s) {mode}, {warnings} warning(s).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Update GitHub star and activity metrics in README.md.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="Dry-run without modifying README.md.")
    group.add_argument("--write", action="store_true", help="Write updated metrics back to README.md.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    return refresh_readme(repo_root / "README.md", write=args.write)


if __name__ == "__main__":
    raise SystemExit(main())
