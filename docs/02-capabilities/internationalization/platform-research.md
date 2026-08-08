# Internationalization platform and standards research

**Status:** Research evidence; normative conclusions live in contracts and ADRs.

## Standards and shared data

BCP 47 defines language tags. Unicode CLDR supplies locale identifiers/data, likely subtags, matching, plural rules, date/number/unit patterns, collation tailorings, display names, and supplemental preferences. ICU exposes services over Unicode/CLDR and time-zone data and explicitly distinguishes requested, valid, and actual locales. IANA tzdb supplies mutable historical/future civil time-zone rules.

Primary sources: [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.html), [CLDR specification](https://unicode.org/reports/tr35/), [CLDR language matching](https://unicode.org/reports/tr35/tr35.html#LanguageMatching), [ICU locale services](https://unicode-org.github.io/icu/userguide/locale/), [IANA Time Zone Database](https://www.iana.org/time-zones).

## Windows

Windows NLS uses locale names based on BCP 47 conventions and exposes language lists, regional/date/number/currency/calendar settings, collation/sort versions, and Windows time-zone identities. Locale names and sort identifiers show that language and sort policy are not one scalar setting. Windows-to-IANA time-zone mapping requires versioned data rather than string equivalence.

Primary sources: [Locale names](https://learn.microsoft.com/en-us/windows/win32/intl/locale-names), [National Language Support](https://learn.microsoft.com/en-us/windows/win32/intl/national-language-support), [Locale information constants](https://learn.microsoft.com/en-us/windows/win32/intl/locale-information-constants), [handling sorting](https://learn.microsoft.com/en-us/windows/win32/intl/handling-sorting-in-your-applications), [time zones](https://learn.microsoft.com/en-us/windows/win32/api/timezoneapi/).

## Linux and portable providers

POSIX locale categories are process-global or thread-scoped depending on APIs and combine concerns differently from BCP 47/CLDR. They are insufficient as the portable semantic model. ICU/ICU4X-style providers can use pinned data independent of installed system locales; system locale/environment observation remains one provider input.

Primary sources: [POSIX locale](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap07.html), [ICU formatting](https://unicode-org.github.io/icu/userguide/format_parse/), [ICU collation](https://unicode-org.github.io/icu/userguide/collation/).

## macOS

Foundation exposes `Locale`, `Calendar`, `TimeZone`, and typed `FormatStyle` families whose results account for locale conventions. User preference changes may occur during application lifetime. Native APIs remain possible providers, but exact OS/data versions and requested/actual locale behavior must appear in evidence.

Primary sources: [`Locale`](https://developer.apple.com/documentation/foundation/locale), [`Calendar`](https://developer.apple.com/documentation/foundation/calendar), [`TimeZone`](https://developer.apple.com/documentation/foundation/timezone), [`FormatStyle`](https://developer.apple.com/documentation/foundation/formatstyle).

## Derived portability conclusions

| Concern | Portable rule |
|---|---|
| Host settings | Versioned preference observation, not ambient global |
| Operation | Explicit immutable locale context |
| Resource matching | Product-supported locales plus deterministic fallback trace |
| Formatting | Typed semantic skeleton/style; human output only |
| Civil time | Explicit zone/calendar/data version and gap/overlap policy |
| Collation | Context/version-scoped order, never identity/security |

