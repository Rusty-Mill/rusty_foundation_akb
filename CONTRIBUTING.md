# Contributing to the AKB

The AKB is specification-first. A contribution should make intent, semantics, boundaries, or verification clearer.

## Change paths

- Editorial clarification: ordinary pull request.
- Durable architecture choice: copy the [ADR template](docs/05-governance/adr-template.md) into `docs/adr/`.
- Cross-cutting, public, or ecosystem proposal: copy the [RFC template](docs/05-governance/rfc-template.md) into `docs/rfc/`.
- Capability addition or change: update its taxonomy entry, dependencies, behavioral contract, profile impact, conformance requirements, and benchmarks together.

## Review standard

Every normative change must be explicit about scope, non-goals, platform variance, security, performance, accessibility, internationalization, observability, compatibility, and verification. Link rather than duplicate shared definitions.

## Status vocabulary

Documents and decisions use: **Draft**, **Proposed**, **Accepted**, **Deprecated**, or **Superseded**. Draft material is not an implementation commitment.
