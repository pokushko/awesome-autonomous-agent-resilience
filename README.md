# Awesome Autonomous Agent Resilience [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of runtime harnesses, foundational research papers, chaos engineering tools, and architectural patterns for engineering **24/7 fault-tolerant, self-healing, and memory-bounded autonomous AI agents**.

Curated and maintained by **Roman Pokushko** ([@pokushko](https://github.com/pokushko)).

---

## Contents

- [Why Agent Resilience?](#why-agent-resilience)
- [Runtime Harnesses & Resilience Frameworks](#runtime-harnesses--resilience-frameworks)
- [Foundational Research Papers](#foundational-research-papers)
- [Chaos Engineering & Fault Injection](#chaos-engineering--fault-injection)
- [Memory Management & Context Boundedness](#memory-management--context-boundedness)
- [Sandbox Isolation & Execution Security](#sandbox-isolation--execution-security)
- [Benchmarks & Stress-Testing Suites](#benchmarks--stress-testing-suites)
- [Architectural Patterns for 24/7 Survival](#architectural-patterns-for-247-survival)
- [Contributing](#contributing)

---

## Why Agent Resilience?

While demo-grade LLM agents perform well in single-turn scripts, **autonomous agents in production loops fail within hours** due to:
1. **Memory Bloat & OOM:** Context window accumulation and uncollected vector cache exhaustion.
2. **Cascading API Drops:** Gateway timeouts (HTTP 502/503), provider rate limits (HTTP 429), and socket disconnects.
3. **State Corruption:** Process terminations wiping uncommitted in-flight reasoning without atomic transaction recovery.
4. **Adversarial Code Escapes:** Dynamic code interpreters executing malicious or destructive tool mutations.

---

## Runtime Harnesses & Resilience Frameworks

- [AgentBunker](https://github.com/pokushko/agent-bunker) - Enterprise chaos engineering & 24/7 resilience harness for AI agents featuring atomic Write-Ahead Logging (WAL), RSS memory ceiling guards, and tri-state circuit breakers.
- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) - NVIDIA's open-source toolkit for adding programmable safety, security, and operational guardrails to LLM applications.
- [LiteLLM](https://github.com/BerriAI/litellm) - Multi-provider LLM gateway supporting automated fallback cascades, load balancing, exponential backoff, and cooldown periods.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Cyclic state-machine agent framework with built-in persistence, human-in-the-loop pause/resume, and time-travel rollbacks.
- [Temporal](https://github.com/temporalio/temporal) - Durable execution platform ensuring that distributed code workflows execute reliably regardless of server crashes or network partitions.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Microsoft's enterprise orchestrator with native telemetry, retry policies, and structured plugin filters.

---

## Foundational Research Papers

### Self-Healing & Reflexive Loops
- **Reflexion: Language Agents with Verbal Reinforcement Learning** (Shinn et al., NeurIPS 2023) - Demonstrates how autonomous agents can evaluate their own execution failures and record verbal self-reflections to self-heal in future turns. [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)
- **Self-Refine: Iterative Refinement with Self-Feedback** (Madaan et al., NeurIPS 2023) - Framework for autonomous multi-step output verification and deterministic self-correction without external ground-truth labels. [arXiv:2303.17651](https://arxiv.org/abs/2303.17651)
- **Toolformer: Language Models Can Teach Themselves to Use Tools** (Schick et al., NeurIPS 2023) - Self-supervised discovery of when and how to call external APIs, gracefully recovering from failed external invocations. [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

### Memory, Context & Attention Stability
- **Lost in the Middle: How Language Models Use Long Contexts** (Liu et al., TACL 2024) - Analyzes severe performance degradation as input context scales, proving the necessity of bounded episodic memory and context pruning. [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
- **MemGPT: Towards LLMs as Operating Systems** (Packer et al., 2023) - Treats LLM memory like OS virtual memory (RAM vs Disk paging), managing bounded context via automated episodic paging. [arXiv:2310.08560](https://arxiv.org/abs/2310.08560)
- **A-MEM: Agentic Memory with Adaptive Decay & Retrieval** (2024) - Biologically inspired memory architectures combining cosine similarity with exponential recency decay.

---

## Chaos Engineering & Fault Injection

- [Chaos Mesh](https://github.com/chaos-mesh/chaos-mesh) - Cloud-native chaos engineering platform for Kubernetes simulating pod kills, network partitions, and clock skew.
- [Chaos Toolkit](https://github.com/chaostoolkit/chaostoolkit) - Declarative, open-source API for automating chaos experiments and verifying automated recovery hypotheses.
- [Toxiproxy](https://github.com/Shopify/toxiproxy) - TCP proxy for simulating network anomalies (latency, bandwidth limits, peer dropouts) in agent test harnesses.

---

## Memory Management & Context Boundedness

- [agentic-vector-memory](https://github.com/pokushko/agentic-vector-memory) - Dual-store episodic and semantic memory engine with exponential temporal decay $e^{-\lambda \Delta t}$, access-frequency reinforcement, and SQLite ACID persistence.
- [DuckDB](https://github.com/duckdb/duckdb) - High-performance embedded columnar analytical database ideal for local agent audit trails, episodic logs, and telemetry storage.
- [Qdrant](https://github.com/qdrant/qdrant) - High-throughput vector search engine with payload-based filtering, quantization, and disk-backed HNSW indexing.

---

## Sandbox Isolation & Execution Security

- [agent-security-sandbox](https://github.com/pokushko/agent-security-sandbox) - AST-level static code inspector and execution sanitizer preventing prompt injections, dangerous OS imports, and dunder escape exploits.
- [gVisor](https://github.com/google/gvisor) - Google's application kernel written in Go that provides a virtualized container boundary for untrusted LLM-generated code execution.
- [eBPF](https://ebpf.io/) - Linux kernel technology enabling real-time syscall interception and execution sandboxing without modifying host application binaries.

---

## Benchmarks & Stress-Testing Suites

- [SWE-bench](https://github.com/swe-bench/SWE-bench) - Evaluates whether language models can resolve end-to-end software engineering GitHub issues in complex real-world codebases.
- [GAIA: General AI Assistants](https://github.com/huggingface/gaia) - Benchmark evaluating multimodal AI agents on complex, multi-modal tasks requiring persistent tool execution.
- [AgentBench](https://github.com/THUDM/AgentBench) - Multi-dimensional benchmark for evaluating LLMs as agents across 8 distinct operating environments (OS, DB, Web, Knowledge).

---

## Architectural Patterns for 24/7 Survival

### 1. Write-Ahead Logging (WAL) for LLM Reasoning
Never execute multi-step agent actions without committing intent to disk first. If the host machine reboots midway through a turn, the WAL ensures atomic replay or safe rollback:

```
[User Task] ➡️ [WAL Intent: 'Start Step 1'] ➡️ [Tool Execution] ➡️ [WAL Status: 'Success']
```

### 2. Tri-State Circuit Breaker Pattern
Protect agents from cascading thread starvation when upstream LLM APIs or search tools fail:
- **CLOSED:** Normal operations; requests route to the primary API.
- **OPEN:** After $N$ consecutive 503/429 errors, instantly route all calls to a local safe heuristic/offline cache without waiting for timeouts.
- **HALF-OPEN:** Periodically send a single canary probe to test upstream recovery.

### 3. Vectorized Peak Drawdown / Failure Braking
Vectorized threshold accumulation to halt tool invocations when failure rates breach safety ceilings ($S_{\text{fail}} > \theta$), preventing unmonitored financial or operational damage.

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

This work is dedicated to the public domain under the Creative Commons CC0 1.0 Universal License.
