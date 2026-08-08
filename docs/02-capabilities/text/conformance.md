# Text, fonts, and layout conformance specification

**Status:** Draft

| ID | Requirements | Method |
|---|---|---|
| TEXT-UNICODE-001 | UNICODE-0001–0005 | Run version-pinned Unicode normalization, grapheme/word/sentence, malformed encoding, and exhaustive boundary conversion vectors |
| TEXT-UNICODE-002 | UNICODE-0006–0009 | Run official bidi/line-break data plus tailored locale/higher-protocol cases; verify logical preservation and version-change reports |
| TEXT-FONT-001 | FONT-0001–0006 | Resolve controlled same-name/different-artifact, variable, synthetic, fallback, missing, color, bitmap, and collection-change fixtures deterministically |
| TEXT-FONT-002 | FONT-0007–0009 | Fuzz malformed fonts under CPU/memory/time limits; deny network/export; test cancellation, untrusted isolation, privacy, and cache provenance |
| TEXT-SHAPE-001 | SHAPE-0001–0004 | Script corpus covers Latin, Arabic, Hebrew, Indic, Southeast Asian, CJK, combining, emoji/ZWJ/variation, vertical, fallback, and many-to-many clusters |
| TEXT-SHAPE-002 | SHAPE-0005–0009 | Compare incremental/full shaping, deterministic replay, pathological limits, caret safety, sync/batch/async equivalence, and exact artifact mutation |
| TEXT-LAYOUT-001 | LAYOUT-0001–0005 | Golden semantic layout fixtures cover bidi, wrapping, mandatory/prohibited breaks, hyphenation, justification, tabs, inline objects, ellipsis, vertical/ruby, and caret affinity |
| TEXT-LAYOUT-002 | LAYOUT-0006–0010 | Property-test hit-test round trips, stale transforms, incremental/full reflow, accessibility semantic ranges, masking, and sensitive-text canaries |
| TEXT-RASTER-001 | RASTER-0001–0007 | Exact-environment raster goldens plus metric/coverage/perceptual cross-provider checks for scale, subpixel phase, hinting, color glyphs, high contrast, and malformed content |

## Corpus and evidence rules

Every vector records Unicode/CLDR version, exact font artifact digest/face/variation/license fixture, shaping/layout/raster provider versions, locale/script/direction/features, scale/transform, and expected semantic mappings. Platform system fonts are not stable conformance fixtures; redistributable pinned test fonts or generated fixtures are required.

Terminal integration additionally proves that font fallback/shaping never changes emulator cell allocation, cursor coordinates, or logical copy/accessibility text. Editor integration proves UTF-8/UTF-16/scalar/grapheme mappings at every IME replacement boundary.

