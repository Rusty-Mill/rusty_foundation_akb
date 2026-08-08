# Rendering, pagination, and color

**RM-PRINT-RENDER-0001:** Geometry uses explicit physical units, media/trim/bleed/content/imageable boxes, transform origin, orientation, and clipping. Device pixels and screen DPI are not document units.

**RM-PRINT-RENDER-0002:** Pagination occurs against the resolved plan. Widow/orphan rules, headers/footers, page numbering, scaling, n-up, booklet/signature imposition, and blank-page insertion belong to a named producer or imposition stage and are never double-applied.

**RM-PRINT-RENDER-0003:** Vector, text, image, transparency, overprint, spot-color, and raster fallback support is declared. Unsupported features follow an explicit fail, flatten, rasterize, substitute, or preview-warning policy with fidelity evidence.

**RM-PRINT-COLOR-0001:** Source/effective color spaces and profiles, rendering intent, black generation where applicable, output mode, conversion owner/version, precision, alpha handling, and calibration assumptions are recorded.

**RM-PRINT-COLOR-0002:** Color/monochrome capability, user choice, document intent, and actual device behavior remain distinct. A color-preview match or destination claim is not a colorimetric guarantee without measured evidence.

**RM-PRINT-RENDER-0004:** Page generation is bounded by memory, time, decoded pixels, path/glyph/object counts, recursion, output bytes, and cancellation checkpoints. Backpressure prevents an unbounded rendered-page or spool queue.

**RM-PRINT-RENDER-0005:** Preview and print share the same immutable pagination/output plan where fidelity is claimed, while explicitly reporting preview-only substitutions and display-versus-paper color limits.
