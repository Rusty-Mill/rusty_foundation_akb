# Development design philosophy and adopted influences

**Status:** Accepted rationale  
**Reviewed inputs:** User-provided global engineering guidance and Unix software-design philosophy, 2026-08-08

This document records how those inputs shape Rusty Mill. It incorporates durable principles into repository authority without importing assistant-specific workflow or treating historical Unix mechanisms as universal cross-platform abstractions.

## Adopted directly

| Principle | Rusty Mill interpretation |
|---|---|
| Composition over inheritance | Build behavior from narrow capabilities, services, profiles, and adapters; inheritance cannot create hidden authority or lifecycle coupling. |
| Clear module boundaries | Domain semantics, orchestration/policy, provider adapters, and native/FFI mechanics have explicit dependency direction. |
| Ports and adapters | Domain logic does not reach into frameworks, ambient globals, native APIs, files, network, or process environment. |
| Explicit over implicit | Authority, policy, configuration, runtime, provider, time, locale, cancellation, and degradation are passed or negotiated explicitly. |
| Make illegal states unrepresentable | Use enums, newtypes, validated builders, ownership, typestate, and private construction when they materially reduce invalid or unsafe states. |
| Clarity and simplicity | Optimize for reviewable invariants and failure behavior; clever compression and speculative abstraction are liabilities. |
| Immutability and data representation | Prefer immutable generations/snapshots and represent policy/schema/state explicitly so generic machinery remains small and auditable. |
| Minimal dependencies | Add external code only when its capability, maintenance, security, licensing, portability, and exit value exceed its permanent cost. |
| Fail visibly and early | Reject invalid input/configuration before effects, preserve typed failure/partial-state evidence, and never silently swallow exceptions or degradation. |
| Focused changes | Keep changes coherent, preserve unrelated work, and state the reason for non-obvious decisions in durable review/decision evidence. |
| Measure before optimizing | Establish semantics, correctness gates, and representative measurements before complexity or unsafe optimization. |

## Adopted with qualification

| Source principle | Qualification |
|---|---|
| “Do one thing well” | Applies to capabilities, functions, modules, tools, and services at the smallest independently testable semantic boundary. It does not require process-per-feature fragmentation. |
| Modular monolith by default | Deployable application/control-plane composition remains cohesive until independent scaling, team/language boundary, hard fault isolation, or security boundary justifies a service. Libraries still use multiple crates only for real ownership/release/target boundaries. |
| Mechanism, not policy | Portable capabilities expose explicit semantics and policy inputs rather than hard-coded product workflows. Some capabilities are policy evaluation/enforcement mechanisms, so “policy” cannot be excluded from the architecture. |
| Text streams as interface | Human-facing CLI, diagnostics, manifests, review artifacts, and simple automation SHOULD offer deterministic documented text/structured-text forms. Binary/media/typed/streaming capability contracts use formats appropriate to their semantics and performance. |
| Silence is golden | Successful CLI/automation is quiet unless output is requested or part of its data contract. Libraries and services still emit governed structured observability; silence cannot hide dropped work, degradation, or security events. |
| Generation | Generate repetitive adapters, schemas, docs, and evidence when inputs and output are deterministic, provenance-bound, reviewable, and independently validated. Generation does not create semantic authority. |
| Extensibility | Preserve compatible evolution seams supported by concrete evidence; do not introduce abstraction before two real call sites or a required provider boundary. |
| Prototype before polishing | Use disposable, explicitly non-authoritative spikes to learn after the specification authorizes a trial. Rusty Mill remains specification-before-implementation, so a prototype cannot establish public contract precedent. |

## Deliberately not incorporated literally

### Everything is a file

Native operating systems often expose files, descriptors, handles, objects, ports, or messages as useful uniform mechanisms. Rusty Mill does not elevate any one mechanism into the portable model. A window, credential, process, clock, GPU resource, accessibility tree, transaction, or cancellation scope is modeled by its capability semantics, authority, lifecycle, and evidence—not coerced into file operations. This is a direct consequence of “abstract capabilities, not operating systems.”

### Text as a universal data model

Text maximizes inspectability and composition for many tools, but it does not preserve every typed, binary, realtime, zero-copy, cryptographic, media, locale, or native-resource contract. Interchange format is a negotiated capability choice with explicit loss and security behavior.

### One tool per feature

Process/service extraction pays distribution, deployment, security, compatibility, and observability costs. Separate deployables require a concrete forcing function; internal modularity is the default response to conceptual separation.

## Out of project scope

The reviewed global guidance also contained assistant memory, conversation, and user-communication instructions. Those govern an assistant's operating behavior and are not software-product, contributor, CI, or release standards. They are intentionally not copied into repository governance.

## Normative consequences

**RM-DEV-PHIL-0001:** Rusty Mill implementations MUST favor composition and narrow explicit interfaces, with dependencies directed from policy/domain semantics toward ports and from adapters toward native mechanisms without reversing authority.

**RM-DEV-PHIL-0002:** A new abstraction, crate, service, dependency, or extension seam MUST cite concrete call sites or a required ownership/release/provider/scaling/fault/security boundary.

**RM-DEV-PHIL-0003:** Human/tool text interfaces MUST NOT force lossy or unsafe text representations onto capabilities whose semantics require typed, binary, realtime, cryptographic, or resource-bound models.

**RM-DEV-PHIL-0004:** Native mechanism uniformity such as files, handles, descriptors, or callbacks MUST remain a backend concern unless the portable behavioral contract independently justifies the same abstraction.

**RM-DEV-PHIL-0005:** A disposable prototype MAY test feasibility only after trial authorization and MUST NOT become maintained code, a dependency, or public precedent without passing ordinary architecture and development gates.
