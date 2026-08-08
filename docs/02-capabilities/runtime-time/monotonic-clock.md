# `rm.time.monotonic-clock` — Monotonic clock

**Status:** Draft  
**Contract version:** 0.1.0  
**Domain:** Time  
**Owner:** Unassigned  
**Profiles:** CLI, Desktop, Server, Embedded/headless (candidate required member)

## Purpose

Provide nondecreasing instants for measuring elapsed duration and constructing deadlines without exposure to calendar-clock adjustments.

## Scope

### Goals

- Read an instant from an explicitly selected monotonic clock domain.
- Compare instants from the same domain and provider epoch.
- Convert differences to a portable duration with checked arithmetic.
- Report nominal resolution and supported clock domains.

### Non-goals

- Calendar time, time zones, formatting, or synchronization.
- Cross-machine timestamp comparison.
- A promise that precision equals accuracy or scheduling resolution.
- Persisting instants across reboot, provider replacement, or process boundary.

## Vocabulary

- **Active domain:** advances while the system is executing and may pause during suspend.
- **Continuous domain:** advances across system suspend without being tied to wall-clock adjustment.
- **Instant:** opaque point in one clock domain and provider epoch.
- **Resolution:** smallest nominal distinguishable clock increment reported by the provider.

## Semantic model

An instant carries enough identity to prevent accidental comparison across clock domains or incompatible epochs. Its numeric representation is not public semantics. Duration subtraction is valid only when both operands are comparable.

## Requirements

- **RM-TIME-MONOTONIC-0001:** A provider **MUST** expose an `active` monotonic domain.
- **RM-TIME-MONOTONIC-0002:** Successive observations from one domain and provider epoch **MUST NOT** decrease.
- **RM-TIME-MONOTONIC-0003:** An active-domain observation **MUST NOT** be affected by adjustments to calendar time.
- **RM-TIME-MONOTONIC-0004:** A provider **MUST** report whether a `continuous` domain is available.
- **RM-TIME-MONOTONIC-0005:** A continuous domain, when provided, **MUST** include elapsed system suspend and **MUST NOT** follow discontinuous calendar adjustments.
- **RM-TIME-MONOTONIC-0006:** Comparison or subtraction of incompatible instants **MUST** fail explicitly rather than produce a duration.
- **RM-TIME-MONOTONIC-0007:** Duration arithmetic **MUST** detect overflow and underflow.
- **RM-TIME-MONOTONIC-0008:** The provider **MUST** expose nominal resolution separately from any accuracy claim.
- **RM-TIME-MONOTONIC-0009:** Instants **MUST NOT** be documented as portable across reboot, provider epoch, machine, or process serialization.
- **RM-TIME-MONOTONIC-0010:** Clock reads **MUST** be safe for concurrent use and **MUST NOT** require ambient mutable global policy.

## Errors

Clock reads are expected to be infallible after provider initialization on common targets, but the contract retains explicit initialization/availability failure. Incompatible comparison and arithmetic failure are programmer-visible typed outcomes, not platform error codes.

## Security and privacy

High-resolution clocks can strengthen timing side channels and fingerprinting. Profiles or sandbox policies **MAY** select reduced precision. Any precision reduction must preserve nondecreasing behavior and be discoverable. Apple-required reason declarations and similar platform policies remain a packaging concern.

## Performance and observability

The base capability is allocation-free on the hot path. Benchmark clock-read latency, concurrency scaling, and conversion overhead against the selected native source. Reading the clock emits no telemetry; diagnostic metadata may report provider, domain, and resolution during initialization.

## Dependencies

None.

## Platform realization

| Platform | Active domain candidates | Continuous domain candidates | Status |
|---|---|---|---|
| Windows | QPC or unbiased interrupt time | Tick/interrupt-time source including sleep | Researching exact source pairing |
| Linux | `CLOCK_MONOTONIC` | `CLOCK_BOOTTIME` | Native |
| macOS | `CLOCK_UPTIME_RAW` | `CLOCK_MONOTONIC_RAW` | Native |

## Conformance plan

| Requirement | Evidence |
|---|---|
| 0001–0005 | Capability discovery plus controlled wall-clock adjustment and suspend-aware platform tests |
| 0002 | High-volume same-thread and cross-thread monotonicity tests |
| 0006–0007 | Deterministic type/contract boundary tests |
| 0008 | Resolution metadata validation and empirical sampling report |
| 0009 | Serialization/API review |
| 0010 | Concurrency and allocation benchmark |

## Open questions

- Must continuous time be required for every Stable backend or remain optional?
- Should privacy-reduced clocks be separate quality levels or separate capabilities?
- What provider-epoch identity is necessary without burdening the common representation?
