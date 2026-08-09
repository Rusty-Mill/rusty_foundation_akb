# Timers, calendars, waits, and deadlines

**RM-WORKFLOW-TIME-0001:** Timers declare monotonic duration, UTC instant, civil/calendar schedule, recurring schedule, business calendar, or event-time condition plus clock/calendar/time-zone/data generations and precision/tolerance.

**RM-WORKFLOW-TIME-0002:** Durable timer state binds intended fire condition, scheduled observation, created history frontier, provider identity, missed/coalesced/catch-up policy, cancellation, and actual fire evidence. Timer firing is a transition hint, not work authority.

**RM-WORKFLOW-TIME-0003:** Civil schedules define gaps/overlaps, leap/time-zone rule changes, locale-independent expression, end conditions, exceptions/holidays, duplicate instants, and migration when calendar data changes.

**RM-WORKFLOW-TIME-0004:** Activity, task, branch, workflow, SLA, escalation, and retention deadlines are distinct and define start milestone, pause/suspend behavior, grace, notification, retry interaction, and terminal consequence.

**RM-WORKFLOW-TIME-0005:** Waits bind exact event/task/child/condition and correlation, accept-before-wait races, buffered history, timeout, cancellation, competing events, and consumption cardinality.

**RM-WORKFLOW-TIME-0006:** Suspend, process restart, clock step, daylight transition, provider outage, delayed queue, and failover preserve durable intent and report late/duplicate/missed behavior honestly.
