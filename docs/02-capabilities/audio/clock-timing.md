# Audio clock and timing

Audio hardware and engines advance a sample-position clock that may be independent of the system monotonic clock. The sample clock is authoritative for stream progress; monotonic time is authoritative for portable deadlines. A correlation snapshot relates them without asserting identity.

**RM-AUDIO-CLOCK-0001:** Every running stream MUST expose a generation-scoped clock identity, frame position, sample rate or measured rate, observation time, uncertainty, and discontinuity state.

**RM-AUDIO-CLOCK-0002:** Scheduling and audiovisual synchronization MUST use explicit correlation snapshots containing sample position, monotonic instant, uncertainty, age, drift estimate, and source quality.

**RM-AUDIO-CLOCK-0003:** Providers MUST detect or surface clock reset, backward motion, endpoint migration, sample-rate change, and discontinuity; they MUST NOT manufacture a continuous position across them.

**RM-AUDIO-CLOCK-0004:** Reported latency MUST identify its boundary: application queue, engine, device, presentation estimate, capture estimate, or measured round trip. Components MUST NOT be summed when their reference points overlap or are unknown.

**RM-AUDIO-CLOCK-0005:** A requested period or latency is a constraint. The result records effective values and stability evidence; it is not a deadline guarantee.

See [ADR-0048](../../adr/0048-audio-stream-time-follows-the-device-sample-clock.md).
