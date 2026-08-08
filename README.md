# Rusty Mill Foundation Architecture Knowledge Base

Rusty Mill is a Rust-first, high-performance, capability-based operating-system abstraction and application platform for native applications on Windows, Linux, and macOS.

> **Guiding principle:** Abstract capabilities, not operating systems.

This repository is the canonical architecture knowledge base (AKB). It records intent, vocabulary, contracts, decisions, and validation requirements before implementation begins. It deliberately contains no product code.

## Start here

1. [Project charter](docs/00-foundation/project-charter.md)
2. [Architecture principles](docs/00-foundation/principles.md)
3. [Architecture overview](docs/01-architecture/overview.md)
4. [Capability model](docs/02-capabilities/model.md)
5. [Ecosystem architecture](docs/04-ecosystem/repository-strategy.md)
6. [Governance](docs/05-governance/governance.md)
7. [Roadmap](docs/06-roadmap/roadmap.md)

The [documentation index](docs/README.md) describes the full information architecture and document lifecycle.

## Current phase

**Foundation / specification.** The current work is to define the platform and its verification model. Implementation repositories, crates, and workspaces are created only after their boundaries and contracts are accepted through the ADR/RFC process.

## Working maxim

**Specify completely. Implement faithfully. Verify continuously. Evolve deliberately.**

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Architectural decisions belong in ADRs; proposals affecting multiple capabilities or repositories belong in RFCs.
