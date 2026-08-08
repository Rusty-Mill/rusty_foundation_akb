# Text platform and standards research

**Status:** Research evidence; normative conclusions live in contracts and ADRs.

## Unicode and OpenType

Unicode specifies logical character properties and versioned algorithms for bidirectional resolution, line breaking, normalization, and segmentation. These algorithms are tailorable and depend on exact Unicode/CLDR data. OpenType shaping maps character sequences through script/language/features and font tables into positioned glyphs; the mapping is not one-to-one.

Primary sources: [Unicode Bidirectional Algorithm](https://unicode.org/reports/tr9/), [Line Breaking Algorithm](https://unicode.org/reports/tr14/), [Unicode Normalization](https://unicode.org/reports/tr15/), [Text Segmentation](https://unicode.org/reports/tr29/), [OpenType shaping](https://learn.microsoft.com/en-us/typography/opentype/spec/shaping), [OpenType font variations](https://learn.microsoft.com/en-us/typography/opentype/spec/otvaroverview).

## Windows: DirectWrite

DirectWrite separates font collections/faces, text analysis/layout, glyph runs, rendering, and color glyph expansion. Its documentation explicitly describes glyph composition/decomposition and face-local glyph runs. This supports semantic text plus many-to-many cluster maps rather than glyph-as-character APIs.

Primary sources: [DirectWrite introduction](https://learn.microsoft.com/en-us/windows/win32/directwrite/introducing-directwrite), [glyphs and glyph runs](https://learn.microsoft.com/en-us/windows/win32/directwrite/glyphs-and-glyph-runs), [text formatting and layout](https://learn.microsoft.com/en-us/windows/win32/directwrite/text-formatting-and-layout), [font fallback](https://learn.microsoft.com/en-us/windows/win32/directwrite/font-fallback), [color fonts](https://learn.microsoft.com/en-us/windows/win32/directwrite/color-fonts).

## Linux ecosystem

HarfBuzz shapes Unicode text with exact font data into glyph positions and clusters. FreeType loads and rasterizes font faces/glyphs. Fontconfig discovers/configures system font matches. Their separation demonstrates that discovery, shaping, and rasterization can remain independent provider contracts even when composed in one implementation.

Primary sources: [HarfBuzz shaping concepts](https://harfbuzz.github.io/what-is-harfbuzz.html), [HarfBuzz clusters](https://harfbuzz.github.io/working-with-harfbuzz-clusters.html), [FreeType glyph management](https://freetype.org/freetype2/docs/tutorial/step2.html), [Fontconfig developer reference](https://fontconfig.pages.freedesktop.org/fontconfig/fontconfig-devel/).

## macOS: Core Text

Core Text supplies font descriptors/collections and cascading, character-to-glyph shaping, positioned glyph runs, line breaking, and frames. Glyph runs share attributes/direction, while font cascading selects replacements. The same semantic boundaries can therefore map to native Core Text without making Core Text structures portable types.

Primary sources: [Core Text](https://developer.apple.com/documentation/coretext), [Core Text programming guide](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/CoreText_Programming/Introduction/Introduction.html).

## Derived portability conclusions

| Concern | Portable rule |
|---|---|
| Text position | Explicit revision and unit |
| Font selection | Policy snapshot resolves exact artifact/face instances |
| Shaping | Exact inputs produce glyph runs and cluster maps |
| Bidi/layout | Logical and visual order remain distinct |
| Rasterization | Provider/configuration-specific pixels |
| Accessibility/copy/search | Consume semantic text, never glyph IDs/pixels |

