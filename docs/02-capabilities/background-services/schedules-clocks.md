# Schedules, clocks, and missed work

A `DurableSchedule` contains immutable schedule identity/generation, workload reference, temporal expression, time domain, time-zone/database revision when civil, ambiguity policy, earliest/deadline window, recurrence rule, jitter/flexibility, wake/power/network constraints, missed-run policy, overlap/concurrency policy, expiration, and authority.

**RM-BACKGROUND-SCHEDULE-0001:** One-shot instant, fixed interval, civil-calendar recurrence, boot/login/session event, idle/maintenance opportunity, and externally signaled work MUST be distinct trigger kinds.

**RM-BACKGROUND-SCHEDULE-0002:** Civil schedules MUST retain local fields, named time zone, rule/database version, gap/overlap policy, and future-rule re-evaluation policy. They MUST NOT be flattened permanently to a fixed UTC offset.

**RM-BACKGROUND-SCHEDULE-0003:** Earliest time, preferred window, deadline, recurrence, jitter, coalescing, wake permission, and exactness quality MUST be explicit. Ordinary schedules MUST NOT claim exact wall-clock launch.

**RM-BACKGROUND-SCHEDULE-0004:** Sleep, shutdown, downtime, clock step, time-zone/rule change, user/session absence, disabled policy, quota, and update MUST produce explicit `missed`, `coalesced`, `deferred`, `expired`, or `ineligible` evidence according to policy.

**RM-BACKGROUND-SCHEDULE-0005:** Missed-run policy MUST select skip, run-once-soon, bounded catch-up, or domain reconciliation. Unbounded replay of every nominal occurrence is forbidden.

**RM-BACKGROUND-SCHEDULE-0006:** Schedule observation and mutation MUST use expected generation and report native normalization, approximation, unsupported constraints, and current next-window evidence.

**RM-BACKGROUND-SCHEDULE-0007:** Registration acceptance persists schedule intent only. It does not prove trigger delivery, launch, resource availability, execution, completion, or durability of application results.
