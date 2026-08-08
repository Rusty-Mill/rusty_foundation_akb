# Framing, streaming, and negotiation

**RM-INTERCHANGE-FRAME-0001:** Framing defines message boundaries, length encoding/unit, type/schema/profile/version identity, flags, compression/encryption/integrity relation, multiplexing, padding, end-of-stream, resynchronization, and limits.

**RM-INTERCHANGE-FRAME-0002:** Length-prefixed frames validate integer overflow, minimum/maximum, remaining bytes, nesting, compression expansion, allocation, truncation, and trailing data before allocation or decode.

**RM-INTERCHANGE-FRAME-0003:** Delimiter/self-delimiting/sequence formats define escaping, delimiter ambiguity, incremental completion, concatenated items, whitespace, malformed-item recovery, and whether trailing bytes are errors.

**RM-INTERCHANGE-STREAM-0001:** Streaming decoders expose consumed bytes/events and terminal completion, preserve state across chunks, bound buffered prefixes/tokens/containers/strings, and define cancellation and end-of-input behavior.

**RM-INTERCHANGE-STREAM-0002:** Streaming encoders disclose when headers/lengths require buffering or backpatching, output partiality on error/cancellation, flush/finalization, and whether emitted bytes may be committed.

**RM-INTERCHANGE-NEGOTIATE-0001:** Negotiation binds initiator/responder authority, ordered supported media/profile/schema/version/compression sets, required semantics, downgrade policy, selected result, transcript, cache key, and failure.

**RM-INTERCHANGE-NEGOTIATE-0002:** Content type, content encoding, schema identity, canonical profile, protocol version, and locale are distinct dimensions and cannot be inferred from filename or payload heuristics at security boundaries.

**RM-INTERCHANGE-FRAME-0004:** Compression occurs at an explicit layer and is bounded against bombs, ratio/oracle leakage, dictionary confusion, checksum ambiguity, and content-length mismatches.
