# Templates, localization, accessibility, and rendering

**RM-COMMS-TEMPLATE-0001:** Template definitions bind stable template ID/version, purpose/topic/classification, supported channels/locales, input schema, required/optional fields, escaping contexts, layout/assets, sender metadata, links/actions, fallback, and approvals.

**RM-COMMS-TEMPLATE-0002:** Rendering binds exact template, locale/language/direction, time zone/calendar/number/date rules, input values and provenance, branding/theme, channel profile, content policy, and renderer generation.

**RM-COMMS-TEMPLATE-0003:** Missing translations, unsupported locale, invalid input, overflow, unsafe markup/URL, inaccessible structure, and channel-limit violations fail or use an approved recorded fallback; raw interpolation is prohibited.

**RM-COMMS-TEMPLATE-0004:** Email and in-app markup provide language, semantic headings/landmarks/lists/tables, meaningful link text, alt text, sufficient contrast, keyboard-operable actions, reflow, text alternatives, and plain-text equivalents where applicable.

**RM-COMMS-TEMPLATE-0005:** SMS/push text remains understandable without color/image/sound, respects grapheme and encoding/segment boundaries, localizes action/expiry context, and avoids ambiguous truncation.

**RM-COMMS-TEMPLATE-0006:** Preview and golden rendering cover representative and adversarial locales, scripts, directions, long/short values, assistive technology, dark/high-contrast/reduced-motion settings, client matrices, and provider transformations.

**RM-COMMS-TEMPLATE-0007:** Rendered artifacts are immutable snapshots with content digest and redacted audit preview; later template edits never change already approved/scheduled content silently.
