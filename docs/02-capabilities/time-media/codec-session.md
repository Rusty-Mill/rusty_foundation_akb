# Codec sessions and encoded samples

`rm.media.codec-session` is a generation-scoped asynchronous transform between typed encoded samples and raw media resources, or the inverse for encoding.

**RM-MEDIA-CODEC-0001:** Resolution MUST bind direction, codec/profile/level/tier/configuration, sample-entry/container context, encrypted/clear state, input/output format constraints, latency/throughput/reordering, hardware preference, isolation, resource budget, and provider provenance.

**RM-MEDIA-CODEC-0002:** An encoded sample MUST carry track/configuration generation, byte-resource ranges, DTS/PTS/duration/time base, random-access/dependency/discard/preroll flags, discontinuity, encryption/subsample descriptors under authority, side data, and integrity/provenance.

**RM-MEDIA-CODEC-0003:** Configuration change, stream parameter change, seek/discontinuity, flush, reset, provider loss, hardware migration, or fallback creates a new generation. Outputs identify the configuration and input dependency generation that produced them.

**RM-MEDIA-CODEC-0004:** Submit acceptance, input consumed, output emitted, drain complete, flush/reset acknowledged, canceled, and resources released are separate milestones. Flush drains pending outputs; reset discards state; close is final.

**RM-MEDIA-CODEC-0005:** Queue and reorder depth are bounded with explicit backpressure. Callbacks deliver owned/leased resources only and cannot run UI, arbitrary plugins, blocking I/O, or exporters on codec threads.

**RM-MEDIA-CODEC-0006:** Hardware decode/encode reports device/driver, memory domain, surface pool, synchronization, supported subset, hidden conversion/copy, protection, concurrency, power, and fallback. Software fallback requires policy and a new resolution report.

**RM-MEDIA-CODEC-0007:** Malformed bitstreams, reference storms, extreme dimensions/rates, decoder stalls/crashes, device loss, corrupt side data, and output format changes remain bounded terminal or recoverable outcomes according to policy.
