# Encode and transcode plans

`rm.image.encode` consumes immutable pixel/frame resources plus an explicit plan and produces an encoded artifact stream with evidence.

**RM-IMAGE-ENCODE-0001:** A plan MUST bind exact container/codec/profile/version, dimensions/frame structure, pixel/color/alpha/orientation policy, lossless/lossy mode, codec-specific control vector, metadata projection, thumbnails/previews, progressive/tile policy, determinism, resource budget, and destination stream requirements.

**RM-IMAGE-ENCODE-0002:** “Quality” MUST NOT be the only portable control. Effective quantization/effort/speed/chroma/bit-depth/lossless/near-lossless/alpha/animation settings are provider- and codec-qualified with requested/effective values.

**RM-IMAGE-ENCODE-0003:** Metadata, color profile, orientation, auxiliary items, animation timing, and unknown blocks are included only by explicit projection. The result reports all preservation, normalization, synthesis, substitution, and loss.

**RM-IMAGE-ENCODE-0004:** Deterministic output binds codec implementation/version, threads, CPU/GPU path, settings, metadata ordering/timestamps/identifiers, and entropy behavior. Semantic reproducibility is separate from byte-identical output.

**RM-IMAGE-ENCODE-0005:** Output reports bytes accepted/emitted, finalization, integrity/checksum, seek/backpatch requirements, and terminal status. Encoder success is not file durability; atomic replacement and synchronization compose filesystem capabilities.

**RM-IMAGE-TRANSCODE-0001:** Lossless transform/rewrite, compressed-domain transcode, decode-transform-encode, metadata-only update, and container rewrap are distinct paths. Providers disclose decoded/recompressed components and generation loss.

**RM-IMAGE-ENCODE-0006:** Sync and async paths share semantics; bounded backpressure prevents output buffering from exceeding the declared plan, and cancellation leaves no implicitly valid final artifact.
