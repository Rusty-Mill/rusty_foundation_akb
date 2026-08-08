# Security and accessibility

**RM-IMAGE-SECURITY-0001:** Probe, metadata projection, preview, full decode, external-resource access, hardware acceleration, encode, metadata preservation, and artifact write use separate authority and policy. Observation never writes or contacts external references.

**RM-IMAGE-SECURITY-0002:** Untrusted/remote/plugin-controlled images default to isolated decode where available. Provider discovery records native/third-party codec provenance, sandbox/process boundary, update source, signature, supported subset, and crash history; installed codec presence does not authorize selection.

**RM-IMAGE-SECURITY-0003:** Decompression bombs, integer overflow, deep/cyclic structures, malformed entropy/tables/profiles/metadata, huge sparse canvases, frame storms, tiny-duration animation, GPU hangs, and parser crashes are required adversarial classes.

**RM-IMAGE-SECURITY-0004:** Diagnostics never include source bytes, decoded pixels, thumbnails, paths/URLs, sensitive metadata, profile fingerprints, or content-derived stable hashes by default. Synthetic fixture IDs replace user content.

**RM-IMAGE-ACCESS-0001:** Image display provides product-owned alternative text/caption/long description and semantic context. Embedded description metadata is untrusted candidate content, not automatically safe or sufficient accessible text.

**RM-IMAGE-ACCESS-0002:** Animated content respects reduced-motion and flash/luminance safety policy with pause/stop/hide controls, static alternative selection, keyboard/assistive operation, and no meaning dependent solely on animation or color.

**RM-IMAGE-ACCESS-0003:** Decode/progress/error UI exposes accessible state without rapid announcement per progressive pass. Orientation, crop, loading placeholder, missing metadata, and degraded color are communicated where material.
