# Accessible text and range model

**RM-ACCESSIBILITY-TEXT-0001:** Accessible text references authoritative [semantic Unicode text](../text/unicode-model.md), exact document/text revision, container identity, language/direction, selections, caret/active endpoint, composition, and read-only/editable/protected state.

**RM-ACCESSIBILITY-TEXT-0002:** A range names endpoints in a provider-independent semantic unit and preserves affinity. Adapter conversions to UIA, AT-SPI, or macOS units are checked mappings with platform variance disclosure.

**RM-ACCESSIBILITY-TEXT-0003:** Navigation supports the truthful subset of grapheme/character, word, line, paragraph, page, document, format run, and embedded-object units. Unsupported units widen or fail only as the target native API contract specifies and disclose the mapping.

**RM-ACCESSIBILITY-TEXT-0004:** Text retrieval is bounded and supports chunked access without forcing one cross-process call per scalar or one unbounded full-document allocation. Returned chunks identify revision and continuation.

**RM-ACCESSIBILITY-TEXT-0005:** Selection/caret changes, text edits, composition, and layout reflow either transform retained ranges to the new revision or invalidate them explicitly. Stale ranges never select or edit a different passage silently.

**RM-ACCESSIBILITY-TEXT-0006:** Range geometry returns zero or more revision-bound rectangles/fragments and distinguishes offscreen, virtualized, clipped, unavailable, and empty ranges. Bidi visual fragments retain logical range mapping.

**RM-ACCESSIBILITY-TEXT-0007:** Embedded objects, links, annotations, generated hyphens/ellipsis, and inline controls retain semantic relationships without inserting misleading source text.

**RM-ACCESSIBILITY-TEXT-0008:** Protected/password text exposes length/value/ranges only under explicit platform and application policy. Masked visual glyphs are not evidence that semantic content is safe to disclose.

**RM-ACCESSIBILITY-TEXT-0009:** Text attributes expose only semantically useful, supported facts with range/revision. Visual color/font differences do not become semantic importance automatically.

