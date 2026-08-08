# Capability meta-model

> This document elaborates the capability portion of the [authoritative architecture model](../01-architecture/architecture-model.md). The authoritative model governs if wording conflicts.

A capability is the smallest independently describable and testable unit of platform behavior. Capabilities are identified by stable names and versions, not by operating-system symbols.

## Capability record

Each capability specification includes:

- Stable identifier, name, domain, maturity, and owner.
- Purpose, scope, and non-goals.
- Required, optional, and conflicting capabilities.
- Behavioral contract and public semantic types.
- Provider selection and policy inputs.
- Resource, event, and authority model.
- Native backend mappings and known variance.
- Conformance tests and benchmark scenarios.
- Profile membership and evolution history.

## Availability states

- **Native:** Contract is satisfied using a first-class platform mechanism.
- **Emulated:** Contract is satisfied with documented cost or limitations.
- **Degraded:** A declared weaker quality level is active.
- **Unavailable:** The provider cannot satisfy the requested contract.

Availability is negotiated from requested requirements and provider evidence. It is never assumed solely from a platform label.

## Dependency graph rules

- The capability graph must be acyclic at specification time.
- Edges are typed as `requires`, `optionally-uses`, or `conflicts-with`.
- Required dependencies are minimal; convenience composition belongs in services or frameworks.
- Cycles indicate an incorrect boundary or a service-level composition that must be refactored.
- Graph changes require profile, conformance, security, and release-impact analysis.

## Stable identifiers

Capability identifiers use the form `rm.<domain>.<capability>`, written in lowercase ASCII with dot-separated segments. Identity describes behavior, not a crate, trait, backend, or OS facility. Examples in draft documents are illustrative until accepted through RFC review.

Versions attach to the capability contract rather than the identifier. A compatible clarification or additive optional behavior does not create a new identity. A semantically distinct behavior does.

## Requirement identifiers

Every normative statement receives a stable identifier:

`RM-<DOMAIN>-<CAPABILITY>-<NNNN>`

The identifier survives editorial movement. It connects specification text to conformance assertions, benchmarks, security evidence, compatibility notes, and implementation claims. Removed requirements are retired rather than reused.

See the [capability template](capability-template.md), [domain-analysis method](domain-analysis.md), and [traceability model](../04-ecosystem/traceability.md).
