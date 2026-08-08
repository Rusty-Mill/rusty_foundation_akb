# Rusty Mill authoritative architecture model

**Status:** Accepted  
**Authority:** Normative source of truth  
**Version:** 1.27.0
**Last updated:** 2026-08-08  
**Decision:** [ADR-0004](../adr/0004-authoritative-architecture-model.md)

## 1. Authority and interpretation

This document is the authoritative model for Rusty Mill's platform architecture. It defines the system's boundaries, layers, architectural entities, dependency rules, contract model, quality obligations, evolution process, ecosystem shape, and evidence chain.

Supporting documents provide rationale, templates, domain detail, research, and operational procedure. If a supporting document conflicts with this model, this model governs unless a later accepted ADR explicitly supersedes the relevant rule. Draft capability specifications cannot amend this model implicitly.

Normative terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express architectural obligations. Examples are illustrative unless labeled normative.

## 2. Mission and boundary

Rusty Mill is a Rust-first, high-performance, capability-based operating-system abstraction and application platform for native applications on Windows, Linux, and macOS.

Its central axiom is:

> **Abstract capabilities, not operating systems.**

Applications state the behavior and quality they require. Rusty Mill selects providers that realize those requirements with native mechanisms, while exposing unsupported behavior and meaningful variance instead of hiding them.

Rusty Mill is not:

- A kernel or replacement for operating-system system libraries.
- A one-for-one wrapper over Win32, POSIX, Cocoa, or another native API family.
- A lowest-common-denominator portability layer.
- A promise that different platforms have identical mechanisms or performance.
- Permission to create public APIs or crates before their contracts and boundaries are understood.

The working maxim is:

> **Specify completely. Implement faithfully. Verify continuously. Evolve deliberately.**

## 3. System context

```mermaid
flowchart LR
    Authors["Application authors"] -->|"requirements and profiles"| Mill["Rusty Mill semantic boundary"]
    Maintainers["Platform maintainers"] -->|"provider implementations"| Mill
    OS["Windows · Linux · macOS mechanisms"] -->|"native facilities"| Maintainers
    Mill -->|"Rust-native capabilities and services"| Apps["Native applications"]
    Mill -->|"contracts, conformance, benchmarks, provenance"| Evidence["Evidence and release claims"]
```

Application authors consume Rust-native capabilities, services, and frameworks. Platform maintainers implement backend contracts against operating-system mechanisms. Rusty Mill owns the semantic boundary between them and the evidence that the boundary is honored.

## 4. Architecture pyramid

![Seven-layer Rusty Mill architecture pyramid](../assets/architecture-pyramid.svg)

### 4.1 Layers

| Layer | Owns | Must not own |
|---|---|---|
| Applications | Product behavior and product policy | Portable OS mechanism abstractions |
| Domain frameworks | Application-oriented compositions and workflows | Backend selection or raw OS calls |
| Platform services | Coordination, orchestration, and policy across capabilities | Platform-specific mechanisms |
| Common APIs | Stable Rust-native interaction surfaces and semantic types | Native handles as the normal abstraction |
| Capability framework | Discovery, negotiation, authority, provider selection, lifecycle, and degradation reporting | Domain-specific application policy |
| Backend contracts | Provider obligations and adaptation boundary | Application workflows |
| OS backends | Native mechanism use, unsafe/FFI isolation, platform diagnostics | Portable policy or public semantic redefinition |

### 4.2 Dependency rules

1. Dependencies **MUST** point downward through the immediately adjacent layer.
2. A layer **MUST NOT** reach around an intermediate layer to use a lower implementation directly.
3. Shared specifications, schemas, test vectors, and evidence formats **MAY** remain dependency-neutral.
4. Backend-specific handles **MUST NOT** cross common APIs except through an explicitly specified escape hatch.
5. Domain logic **MUST** remain independent of OS APIs, FFI bindings, and I/O frameworks.
6. A cross-layer exception requires an accepted ADR, stated scope, and migration path.

The default deployment architecture is a modular monolith. A separate process or service requires a forcing function such as independent scaling, ownership, language boundary, privilege separation, or fault isolation.

## 5. Architectural entity model

```mermaid
flowchart LR
    Profile["Profile"] -->|"requires"| Capability["Capability"]
    Capability -->|"defined by"| Contract["Behavioral contract"]
    Capability -->|"exposed through"| Interface["Rust-native interface"]
    Provider["Provider / backend"] -->|"realizes"| Capability
    Provider -->|"proves with"| Evidence["Conformance evidence"]
    Policy["Policy"] -->|"selects under"| Authority["Authority"]
    Authority --> Provider
    Capability -->|"governs"| Resource["Resource"]
    Capability -->|"emits or observes"| Event["Event"]
    Service["Platform service"] -->|"composes"| Capability
    Framework["Domain framework"] -->|"composes services and"| Capability
```

### 5.1 Capability

The smallest independently describable, selectable, securable, testable, and evolvable unit of platform behavior. A capability describes an outcome, not an OS symbol, crate, trait, or implementation.

Stable identity uses `rm.<domain>.<capability>`. Contract versions attach to the identity using SemVer. A capability specification records purpose, non-goals, maturity, owner, dependencies, semantics, authority, quality levels, platform mappings, verification, and history.

### 5.2 Behavioral contract

The normative definition of what consumers may rely on and providers must prove. It covers:

- Preconditions, outputs, invariants, guarantees, and non-guarantees.
- Resource ownership, borrowing, transfer, cleanup, and behavior after failure.
- Ordering, concurrency, thread safety, reentrancy, fairness, and atomicity.
- Async and sync behavior, blocking, cancellation, and backpressure.
- Typed errors, partial completion, recovery, retry safety, and idempotency.
- Authority, privilege, trust boundaries, and sensitive information.
- Performance, accessibility, internationalization, and observability.
- Platform realization, emulation, degradation, and incompatibility.
- Compatibility, deprecation, conformance assertions, and benchmarks.

Every normative statement receives a stable identifier of the form `RM-<DOMAIN>-<CAPABILITY>-<NNNN>`. Identifiers survive editorial movement and are never reused after retirement.

### 5.3 Interface

The Rust-native typed surface through which a consumer uses a contract. Interface design follows accepted semantics. A public type or trait is not itself the contract and cannot silently strengthen or weaken it.

### 5.4 Provider and backend

A provider realizes one or more capabilities. An OS backend is a provider at the native platform boundary. Providers declare exact contract versions, quality levels, platform constraints, and evidence. Selection is based on requirements and evidence, not OS name alone.

### 5.5 Resource

An owned or borrowed entity with explicit lifetime, authority, concurrency, cancellation, and cleanup rules. Illegal resource states should be unrepresentable where practical. Native resource identities stay behind the backend boundary unless an escape contract says otherwise.

### 5.6 Event

A typed observation of a transition or external occurrence. Contracts define ordering, duplication, loss, backpressure, timestamp domain, delivery context, and shutdown behavior.

### 5.7 Policy

A separately configurable rule governing provider selection, authority, fallback, quality, budgets, or orchestration. Backends implement mechanism; policy chooses acceptable behavior. Policy must not be hidden in platform-specific code.

Security policy evaluation is advisory: it may return permit, deny, indeterminate, or not-applicable with provenance and freshness, but the protected native operation remains the authorization point. A prior permit never guarantees later success ([ADR-0010](../adr/0010-native-operation-is-the-authorization-point.md)).

### 5.8 Service

A cohesive runtime facility that coordinates multiple capabilities, resources, and policies. Coordination belongs in a service when placing it in a base capability would create dependency cycles or mix independent lifecycles.

### 5.9 Domain framework

An application-oriented composition above platform services. Frameworks may offer opinionated workflows but cannot redefine capability guarantees.

### 5.10 Profile

A named, versioned declaration of required, conditional, optional, and prohibited capabilities and services, contract ranges, quality levels, and security constraints for a workload class. Initial foundation profile families are CLI, Desktop, Server, and Embedded/headless; their current exact membership is specified while missing application domains remain explicit gaps.

Profiles select exact capability contracts and platform services—not undifferentiated domains, crates, or OS features. Members are required, conditional, optional, or prohibited and carry independent quality, authority, interaction, budget, degradation, and evidence constraints. Current `foundation` profiles preserve explicit domain gaps and cannot imply complete application support. Satisfied resolution produces an immutable evidence-bound report ([ADR-0013](../adr/0013-profiles-select-contracts-not-domains.md)).

## 6. Capability dependency graph

The graph is a versioned architecture artifact derived from capability specifications.

### 6.1 Edge types

- `requires`: the source cannot satisfy its minimum contract without the target.
- `optionally-uses`: the target improves quality or enables declared optional behavior.
- `conflicts-with`: the specified nodes or versions cannot coexist under stated conditions.

Edges may carry version constraints, conditions, rationale, and requirement identifiers.

### 6.2 Invariants

1. The directed `requires` subgraph **MUST** be acyclic.
2. Every edge **MUST** appear in the source specification.
3. A required edge **MUST** target the narrowest sufficient capability.
4. An optional edge **MUST NOT** silently change minimum guarantees.
5. A conflict **MUST** state whether it is semantic, authority, resource, or transitional.
6. OS names, crate names, and implementation symbols **MUST NOT** be graph targets.
7. Resolution **MUST** produce a satisfiable graph or diagnostics for every unsatisfied constraint.

Required cycles indicate an incorrect capability boundary or orchestration that belongs in a service.

## 7. Capability availability and negotiation

Provider availability is one of:

- **Native:** satisfied using a first-class platform mechanism.
- **Emulated:** satisfied with explicitly documented cost or limitations.
- **Degraded:** a declared weaker quality level remains within the contract.
- **Unavailable:** requested semantics or quality cannot be satisfied.

Unknown is a research/specification state, not a runtime availability claim.

Resolution consumes a profile or explicit requirements plus policy and authority. It returns selected providers, exact versions and quality levels, emulation/degradation disclosures, and diagnostics for unsatisfied constraints. Silent fallback or silent weakening is prohibited.

```mermaid
flowchart TD
    Request["Profile or explicit requirements"] --> Expand["Expand transitive required capabilities"]
    Expand --> Discover["Discover eligible providers and evidence"]
    Discover --> Authority["Apply authority and security policy"]
    Authority --> Quality["Match contract versions and quality levels"]
    Quality --> Satisfiable{"All constraints satisfied?"}
    Satisfiable -->|"yes"| Selection["Selected providers + exact versions"]
    Selection --> Disclosure["Native, emulated, and degraded disclosures"]
    Satisfiable -->|"no"| Diagnostic["Structured unsatisfied-constraint report"]
```

## 8. Portability and platform variance

Portability means stable promised semantics, explicit discovery, typed failures, declared variance, and testable behavior—not identical implementation.

Each capability classifies its expected Windows, Linux, and macOS realization and records native mechanisms as research. Platform-specific extensions are permitted when a truthful common contract is impossible. Consumers opt into them explicitly; their presence cannot be inferred merely from OS identity.

Escape hatches must preserve ownership and safety, declare lost portability, and avoid making common paths depend on native handles.

Filesystem paths are lossless platform-native semantic values, not necessarily Unicode strings. Display conversion, normalization, case behavior, and object identity are separate concerns ([ADR-0006](../adr/0006-paths-are-lossless-native-values.md)). Security-sensitive filesystem lookup begins from explicit directory authority and uses declared handle-relative resolution strength; lexical canonicalization alone cannot prove containment ([ADR-0007](../adr/0007-directory-relative-resolution-is-the-security-boundary.md)).

Filesystem namespace visibility, atomicity, and durability are distinct guarantees. Atomic same-filesystem replacement remains a capability; stronger durable publication may compose it with file/directory synchronization as a platform service ([ADR-0008](../adr/0008-atomic-replacement-is-a-capability.md)). Providers declare resolution quality and durability level against exact filesystem and storage contexts rather than inheriting guarantees from OS identity.

Portable process creation begins with direct launch of an explicit executable, structured native arguments, explicit environment construction, and allowlisted inheritance. Shell parsing, executable search, activation, elevation, and durable service registration are separate opt-in contracts. Where an OS requires command-line serialization, providers declare the target parsing convention and cannot claim universal round-trip fidelity ([ADR-0014](../adr/0014-direct-process-launch-is-the-base-contract.md)).

Executable resolution is separate from launch and consumes explicit ordered directory authority; ambient path/current-directory search is not a base behavior ([ADR-0016](../adr/0016-executable-search-uses-explicit-authority.md)). Control of one owned child is a capability. Supervision of a dynamic process set is a platform service with scoped containment evidence; observed ancestry cannot be represented as a universally contained process tree ([ADR-0015](../adr/0015-process-set-supervision-is-a-service.md)).

Anonymous byte pipes are independent IPC capabilities with directional ownership, EOF, broken-peer, backpressure, atomicity, and async quality semantics. Process spawning only binds compatible endpoints; multi-process pipeline lifecycle is a service/framework composition ([ADR-0017](../adr/0017-byte-pipes-are-independent-ipc-capabilities.md)).

Pseudoterminals are stateful protocol-bearing terminal resources, not byte pipes. Their capability owns attachment, character-cell size, wire profile, terminal state, transport, resize, and hangup. A terminal session service composes process launch/supervision; emulation, rendering, structured input, Unicode layout, and accessible presentation remain higher layers with separate evidence ([ADR-0018](../adr/0018-pseudoterminals-are-not-byte-pipes.md)).

Terminal emulation is a domain framework above the terminal session boundary. Portable parser/state, structured input, renderer and accessibility adapters, privileged-effect policy, and recording remain narrow framework/service contracts. OS backends cannot redefine emulator semantics, and no component's conformance implies whole-terminal-product conformance ([ADR-0019](../adr/0019-terminal-emulation-is-a-domain-framework.md)).

Portable window state is negotiated rather than synchronously assigned. Requests and effective native state are distinct; logical extent, scale/transform, surface extent, display association, and presentation-surface generation are committed atomically in revisioned snapshots. Native callback reentrancy is contained behind ordered portable delivery, and exact placement/global coordinates remain optional provider claims ([ADR-0020](../adr/0020-window-state-is-negotiated.md)).

Window logical, surface-pixel, display-logical, and backend-native coordinates are distinct spaces. Conversion uses an explicit revision-bound transform and declared rounding; physical DPI and global placement are optional observations rather than universal truths ([ADR-0021](../adr/0021-coordinate-spaces-are-typed.md)). Windowing owns presentation-surface lifetime and generation, while graphics owns rendering and presentation mechanics.

Graphics providers are selected against exact versioned workload vectors rather than API names or a scalar acceleration label. The base architecture does not standardize a universal rendering command interface before multiple concrete renderers establish shared semantics ([ADR-0022](../adr/0022-graphics-selection-uses-workload-contracts.md)). Devices, queues, resources, synchronization, and evidence are scoped to immutable device epochs; loss requires explicit terminal classification and re-resolution.

Windowing owns the presentation-surface generation. A graphics presentation service composes that surface with device, queue, image-pool, synchronization, color, and frame policy. Frame leases are bounded; submission, presentation acceptance, and observed display are distinct milestones; reconfiguration creates a new session generation ([ADR-0023](../adr/0023-presentation-is-a-graphics-service.md)).

Keyboard observations and text input are separate coordinated contracts. Physical control, logical key meaning, modifier/layout revision, provisional composition, and committed Unicode text remain distinguishable. A text-input service owns focused editable-target context, surrounding-text disclosure, caret/selection geometry, composition, commit, and cancellation; backends do not synthesize committed text by blindly mapping keys ([ADR-0024](../adr/0024-text-input-is-not-keyboard-input.md)).

Input provenance is evidence rather than authority. Hardware-associated, OS/accessibility, remote, replayed, application-synthetic, and unknown origins remain explicit; security-sensitive actions authorize independently. Focused input, background observation, capture/lock/confinement, and injection are separately negotiated capabilities with independent authority ([ADR-0025](../adr/0025-input-provenance-is-not-authority.md)).

Semantic Unicode text remains authoritative across editing, text services, layout, accessibility, search, and copy. Glyphs, pixels, bidi visual order, and generated layout content are derived artifacts with explicit revisioned mappings; glyph IDs are local to one exact font face instance ([ADR-0026](../adr/0026-semantic-text-is-not-glyph-output.md)). Every position/range names its encoding or semantic unit and text revision.

Font discovery/resolution precedes reproducible shaping. It converts policy plus a versioned collection snapshot into an immutable ordered plan of exact artifact, face, variation, fallback, trust, and license identities. Shaping consumes that plan without ambient discovery or network access ([ADR-0027](../adr/0027-font-resolution-precedes-shaping.md)). Segmentation, bidi, shaping, line layout, and rasterization remain separately versioned stages.

Accessibility semantics are application/domain state independent of renderer output and native API vocabularies. Applications publish immutable revisioned roles, states, relationships, focus, text/ranges, geometry, actions, and live-update intent; UI Automation, AT-SPI, and macOS Accessibility are adapter mappings with declared variance ([ADR-0028](../adr/0028-accessibility-semantics-are-domain-state.md)). Pixels, glyphs, and untrusted content cannot establish privileged semantic truth.

Accessibility invocations become versioned semantic action requests through the ordinary domain command path. They retain provenance but do not grant authority or bypass state, confirmation, sandbox, destructive-operation, or audit policy. Request acceptance, command completion, state commitment, and native notification are separate milestones ([ADR-0029](../adr/0029-accessibility-actions-use-domain-command-path.md)).

Clipboard and drag-and-drop compose immutable typed data offers whose metadata can be inspected without rendering payloads. Materialization requests one exact representation under explicit size, time, resource, destination, authority, and conversion policy and returns a bounded async stream. Conversion provenance and source/offer lifetime remain explicit ([ADR-0030](../adr/0030-data-transfer-uses-lazy-typed-offers.md)).

Cross-application move is a committed transfer, not a gesture result. The target selects, materializes, validates, and commits content before acknowledging success; only then may the source apply declared deletion/mutation. Target commit and source cleanup failures remain separate outcomes, and global atomicity is not implied ([ADR-0031](../adr/0031-move-is-a-committed-transfer.md)).

Locale-sensitive operations consume an immutable explicit locale context resolved from versioned user-preference snapshots, application policy/resources, and exact Unicode/CLDR/time-zone/provider data. Requested resource language, formatting region, script, calendar, numbering, collation, measurement, and time zone remain distinct, and preference/data changes create new coordinated contexts rather than mutating ambient process behavior ([ADR-0032](../adr/0032-locale-sensitive-operations-use-explicit-context.md)).

Localized formatting is human presentation, not canonical serialization, identity, database/protocol data, signature input, filesystem semantics, or a guaranteed parse round trip. Parsing and collation are explicit versioned contracts with ambiguity and scope; collation equivalence never establishes security or object identity ([ADR-0033](../adr/0033-localized-output-is-not-canonical-data.md)).

## 9. Execution and concurrency model

Rusty Mill is **async-first and sync-complete**.

1. Potentially blocking capabilities **MUST** provide an async path that does not occupy a worker thread solely while waiting when native completion/readiness is available.
2. Stable capabilities **MUST** document a synchronous path.
3. Sync implementations **MUST NOT** create or nest a hidden async runtime.
4. Async implementations **MUST** define cancellation safety, completion ownership, executor assumptions, and backpressure.
5. Sync and async paths **MUST** share behavioral guarantees unless the contract explicitly documents a difference.
6. Thread safety, ordering, reentrancy, and fairness are contract properties, not framework assumptions.

Cancellation is cooperative unless an operation contract proves stronger native behavior. A cancellation request races with normal completion and is not confirmation that an operation was aborted.

## 10. Cross-cutting quality obligations

Every capability, profile, backend, service, framework, and stable release addresses these dimensions or gives a reviewable reason they do not apply.

### 10.1 Security

- Capability possession and authority are distinct where useful.
- Least privilege and safe defaults are mandatory.
- External input is validated at boundaries.
- Unsafe and native boundaries are isolated, documented, reviewed, and tested.
- Sensitive operations provide auditability without exposing secrets.
- Threat assumptions and degradation effects are explicit.

Principal claims, security-context snapshots, authority, grants, and constraints are distinct. Identity does not confer authority. Security-sensitive base contracts accept explicit resource- and operation-scoped authority where practical; portable derivation is attenuation-only; constraints compose by intersection; and missing required evidence fails closed ([ADR-0009](../adr/0009-identity-is-not-authority.md)). Authority is not serializable or transferable unless a dedicated contract defines its security properties.

Restricted execution is a platform service rather than a scalar capability. It composes process creation, authority attenuation, explicit inheritance, native isolation, readiness, and supervision from an immutable deny-by-default manifest. Required restrictions are applied and verified before child-controlled code runs; degradation requires prior policy permission ([ADR-0011](../adr/0011-restricted-execution-is-a-platform-service.md)).

Secret protection is negotiated as a scoped vector of persistence, boundary, subject binding, interaction, exportability, availability, replication, deletion, and assurance—not as a boolean or total security level. Unknown dimensions fail required constraints. Secret-value exposure semantics and secret-store persistence semantics remain distinct ([ADR-0012](../adr/0012-secret-protection-is-a-vector.md)).

### 10.2 Performance

- Native performance is a requirement, not an unsupported claim.
- Avoidable allocations, copies, indirection, context switches, and wakeups are measured and minimized.
- Benchmarks separate native baseline, abstraction overhead, and end-to-end workload.
- Latency distributions, throughput, memory, allocation, startup, binary size, CPU, and power are measured where relevant.
- Regression budgets are capability-specific and evidence-based.

### 10.3 Accessibility

User-facing capabilities preserve semantic roles, focus, input behavior, assistive-technology integration, user preferences, and accessible fallback behavior.

### 10.4 Internationalization

Text, locale, time, collation, input, and layout behavior avoids implicit host-locale assumptions. Encoding, normalization, directionality, and formatting semantics are explicit.

### 10.5 Observability

Diagnostics use stable structured events, correlation, and causal context. Instrumentation is low-overhead, privacy-aware, exporter-neutral, and optional where the contract permits.

## 11. Specification and maturity lifecycle

Capabilities progress through:

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Experimental: "contract trial and evidence plan"
    Experimental --> Draft: "semantic revision"
    Experimental --> Stable: "all promotion gates pass"
    Stable --> Deprecated: "replacement and migration accepted"
    Deprecated --> Retired: "support window closes"
    Stable --> Stable: "compatible evolution"
```

- **Draft:** semantics are being discovered; no compatibility promise.
- **Experimental:** implementation may exist for learning; interfaces can change.
- **Stable:** contract and compatibility promises are active.
- **Deprecated:** supported temporarily with replacement and migration path.
- **Retired:** no longer supported; identifiers and history remain reserved.

Stable promotion requires accepted semantics, supported-platform providers, profile analysis, security and quality review, compatibility policy, conformance coverage, benchmark baselines, ownership, and release evidence.

Disposable research spikes are allowed but cannot establish stable precedent or become dependencies of stable code without review.

## 12. Architecture governance

### 12.1 Decision instruments

- **Architecture model:** current normative system rules.
- **ADR:** immutable record of a durable decision, alternatives, and consequences.
- **RFC:** reviewed proposal for new stable capabilities, public contracts, cross-repository changes, governance, compatibility, or delivery mechanisms.
- **Capability specification:** normative domain behavior after acceptance.
- **Research note:** descriptive evidence without decision authority.

### 12.2 Change procedure

A model change requires:

1. An ADR or RFC stating the affected rule, alternatives, and consequences.
2. Impact analysis across capabilities, profiles, security, performance, compatibility, repositories, conformance, benchmarks, and releases.
3. Review by the relevant architecture and specialist owners.
4. An atomic update to this document and affected elaborations.
5. Migration guidance when stable consumers or providers are affected.

Accepted ADRs preserve why the model changed. This document preserves what the architecture currently is.

## 13. Evidence and traceability

```mermaid
flowchart TD
    Charter["Charter and principles"] --> Model["Authoritative architecture model"]
    Decision["Accepted ADR / RFC"] -->|"amends with rationale"| Model
    Model --> Capability["Capability requirement"]
    Model --> Profile["Profile requirement"]
    Capability --> Assertion["Conformance assertion"]
    Profile --> ProfileConformance["Profile conformance"]
    Assertion --> ProviderEvidence["Provider evidence"]
    ProfileConformance --> ProviderEvidence
    ProviderEvidence --> Release["Release claim"]
    Benchmark["Benchmark result"] --> Release
    Security["Security evidence"] --> Release
    Provenance["Artifact digest · provenance · SBOM"] --> Release
```

### 13.1 Rules

1. A Stable normative requirement **MUST** have a verification method or documented justification for manual evidence.
2. A passing test establishes no promise unless it traces to a normative requirement.
3. Benchmarks identify workload, environment, baseline, contract version, and statistical method.
4. Provider claims identify provider version, platform, architecture, configuration, and evidence.
5. Waivers are explicit, owned, time-bounded, and visible in release claims.
6. Release claims bind evidence to immutable artifact digests and provenance.

## 14. Conformance and benchmark architecture

Contract assertions are backend-neutral. Provider adapters supply setup and platform evidence without changing expected semantics. Suites cover success, failure, boundaries, cancellation, concurrency, cleanup, security, and declared degradation.

Benchmarks compare an idiomatic native baseline, Rusty Mill abstraction path, and representative workload separately. Results include environmental variance and do not compare unlike guarantees.

Stable release gates include required-profile conformance, security and compatibility checks, supply-chain evidence, and performance within accepted budgets. Exceptions require a time-bounded decision with owner and remediation.

## 15. Ecosystem and repository architecture

Repository boundaries follow cohesion, ownership, release cadence, native toolchain boundaries, security isolation, and independent lifecycle—not one repository per concept.

```mermaid
flowchart TB
    AKB["Foundation AKB"] --> Specs["Versioned specifications"]
    Specs --> Core["Core platform workspace"]
    Specs --> Verification["Conformance and benchmarks"]
    Core --> Windows["Windows backend"]
    Core --> Linux["Linux backend"]
    Core --> MacOS["macOS backend"]
    Core --> Services["Platform services"]
    Services --> Frameworks["Domain frameworks"]
    Frameworks --> Apps["Applications"]
    Verification -.->|"validates"| Windows
    Verification -.->|"validates"| Linux
    Verification -.->|"validates"| MacOS
    Tooling["Build, release, and diagnostic tooling"] -.->|"supports"| Core
    Tooling -.->|"publishes evidence"| Verification
```

Repository classes may include the foundation AKB, specifications, core platform, backends, frameworks, verification, and tooling. Start cohesive work as a modular monolith. Extract only when a concrete forcing function appears.

Crates have one coherent responsibility and narrow typed interfaces. Workspaces group shared build, test, and release mechanics. Public semantic types live above backend implementations. Platform bindings remain private where possible. Feature flags are additive capability selection, not incompatible product modes. Final names and boundaries require evidence from at least two real call sites or an accepted RFC.

Documentation flows from this model to domain specifications, capability contracts, repository guides, crate/API documentation, and operational runbooks. Lower levels add detail but cannot contradict higher-level rules.

## 16. Compatibility, packaging, and supply chain

SemVer applies to independently published crates and versioned contracts, but behavioral compatibility matters in addition to Rust signatures. Coordinated release labels do not require every repository to share a version.

Release artifacts include appropriate checksums, licenses, debug information, SBOMs, and provenance. Applications use authenticated updates, signed manifests, staged rollout, rollback, and downgrade protection where required. Update mechanism and product update policy remain separate.

CI and release inputs are pinned; third-party dependencies are minimized and reviewed. Publishing credentials use least privilege. Reproducibility, vulnerability response, license policy, signing-key rotation, and maintainer recovery are designed before production release.

## 17. Current application of the model

The [runtime and time vertical slice](../02-capabilities/runtime-time/README.md) is the first trial. Its monotonic-clock, deadline-timer, cancellation, and orderly-shutdown documents exercise the entity, dependency, service, contract, quality, and evidence rules. [ADR-0005](../adr/0005-orderly-shutdown-is-a-platform-service.md) classifies orderly shutdown as a platform service rather than a capability. The specifications remain Draft and cannot amend this model.

The [filesystem foundations vertical slice](../02-capabilities/filesystem/README.md) is the second trial. It exercises lossless semantic values, directory authority, race-resistant resolution, resource identity and lifetime, partial asynchronous I/O, metadata availability, namespace atomicity, and durability boundaries. Its specifications remain Draft and cannot amend this model.

The [windowing foundations vertical slice](../02-capabilities/windowing/README.md) defines negotiated top-level window state, display topology, typed coordinate spaces, event delivery, and generation-scoped presentation surfaces. Graphics, input interpretation, widget layout, and application accessibility content remain separate domains. Its specifications remain Draft and cannot amend this model.

The [graphics and presentation vertical slice](../02-capabilities/graphics/README.md) defines workload-vector resolution, device epochs, resource memory, explicit submission/synchronization, bounded frame scheduling, and a presentation service over window surfaces. Rendering command models, shaders, text, UI scenes, and codecs remain unresolved pending concrete workload evidence. Its specifications remain Draft and cannot amend this model.

The [input foundations vertical slice](../02-capabilities/input/README.md) defines keyboard, pointer, touch, focus/capture routing, provenance, and a revision-bound text composition service. Shortcut resolution, widget focus, editing behavior, gestures, terminal encoding, and input injection remain higher-layer or separate capability concerns. Its specifications remain Draft and cannot amend this model.

The [text, fonts, and layout vertical slice](../02-capabilities/text/README.md) defines typed Unicode positions, exact font resolution, shaping/cluster maps, bidi/line layout, caret/hit-test geometry, and rasterization boundaries. Editing models, widget semantics, application localization content, and platform accessibility adapters remain separate concerns. Its specifications remain Draft and cannot amend this model.

The [accessibility foundations vertical slice](../02-capabilities/accessibility/README.md) defines application-owned semantic trees, accessible text ranges, focus/actions/events/live updates, user preferences, virtualization, and native adapter services. It requires end-to-end assistive-technology evidence in addition to headless semantic tests. Its specifications remain Draft and cannot amend this model.

The [clipboard and drag-and-drop data-transfer vertical slice](../02-capabilities/data-transfer/README.md) defines typed lazy offers, clipboard ownership/generations, drag negotiation and commit, file/content promises, streaming, authority, privacy, accessibility, interoperability, and failure recovery. Data remains untrusted at every cross-process boundary. Its specifications remain Draft and cannot amend this model.

The [internationalization and localization vertical slice](../02-capabilities/internationalization/README.md) defines locale preference snapshots/contexts, resource and typed-message resolution, formatting/parsing, calendar/time-zone behavior, collation/search, data-version evidence, pseudolocalization, and live preference/resource changes. Its specifications remain Draft and cannot amend this model.

The [configuration and change-notification vertical slice](../02-capabilities/configuration/README.md) defines typed versioned schemas, explicit source plans and provenance, coherent immutable snapshots, validation and reload policy, secret-reference boundaries, and reconciliation after native invalidation or loss. Native notifications trigger re-read and convergence; they are not represented as a lossless cross-platform write journal ([ADR-0034](../adr/0034-configuration-publishes-validated-snapshots.md), [ADR-0035](../adr/0035-configuration-notifications-trigger-reconciliation.md)). Its specifications remain Draft and cannot amend this model.

The [observability, diagnostics, and crash-reporting vertical slice](../02-capabilities/observability/README.md) defines stable structured event schemas, explicit causal context and clock quality, bounded metrics/tracing pipelines, exporter-independent production, diagnostic bundles, privacy governance, loss accounting, and a minimal separated fatal-capture path. Telemetry is evidence rather than authority, exporter acceptance is not backend durability, and raw crash memory is restricted diagnostic data ([ADR-0036](../adr/0036-observability-producers-are-exporter-independent.md), [ADR-0037](../adr/0037-fatal-capture-is-a-minimal-separated-path.md)). Its specifications remain Draft and cannot amend this model.

The [application lifecycle and session-integration vertical slice](../02-capabilities/lifecycle/README.md) defines application-instance epochs, typed activation, session/power observations, cooperative termination and scoped inhibition, readiness milestones, and disposable restoration metadata. No lifecycle callback is a portable cleanup guarantee; durable state is committed during ordinary operation and orderly shutdown runs only when the observed native request permits it ([ADR-0038](../adr/0038-lifecycle-events-do-not-guarantee-cleanup.md), [ADR-0039](../adr/0039-restoration-state-is-disposable-continuity-metadata.md)). Its specifications remain Draft and cannot amend this model.

The [networking foundations vertical slice](../02-capabilities/networking/README.md) defines service intent and endpoint types, expiring resolution candidates, bounded connection racing, full-duplex byte streams, datagrams, listeners, path observations, and secure-channel composition. Resolution is neither identity nor authority; transport establishment, cryptographic security, peer authentication, and application readiness are separate milestones ([ADR-0040](../adr/0040-resolution-results-are-candidates-not-authority.md), [ADR-0041](../adr/0041-secure-channels-compose-over-transports.md)). Its specifications remain Draft and cannot amend this model.

The [memory and mapping foundations vertical slice](../02-capabilities/memory/README.md) defines virtual-region state, file and shared mappings, protection, residency/discard controls, allocation-service boundaries, and separately authorized executable-memory publication. Address reservation, backing commitment, residency, locking, and durability are independent claims; mapped bytes do not automatically form safe typed Rust objects ([ADR-0042](../adr/0042-address-reservation-is-not-memory-commitment.md), [ADR-0043](../adr/0043-executable-memory-is-a-separate-authorized-service.md)). Its specifications remain Draft and cannot amend this model.

The [plugin and module lifecycle vertical slice](../02-capabilities/plugins/README.md) defines immutable package identity/provenance, metadata-only discovery, interface and dependency resolution, trust/isolation classes, attenuated authority, lifecycle generations, staged updates, rollback, and supply-chain evidence. In-process native plugins are fully trusted host components rather than a sandbox, and updates use immutable generation replacement rather than assuming unload safety ([ADR-0044](../adr/0044-in-process-native-plugins-are-fully-trusted.md), [ADR-0045](../adr/0045-plugin-updates-use-generation-replacement.md)). Its specifications remain Draft and cannot amend this model.

The [threading and synchronization foundations vertical slice](../02-capabilities/threading/README.md) defines native thread lifecycle, mutex/reader-writer lock semantics, condition/semaphore/event waiting, Rust-model atomics, scheduling/affinity/realtime requests, and thread-local lifecycle. Scheduling controls are scoped requests rather than execution guarantees, and poisoning is optional application consistency policy rather than base lock semantics ([ADR-0046](../adr/0046-scheduling-controls-are-scoped-requests.md), [ADR-0047](../adr/0047-poisoning-is-consistency-policy-not-lock-semantics.md)). Its specifications remain Draft and cannot amend this model.

The [audio foundations vertical slice](../02-capabilities/audio/README.md) defines generation-scoped endpoints, exact PCM formats, render/capture streams, explicit routing, device-sample clocks, monotonic correlation, XRUN/discontinuity evidence, and restricted realtime processing. Stream progress follows the device sample clock rather than inferred wall time, and realtime callbacks use a bounded data plane separated from control-plane work ([ADR-0048](../adr/0048-audio-stream-time-follows-the-device-sample-clock.md), [ADR-0049](../adr/0049-realtime-audio-callbacks-are-a-restricted-execution-domain.md)). Codecs, containers, MIDI, speech, and general media graphs remain separate. Its specifications remain Draft and cannot amend this model.

The [device discovery and hardware-change foundations vertical slice](../02-capabilities/devices/README.md) defines scoped queries, coherent revisioned snapshots, generation-bound references, typed/provenanced properties and topology, change reconciliation, privacy, and class-specific handoff. Native identifiers are identity evidence rather than universal physical identity, and device notifications trigger reconciliation rather than forming a portable lossless journal ([ADR-0050](../adr/0050-device-identity-is-generation-scoped-evidence.md), [ADR-0051](../adr/0051-device-notifications-trigger-reconciliation.md)). Device-class protocols and authority remain separate. Its specifications remain Draft and cannot amend this model.

The [asynchronous I/O foundations vertical slice](../02-capabilities/async-io/README.md) defines completion-oriented operations over native completion engines, readiness translation, and disclosed blocking adapters; exact terminal progress; registration/resource generations; bounded load; runtime separation; cancellation lifetime; observability; conformance; and benchmarks. Readiness remains a backend hint rather than portable completion, and cancellation does not release operation-owned state before terminal acknowledgement ([ADR-0052](../adr/0052-portable-asynchronous-io-is-completion-oriented.md), [ADR-0053](../adr/0053-cancellation-does-not-end-operation-lifetime.md)). Domain capabilities retain their own I/O semantics. Its specifications remain Draft and cannot amend this model.

The [storage volumes and removable-media foundations vertical slice](../02-capabilities/storage/README.md) defines distinct device/media/region/filesystem/mount entities, namespace-scoped observation, capacity/properties, mount arbitration, staged removal, durability evidence, authority, accessibility, conformance, and benchmarks. A mount is a namespace relationship rather than volume identity, and safe removal is observable coordination rather than a stronger durability or continued-presence guarantee ([ADR-0054](../adr/0054-a-mount-is-a-namespace-relationship-not-volume-identity.md), [ADR-0055](../adr/0055-safe-removal-is-coordination-not-a-durability-guarantee.md)). Destructive storage management remains separate. Its specifications remain Draft and cannot amend this model.

The [camera and media-capture foundations vertical slice](../02-capabilities/capture/README.md) defines side-effect-free camera observation, explicit revocable capture authority, negotiated session generations, exact raw frame/color/orientation layouts, capture clocks, controls, bounded delivery, privacy/accessibility, conformance, and benchmarks. Capture authority is revalidated per session, while raw capture remains distinct from preview, still processing, encoding, recording, transport, and storage ([ADR-0056](../adr/0056-capture-authority-is-session-scoped-and-revocable.md), [ADR-0057](../adr/0057-raw-capture-is-not-recording-or-encoding.md)). Its specifications remain Draft and cannot amend this model.

## 18. Deliberately unresolved choices

This model does not yet choose:

- Rust trait, type, or error representations.
- Crate and workspace names or final repository boundaries.
- Runtime or executor implementation.
- Machine-readable metadata serialization.
- Minimum supported OS versions.
- Exact membership of workload profiles.
- Whether every candidate composition is a capability, service, or framework.

Those choices require domain evidence and the ADR/RFC process. Deferring them is part of the architecture, not missing authority.

## 19. Supporting elaborations

- [Architecture overview](overview.md)
- [Behavioral contracts](behavioral-contracts.md)
- [Cross-cutting qualities](cross-cutting-qualities.md)
- [Capability model](../02-capabilities/model.md)
- [Capability graph model](../02-capabilities/graph-model.md)
- [Capability profiles](../02-capabilities/profiles.md)
- [Repository strategy](../04-ecosystem/repository-strategy.md)
- [Verification architecture](../04-ecosystem/verification.md)
- [Traceability model](../04-ecosystem/traceability.md)
- [Delivery strategy](../03-delivery/strategy.md)
- [Governance](../05-governance/governance.md)

These documents should link to this model and elaborate their subject without independently redefining it.
