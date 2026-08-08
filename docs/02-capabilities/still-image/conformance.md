# Still-image and image-codec conformance specification

| Area | Required evidence |
|---|---|
| Probe/container | extension/MIME/signature conflicts, truncation/incremental bytes, unknown brands/chunks, nested/multi-item/auxiliary/thumbnail structures, ambiguous providers |
| Decode limits | extreme dimensions/counts/depth/ratio, overflow, sparse/tiled/cyclic references, malformed entropy/tables/profiles/metadata, timeout/cancel/crash/GPU hang |
| Pixels | packed/planar/indexed/gray/RGB/YUV/CMYK, range/chroma/endian/depth/stride, straight/premultiplied/absent alpha, orientation/aspect/crop, exact color descriptions |
| Progressive/region | every pass/revision, final equivalence, incomplete/end distinction, update storms, oriented coordinates, block expansion, native-versus-full-decode evidence |
| Animation | blend/disposal/background/restore, timing/loop edge cases, random access dependencies, reduced motion, huge canvas/frame storm, cancellation/drop policy |
| Metadata | EXIF/XMP/IPTC/container/vendor conflicts, lazy bounds, sensitive-field projection, unknown preservation, edit/rewrite/re-encode evidence, signature nonclaims |
| Encode/transcode | lossless/lossy control vectors, metadata/color/orientation, deterministic/semantic claims, streaming/backpatch/finalization, cancellation, durability separation |
| Cross-cutting | native/third-party/isolation providers, platform-version matrices, privacy redaction, accessible alternatives/status/animation controls, bounded concurrency |

The corpus contains standards-authoritative vectors, independently generated valid files, malformed/truncated/mutated/fuzz regressions, decompression bombs that are rejected before dangerous allocation, metadata/profile adversaries, color/alpha/orientation numeric oracles, and multi-provider differential cases. Expected disagreements are classified by specification ambiguity, unsupported feature, provider defect, or policy—not silently normalized.

Reports bind corpus case/digest/provenance/license, format/profile/brands, provider/codec/version/build/signature/isolation, OS/architecture, hardware/driver, requested/effective plan and budgets, output layout/color/metadata digests, transform engine, timing/memory/allocation/handle evidence, and every fidelity/security/determinism nonclaim. User images and sensitive metadata never enter the corpus or failure bundles.
