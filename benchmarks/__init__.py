"""Executable 10-mode production resilience benchmark mapped to TAXONOMY.md."""

from .resilience_bench import (
    FAILURE_MODES,
    HardenedReferenceAgent,
    NaiveBaselineAgent,
    render_badge_svg,
    run_benchmark,
)

__all__ = [
    "FAILURE_MODES",
    "HardenedReferenceAgent",
    "NaiveBaselineAgent",
    "render_badge_svg",
    "run_benchmark",
]
