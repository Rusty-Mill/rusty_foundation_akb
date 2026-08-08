# Capture formats, color, and orientation

A capture format records pixel/sample encoding, dimensions, plane count/layout, row/plane strides, valid region, chroma subsampling/siting, numeric range, bit depth/container, endianness where relevant, color primaries, transfer function, matrix, mastering/HDR metadata availability, frame-rate range, interlace/field state, and memory-domain constraints.

**RM-CAPTURE-FORMAT-0001:** Requested, negotiated, and per-frame effective format MUST be separately observable.

**RM-CAPTURE-FORMAT-0002:** Pixel format identity MUST define plane geometry and address calculations; consumers MUST reject overflow, undersized planes, invalid stride, inconsistent subsampling, and unsupported metadata.

**RM-CAPTURE-FORMAT-0003:** Unknown, absent, inferred, device-reported, driver-reported, and transformed color information MUST remain distinguishable. Providers MUST NOT silently assume sRGB/Rec.709/full range.

**RM-CAPTURE-FORMAT-0004:** Sensor orientation, device pose, stream rotation/mirroring instruction, pixel-memory orientation, crop, clean aperture, and display transform MUST be separately represented.

**RM-CAPTURE-FORMAT-0005:** Scaling, cropping, rotation, deinterlacing, color conversion, denoise, stabilization, HDR fusion, and beauty/effect processing MUST be disclosed transformations with latency, precision, metadata, and hardware/software provenance.

Encoded camera output may be transported as an explicitly named encoded-sample capability, but it is not interchangeable with raw frames and does not define a container or recording contract.
