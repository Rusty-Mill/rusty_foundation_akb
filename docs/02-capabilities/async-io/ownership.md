# Async I/O ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | Async I/O integration owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| Security reviewer | Foundation security/privacy review for native state, buffers, resource authority, stale/forged completions, fork/transfer, and observability |
| Evidence reviewer | Foundation concurrency, I/O conformance, reliability, power, and performance review |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

## Ownership duties

The owner maintains operation identity/lifecycle, readiness/completion translation, cancellation/lifetime, registration generations, backpressure/fairness, runtime/executor integration, shutdown, errors/observability, dependency/composition, source, quality, conformance, benchmark, and promotion semantics. Provider owners maintain separate IOCP/overlapped, io_uring, epoll, kqueue/dispatch, and bounded-blocking mappings per operation/resource/version; consuming-domain owners retain effect semantics.

## Bounded trial plan

A later disposable trial may exercise a small filesystem-file and IPC-byte-pipe matrix across immediate/deferred completion, readiness retry, native completion, bounded blocking fallback, cancellation at every phase, descriptor/handle reuse, registration churn, queue saturation, hot-resource fairness, executor migration/loss, and stop-admission/cancel/drain shutdown. Unsupported platform operations remain explicit rather than coerced into a common mechanism.

The trial uses the [foundation trial template](../../05-governance/implementation-trials/trial-template.md), synthetic nonsecret buffers/resources, disposable files/pipes, hard queue/memory/thread/batch quotas, isolated native code, no production data/devices, no global runtime installation, and no release publication. It does not select public Rust APIs, crates/workspaces, executor/runtime/reactor, universal operation enum, provider library, performance budgets, product power policy, or production support.

Stop conditions include duplicate/wrong-generation terminalization, use-after-free/ABA, early buffer reuse, false cancellation/progress, wrong-resource event delivery, unbounded queue/memory/thread growth, busy spinning, starvation beyond declared policy, arbitrary consumer code on provider callbacks, hidden runtime/event-loop pumping, stuck shutdown without bounded survivor evidence, sensitive identifier/payload leakage, provenance loss, or material source/contract/environment drift.

**RM-ASYNC-OWNER-0001:** Promotion and trial records MUST name accountable people for the framework, every claimed provider/operation/resource, consuming domain, exact generations, reviewer independence, and unresolved limitations.

**RM-ASYNC-OWNER-0002:** Trial hypotheses MUST distinguish submission, native issue, readiness, syscall progress, completion, dequeue, cancellation request/acknowledgement, wake, resume, domain effect, and reclamation.

**RM-ASYNC-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize implementation, unsafe/native interfaces, runtime/provider selection, arbitrary device/network access, packaging, or release.

**RM-ASYNC-OWNER-0004:** Closeout MUST stop admission, terminalize or classify every operation, drain/reject late events safely, deregister/release resources and buffers, stop bounded workers/pollers, account for traces/canaries, retain negative evidence, and exclude trial artifacts from release channels.
