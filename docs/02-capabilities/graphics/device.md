# `rm.graphics.device`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

## Negotiation

A workload requirement identifies operation families, formats, limits, queue classes, memory properties, synchronization primitives, presentation needs, power preference, latency policy, protected-content needs, and acceptable emulation/degradation. Resolution returns an exact immutable device contract and evidence—not a mutable bag of guessed support.

**RM-GRAPHICS-DEVICE-0001:** Device enumeration returns opaque adapter identities, provider identity/version, driver evidence, device class, power/removability facts, memory-budget availability, supported contract versions, and feature/limit vectors with known/unknown provenance.

**RM-GRAPHICS-DEVICE-0002:** Selection evaluates the complete workload requirement and target presentation-surface compatibility before publishing a device. Unknown required features fail resolution; optional features do not silently change minimum guarantees.

**RM-GRAPHICS-DEVICE-0003:** The selected device exposes one immutable capability snapshot and monotonically increasing device epoch. Native capability queries remain backend evidence and do not leak as the portable contract.

**RM-GRAPHICS-DEVICE-0004:** Device creation declares validation/debug behavior, robustness/isolation, compilation/cache policy, memory budget, power preference, queue topology, and recovery policy. Debug behavior cannot silently alter stable semantics.

**RM-GRAPHICS-DEVICE-0005:** Device loss transitions the epoch exactly once to `lost`, records a structured reason where safely available, rejects new work, and resolves outstanding work as completed, cancelled, or indeterminate without claiming execution that cannot be proven.

**RM-GRAPHICS-DEVICE-0006:** Recovery creates a new device epoch through normal resolution. Resources, pipelines, queues, synchronization objects, and presentation sessions from the old epoch never become valid merely because the same physical adapter returns.

**RM-GRAPHICS-DEVICE-0007:** Adapter migration and software fallback require policy permission and a new resolution report disclosing changed features, formats, performance, color behavior, power, and protection properties.

**RM-GRAPHICS-DEVICE-0008:** Native handles, driver strings, hardware identifiers, fault data, and memory telemetry are privacy/security-sensitive. Diagnostics are bounded and redact application content, shader source, and resource bytes by default.

**RM-GRAPHICS-DEVICE-0009:** Destruction is idempotent, does not wait indefinitely for a hung device, and reports whether outstanding work was drained, abandoned, or indeterminate.

## Quality vector

Quality is expressed by acceleration class, feature fidelity, robustness, queue concurrency, memory visibility/budget precision, compilation behavior, presentation modes, timing quality, color/HDR, power class, protected-content properties, validation availability, and recovery evidence.

