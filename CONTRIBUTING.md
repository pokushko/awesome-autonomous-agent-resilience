# Contributing to Awesome Autonomous Agent Resilience

Contributions that improve the engineering rigor, accuracy, and completeness of this index are welcome! Please follow the guidelines below before opening a Pull Request.

## Submission Guidelines

1. **Focus on Agent Resilience:** Submissions must directly address durable execution, memory boundedness, chaos testing, prompt-injection defense, execution isolation, observability, formal verification, benchmark evaluation, or documented real-world incidents involving autonomous AI agents.
2. **Quality and Maintenance Standards:**
   - Software tools must point to active, non-archived repositories (unless historically seminal and clearly marked) with clear documentation and reproducible behavior.
   - Research entries must cite verified primary publications (e.g., arXiv, peer-reviewed conferences, Zenodo DOI) with accurate author attributions and years.
   - Post-mortems and incidents must link directly to verified primary disclosures, court/tribunal records, CVE advisories, or reputable journalism—no fabricated or unsourced anecdotes.
3. **Standard Formatting Rules:**
   - Format GitHub repositories as:
     `- [Project Name](URL) - Concise one-line description not starting with the item name. (maturity, stars, YYYY-MM)`
   - Format non-GitHub standards, papers, or incidents as:
     `- [Title](URL) - Concise one-line description not starting with the title. (maturity)`
   - Valid maturity tags: `production`, `research`, `standard`, `guide`, `registry`, `incident`, `maintainer's project`, `maintainer's preprint`.
   - Start descriptions with a capitalized word, avoid repeating the project name at the start of the description, and end every bullet item with sentence punctuation (`).` or `.`).
4. **No Duplicate Links:** Each URL may appear only once across `README.md`.
5. **Maintainer Conflict-of-Interest Policy:** Any tool or preprint authored by the maintainer must be placed at the end of its section and tagged explicitly with `maintainer's project` or `maintainer's preprint`.

## Local Validation

Before submitting your PR, run both checks locally:

```bash
npx awesome-lint README.md
python scripts/update_metrics.py --check
```

Please also review the [Code of Conduct](CODE_OF_CONDUCT.md) before participating.
