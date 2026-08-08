# Frame format, color, and timing

A `CaptureFrame` is an immutable observation bound to session and source generations. It carries sequence, discontinuity, pixel extent, valid-content rectangle, plane layouts and strides, memory domain and synchronization, alpha semantics, an immutable [image description](../display-color/image-description.md), orientation/transform, damage evidence, timestamp boundary/domain/quality, provider transformations, and lease lifetime.

**RM-SCREEN-CAPTURE-FRAME-0001:** Every frame MUST describe exact pixel format, dimensions, planes, strides, offsets, valid bytes, alpha, memory domain, synchronization, and lifetime with checked arithmetic.

**RM-SCREEN-CAPTURE-FRAME-0002:** Color primaries, transfer, matrix, range, luminance interpretation, reference white, HDR metadata, and provider conversion MUST be explicit or unknown; pixel format alone MUST NOT imply color semantics.

**RM-SCREEN-CAPTURE-FRAME-0003:** Timestamps MUST name the observed boundary, clock domain, uncertainty/quality, and correlation revision. Delivery time MUST NOT be substituted for compositor/source time without disclosure.

**RM-SCREEN-CAPTURE-FRAME-0004:** Sequence gaps, duplicate/unchanged output, stale frames, timestamp discontinuities, and source/configuration generation changes MUST be observable.

**RM-SCREEN-CAPTURE-FRAME-0005:** Damage or dirty-region metadata is optimization evidence only. Consumers requiring a complete image MUST maintain and reset state according to generation and provider rules.

**RM-SCREEN-CAPTURE-FRAME-0006:** A frame MUST distinguish buffer extent from valid content, source-space crop, padding, scaling, rotation, and letterbox regions.

**RM-SCREEN-CAPTURE-FRAME-0007:** CPU mapping, GPU import, conversion, copying, and ownership transfer MUST be explicit operations with bounded failure and synchronization behavior.

Frame acquisition never implies encoding, compression, persistence, OCR, accessibility semantics, or permission to disclose the pixels to another principal.
