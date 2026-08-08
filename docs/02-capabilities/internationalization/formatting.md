# Number, currency, unit, date, and duration formatting

**RM-I18N-FORMAT-0001:** Formatting consumes a typed value, immutable locale context, semantic style/skeleton/options, rounding/precision policy, and output purpose. Raw translator/platform pattern strings are not the normal portable contract.

**RM-I18N-FORMAT-0002:** Number formatting declares decimal/percent/scientific/compact/accounting intent, grouping, sign, rounding mode/increment, precision/significant digits, numbering system, and special-value policy. Output may include semantic field spans.

**RM-I18N-FORMAT-0003:** Currency values carry amount and explicit ISO currency identity. Locale may choose display conventions but never supplies the business currency implicitly. Cash versus accounting rounding is explicit.

**RM-I18N-FORMAT-0004:** Measurement formatting carries value plus exact unit and conversion policy. Locale may choose display unit only when product policy permits; conversion precision and original value/unit remain available.

**RM-I18N-FORMAT-0005:** Date/time formatting distinguishes instant versus civil value, calendar, time-zone identity/version, field set/skeleton, hour cycle, relative versus absolute style, and ambiguity policy. A time-zone abbreviation alone is never a stable zone identity.

**RM-I18N-FORMAT-0006:** Duration formatting distinguishes elapsed duration from calendar-relative period. Months/days are not converted to fixed seconds without an explicit reference calendar/time zone.

**RM-I18N-FORMAT-0007:** Formatting output is human presentation and is not used as canonical serialization, database key, protocol token, signature input, or round-trip guarantee unless a separate machine format specifies it.

**RM-I18N-FORMAT-0008:** Parsing is a separate contract that declares accepted locale/context, strictness, complete-consumption requirement, ambiguity, grouping/sign/currency/unit policy, calendar/time zone, and returned confidence/diagnostics. Display-formatted text is not assumed safely parseable.

**RM-I18N-FORMAT-0009:** Formatters are immutable or isolated for concurrency. Cache identity includes context digest, data/provider version, and full style/options; context changes never mutate cached formatter behavior.

**RM-I18N-FORMAT-0010:** Output embeds bidi isolation/semantic field information where needed so dynamic values cannot corrupt surrounding direction or accessibility reading order.

