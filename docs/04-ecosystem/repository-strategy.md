# Ecosystem and repository architecture

The GitHub organization is **Rusty-Mill**. Repository boundaries should follow ownership, release cadence, dependency direction, and failure/isolation needs—not one repository per idea.

## Repository taxonomy

| Repository class | Responsibility |
|---|---|
| Foundation AKB | Canonical charter, architecture, ADRs, RFCs, and ecosystem policies |
| Specification | Versioned capability contracts, schemas, and generated references when scale justifies separation |
| Core platform | Capability framework and common APIs in a cohesive Rust workspace |
| Backend | Platform-specific implementations when native dependencies and release needs justify separation |
| Framework | Domain/application compositions above common APIs |
| Verification | Shared conformance harnesses, fixtures, and benchmark orchestration |
| Tooling | Developer, packaging, release, and diagnostic tools |

Start as a modular monolith where cohesion is high. Extract only for a concrete forcing function such as independent release cadence, ownership, native toolchain boundary, security isolation, or repository size.

## Crates and workspaces

- A crate has one coherent responsibility and a narrow public surface.
- Workspace membership follows shared build/test/release mechanics.
- Public traits and types live above backend implementations; domain logic does not depend on OS bindings.
- Platform bindings are private implementation dependencies where possible.
- Feature flags express additive compile-time capability, not incompatible product modes.
- Avoid a single “everything” crate; profiles and facade crates may provide curated entry points.

## Naming

Names should communicate layer and responsibility. Final crate and repository names are assigned through an RFC after capability boundaries exist; this AKB intentionally does not reserve speculative packages.

## Documentation hierarchy

Organization policy -> foundation AKB -> volume/domain specifications -> capability contracts -> repository architecture guides -> crate/API documentation -> operational runbooks.

Higher levels define intent and invariants. Lower levels link upward and may add detail but must not silently contradict them.
