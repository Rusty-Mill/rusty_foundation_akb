# Text layout service

| Field | Value |
|---|---|
| Status | Draft platform service 0.1.0 |

The service composes segmentation, bidi, font resolution, shaping, line breaking, inline objects, paragraph style, and geometry. It produces immutable layout revisions; it does not edit semantic text or draw pixels.

**RM-TEXT-LAYOUT-0001:** Input binds semantic text/spans, text revision, available inline extent, writing mode, base direction, locale, line-break/hyphenation policy, tabs, alignment/justification, spacing, max lines/overflow, font policy, and exact algorithm/data versions.

**RM-TEXT-LAYOUT-0002:** Output contains paragraph/line fragments, logical and visual runs, baselines/metrics, glyph runs, decorations, inline-object placements, clipping/ellipsis, cluster maps, caret stops, and semantic-to-geometry hit-test maps under one layout revision.

**RM-TEXT-LAYOUT-0003:** Bidi resolution occurs by paragraph; line breaking uses resolved levels and reorders each line without changing logical storage. Selection/copy/accessibility return logical semantic ranges unless a caller explicitly requests visual traversal.

**RM-TEXT-LAYOUT-0004:** Line breaking never splits a prohibited grapheme/shaping boundary. Hyphen insertion is a visual/layout artifact with a mapping to the original semantic range and is not silently copied as source text.

**RM-TEXT-LAYOUT-0005:** Caret movement distinguishes logical, visual, grapheme, word, and line navigation policies. Every caret stop maps to a valid semantic boundary and affinity; ambiguous bidi positions retain leading/trailing affinity.

**RM-TEXT-LAYOUT-0006:** Hit testing consumes the exact layout and window-transform revisions. Outside/ambiguous positions return explicit nearest/inside/affinity results; stale geometry is rejected or reconciled.

**RM-TEXT-LAYOUT-0007:** Justification, letter/word spacing, tabs, baseline alignment, ruby/vertical text, truncation, and inline objects are feature-vector claims. Unsupported required behavior fails rather than approximating silently.

**RM-TEXT-LAYOUT-0008:** Incremental reflow declares the earliest affected boundary and produces the same final layout as full recomputation under identical inputs. Caches key exact text/font/algorithm/policy identity.

**RM-TEXT-LAYOUT-0009:** Accessibility exposes original semantic text, language, direction, logical ranges, and geometry mappings. Glyph order, elision, generated hyphens, and decorative text do not replace semantic truth.

**RM-TEXT-LAYOUT-0010:** Password masking is a presentation transform. Layout/accessibility/clipboard/diagnostics follow independent sensitive-text policy and never assume masked glyphs erase the underlying text.

