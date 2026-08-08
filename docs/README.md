# Documentation index

The AKB is organized from stable intent to evolving detail.

| Area | Purpose |
|---|---|
| [00 Foundation](00-foundation/project-charter.md) | Charter, scope, principles, glossary |
| [01 Architecture](01-architecture/architecture-model.md) | Authoritative model, layering, contracts, and cross-cutting qualities |
| [02 Capabilities](02-capabilities/taxonomy.md) | Taxonomy, dependency graphs, profiles |
| [03 Delivery](03-delivery/strategy.md) | Versioning, packaging, updates, supply chain |
| [04 Ecosystem](04-ecosystem/repository-strategy.md) | Organization, repository, crate, and workspace boundaries |
| [05 Governance](05-governance/governance.md) | Decision process and templates |
| [06 Roadmap](06-roadmap/roadmap.md) | Specification-led sequencing and exit criteria |
| [ADRs](adr/README.md) | Accepted architecture decisions |
| [RFCs](rfc/README.md) | Proposals under review |

## Active vertical slices

- [Runtime and time](02-capabilities/runtime-time/README.md)
- [Filesystem](02-capabilities/filesystem/README.md)
- [Security](02-capabilities/security/README.md)
- [Process](02-capabilities/process/README.md)
- [IPC](02-capabilities/ipc/README.md)
- [Terminal](02-capabilities/terminal/README.md)
- [Windowing](02-capabilities/windowing/README.md)
- [Graphics and presentation](02-capabilities/graphics/README.md)
- [Input](02-capabilities/input/README.md)
- [Text, fonts, and layout](02-capabilities/text/README.md)
- [Accessibility](02-capabilities/accessibility/README.md)
- [Clipboard and drag-and-drop data transfer](02-capabilities/data-transfer/README.md)
- [Internationalization and localization](02-capabilities/internationalization/README.md)
- [Configuration and change notification](02-capabilities/configuration/README.md)
- [Observability, diagnostics, and crash reporting](02-capabilities/observability/README.md)
- [Application lifecycle and session integration](02-capabilities/lifecycle/README.md)
- [Networking foundations](02-capabilities/networking/README.md)
- [Memory and mapping foundations](02-capabilities/memory/README.md)
- [Plugin and module lifecycle](02-capabilities/plugins/README.md)

## Planned volumes

1. Foundation and meta-model
2. Runtime and capability domain analysis
3. Core OS services
4. User experience and application frameworks
5. Backend contracts and platform implementations
6. Tooling, delivery, conformance, benchmarks, and governance

Each volume progresses independently from inventory to semantics, contracts, verification, and only then implementation.

## Authoring specifications

- [Domain-analysis method](02-capabilities/domain-analysis.md)
- [Capability specification template](02-capabilities/capability-template.md)
- [Traceability model](04-ecosystem/traceability.md)
- [RFC-0001: Capability specification system](rfc/0001-capability-specification-system.md)

## Document authority

The [Rusty Mill authoritative architecture model](01-architecture/architecture-model.md) is the normative source of truth. Supporting documents elaborate it. Accepted ADRs record why it changes; draft documents cannot override it.
