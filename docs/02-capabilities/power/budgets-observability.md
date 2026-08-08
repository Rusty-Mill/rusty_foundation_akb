# Energy budgets, measurement, and observability

Portable energy budgeting is expressed as product constraints and measured evidence, not promises derived from battery percentage or saver state. A budget names workload, energy/power target, time window, hardware class, acceptable quality, measurement method, and enforcement/adaptation policy.

**RM-POWER-BUDGET-0001:** Energy and power measurements MUST state boundary—process estimate, component, package, whole-system input, battery discharge, or external instrument—plus units, sampling, calibration, uncertainty, and attribution limits.

**RM-POWER-BUDGET-0002:** Estimated energy attribution MUST NOT be represented as billing-grade, security-authoritative, or exact per-operation consumption.

**RM-POWER-BUDGET-0003:** Budget enforcement MUST define observation lag, hysteresis, adaptation steps, minimum quality/correctness, recovery, and behavior when measurement is unavailable.

**RM-POWER-OBSERVE-0007:** Telemetry MUST cover snapshot revisions/quality, saver/thermal transitions, lease target/effective state/duration, adaptation decisions, work deferred/cancelled, and measured performance/energy without high-cardinality battery/device identity.

**RM-POWER-OBSERVE-0008:** Battery serials, manufacturer data, usage history, health, charge patterns, location-correlated power events, assertion reasons, and user policy are privacy-sensitive and redacted/minimized.

Instrumentation must remain bounded and avoid increasing wakeups or polling enough to materially invalidate the energy measurement it seeks to observe.
