# Audio formats and channel layouts

## Format value

An audio format is immutable and records encoding/sample representation, sample rate, channel count, semantic channel layout and order, interleaving, container bits, valid bits, numeric range, and byte order where meaningful. A frame contains one sample for every channel.

**RM-AUDIO-FORMAT-0001:** Requested, negotiated, and effective formats MUST be separately observable.

**RM-AUDIO-FORMAT-0002:** A format MUST NOT infer channel meaning from channel count alone. Unknown, discrete, ambisonic, and named speaker layouts remain distinguishable.

**RM-AUDIO-FORMAT-0003:** Frame/byte arithmetic MUST reject overflow, invalid alignment, non-integral frames, unsupported representations, and inconsistent channel layouts before buffer access.

**RM-AUDIO-FORMAT-0004:** The base stream capability MUST NOT perform undisclosed sample-rate conversion, remixing, dithering, gain, endian conversion, or sample conversion. A selected conversion service reports its exact transformation and latency.

**RM-AUDIO-FORMAT-0005:** PCM silence and clipping rules MUST be defined for every supported numeric representation; raw encoded packets are not PCM frames.

Negotiation returns the accepted format, period/quantum constraints, buffer capacity, alignment, conversion path if separately authorized, and the reasons requested properties were rejected or degraded. “Closest format” is not success unless the request explicitly permits bounded alternatives.
