# Exact timeline and timestamp model

**RM-MEDIA-TIME-0001:** Every time value MUST include domain/epoch, signed exact rational value or integer plus time base, validity, origin, and precision. Conversion uses checked arithmetic and declared rounding; floating-point seconds are presentation conveniences only.

**RM-MEDIA-TIME-0002:** Container/media time, decode timestamp (DTS), presentation timestamp (PTS), sample duration, composition offset, stream time, running/presentation time, selected clock time, audio/video device time, wall time, and live-program date/time remain distinct.

**RM-MEDIA-TIME-0003:** Mappings preserve start offsets, edits, gaps, overlaps, negative timestamps, preroll, trim, delay, discontinuity sequence/generation, rate, and uncertainty. Missing timestamps are never fabricated silently.

**RM-MEDIA-TIME-0004:** Decode order, presentation order, arrival order, and display order remain separate. Reordering buffers are bounded and flush on discontinuity according to codec dependency rules.

**RM-MEDIA-TIME-0005:** Duration may be unknown, estimated, growing, invalid, or exact. End-of-stream, last timestamp, last duration, live edge, seekable ranges, and buffered ranges are independent observations.

**RM-MEDIA-TIME-0006:** Clock correlation records paired instants, rate/error/uncertainty, update time, provider generation, and discontinuities. It MUST NOT imply wall-clock synchronization or causal ordering outside the measured domains.

**RM-MEDIA-TIME-0007:** Timestamp overflow, wraparound, discontinuity, nonmonotonicity, duplicate values, missing duration, and extreme rates are explicit cases in parse, scheduling, and observability.

See [ADR-0070](../../adr/0070-media-time-is-exact-domain-tagged-and-discontinuous.md).
