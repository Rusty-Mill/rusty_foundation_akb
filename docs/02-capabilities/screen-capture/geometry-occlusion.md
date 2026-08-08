# Geometry, occlusion, and observation boundaries

**RM-SCREEN-CAPTURE-GEOMETRY-0001:** Source logical geometry, compositor geometry, physical pixels, frame pixels, crop coordinates, and destination coordinates MUST be distinct typed spaces with explicit revisioned transforms.

**RM-SCREEN-CAPTURE-GEOMETRY-0002:** Window capture MUST report whether output includes decorations, shadows, owned popups, child surfaces, transparency, offscreen portions, occluding windows, minimized content, and provider-generated padding.

**RM-SCREEN-CAPTURE-GEOMETRY-0003:** Display capture MUST report rotation, scale, origin, mode/topology generation, mirrored/virtual/remote provenance, and whether overlays or hardware planes are composited into the observation.

**RM-SCREEN-CAPTURE-GEOMETRY-0004:** Resize, display migration, crop change, scale change, or transform change MUST produce a new geometry/configuration revision before affected frames are interpreted.

**RM-SCREEN-CAPTURE-GEOMETRY-0005:** If content extent and buffer allocation differ during resize, frames MUST expose both and guarantee that padding or stale memory cannot disclose previous content.

**RM-SCREEN-CAPTURE-GEOMETRY-0006:** Region capture MUST define clipping when the region leaves its source, and MUST invalidate rather than retarget when the owning source continuity is unproven.

## Observation boundary

Provider output can be pre-composition, post-composition, reconstructed, cached, synthesized, or policy-filtered. Window capture may show an unobscured window even when the user sees it occluded; display capture may omit hardware overlays or secure UI. Therefore the contract records provider semantics and nonclaims rather than inventing a universal pixel truth.
