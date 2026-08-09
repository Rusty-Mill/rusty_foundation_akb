# Streaming, framing, dictionaries, and integrity

**RM-ARCHIVE-STREAM-0001:** Streaming sessions consume and produce bounded buffers with explicit progress, need-input, need-output, frame-complete, stream-complete, cancelled, and failed states; zero progress cannot spin indefinitely.

**RM-ARCHIVE-STREAM-0002:** Decoder budgets cover compressed and expanded bytes, ratio, frames/members/blocks, dictionaries, window and retained history, CPU/work units, wall time, nesting, allocations, and output backpressure.

**RM-ARCHIVE-STREAM-0003:** Cancellation reports accepted input, emitted but unverified output, verified output, frame/member boundary, and whether resumable state exists. Partial output is never labeled complete.

**RM-ARCHIVE-DICT-0001:** Dictionaries are immutable content-identified inputs with codec/profile scope, maximum size, provenance, sensitivity, lifecycle, and distribution authority. An integer dictionary ID alone is not global identity.

**RM-ARCHIVE-INTEGRITY-0001:** Format checksums detect corruption only within their named coverage and threat model. Cryptographic digests and authenticators remain independent evidence.

**RM-ARCHIVE-INTEGRITY-0002:** Consumers choose release policy for bytes before terminal integrity/authentication: buffer, stage, mark tainted, or stream only to a rollback-capable sink. Unverified bytes cannot become trusted executable/configuration state.

**RM-ARCHIVE-INTEGRITY-0003:** Concatenation, skippable frames, padding, unknown extensions, and trailing bytes use explicit accept/reject/preserve rules and remain observable.
