# Awesome Autonomous Agent Resilience [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Awesome Autonomous Agent Resilience](assets/awesome_banner.svg)

A curated index of durable execution engines, observability stacks, prompt-injection defenses, execution sandboxes, benchmarks, peer-reviewed research, and documented real-world post-mortems for building **24/7 fault-tolerant, memory-bounded, and self-healing autonomous AI agents**.

See the companion [Agent Failure Taxonomy Matrix and Reference Patterns](TAXONOMY.md) for a 10-mode production failure catalog mapped to MAST and OWASP Agentic Top 10 with Python mitigation patterns, and the [Resilience Chaos Benchmark Suite](benchmarks/README.md) to score agents against `F01–F10`. Maintained by [Roman Pokushko](https://github.com/pokushko) (EvoNova Labs).

## Contents

- [Durable Execution and Agent Runtimes](#durable-execution-and-agent-runtimes)
- [Structured Output and Human-in-the-Loop Controls](#structured-output-and-human-in-the-loop-controls)
- [Observability, Tracing, and Evaluation](#observability-tracing-and-evaluation)
- [Prompt Injection, Guardrails, and Red-Teaming](#prompt-injection-guardrails-and-red-teaming)
- [Sandboxing and Execution Isolation](#sandboxing-and-execution-isolation)
- [Memory Management and Bounded Context](#memory-management-and-bounded-context)
- [Chaos Engineering and Fault Injection](#chaos-engineering-and-fault-injection)
- [Causal Inference and Formal Verification](#causal-inference-and-formal-verification)
- [Multi-Agent Coordination, Debate, and Failure Analysis](#multi-agent-coordination-debate-and-failure-analysis)
- [Benchmarks and Stress-Testing Suites](#benchmarks-and-stress-testing-suites)
- [Research Papers and Engineering Guides](#research-papers-and-engineering-guides)
- [Real-World Incidents and Post-Mortems](#real-world-incidents-and-post-mortems)

## Durable Execution and Agent Runtimes

- [Temporal](https://github.com/temporalio/temporal) - Durable execution platform guaranteeing fault-tolerant completion of distributed workflows across server crashes and network partitions. (production, 24.6k stars, 2026-11)
- [Restate](https://github.com/restatedev/restate) - Resilient distributed execution engine providing event-driven state recovery and idempotent handlers for long-lived agents. (production, 4.7k stars, 2026-11)
- [DBOS](https://github.com/dbos-inc/dbos-transact-py) - Lightweight durable workflow library persisting every agent step and side effect transactionally in PostgreSQL or SQLite. (production, 1.7k stars, 2026-11)
- [Inngest](https://github.com/inngest/inngest) - Event-driven durable workflow platform with per-step retries, concurrency controls, and dead-letter recovery. (production, 6.1k stars, 2026-11)
- [Hatchet](https://github.com/hatchet-dev/hatchet) - Distributed task queue supporting durable execution, rate limiting, DAG dependencies, and failure backoff. (production, 8.3k stars, 2026-11)
- [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) - Open-source background jobs platform supporting checkpointed long-running AI tasks without serverless timeout limits. (production, 16.8k stars, 2026-11)
- [Prefect](https://github.com/PrefectHQ/prefect) - Python workflow orchestration framework offering typed task retries, state caching, and observability hooks. (production, 24.2k stars, 2026-11)
- [Apache Burr](https://github.com/apache/burr) - Lightweight Python state-machine framework tracking application state transitions for resumable decision-making agents. (production, 2.6k stars, 2026-11)
- [LangGraph](https://github.com/langchain-ai/langgraph) - Stateful cyclic graph orchestration library with thread-level checkpointing, human-in-the-loop interrupts, and time-travel debugging. (production, 45.3k stars, 2026-11)
- [LiteLLM](https://github.com/BerriAI/litellm) - Unified LLM gateway and Python SDK providing cross-provider fallback cascades, rate-limit cooldowns, and spend budgets. (production, 63.8k stars, 2026-11)
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - Enterprise AI orchestration SDK featuring telemetry filters, retry policies, and multi-agent runtime abstractions. (production, 28.8k stars, 2026-11)
- [PydanticAI](https://github.com/pydantic/pydantic-ai) - Type-safe Python agent framework enforcing schema validation, model-retry recovery, and OpenTelemetry instrumentation. (production, 21.4k stars, 2026-11)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Lightweight Python runtime for multi-agent handoffs, input/output guardrails, and built-in execution tracing. (production, 30.8k stars, 2026-11)
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) - Official Python SDK for building tool-using agents with structured hooks, permission controls, and bounded turns. (production, 8.6k stars, 2026-11)
- [Google ADK](https://github.com/google/adk-python) - Code-first Python toolkit from Google for building, composing, and evaluating hierarchical multi-agent systems. (production, 22.3k stars, 2026-11)
- [Strands Agents SDK](https://github.com/strands-agents/harness-sdk) - Model-driven Python SDK focused on modular tool orchestration and production lifecycle hooks. (production, 9.3k stars, 2026-11)
- [AgentBunker](https://github.com/pokushko/agent-bunker) - Lightweight chaos and resilience harness providing atomic SQLite WAL journaling, RSS ceiling guards, and tri-state circuit breakers. (maintainer's project, 2026-11)

## Structured Output and Human-in-the-Loop Controls

- [Instructor](https://github.com/567-labs/instructor) - Python library validating LLM responses against Pydantic models with automatic schema-error retry loops. (production, 14.1k stars, 2026-11)
- [BAML](https://github.com/BoundaryML/baml) - Domain-specific language and compiler generating type-safe, resilient structured output clients with partial parsing. (production, 9.5k stars, 2026-11)
- [Outlines](https://github.com/dottxt-ai/outlines) - Finite-state-machine constrained generation engine guaranteeing syntactically valid JSON and regex outputs from local models. (production, 16.0k stars, 2026-09)
- [Guidance](https://github.com/guidance-ai/guidance) - Constrained decoding runtime interleaving Python control flow with grammar-enforced LLM generation. (production, 21.8k stars, 2026-05)
- [HumanLayer](https://github.com/humanlayer/humanlayer) - API and SDK adding asynchronous human approval gates in front of privileged or destructive agent tool calls. (production, 12.9k stars, 2026-11)
- [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) - Engineering methodology outlining design principles for controllable, stateful, production-grade LLM applications. (guide, 27.4k stars, 2025-09)

## Observability, Tracing, and Evaluation

- [Langfuse](https://github.com/langfuse/langfuse) - Open-source LLM engineering platform for OpenTelemetry tracing, prompt versioning, latency monitoring, and regression evaluations. (production, 37.8k stars, 2026-11)
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) - Open-source observability and evaluation workbench for inspecting multi-step agent traces, retrieval drift, and tool errors. (production, 12.4k stars, 2026-11)
- [OpenInference](https://github.com/Arize-ai/openinference) - OpenTelemetry instrumentation plugins capturing LLM spans, tool calls, and token usage across major frameworks. (standard, 1.3k stars, 2026-11)
- [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) - Official OpenTelemetry specification standardizing span, metric, and event schemas for AI models and agents. (standard)
- [OpenTelemetry GenAI Conventions Repo](https://github.com/open-telemetry/semantic-conventions-genai) - Working-group repository maintaining semantic convention definitions for generative AI observability. (standard, 560 stars, 2026-11)
- [OpenTelemetry Python](https://github.com/open-telemetry/opentelemetry-python) - Core Python observability SDK used to export agent spans, timeouts, and error metrics cleanly. (production, 2.7k stars, 2026-11)
- [OpenLIT](https://github.com/openlit/openlit) - OpenTelemetry-native observability and GPU telemetry suite supporting zero-code agent instrumentation and cost tracking. (production, 3.1k stars, 2026-11)
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - Extension suite built atop OpenTelemetry for tracing multi-provider LLM workflows and vector database queries. (production, 7.6k stars, 2026-11)
- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability proxy offering request caching, latency analytics, rate-limit alerts, and fallback routing. (production, 6.3k stars, 2026-11)
- [AgentOps](https://github.com/AgentOps-AI/agentops) - Monitoring SDK focused on session replays, tool-failure tracking, and token-budget visibility for agent workflows. (production, 6.0k stars, 2026-06)
- [Weights and Biases Weave](https://github.com/wandb/weave) - Lightweight toolkit for logging nested agent traces, versioning evaluation datasets, and scoring iterative changes. (production, 1.2k stars, 2026-11)
- [Portkey AI Gateway](https://github.com/Portkey-AI/gateway) - High-throughput AI gateway implementing automatic retries, provider failovers, semantic caching, and schema guardrails. (production, 13.4k stars, 2026-11)
- [MLflow](https://github.com/mlflow/mlflow) - End-to-end AI lifecycle platform supporting agent execution tracing, prompt registries, and automated evaluation suites. (production, 28.9k stars, 2026-11)
- [DeepEval](https://github.com/confident-ai/deepeval) - Open-source LLM evaluation framework running unit tests on hallucination rates, tool correctness, and CI regressions. (production, 19.6k stars, 2026-11)
- [AutoEvals](https://github.com/braintrustdata/autoevals) - Scoring library from Braintrust providing deterministic and model-graded checks for agent outputs. (production, 1.1k stars, 2026-11)
- [Sci Integrity Guard](https://github.com/pokushko/sci-integrity-guard) - Neuro-symbolic linter verifying CrossRef and OpenAlex DOIs, cross-table numerical parity, and LaTeX-to-Word OMML formulas. (maintainer's project, 2026-11)

## Prompt Injection, Guardrails, and Red-Teaming

- [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) - Industry security standard cataloguing critical agent threats including goal hijacking, tool misuse, and excessive agency. (standard)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) - Foundational security taxonomy covering prompt injection, sensitive data disclosure, and insecure plugin designs. (standard)
- [OWASP LLM Top 10 Repository](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) - Community source repository hosting threat guidance, mitigations, and risk checklists for generative AI engineers. (standard, 1.5k stars, 2026-08)
- [OWASP AI Security and Privacy Guide](https://github.com/OWASP/www-project-ai-security-and-privacy-guide) - Reference guide covering threat modeling, red-teaming practices, and lifecycle security controls for AI systems. (standard, 444 stars, 2026-11)
- [MITRE ATLAS](https://atlas.mitre.org/) - Knowledge base mapping adversarial tactics and techniques observed against production machine-learning and agentic systems. (standard)
- [MITRE ATLAS Data](https://github.com/mitre-atlas/atlas-data) - Structured YAML dataset of adversarial AI techniques, mitigations, and documented real-world case studies. (standard, 208 stars, 2026-10)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Voluntary federal framework detailing governance, measurement, and operational risk controls for trustworthy AI. (standard)
- [CaMeL](https://github.com/google-research/camel-prompt-injection) - Reference implementation from Google Research defending LLM agents against prompt injections via control/data flow separation. (research, 425 stars, 2025-06)
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - Programmable runtime rail toolkit from NVIDIA enforcing topical boundaries, PII filters, and safe tool policies. (production, 7.6k stars, 2026-11)
- [PurpleLlama](https://github.com/meta-llama/PurpleLlama) - Meta security suite bundling LlamaFirewall, Prompt Guard, and CodeShield for real-time agent defense. (production, 4.5k stars, 2026-11)
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Python framework validating LLM inputs and outputs against composable structural and safety validators. (production, 7.6k stars, 2026-11)
- [Garak](https://github.com/NVIDIA/garak) - Automated LLM vulnerability scanner probing endpoints for jailbreaks, prompt injections, and data leakage. (production, 10.1k stars, 2026-11)
- [PyRIT](https://github.com/microsoft/PyRIT) - Microsoft AI Red Team automation toolkit executing multi-turn adversarial probes and risk scoring workflows. (production, 5.0k stars, 2026-11)
- [Promptfoo](https://github.com/promptfoo/promptfoo) - CLI testing and red-teaming harness scanning prompts, RAG pipelines, and agents for regressions in CI. (production, 27.6k stars, 2026-11)
- [Snyk Agent-Scan](https://github.com/snyk/agent-scan) - Security scanner (formerly Invariant Labs MCP-Scan) detecting MCP tool poisoning, prompt injections, and toxic agent data flows. (production, 3.3k stars, 2026-11)

## Sandboxing and Execution Isolation

- [E2B](https://github.com/e2b-dev/E2B) - Open-source cloud sandbox runtime running untrusted AI-generated code inside isolated Firecracker microVMs. (production, 15.0k stars, 2026-11)
- [Modal Client](https://github.com/modal-labs/modal-client) - Python SDK for spawning ephemeral, container-isolated serverless sandboxes for agent code execution. (production, 540 stars, 2026-11)
- [Kubernetes Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) - Kubernetes SIG controller managing isolated, stateful execution sandboxes with strong security boundaries for AI agents. (production, 4.7k stars, 2026-11)
- [Microsandbox](https://github.com/superradcompany/microsandbox) - Self-hosted microVM runtime enabling fast, hardware-isolated local code execution for AI coding workflows. (production, 9.2k stars, 2026-11)
- [gVisor](https://github.com/gvisor/gvisor) - Application kernel from Google intercepting system calls in user space to isolate untrusted containers from the Linux host. (production, 20.1k stars, 2026-11)
- [Firecracker](https://github.com/firecracker-microvm/firecracker) - Lightweight KVM hypervisor booting hardware-isolated microVMs in ~125 ms for multi-tenant serverless agent execution. (production, 38.2k stars, 2026-11)
- [Kata Containers](https://github.com/kata-containers/kata-containers) - Open-source runtime wrapping Linux workloads inside lightweight virtual machines with OCI container compatibility. (production, 9.2k stars, 2026-11)
- [Cilium Tetragon](https://github.com/cilium/tetragon) - Kernel-level eBPF security observability and runtime enforcement engine blocking unauthorized syscalls and socket egress. (production, 5.2k stars, 2026-11)
- [eBPF](https://ebpf.io/) - Linux kernel technology enabling zero-overhead syscall filtering, network isolation, and runtime auditing without binary edits. (production)
- [Wasmtime](https://github.com/bytecodealliance/wasmtime) - Capability-based WebAssembly runtime executing untrusted plugins inside strict memory and filesystem sandboxes. (production, 18.9k stars, 2026-11)
- [Pyodide](https://github.com/pyodide/pyodide) - Python distribution compiled to WebAssembly for isolated browser and worker execution without host OS access. (production, 15.0k stars, 2026-11)
- [Bubblewrap](https://github.com/containers/bubblewrap) - Unprivileged Linux namespaces sandbox wrapping local subprocesses with read-only rootfs and network isolation. (production, 9.6k stars, 2026-10)
- [nsjail](https://github.com/google/nsjail) - Lightweight Linux process isolation tool combining namespaces, seccomp-bpf policies, and cgroups memory ceilings. (production, 4.2k stars, 2026-11)
- [Agent Security Sandbox](https://github.com/pokushko/agent-security-sandbox) - Pre-flight Python AST security inspector blocking dangerous imports, dunder reflection escapes, and secret leaks. (maintainer's project, 2026-11)

## Memory Management and Bounded Context

- [Letta](https://github.com/letta-ai/letta) - Stateful agent runtime (formerly MemGPT) managing bounded context via explicit hierarchical memory paging and persistent blocks. (production, 25.5k stars, 2026-10)
- [Letta Agent File](https://github.com/letta-ai/agent-file) - Open file specification for serializing, checkpointing, and migrating stateful agent memory and tool configurations. (standard, 1.2k stars, 2026-10)
- [Mem0](https://github.com/mem0ai/mem0) - Universal memory layer extracting, consolidating, and pruning long-horizon facts across multi-session agent runs. (production, 69.4k stars, 2026-11)
- [Graphiti](https://github.com/getzep/graphiti) - Temporal knowledge graph engine tracking evolving facts and bi-temporal validity windows for long-running AI agents. (production, 33.0k stars, 2026-11)
- [Cognee](https://github.com/topoteretes/cognee) - Modular memory pipeline transforming heterogeneous documents and agent traces into structured graph and vector stores. (production, 33.5k stars, 2026-11)
- [A-MEM](https://github.com/agiresearch/A-mem) - Zettelkasten-inspired agentic memory framework implementing structured note creation, dynamic linking, and memory evolution. (research, 1.2k stars, 2025-12)
- [DuckDB](https://github.com/duckdb/duckdb) - Embedded columnar analytical database ideal for local audit logs, trace inspection, and out-of-core execution history. (production, 43.3k stars, 2026-11)
- [Qdrant](https://github.com/qdrant/qdrant) - Rust vector database offering payload filtering, scalar quantization, and disk-backed HNSW indices for bounded RAM. (production, 35.7k stars, 2026-11)
- [Chroma](https://github.com/chroma-core/chroma) - Open-source embedding database supporting persistent local or client-server vector retrieval for agent workflows. (production, 29.7k stars, 2026-11)
- [Milvus](https://github.com/milvus-io/milvus) - Cloud-native distributed vector database engineered for billion-scale hybrid search and tiered disk storage. (production, 46.7k stars, 2026-11)
- [Weaviate](https://github.com/weaviate/weaviate) - Hybrid vector and keyword database featuring multi-tenancy isolation and time-to-live (TTL) object expiration. (production, 17.0k stars, 2026-11)
- [LanceDB](https://github.com/lancedb/lancedb) - Embedded multimodal vector store built on the Lance columnar format with disk-based ANN queries and zero server overhead. (production, 12.0k stars, 2026-11)
- [sqlite-vec](https://github.com/asg017/sqlite-vec) - Zero-dependency C vector search extension embedded directly inside transactional SQLite database files. (production, 8.3k stars, 2026-05)
- [Agentic Vector Memory](https://github.com/pokushko/agentic-vector-memory) - Dual-store episodic memory library combining cosine similarity, exponential recency decay, and SQLite ACID persistence. (maintainer's project, 2026-11)

## Chaos Engineering and Fault Injection

- [Chaos Mesh](https://github.com/chaos-mesh/chaos-mesh) - Cloud-native chaos engineering platform for Kubernetes injecting pod kills, network partitions, I/O faults, and clock skew. (production, 8.0k stars, 2026-11)
- [Chaos Toolkit](https://github.com/chaostoolkit/chaostoolkit) - Declarative Python framework for codifying steady-state hypotheses and running automated fault-injection experiments. (production, 2.0k stars, 2026-10)
- [Toxiproxy](https://github.com/Shopify/toxiproxy) - Programmable TCP proxy simulating upstream API latency, bandwidth throttling, connection resets, and timeouts in CI. (production, 12.5k stars, 2026-11)
- [LitmusChaos](https://github.com/litmuschaos/litmus) - CNCF-hosted chaos engineering framework orchestrating cross-cluster resilience tests and automated probes. (production, 5.7k stars, 2026-11)
- [ChaosBlade](https://github.com/chaosblade-io/chaosblade) - Chaos fault-injection toolkit supporting container, process CPU/memory pressure, network, and JVM/Linux syscall faults. (production, 6.5k stars, 2026-11)
- [Pumba](https://github.com/alexei-led/pumba) - Lightweight chaos CLI injecting container kills, pauses, and network emulation delays on Docker hosts. (production, 3.2k stars, 2026-11)

## Causal Inference and Formal Verification

- [DoWhy](https://github.com/py-why/dowhy) - Causal inference library structuring modeling, backdoor identification, estimation, and refutation checks to test invariants. (production, 8.4k stars, 2026-11)
- [EconML](https://github.com/py-why/EconML) - Double-machine-learning library from Microsoft Research estimating heterogeneous treatment effects under confounding. (production, 4.9k stars, 2026-11)
- [Z3 Theorem Prover](https://github.com/Z3Prover/z3) - Industrial SMT solver used in neuro-symbolic verification to check arithmetic bounds, scheduling rules, and policy invariants. (production, 13.0k stars, 2026-11)
- [Lean 4](https://github.com/leanprover/lean4) - Interactive theorem prover and functional language widely adopted for formalizing and verifying LLM-generated proofs. (production, 10.3k stars, 2026-11)
- [Dafny](https://github.com/dafny-lang/dafny) - Verification-aware programming language enabling static formal verification of agent-generated preconditions and postconditions. (production, 3.6k stars, 2026-11)
- [SymPy](https://github.com/sympy/sympy) - Symbolic mathematics engine checking algebraic conservation laws, dimensional consistency, and differential equation derivatives. (production, 15.1k stars, 2026-11)
- [PySR](https://github.com/astroautomata/PySR) - High-performance symbolic regression engine extracting closed-form analytical laws directly from empirical observations. (production, 4.3k stars, 2026-11)
- [EvoNova Causal Guard](https://github.com/pokushko/evonova-causal-guard) - Zero-dependency Python Pearl do-calculus DAG verifier, Tabu memory archive, and multi-agent debate arbiter. (maintainer's project, 2026-11)

## Multi-Agent Coordination, Debate, and Failure Analysis

- [MAST](https://github.com/multi-agent-systems-failure-taxonomy/MAST) - Official codebase, annotated trace corpus, and LLM-as-a-Judge failure analyzer accompanying the 14-mode MAST taxonomy. (research, 441 stars, 2025-07)
- [ChatEval](https://github.com/thunlp/ChatEval) - Official THUNLP codebase implementing role-diverse referee debates to evaluate generation quality and reduce bias. (research, 346 stars, 2024-10)
- [DSPy](https://github.com/stanfordnlp/dspy) - Declarative framework compiling declarative signatures and verification assertions into self-optimizing multi-stage pipelines. (production, 39.2k stars, 2026-11)
- [AG2](https://github.com/ag2ai/ag2) - Community-driven multi-agent orchestration framework extending the AutoGen conversation architecture with structured patterns. (production, 5.1k stars, 2026-11)
- [CrewAI](https://github.com/crewAIInc/crewAI) - Role-based multi-agent orchestration framework supporting event-driven flows, guardrails, and state persistence. (production, 61.2k stars, 2026-11)
- [CAMEL](https://github.com/camel-ai/camel) - Communicative agent research framework supporting large-scale role-playing, structured verifiers, and synthetic trace generation. (research, 18.1k stars, 2026-11)
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - Standardized operating-procedure multi-agent framework enforcing structured artifacts between specialized software roles. (research, 71.4k stars, 2026-01)
- [OpenHands](https://github.com/OpenHands/OpenHands) - Open-source software engineering agent platform featuring event-stream logging and isolated container runtimes. (production, 94.2k stars, 2026-11)
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - Autonomous repository-repair agent pairing constrained agent-computer interfaces with Docker-sandboxed test verification. (research, 20.9k stars, 2026-11)
- [Concordia](https://github.com/google-deepmind/concordia) - Google DeepMind library simulating grounded multi-agent interactions moderated by a shared environment controller. (research, 1.9k stars, 2026-11)
- [Orchestration Engine](https://github.com/pokushko/orchestration-engine) - Minimal asynchronous Python task router supporting typed worker roles, DAG handoffs, and consensus callbacks. (maintainer's project, 2026-11)

## Benchmarks and Stress-Testing Suites

- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - End-to-end software engineering benchmark evaluating autonomous agents on real GitHub repository issues inside Docker containers. (research, 6.2k stars, 2026-09)
- [Tau-bench](https://github.com/sierra-research/tau-bench) - Benchmark measuring tool-agent-user policy adherence and multi-turn consistency across airline and retail domains. (research, 1.5k stars, 2026-03)
- [Tau2-bench](https://github.com/sierra-research/tau2-bench) - Extended dual-control simulation environment evaluating collaborative fault recovery and tool coordination. (research, 2.5k stars, 2026-11)
- [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) - Containerized command-line benchmark evaluating agents on compilation, debugging, systems administration, and recovery tasks. (research, 1.1k stars, 2026-11)
- [Terminal-Bench 2](https://github.com/harbor-framework/terminal-bench-2) - Expanded second-generation suite of verified terminal tasks hosted on the Harbor evaluation harness. (research, 451 stars, 2026-04)
- [OSWorld](https://github.com/xlang-ai/OSWorld) - Real-OS execution environment testing multimodal computer-use agents on open-ended Ubuntu, Windows, and macOS workflows. (research, 3.3k stars, 2026-11)
- [WebArena](https://github.com/web-arena-x/webarena) - Self-hosted suite of functional web applications benchmarking multi-step browser navigation and failure recovery. (research, 1.6k stars, 2025-11)
- [GAIA Benchmark](https://huggingface.co/gaia-benchmark) - Multi-step real-world assistant benchmark requiring deterministic tool use, web browsing, and file analysis. (research)
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) - UK AI Security Institute evaluation framework supporting sandboxed tool agents, custom scorers, and reproducible transcripts. (production, 3.3k stars, 2026-11)
- [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) - Community-maintained catalog of security, autonomy, and agentic safety benchmarks built on Inspect. (research, 756 stars, 2026-11)
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - Dynamic security evaluation suite from ETH Zurich benchmarking indirect prompt-injection attacks and agent defenses. (research, 1.1k stars, 2026-06)
- [AgentBench](https://github.com/THUDM/AgentBench) - Multi-environment benchmark evaluating autonomous agents across eight operating systems, databases, and interactive arenas. (research, 3.8k stars, 2026-02)
- [ToolBench](https://github.com/OpenBMB/ToolBench) - Large-scale tool-use benchmark testing multi-step API planning, error parsing, and fallback path recovery. (research, 5.8k stars, 2025-05)
- [Berkeley Function-Calling Leaderboard (Gorilla)](https://github.com/ShishirPatil/gorilla) - Executable benchmark suite measuring single-turn, parallel, and multi-turn function-calling accuracy and abstention. (research, 13.1k stars, 2026-10)
- [WorkArena](https://github.com/ServiceNow/WorkArena) - Enterprise web-agent benchmark testing realistic SaaS workflow completion and UI state resilience. (research, 281 stars, 2026-09)
- [HELM](https://github.com/stanford-crfm/helm) - Stanford holistic evaluation framework measuring robustness, calibration, safety, and efficiency across foundation models. (research, 3.0k stars, 2026-09)
- [OpenAI Evals](https://github.com/openai/evals) - Extensible evaluation framework for automating behavioral regression tests and custom task suites. (production, 19.8k stars, 2026-04)

## Research Papers and Engineering Guides

### Failure Taxonomies and Agent Architecture

- [Why Do Multi-Agent LLM Systems Fail? (Cemri et al., 2025)](https://arxiv.org/abs/2503.13657) - Introduces MAST, cataloging 14 empirical failure modes across 1,600+ annotated multi-agent execution traces. (research)
- [Building Effective Agents (Anthropic, 2024)](https://www.anthropic.com/engineering/building-effective-agents) - Practical engineering guide to composable agent workflows, clear stopping criteria, and agent-computer interface design. (guide)
- [ReAct: Synergizing Reasoning and Acting in Language Models (Yao et al., 2022)](https://arxiv.org/abs/2210.03629) - Foundational paradigm interleaving chain-of-thought reasoning traces with grounded external tool observations. (research)
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models (Yao et al., 2023)](https://arxiv.org/abs/2305.10601) - Generalizes chain-of-thought into heuristic search over branching reasoning states with lookahead and backtracking. (research)
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (Lu et al., 2024)](https://arxiv.org/abs/2408.06292) - End-to-end automated research pipeline documenting empirical loop failure modes and review-gate lessons. (research)

### Self-Correction and Tool Reliability

- [Reflexion: Language Agents with Verbal Reinforcement Learning (Shinn et al., 2023)](https://arxiv.org/abs/2303.11366) - Episodic verbal self-critique mechanism allowing agents to avoid repeating execution failures without weight updates. (research)
- [Self-Refine: Iterative Refinement with Self-Feedback (Madaan et al., 2023)](https://arxiv.org/abs/2303.17651) - Iterative model self-feedback and refinement loop improving task outputs without supervised fine-tuning. (research)
- [Toolformer: Language Models Can Teach Themselves to Use Tools (Schick et al., 2023)](https://arxiv.org/abs/2302.04761) - Self-supervised method teaching language models when and how to invoke external APIs reliably. (research)
- [Voyager: An Open-Ended Embodied Agent with Large Language Models (Wang et al., 2023)](https://arxiv.org/abs/2305.16291) - Iterative skill-library architecture verifying executable code artifacts against environment feedback before reuse. (research)
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering (Yang et al., 2024)](https://arxiv.org/abs/2405.15793) - Demonstrates that well-designed agent-computer interfaces and linters substantially curb loop and syntax failures. (research)
- [SkillBridge: Cost-Aware Diagnosis and Repair of Cross-OS Compatibility Defects in Agent Skills (Xu et al., 2026)](https://arxiv.org/abs/2611.26256) - Cost-aware diagnostic and repair framework resolving OS-level compatibility defects in executable agent skills. (research)
- [Beyond Weight Updates: Evolving Agent Harnesses for Domain Specialization (Chen, 2026)](https://arxiv.org/abs/2611.25380) - Empirical study on evolving agent harnesses across prompts, tool schemas, and skills while keeping model weights frozen. (research)

### Memory and Long-Context Stability

- [Lost in the Middle: How Language Models Use Long Contexts (Liu et al., 2023)](https://arxiv.org/abs/2307.03172) - Empirical study proving attention degrades sharply for mid-context facts, motivating bounded memory compaction. (research)
- [MemGPT: Towards LLMs as Operating Systems (Packer et al., 2023)](https://arxiv.org/abs/2310.08560) - Introduces virtual context management inspired by OS RAM-to-disk paging for unbounded multi-session conversations. (research)
- [A-MEM: Agentic Memory for LLM Agents (Xu et al., 2025)](https://arxiv.org/abs/2502.12110) - Zettelkasten-inspired memory architecture generating structured notes that dynamically link and evolve historical context. (research)
- [Generative Agents: Interactive Simulacra of Human Behavior (Park et al., 2023)](https://arxiv.org/abs/2304.03442) - Pioneers recency-importance-relevance memory retrieval scoring and periodic reflection trees. (research)

### Prompt Injection, Security, and Alignment

- [Defeating Prompt Injections by Design (Debenedetti et al., 2025)](https://arxiv.org/abs/2503.18813) - Proposes CaMeL, isolating control flows from untrusted data via capability tracking in an interpreter layer. (research)
- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection (Greshake et al., 2023)](https://arxiv.org/abs/2302.12173) - Foundational taxonomy of indirect prompt injection attacks delivered through retrieved web content and tool outputs. (research)
- [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents (Debenedetti et al., 2024)](https://arxiv.org/abs/2406.13352) - Introduces a stateful, dynamic suite quantifying both utility and attack success rate under tool-mediated prompt injection. (research)
- [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents (Andriushchenko et al., 2024)](https://arxiv.org/abs/2410.09024) - Evaluates multi-step malicious task robustness and jailbreak resilience across tool-augmented agents. (research)
- [EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System (Reddy et al., 2025)](https://arxiv.org/abs/2509.10540) - Detailed technical analysis of CVE-2025-32711, demonstrating zero-click enterprise data exfiltration chains. (research)
- [Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI) (Wang et al., 2026)](https://arxiv.org/abs/2611.26553) - Forensic evaluation framework reproducing, validating, and root-cause auditing real-world agentic security incidents. (research)
- [Constitutional AI: Harmlessness from AI Feedback (Bai et al., 2022)](https://arxiv.org/abs/2212.08073) - Principle-driven critique and revision method bounding harmful autonomous agent behaviors. (research)

### Multi-Agent Debate and Evaluation Papers

- [Improving Factuality and Reasoning in Language Models through Multiagent Debate (Du et al., 2023)](https://arxiv.org/abs/2305.14325) - Study by MIT and Google Brain demonstrating multi-agent debate reduces hallucinations and improves reasoning accuracy. (research)
- [ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate (Chan et al., 2023)](https://arxiv.org/abs/2308.07201) - Multi-agent referee panel architecture improving evaluation consistency over single-model judges. (research)
- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation (Wu et al., 2023)](https://arxiv.org/abs/2308.08155) - Multi-agent conversation framework formalizing automated human-proxy termination and code execution loops. (research)
- [GAIA: a benchmark for General AI Assistants (Mialon et al., 2023)](https://arxiv.org/abs/2311.12983) - Proposes realistic multi-step assistant benchmarks exposing tool-orchestration brittleness on tasks trivial for humans. (research)
- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments (Xie et al., 2024)](https://arxiv.org/abs/2404.07972) - Evaluates GUI and CLI computer-use agents inside real VM snapshots across multi-application workflows. (research)
- [Tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (Yao et al., 2024)](https://arxiv.org/abs/2406.12045) - Exposes low `pass^k` multi-trial consistency in tool-calling agents over long policy-constrained interactions. (research)

### Maintainer Preprints

- [EvoNova Scientist: A Neuro-Symbolic Multi-Agent Framework for Physical Constraint-Preserving Autonomous Scientific Discovery (Pokushko and Pokushko, 2026)](https://doi.org/10.5281/zenodo.23942797) - Zenodo preprint decoupling generative hypotheses from deterministic dimensional and thermodynamic verification. (maintainer's preprint)

## Real-World Incidents and Post-Mortems

- [AI Incident Database](https://incidentdatabase.ai/) - Public repository indexing real-world AI failures, safety harms, and near-misses for empirical risk engineering. (registry)
- [GenAI Incidents](https://github.com/emmanuelgjr/genai_incidents) - Machine-readable catalog mapping AI Incident Database and CVE advisories to OWASP Agentic Top 10 controls. (registry, 32 stars, 2026-11)
- [Replit AI Agent Production Database Deletion (July 2025)](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/) - Coding agent disregarded a user-declared freeze and wiped a live production database, prompting dev/prod separation controls. (incident)
- [Moffatt v. Air Canada (2024 BCCRT 149)](https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada) - Landmark Canadian tribunal ruling holding a corporation legally liable for a customer-service chatbot's policy hallucination. (incident)
- [Microsoft 365 Copilot EchoLeak (CVE-2025-32711, 2025)](https://nvd.nist.gov/vuln/detail/CVE-2025-32711) - Critical zero-click indirect prompt injection (CVSS 9.3) allowing enterprise data exfiltration via crafted emails. (incident)
- [Slack AI Indirect Prompt Injection Data Exfiltration (August 2024)](https://simonwillison.net/2024/Aug/20/data-exfiltration-from-slack-ai/) - Disclosed exploit demonstrating how malicious messages in public channels exfiltrated private workspace secrets via Markdown link rendering. (incident)
- [MCP Tool Poisoning Attacks Disclosure (April 2025)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) - Vulnerability disclosure revealing how malicious instructions hidden inside MCP tool descriptions hijack agent behavior. (incident)
- [DPD Customer Support Chatbot Jailbreak (January 2024)](https://www.theguardian.com/technology/2024/jan/20/dpd-ai-chatbot-swears-calls-itself-useless-and-criticises-firm) - Customer prompted an unguarded support agent to swear and disparage its own operator, forcing immediate service suspension. (incident)
- [Chevrolet of Watsonville Chatbot $1 Tahoe Offer (December 2023)](https://www.businessinsider.com/car-dealership-chevrolet-chatbot-chatgpt-pranks-chevy-2023-12) - Unguarded dealership ChatGPT bot accepted an adversarial instruction to offer a new SUV as a binding sale for $1. (incident)

## Contributing

Contributions are warmly welcomed! Please read our [contribution guidelines](CONTRIBUTING.md) and abide by our [code of conduct](CODE_OF_CONDUCT.md) before opening a Pull Request.
