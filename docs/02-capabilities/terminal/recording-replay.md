# Terminal recording and replay platform service

| Field | Value |
|---|---|
| Status | Draft service contract |
| Contract version | 0.1.0 |
| Layer | Platform services |

## Purpose

Capture an explicitly authorized terminal event stream for diagnostics, audit, support, or reproducible emulator replay under strict confidentiality, integrity, retention, and disclosure policy.

Recording is not observability-by-default, keylogging, a substitute for process audit, or proof of deterministic live-process re-execution.

## Event model

Events may include monotonic timestamp/delta, session metadata, output bytes, structured input or redacted input markers, resize, emulator configuration/dialect, policy decisions, control actions, child/session milestones, semantic marks, checkpoints, gaps, and terminal result. Each event has sequence, schema version, sensitivity class, and integrity-chain position.

## Requirements

- **RM-TERMINAL-RECORD-0001:** Recording **MUST** be disabled unless explicit capture authority, purpose, subject/user disclosure policy, data classes, and destination protection claims are satisfied.
- **RM-TERMINAL-RECORD-0002:** Input, output, metadata, clipboard, title/path, and semantic marks **MUST** have independent include/redact/omit policies; enabling output **MUST NOT** enable input.
- **RM-TERMINAL-RECORD-0003:** Secure/password input mode **MUST** suppress input capture and emit only a non-sensitive gap marker where policy requires chronology.
- **RM-TERMINAL-RECORD-0004:** The stream **MUST** bind schema, dialect, Unicode/width policy, initial size/state, clock domain, provider versions, and configuration required for declared replay fidelity.
- **RM-TERMINAL-RECORD-0005:** Event ordering, gaps, loss, truncation, backpressure, clock discontinuity, and partial finalization **MUST** be explicit and integrity protected.
- **RM-TERMINAL-RECORD-0006:** Storage **MUST** use an authorized provider with confidentiality, integrity, persistence, backup/sync, export, retention, deletion, and key-management claims matching policy.
- **RM-TERMINAL-RECORD-0007:** Recording backpressure **MUST** select pause session, drop-with-gap, stop recording, or fail session; it **MUST NOT** silently lose events.
- **RM-TERMINAL-RECORD-0008:** Replay **MUST** target an isolated emulator by default; sending recorded input to a live process requires separate explicit authority, confirmation, rate/stop controls, and threat review.
- **RM-TERMINAL-RECORD-0009:** Deterministic emulator replay **MUST** verify artifact/configuration digests and checkpoint/state revisions and report the first divergence.
- **RM-TERMINAL-RECORD-0010:** Timing replay **MUST** support original, scaled, stepped, and immediate modes without changing event order; original timing is not process determinism.
- **RM-TERMINAL-RECORD-0011:** Export **MUST** preserve or intentionally transform sensitivity labels, redactions, integrity/gap disclosures, and provenance.
- **RM-TERMINAL-RECORD-0012:** Delete **MUST** report scoped effects on active store, replicas, backups, exports, caches, and cryptographic keys without claiming physical erasure absent evidence.

## Replay fidelity

| Level | Claim |
|---|---|
| R0 — Event inspection | Events decode and validate; no state reproduction claim |
| R1 — Visual-state replay | Emulator logical state/checkpoints reproduce under exact declared artifacts/configuration |
| R2 — Semantic replay | Logical state plus accessibility/semantic event stream reproduces |
| R3 — Live interaction experiment | Recorded inputs drive an isolated live target under separate authority; nondeterminism and side effects are expected |

R3 is not stronger deterministic evidence than R2 and is prohibited in ordinary playback.

