# Image descriptions and color semantics

`rm.color.image-description` is an immutable semantic value that links encoded component values to colorimetry and luminance meaning.

**RM-COLOR-DESCRIPTION-0001:** A description MUST identify component model/order, numeric encoding/range/precision, chroma subsampling/siting where relevant, primaries/white point, transfer characteristic, matrix coefficients where relevant, alpha association, reference white, minimum/maximum luminance semantics, and provenance/unknowns.

**RM-COLOR-DESCRIPTION-0002:** Primary color volume, target/mastering color volume, MaxCLL/MaxFALL or dynamic metadata, scene/display reference, viewing environment, and signal legal range MUST remain distinct and optional. Contradictory metadata is rejected or explicitly quarantined.

**RM-COLOR-DESCRIPTION-0003:** Named spaces such as sRGB, Display P3, scRGB, BT.709, BT.2020/PQ, HLG, and linear variants resolve to exact versioned semantics; similar names MUST NOT be treated as equivalent without evidence.

**RM-COLOR-DESCRIPTION-0004:** ICC profile bytes are one opaque, size-bounded representation with digest, profile class/version, validation, provenance, and parser/engine identity. Profile presence does not imply calibration, correctness, or safe content.

**RM-COLOR-DESCRIPTION-0005:** Equality and cache keys bind the complete normalized semantic description plus interpretation-engine/version where representation-dependent. Display names and profile filenames are never identity.

**RM-COLOR-DESCRIPTION-0006:** Undefined, out-of-domain, non-finite, out-of-gamut, over-range, and negative component behavior is explicit. Providers MUST NOT silently clamp before the selected conversion policy.

See [ADR-0066](../../adr/0066-color-is-an-immutable-semantic-description.md).
