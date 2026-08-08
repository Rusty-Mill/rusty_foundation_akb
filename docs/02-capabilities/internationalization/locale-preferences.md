# `rm.i18n.locale-preferences`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-I18N-PREF-0001:** A preference snapshot has immutable revision/provenance and separately reports ordered UI languages, formatting locale/region, script where meaningful, calendar, numbering system, hour cycle, first weekday/week rules, measurement system, currency preference, collation, time zone, and whether every field is explicit, inferred, defaulted, or unavailable.

**RM-I18N-PREF-0002:** Locale/language tags are parsed and canonicalized under a declared BCP 47/CLDR data version while retaining the original requested form for diagnostics. Unknown valid extensions are preserved where possible, not discarded silently.

**RM-I18N-PREF-0003:** User and application overrides are independent. The provider reports OS preferences; application policy chooses whether and how to combine them without writing global/system settings.

**RM-I18N-PREF-0004:** Subscription yields an initial snapshot and increasing revisions or an explicit gap/resnapshot. Locale, language, region, time zone, calendar, or format changes can occur during a session without requiring process restart.

**RM-I18N-PREF-0005:** Preference values are user-sensitive and may reveal language, region, religion/culture, location, or identity. Telemetry records only the minimum approved aggregate and never full preference vectors by default.

**RM-I18N-PREF-0006:** A missing preference does not authorize an `en-US`, Gregorian, Latin-digit, UTC, or metric/US default silently. Product policy supplies and discloses deterministic fallback.

