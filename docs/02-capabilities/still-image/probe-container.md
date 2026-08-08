# Probe and container inspection

`rm.image.probe` performs bounded, side-effect-free identification and structural inspection over an explicit byte source. It does not decode pixels or load external resources.

**RM-IMAGE-PROBE-0001:** Results MUST preserve claimed MIME/extension, signature/brand matches, provider candidates, bytes inspected, required additional bytes/seek behavior, confidence/provenance, ambiguity, and terminal/incomplete status independently.

**RM-IMAGE-PROBE-0002:** Selection MUST NOT rely solely on extension, MIME, one magic prefix, or provider registration order. Conflicting evidence is reported; policy chooses whether to reject or attempt a bounded decoder.

**RM-IMAGE-CONTAINER-0001:** Inspection MUST expose container identity/version/brands, item/frame count or bounded unknown, logical canvas, declared dimensions, thumbnails/previews, animation/multi-image structure, metadata block inventory, color/orientation evidence, external references, and truncation/unknowns without materializing full payloads.

**RM-IMAGE-CONTAINER-0002:** Item identifiers, frame indices, primary item, auxiliary/depth/alpha items, thumbnails, previews, layers, pages, and animation frames MUST remain typed relationships. A first item is not silently the primary display image.

**RM-IMAGE-CONTAINER-0003:** Container and codec support are capability vectors: probe, metadata, full/incremental/region decode, animation, encode, lossless rewrite, color depth, alpha, hardware path, and isolation. A provider MUST NOT claim “supports format” without the selected operations and constraints.

**RM-IMAGE-CONTAINER-0004:** Inspection uses checked offset/length/count arithmetic, nesting and metadata limits, cycle/reference validation, and declared-versus-available byte reconciliation. Unknown extension data is skipped or preserved only under explicit policy.

See [ADR-0068](../../adr/0068-image-format-detection-is-evidence-not-trust.md).
