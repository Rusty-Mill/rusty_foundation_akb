# Internationalization and localization conformance specification

**Status:** Draft

| ID | Requirements | Method |
|---|---|---|
| I18N-PREF-001 | PREF-0001–0006 | Enumerate mixed language/region/script/calendar/number/hour/unit/collation/time-zone preferences, unknown fields, changes, privacy, and no-default fixtures |
| I18N-CONTEXT-001 | CONTEXT-0001–0007 | BCP 47 canonicalization/extensions, likely-subtag and matching vectors, per-service actual locale, bounded fallback, update immutability, cross-machine revalidation |
| I18N-MESSAGE-001 | MESSAGE-0001–0005 | Schema/type/key/fallback/missing/empty fixtures and CLDR cardinal/ordinal/select categories with fractions, zero, negatives, visible precision |
| I18N-MESSAGE-002 | MESSAGE-0006–0009 | Hostile rich messages/bidi/URLs, pseudolocales, hot authenticated update, schema mismatch, translator-token preservation, sensitive diagnostics |
| I18N-FORMAT-001 | FORMAT-0001–0006 | CLDR/ICU vectors for numbers/currency/units/date/time/duration across representative locales/calendars/number systems/hour cycles and boundary values |
| I18N-FORMAT-002 | FORMAT-0007–0010 | Prohibit machine reuse, strict/lenient parsing ambiguity, formatter cache isolation, bidi field spans, concurrent context revisions |
| I18N-TIME-001 | TIMEZONE-0001–0005 | Every tzdb transition class, overlap/gap policies, historical/future/alias/fixed-offset mappings, calendar arithmetic/end-of-month/range boundaries |
| I18N-TIME-002 | TIMEZONE-0006–0008 | tzdb upgrade/re-evaluation/replay, system zone change, denied location inference, leap/smear/range/pre-standard quality claims |
| I18N-COLLATE-001 | COLLATE-0001–0006 | UCA/CLDR conformance and tailoring corpus, sort/search modes, strength/case/numeric/normalization, sort-key upgrade, semantic ranges, resource bounds |

## Product evidence

Every supported UI locale is tested for bundle completeness, typed arguments, plural/select coverage, layout expansion, truncation, bidi isolation, keyboard/IME, fonts/fallback, accessibility names/live updates, screenshots only as supplementary evidence, and locale change without restart where claimed. Pseudolocales cover at least accented expansion, extreme length, RTL mirroring/isolation, and non-Latin digits.

Time/date golden results bind the exact tzdb, CLDR, calendar, locale context, provider, and instant/civil ambiguity policy. Collation golden order and sort keys bind exact collator versions. Platform differences outside the selected contract are disclosed, not normalized by changing expected data silently.

