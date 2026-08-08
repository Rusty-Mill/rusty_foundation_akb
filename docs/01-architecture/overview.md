# Architecture overview

> This is a concise orientation. The [authoritative architecture model](architecture-model.md) is the normative source of truth.

## Architecture pyramid

![Seven-layer Rusty Mill architecture pyramid](../assets/architecture-pyramid.svg)

| Layer | Responsibility |
|---|---|
| Applications | Consume profiles, services, and domain frameworks |
| Domain frameworks | Compose capabilities into application-oriented models |
| Platform services | Coordinate resources and policy across capabilities |
| Common APIs | Present stable Rust-native interaction surfaces |
| Capability framework | Discovery, selection, authority, lifecycle, and degradation |
| Backend contracts | Define obligations for capability providers |
| OS backends | Map contracts to native platform mechanisms |

Dependencies point downward through the immediately adjacent layer. A layer may expose abstractions derived from lower layers but may not depend directly on a non-adjacent implementation. Shared schema and test artifacts remain dependency-neutral.

## Mechanism and policy

Backends implement mechanism. Policy determines which provider, authority, fallback, quality level, or resource budget is acceptable. Separating them prevents platform details and application preferences from becoming inseparable.

## Portability model

Portable does not mean identical internals. It means stable semantics where promised, explicit capability discovery, defined variance, typed failures, and testable behavior across supported targets.

## Architectural constraints

- Domain logic remains independent of OS APIs and I/O frameworks.
- Backend-specific handles do not cross common interfaces unless a contract explicitly defines an escape hatch.
- Optional capabilities are queried or required through profiles, never inferred from OS name alone.
- Unsafe boundaries are isolated, documented, and covered by platform-specific verification.

See [behavioral contracts](behavioral-contracts.md), [cross-cutting qualities](cross-cutting-qualities.md), and the [capability model](../02-capabilities/model.md).
