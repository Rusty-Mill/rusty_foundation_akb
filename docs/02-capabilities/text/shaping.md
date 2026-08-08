# `rm.text.shaping`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-TEXT-SHAPE-0001:** Input binds one text revision/range, exact font-resolution plan, size/scale-independent design units, script, language, direction, cluster level, OpenType features/variations, and shaping-engine/data versions.

**RM-TEXT-SHAPE-0002:** Output is ordered glyph runs containing exact face instance, glyph IDs, advances/offsets, cluster-to-text mapping, direction, unsafe-to-break flags where supported, and missing/fallback/degradation evidence.

**RM-TEXT-SHAPE-0003:** Glyph IDs are face-instance-local opaque values. They are not Unicode values, stable across font artifacts, or accessibility/search content.

**RM-TEXT-SHAPE-0004:** The cluster mapping supports many scalars to one glyph, one scalar to multiple glyphs, reordering, combining marks, default ignorables, variation selectors, emoji sequences, and zero-advance glyphs without inventing one-character/one-glyph correspondence.

**RM-TEXT-SHAPE-0005:** Incremental shaping may reuse unaffected runs only when the provider proves the edit cannot affect surrounding shaping context. Otherwise the declared context window or containing shaping segment is recomputed.

**RM-TEXT-SHAPE-0006:** Shaping is deterministic for identical text, exact font artifacts, features, direction/language/script, engine/data versions, and policy. Environment font discovery is excluded from this operation.

**RM-TEXT-SHAPE-0007:** Malformed font tables, excessive glyph expansion, recursion, pathological lookups, and oversized inputs are bounded with typed failure; partial output is not reported as complete.

**RM-TEXT-SHAPE-0008:** Hit testing and caret construction do not split a shaping cluster unless the exact script/font/provider supplies valid internal caret positions. Grapheme boundaries alone do not prove glyph-cluster caret validity.

**RM-TEXT-SHAPE-0009:** Shaping may be synchronous for bounded in-memory runs and also supplies a batch/async path for large documents or remote/isolation providers. Neither path mutates input text or font plans.

