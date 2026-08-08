# Raw audio, video, and metadata output

**RM-MEDIA-VIDEO-0001:** Video output reuses still-image pixel/color semantics and additionally carries coded/visible/display geometry, pixel aspect, interlace/field order, rotation/flip, PTS/duration/time domain, frame/dependency identity, discontinuity, corruption/concealment, memory domain, and lease lifetime.

**RM-MEDIA-VIDEO-0002:** Color description, HDR/static/dynamic metadata, mastering/target volume, clean aperture, film grain, alpha, auxiliary/depth, and transformation provenance are per-configuration or per-frame as defined; changes are not hidden.

**RM-MEDIA-AUDIO-0001:** Audio output MUST state exact sample format, endianness, sample rate, channel count/order/layout/coordinates, planes/strides, valid frame count/capacity, PTS/duration/domain, priming/padding/trim, discontinuity, concealment, memory domain, and lifetime.

**RM-MEDIA-AUDIO-0002:** Encoded channel signaling, decoded layout, remap/downmix/upmix, resample, loudness normalization, gain, time stretch, and device layout are separate stages with requested/effective matrices, precision, delay, and clipping evidence.

**RM-MEDIA-RAW-0001:** Raw resources are immutable, closeable leases. Clone/transfer semantics preserve ownership and pool pressure; native/GPU pointers are never exposed as unconstrained Rust references or serialized across trust boundaries.

**RM-MEDIA-RAW-0002:** Corrupt/concealed/partial output is explicitly marked with affected region/range and policy. Consumers MUST NOT silently treat concealed frames/samples as bit-exact decode.

**RM-MEDIA-METADATA-0001:** Timed metadata events bind schema, track/source generation, PTS/duration/domain, payload type/size/provenance, ordering, late/duplicate/discontinuity status, and privacy class. Payload parsing is separately bounded.
