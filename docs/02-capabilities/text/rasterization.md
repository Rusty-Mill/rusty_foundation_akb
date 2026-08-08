# Glyph rasterization adapter

| Field | Value |
|---|---|
| Status | Draft adapter contract 0.1.0 |

**RM-TEXT-RASTER-0001:** Rasterization consumes exact font face/glyph IDs, size, device transform/scale, origin/subpixel phase, hinting, antialiasing, color-font palette, contrast/gamma policy, and target color/alpha format.

**RM-TEXT-RASTER-0002:** Output identifies coverage/image/vector representation, bearings/extent, format/color space, cache identity, and degradation. Raster metrics do not silently replace shaping advances.

**RM-TEXT-RASTER-0003:** Grayscale, subpixel, monochrome, outline, bitmap strike, SVG, layered/vector color, and embedded-paint glyphs are negotiated modes. Subpixel rendering is not used where composition/transform/output makes its assumptions invalid.

**RM-TEXT-RASTER-0004:** Raster caches include exact font artifact/face/variation, glyph, size, transform/subpixel phase, rendering policy, scale, color palette, and provider version. Font/display/policy changes invalidate affected entries.

**RM-TEXT-RASTER-0005:** Missing, malformed, oversized, or unsupported glyph representations fail or use the resolved missing-glyph policy under bounded resources. They cannot execute arbitrary font-contained code.

**RM-TEXT-RASTER-0006:** Pixel equality is promised only for an exact provider/configuration/artifact environment. Cross-provider conformance uses semantic mapping, metrics tolerance, coverage, and perceptual/reference evidence rather than universal identical pixels.

**RM-TEXT-RASTER-0007:** High contrast, forced colors, zoom, transparency, reduced motion, and capture/content sensitivity remain renderer/accessibility policy inputs; glyph rasterization does not infer them from text.

