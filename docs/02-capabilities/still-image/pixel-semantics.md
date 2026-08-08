# Pixel, color, alpha, and orientation semantics

**RM-IMAGE-PIXEL-0001:** Every output MUST state pixel/sample encoding, component order/model, dimensions, planes, row/plane strides, valid region, subsampling/siting, numeric range, bit/container depth, endianness where relevant, alpha mode, memory domain, map/copy rules, and lifetime.

**RM-IMAGE-PIXEL-0002:** Output binds an immutable [`rm.color.image-description`](../display-color/image-description.md) or explicitly unknown color semantics. Providers MUST NOT silently assign sRGB/BT.709, full range, opaque alpha, or gamma behavior.

**RM-IMAGE-PIXEL-0003:** Straight, premultiplied, coverage, associated-in-encoded-space, absent, binary, and auxiliary alpha remain distinguishable. Premultiplication states the linear/nonlinear domain and zero-alpha color policy.

**RM-IMAGE-PIXEL-0004:** Stored dimensions/orientation metadata, clean aperture/crop, pixel aspect ratio, display transform, and returned pixel orientation are separate. Applying rotation/mirroring is explicit and changes geometry/output generation; metadata is then updated or removed coherently.

**RM-IMAGE-PIXEL-0005:** Palette/indexed data, grayscale, RGB, YCbCr, CMYK, Lab, depth, masks, gain maps, and auxiliary images remain typed. Conversion to an application-preferred layout reports precision, gamut/range, alpha, metadata, and hardware/software changes.

**RM-IMAGE-PIXEL-0006:** Consumers validate all plane/stride/extent arithmetic and MUST NOT construct Rust references to padding, uninitialized, aliased, misaligned, or provider-owned memory beyond the lease.

**RM-IMAGE-PIXEL-0007:** Content hash, encoded artifact identity, decoded semantic identity, and perceptual similarity are different. Re-encoding, metadata edits, orientation application, color conversion, or decoder version can change one without equivalence in the others.
