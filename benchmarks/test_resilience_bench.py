"""Pytest verification suite for the F01-F10 Resilience Chaos Benchmark."""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET

from benchmarks.resilience_bench import (
    FAILURE_MODES,
    HardenedReferenceAgent,
    NaiveBaselineAgent,
    main as bench_main,
    render_badge_svg,
    run_benchmark,
)


def test_naive_baseline_scores_zero() -> None:
    report = run_benchmark(NaiveBaselineAgent())
    assert report["total"] == len(FAILURE_MODES) == 10
    assert report["passed"] == 0
    assert report["score"] == 0


def test_hardened_reference_scores_hundred() -> None:
    report = run_benchmark(HardenedReferenceAgent())
    assert report["total"] == 10
    assert report["passed"] == 10
    assert report["score"] == 100
    assert all(r["passed"] for r in report["results"])


def test_svg_badge_is_valid_xml() -> None:
    svg_green = render_badge_svg(100)
    root = ET.fromstring(svg_green)
    assert root.tag.endswith("svg")
    assert "100/100" in svg_green

    svg_red = render_badge_svg(0)
    ET.fromstring(svg_red)
    assert "0/100" in svg_red


def test_cli_compare_writes_json_and_badge(tmp_path) -> None:
    out_json = tmp_path / "bench.json"
    out_svg = tmp_path / "badge.svg"
    rc = bench_main(["--target", "compare", "--json", str(out_json), "--badge", str(out_svg)])
    assert rc == 0

    data = json.loads(out_json.read_text(encoding="utf-8"))
    assert data["reports"][0]["score"] == 0
    assert data["reports"][1]["score"] == 100
    ET.fromstring(out_svg.read_text(encoding="utf-8"))
