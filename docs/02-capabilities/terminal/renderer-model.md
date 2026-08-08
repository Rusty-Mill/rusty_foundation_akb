# Terminal renderer adapter model

**Status:** Draft component contract 0.1.0

## Purpose

Present a versioned terminal logical-state snapshot/delta through a windowing/graphics/text stack while preserving the emulator's grid, cursor, selection, style, and viewport truth. The renderer does not parse terminal bytes or determine terminal protocol semantics.

## Inputs and outputs

Inputs include emulator revision, grid/history viewport, dirty regions, cell content/attributes, cursor/selection, theme and palette, font policy, display scale/color information, user accessibility preferences, animation clock, and target surface generation. Output is a presented frame result with consumed revision, damage, timing, quality/degradation, and device/surface status.

## Requirements

- **RM-TERMINAL-RENDER-0001:** Every frame **MUST** identify one complete emulator revision and viewport transform; mixed-revision cell state **MUST NOT** be presented as coherent.
- **RM-TERMINAL-RENDER-0002:** The emulator's cell allocation and cursor coordinates **MUST** remain authoritative; shaping, fallback, hinting, and ligatures **MUST NOT** silently move logical content between cells.
- **RM-TERMINAL-RENDER-0003:** Font family/fallback, size, weight/style, feature/ligature, rasterization, emoji, and missing-glyph policy **MUST** be explicit and observable.
- **RM-TERMINAL-RENDER-0004:** Grapheme, combining, wide/ambiguous, variation-selector, emoji, bidi/control, and orphan-cell cases **MUST** render under the exact emulator Unicode/width policy or disclose incompatibility.
- **RM-TERMINAL-RENDER-0005:** Display scale, cell metrics, padding, viewport rounding, and resize **MUST** avoid cumulative drift and preserve a deterministic mapping between pointer pixels and terminal cells for a given transform revision.
- **RM-TERMINAL-RENDER-0006:** Dirty-region optimization **MUST** be observationally equivalent to a full redraw of the same revision.
- **RM-TERMINAL-RENDER-0007:** Palette, true color, alpha/compositing, inverse, faint, underline variants, strike, conceal, selection, search, cursor, and hyperlink decoration **MUST** define precedence and color-space behavior.
- **RM-TERMINAL-RENDER-0008:** High-contrast/forced-color and non-color-only policies **MUST** preserve actionable host distinctions even when application-requested colors are overridden.
- **RM-TERMINAL-RENDER-0009:** Blink, cursor animation, bell flash, smooth scroll, and transitions **MUST** obey reduced-motion/animation preferences and pause when not visible under policy.
- **RM-TERMINAL-RENDER-0010:** Frame scheduling **MUST** coalesce revisions without losing the final state, bound latency/memory, and report dropped/intermediate visual revisions when relevant.
- **RM-TERMINAL-RENDER-0011:** Surface resize/recreation, occlusion, display migration, scale/color change, GPU/device loss, suspend/resume, and renderer fallback **MUST** recover from a retained logical snapshot without mutating emulator truth.
- **RM-TERMINAL-RENDER-0012:** Selection/cursor/hyperlink hit testing **MUST** consume the exact viewport transform revision and reject or re-evaluate stale coordinates.
- **RM-TERMINAL-RENDER-0013:** Screenshots, frame capture, thumbnails, GPU diagnostics, and crash artifacts **MUST** be treated as sensitive terminal content and disabled or redacted by default.
- **RM-TERMINAL-RENDER-0014:** The renderer **MUST NOT** serve as the accessibility source of truth; accessibility adapters consume logical emulator state.

## Quality dimensions

Renderer claims form a vector: supported scripts/emoji, font fallback fidelity, color space/HDR, damage precision, presentation timing, device acceleration, software fallback, power behavior, accessibility preferences, and capture protection. “GPU accelerated” alone is not a quality level.

## Windowing and graphics boundary

The adapter consumes a surface/presentation capability and display metrics from future windowing/graphics domains. It may have software, GPU, or remote implementations. Native handles and graphics APIs remain behind those providers; the terminal framework sees surface generation, size/scale/color properties, frame timing, damage, and loss/recovery outcomes.

