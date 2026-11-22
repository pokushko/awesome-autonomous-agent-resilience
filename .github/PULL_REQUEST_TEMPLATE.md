## Summary

<!-- Describe what entry, taxonomy improvement, or benchmark enhancement this PR adds. -->

## Contributor Checklist

- [ ] Entry uses the exact format: `- [Name](https://url) - Concise factual description ending with a period.`
- [ ] Primary source URL resolves with HTTP `200` and is not an archived or unmaintained fork.
- [ ] Passed local `npx --yes awesome-lint README.md` with 0 errors and 0 warnings.
- [ ] If modifying `benchmarks/`, verified `pytest benchmarks/test_resilience_bench.py -v` and `ruff check --select E,F --ignore E501 benchmarks/`.
