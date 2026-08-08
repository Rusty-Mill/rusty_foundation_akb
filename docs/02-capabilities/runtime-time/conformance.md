# Runtime and time conformance specification

**Status:** Draft  
**Suite version:** 0.1.0  
**Scope:** `rm.time.monotonic-clock`, `rm.time.deadline-timer`, `rm.runtime.cancellation`, and the orderly shutdown platform service

## Purpose

Define backend-neutral assertions that turn every normative requirement in the runtime/time slice into reproducible evidence. This document specifies tests; it does not select a test framework or implementation language.

## Evidence classes

| Class | Meaning | Release use |
|---|---|---|
| D | Deterministic functional assertion | Required on every supported target |
| C | Concurrent/model-based assertion | Required under configured stress envelope |
| E | Environment-sensitive assertion | Required on controlled physical or virtual test hosts |
| P | Performance/quality observation | Reported through the benchmark suite |
| R | Review or artifact inspection | Signed review evidence required |

An assertion passes, fails, is unsupported by the declared provider contract, or is not run with a reason. “Flaky pass” is not a conformance state.

## Test identity

Assertion identifiers use `CT-<DOMAIN>-<SUBJECT>-<NNN>`. They are never reused. Each result records suite version, requirement identifiers, provider and contract versions, OS build, architecture, hardware/VM identity, power state, configuration, start/end instants, and artifact provenance.

## Monotonic-clock assertions

| Assertion | Requirements | Class | Procedure and pass condition |
|---|---|---|---|
| CT-TIME-MONO-001 | 0001, 0004 | D | Discover domains. Active is present; continuous availability is explicit. |
| CT-TIME-MONO-002 | 0002 | C | Sample concurrently at high volume; no comparable observation decreases. |
| CT-TIME-MONO-003 | 0003 | E | Adjust calendar time forward/backward in an isolated host; active instants remain ordered and elapsed duration stays within environmental tolerance. |
| CT-TIME-MONO-004 | 0005 | E | Suspend for a measured interval; continuous elapsed includes suspend within declared accuracy. Unsupported is permitted only when continuous was not claimed. |
| CT-TIME-MONO-005 | 0006 | D | Compare different domains and provider epochs; operation fails with the specified incompatibility outcome. |
| CT-TIME-MONO-006 | 0007 | D | Exercise maximum/minimum duration arithmetic; overflow and underflow are detected. |
| CT-TIME-MONO-007 | 0008 | D/P | Resolution is present, positive, stable for the provider epoch, and distinct from measured read cost/accuracy. |
| CT-TIME-MONO-008 | 0009 | R | Public representation and documentation do not promise cross-reboot, cross-provider, cross-machine, or serialized comparability. |
| CT-TIME-MONO-009 | 0010 | C/P | Concurrent reads require no mutable ambient policy and meet allocation/concurrency claims. |

## Deadline-timer assertions

| Assertion | Requirements | Class | Procedure and pass condition |
|---|---|---|---|
| CT-TIME-DEADLINE-001 | 0001 | D | Reject a deadline from an incompatible clock domain or provider epoch. |
| CT-TIME-DEADLINE-002 | 0002, 0003 | E | Past deadlines become ready; future deadlines never report before the bound clock reaches the deadline. |
| CT-TIME-DEADLINE-003 | 0004 | C/R | Saturate the async path while recording worker occupancy; no worker is dedicated solely to each wait. |
| CT-TIME-DEADLINE-004 | 0005 | D/R | Sync wait works without an executor and architecture inspection finds no hidden runtime creation. |
| CT-TIME-DEADLINE-005 | 0006, 0007 | C | Race disarm against expiry repeatedly; exactly one terminal outcome is observed and no post-disarm expiry leaks. |
| CT-TIME-DEADLINE-006 | 0008 | E/P | With declared tolerance, delivery is never early and measured lateness stays within the provider's documented quality envelope. |
| CT-TIME-DEADLINE-007 | 0009 | D | Metadata reports resolution, tolerance, clock domain, suspend behavior, and wake behavior. |
| CT-TIME-DEADLINE-008 | 0010 | C | Race cancellation and expiry; exactly one typed outcome is observed and cancellation is never labeled expiry. |
| CT-TIME-DEADLINE-009 | 0011 | D/R | Base timers cannot silently acquire wake authority; wake behavior requires a discoverable authorized extension. |
| CT-TIME-DEADLINE-010 | 0001–0011 | E | Suspend/resume matrix confirms active and continuous deadline behavior against the declared clock semantics. |

## Cancellation assertions

| Assertion | Requirements | Class | Procedure and pass condition |
|---|---|---|---|
| CT-RUNTIME-CANCEL-001 | 0001 | C | Many threads request cancellation; one state transition occurs and all calls are safe. |
| CT-RUNTIME-CANCEL-002 | 0002, 0003 | C | Existing and late observers all observe the request without another transition. |
| CT-RUNTIME-CANCEL-003 | 0004 | D/R | Async waiting uses notification rather than one worker per observer; sync polling requires no runtime. |
| CT-RUNTIME-CANCEL-004 | 0005 | D | Dropping a source follows the explicitly selected policy and does not cancel by default. |
| CT-RUNTIME-CANCEL-005 | 0006 | C | Parent request reaches descendants; child request never reaches parent or siblings. |
| CT-RUNTIME-CANCEL-006 | 0007 | C | Reentrant callback operations cannot deadlock on internal cancellation-state locks. |
| CT-RUNTIME-CANCEL-007 | 0008, 0009 | C | Linearized model tests cover completion/request/observation races and preserve the actual terminal outcome and partial-effect contract. |
| CT-RUNTIME-CANCEL-008 | 0010 | C | Deep scope propagation remains bounded in stack usage and completes within the declared scaling envelope. |
| CT-RUNTIME-CANCEL-009 | 0001–0010 | C | Callback panic/failure isolation does not prevent other observers or corrupt state. |

## Orderly-shutdown service assertions

| Assertion | Requirements | Class | Procedure and pass condition |
|---|---|---|---|
| ST-RUNTIME-SHUTDOWN-001 | 0001, 0009 | C | Concurrent and reentrant initiation joins one operation and produces one shared terminal report. |
| ST-RUNTIME-SHUTDOWN-002 | 0002, 0008 | C | Work registration races with quiescing; ordinary work is rejected after the transition and shutdown-owned work is explicitly distinguished. |
| ST-RUNTIME-SHUTDOWN-003 | 0003 | D/C | A generated dependency DAG stops in reverse topological order, honoring explicit overrides and rejecting cycles. |
| ST-RUNTIME-SHUTDOWN-004 | 0004, 0010 | E | Each phase observes its monotonic deadline and applies the configured escalation without claiming arbitrary work was killed safely. |
| ST-RUNTIME-SHUTDOWN-005 | 0005, 0006 | D/C | Multiple independent component failures are aggregated; remaining independent components still receive notification. |
| ST-RUNTIME-SHUTDOWN-006 | 0007 | D/R | Async wait and sync observation produce the same report without nested runtime creation. |
| ST-RUNTIME-SHUTDOWN-007 | 0001–0010 | C | Randomized lifecycle model verifies legal state transitions and exactly-once terminal reporting. |

## Cross-platform matrix

Every capability assertion runs on supported Windows, Linux, and macOS configurations. Service assertions run once per supported runtime/provider composition on each platform. Environment-sensitive jobs include:

- Bare-metal or suspend-capable host for suspend/resume.
- Privileged isolated host for calendar-clock adjustment.
- At least one virtualized environment per platform family.
- Power-policy variants where timers or clock sources are affected.
- Debug and optimized builds for overflow, race, and timing sensitivity.

## Failure artifacts

A failure bundle contains normalized assertion result, seed and schedule when randomized, recent structured events, provider metadata, timing samples, platform facts, and minimal reproduction instructions. It excludes secrets, full environment dumps, and unrelated user data.

## Coverage gate

Experimental promotion requires all deterministic assertions plus concurrency assertions for the implemented scope. Stable promotion requires every applicable D, C, E, and R assertion on each claimed platform and a linked benchmark report for every P assertion.
