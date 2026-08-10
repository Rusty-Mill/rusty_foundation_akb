# Contributing to the AKB

The AKB is specification-first. A contribution should make intent, semantics, boundaries, or verification clearer.

Implementation repositories and trials additionally follow the [Rusty Mill software development standards](docs/05-governance/software-development/README.md). Those standards do not authorize implementation by themselves; the affected domain must first pass its promotion and trial gates.

The [authoritative architecture model](docs/01-architecture/architecture-model.md) governs current architecture. Changes to architectural rules must update the model and their ADR/RFC in the same contribution.

## Branch Protection

`main` is protected:

- Changes land only through pull requests. Direct pushes to `main` are blocked.
- Force-pushes and branch deletion are blocked on `main`.
- The `audit` CI check (`.github/workflows/akb-audit.yml`, running `tools/akb_audit.py --check`) runs on every PR and **must pass before a PR can merge**.

## Change paths

- Editorial clarification: ordinary pull request.
- Durable architecture choice: copy the [ADR template](docs/05-governance/adr-template.md) into `docs/adr/`.
- Cross-cutting, public, or ecosystem proposal: copy the [RFC template](docs/05-governance/rfc-template.md) into `docs/rfc/`.
- Bounded implementation experiment: use the [implementation trial template](docs/05-governance/implementation-trials/trial-template.md) only after every trial entry gate passes.
- Capability addition or change: update its taxonomy entry, dependencies, behavioral contract, profile impact, conformance requirements, and benchmarks together.

## Review standard

Every normative change must be explicit about scope, non-goals, platform variance, security, performance, accessibility, internationalization, observability, compatibility, and verification. Link rather than duplicate shared definitions.

## Merge strategy

This repository merges via merge commit only — squash and rebase are disabled. Merge once a pull request reflects the intended change and review feedback is addressed.

## Status vocabulary

Documents and decisions use: **Draft**, **Proposed**, **Accepted**, **Deprecated**, or **Superseded**. Draft material is not an implementation commitment.
