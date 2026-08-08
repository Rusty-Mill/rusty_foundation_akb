# Calendar and time-zone service

| Field | Value |
|---|---|
| Status | Draft platform service 0.1.0 |

**RM-I18N-TIMEZONE-0001:** An instant is a timeline value independent of calendar/time zone. A civil date/time is calendar fields without a unique instant. A zoned date/time binds fields, calendar, IANA/provider zone identity, offset, and exact rule-data version.

**RM-I18N-TIMEZONE-0002:** Instant-to-local conversion returns calendar fields, offset, abbreviation/display metadata, and rule provenance for the exact zone/data version.

**RM-I18N-TIMEZONE-0003:** Local-to-instant conversion detects unique, ambiguous overlap, and nonexistent gap results. Caller policy explicitly chooses earlier/later, reject, shift, or domain-specific resolution; the service never picks silently.

**RM-I18N-TIMEZONE-0004:** Calendar arithmetic declares calendar, field operation, overflow/clamping, end-of-month, daylight-transition, and ambiguity policy. It is distinct from elapsed-duration arithmetic.

**RM-I18N-TIMEZONE-0005:** Time-zone aliases/windows mappings and canonical IDs retain source, confidence, and data version. Fixed offset and named zone are not equivalent future scheduling rules.

**RM-I18N-TIMEZONE-0006:** Time-zone database updates publish a new immutable generation. Stored future schedules preserve intended civil/zone policy and are re-evaluated explicitly; historical outputs remain reproducible when old data is retained.

**RM-I18N-TIMEZONE-0007:** System time-zone detection is an observation with revision/provenance. Location-derived or geocoded zone selection is a separate privacy/authority-bearing capability.

**RM-I18N-TIMEZONE-0008:** Leap-second representation/support, clock smearing, range limits, and pre-standard historical accuracy are declared provider qualities, not inferred from an epoch timestamp type.

