# IPC byte-pipe ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | IPC capability owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| Security reviewer | Foundation security/privacy review for endpoint authority/transfer, inheritance, native signals, diagnostics, and content non-capture |
| Evidence reviewer | Foundation IPC conformance, process-integration, reliability, and performance review |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

## Ownership duties

The owner maintains byte-stream, endpoint authority/lifecycle, EOF/broken-peer, partial progress, capacity/backpressure, atomicity, duplication/transfer, sync/async Q-level, cancellation, concurrency, error, dependency/profile, source, quality, conformance, benchmark, and promotion semantics. Provider owners maintain separate Windows, Linux, and macOS mechanisms and exact runtime/process-integration frontiers.

## Bounded trial plan

A later disposable trial may exercise atomic pair creation, direction/noninheritance, partial transfers, bounded backpressure, all-reference EOF, broken-peer containment, scoped concurrent-writer atomicity, endpoint duplication/transfer, Q0–Q3 paths where available, cancel/complete races, and one synthetic process redirection/pipeline composition. The matrix includes supported Windows builds, Linux kernels/libcs, and macOS/SDK generations with declared native mechanisms and runtime integrations.

The trial uses the [foundation trial template](../../05-governance/implementation-trials/trial-template.md), synthetic nonsecret bytes and canaries, disposable children/endpoints, bounded resource/worker quotas, isolated native code, no production streams/data, and no release publication. It does not select public Rust APIs, crates/workspaces, async runtime/reactor, named/duplex/message IPC, terminal model, process pipeline product policy, capacity tuning, performance budgets, or production support.

Stop conditions include wrong-direction authority, unintended inheritance/transfer, endpoint leak, premature/late EOF, host termination from broken-peer signaling, buffer reuse before terminal completion, false cancellation/progress, unbounded accepted bytes or worker growth, busy spinning, payload leakage, atomicity/Q-level claim inflation, child escape, provenance loss, or material source/contract/environment drift.

**RM-IPC-OWNER-0001:** Promotion and trial records MUST name accountable people for the domain and every claimed provider/runtime/process context, exact generations, reviewer independence, and unresolved limitations.

**RM-IPC-OWNER-0002:** Trial hypotheses MUST distinguish write acceptance, buffer residency, read progress, pending/would-block, confirmed cancellation, broken peer, EOF, close, and inherited-reference reconciliation.

**RM-IPC-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize implementation, unsafe/native interfaces, arbitrary process inheritance, runtime selection, content collection, packaging, or release.

**RM-IPC-OWNER-0004:** Closeout MUST close and inventory every endpoint/duplicate/operation/child, revoke temporary transfer authority, account for traces/canaries, retain negative evidence, and exclude trial artifacts from release channels.
