# Power-source and battery observation

`rm.power.observer` publishes immutable snapshots containing provider/scope/revision, observation bounds, aggregate external/on-battery state, saver/low-power state, battery/UPS devices, lid state where appropriate, warning level, and per-field provenance/quality.

**RM-POWER-OBSERVE-0001:** External power, charging, discharging, idle, full, empty, absent, faulted, and unknown MUST remain distinguishable.

**RM-POWER-OBSERVE-0002:** Percentage, current/full/design energy, voltage, rate, cycle/health, time-to-empty/full, temperature, and warning state MUST carry units, validity, age, source, uncertainty/unknown, and applicable-device generation.

**RM-POWER-OBSERVE-0003:** Aggregate system state MUST NOT be derived from one arbitrarily selected battery when multiple batteries, UPSes, docks, or hot-swappable sources exist.

**RM-POWER-OBSERVE-0004:** Remaining-time and rate values MUST be represented as volatile estimates and MUST NOT be used as deadlines, durability guarantees, or authority for destructive actions.

**RM-POWER-OBSERVE-0005:** Native notifications are invalidation hints. Providers re-read coherent state after change, overflow, source restart, resume, dock/undock, or battery replacement.

**RM-POWER-OBSERVE-0006:** Observation MUST NOT alter charging policy, wake devices for optional detail, suppress system warnings, or request sleep inhibition.

See [ADR-0060](../../adr/0060-power-observations-are-estimates-not-budgets.md).
