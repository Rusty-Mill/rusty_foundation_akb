# Capability meta-model

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
