# Notification scheduling and lifecycle

Scheduling requests future eligibility for native presentation; it does not guarantee wake, exact time, ordering, persistence, or presentation. The request binds a monotonic-relative or civil-time specification, timezone/calendar policy, relevance interval, recurrence policy if separately supported, content/resource revision, and replacement key.

**RM-NOTIFY-SCHEDULE-0001:** Scheduled results MUST report provider identifier, effective trigger representation, persistence/reboot quality, clock/timezone behavior, update/cancel support, and platform limits.

**RM-NOTIFY-SCHEDULE-0002:** Civil-time gaps, overlaps, timezone changes, clock corrections, sleep, reboot, logout, application update/removal, and missed triggers MUST have explicit provider or product policy.

**RM-NOTIFY-SCHEDULE-0003:** Recurrence SHOULD be generated from domain scheduling state rather than unlimited native recurrence; every occurrence has independent relevance and deduplication identity.

**RM-NOTIFY-SCHEDULE-0004:** Startup MUST reconcile owned pending/domain notifications where the platform permits and MUST preserve unknown provider state rather than assuming absence means delivery.

**RM-NOTIFY-SCHEDULE-0005:** Shutdown flush MAY submit already-authorized notifications but MUST remain bounded and cannot make application durability depend on provider acceptance.

Remote push registration, token/channel lifecycle, provider authentication, payload confidentiality, collapse semantics, wake/background execution, retry, and server delivery receipts are a separate transport capability that may feed the same local content/policy path.
