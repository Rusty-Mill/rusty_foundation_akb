# `rm.time.deadline-timer` — Deadline timer

**Status:** Draft  
**Contract version:** 0.1.0  
**Domain:** Time  
**Owner:** Runtime/time capability owner; named assignee required for promotion

**Profiles:** CLI, Desktop, Server, Embedded/headless (candidate required member)

## Purpose

Notify a consumer when a deadline in a selected monotonic clock domain has been reached, through both asynchronous and synchronous use paths.

## Scope

One-shot deadlines are the primitive contract. Periodic scheduling is deferred because missed-tick, drift, and catch-up policy require a separate composition or capability.

Wake-from-suspend is not part of the base contract. A continuous-domain deadline may become overdue while suspended and be observed after resume without waking the machine.

## Requirements

- **RM-TIME-DEADLINE-0001:** A timer **MUST** bind to one monotonic-clock domain and provider epoch.
- **RM-TIME-DEADLINE-0002:** A timer **MUST NOT** report expiration before its deadline according to that clock.
- **RM-TIME-DEADLINE-0003:** A deadline at or before the current instant **MUST** become ready without an additional positive delay requirement.
- **RM-TIME-DEADLINE-0004:** The asynchronous path **MUST NOT** occupy a worker thread solely to wait.
- **RM-TIME-DEADLINE-0005:** The synchronous path **MUST** block the calling thread without creating or nesting an async runtime.
- **RM-TIME-DEADLINE-0006:** Dropping or explicitly disarming a pending timer **MUST** release provider resources eventually and **MUST NOT** deliver a consumer-visible expiration afterward.
- **RM-TIME-DEADLINE-0007:** A disarm racing with expiration **MUST** resolve to exactly one terminal observation: expired or disarmed.
- **RM-TIME-DEADLINE-0008:** Optional tolerance **MAY** permit delivery after the deadline for coalescing but **MUST NOT** permit early delivery.
- **RM-TIME-DEADLINE-0009:** The provider **MUST** expose supported resolution, tolerance, clock-domain, and suspend behavior.
- **RM-TIME-DEADLINE-0010:** Cancellation observation **MUST** follow the cancellation contract and **MUST NOT** be reported as timer expiration.
- **RM-TIME-DEADLINE-0011:** Wake-from-suspend behavior **MUST** require a separately discoverable extension and explicit authority.

## Lifecycle and races

```text
created -> armed -> expired
              \-> disarmed
              \-> canceled (when observed through cancellation composition)
```

Only one terminal outcome is visible to a given waiter. Provider cleanup may continue internally after the outcome becomes visible.

## Errors

Typed failures include incompatible deadline domain, unavailable quality/wake policy, resource exhaustion, provider shutdown, and invalid duration arithmetic. Late delivery is a quality observation, not automatically an error.

## Quality model

- **Resolution:** provider's nominal scheduling granularity.
- **Tolerance:** consumer-authorized late-delivery window used for coalescing.
- **Lateness:** observed delivery instant minus deadline.
- **Wake policy:** no-wake in the base contract; authorized wake as an extension.

Accessibility and internationalization are not directly applicable. Power usage is material: zero-tolerance/high-frequency timers should be visible to diagnostics and policy.

## Dependencies

| Relationship | Capability | Reason |
|---|---|---|
| requires | `rm.time.monotonic-clock` | Defines the deadline domain |
| optionally-uses | `rm.runtime.cancellation` | Allows cooperative abandonment |

## Platform realization

| Platform | Candidate async mechanism | Candidate sync mechanism | Key variance |
|---|---|---|---|
| Windows | Thread-pool or waitable timer integrated with completion | Waitable timer wait | Relative timer suspend behavior and timer tolerance |
| Linux | `timerfd` with `epoll` | `clock_nanosleep(TIMER_ABSTIME)` | Signals, timer slack, clock choice |
| macOS | Dispatch source timer | Semaphore/condition or clock sleep path | Dispatch leeway and selected clock domain |

## Conformance plan

Test past deadlines, no-early-fire behavior, disarm/expiry races, high concurrency, cleanup, suspend/resume for each clock domain, async executor starvation, sync path independence, and tolerance boundaries. Timing tests report distributions and environmental noise rather than using brittle single thresholds.

## Benchmark plan

Measure creation/arm/disarm cost, memory per pending timer, throughput, delivery-lateness distribution, cancellation storms, and scaling from one to at least one million pending logical timers where the backend design supports aggregation.

## Open questions

- Does the platform expose one logical timer per consumer or a runtime-managed timer wheel/heap behind the contract?
- What guarantees are appropriate for resource cleanup after drop?
- Should periodic schedules be a separate capability or a platform service above one-shot deadlines?
