# Codec identity, parameters, and negotiation

**RM-ARCHIVE-CODEC-0001:** Encode and decode requests select exact codec identity and framing independently from any surrounding container; raw DEFLATE, zlib, gzip, ZIP method DEFLATE, and HTTP content coding are not interchangeable labels.

**RM-ARCHIVE-CODEC-0002:** Parameters include level/strategy, window/block/frame sizes, checksum mode, dictionary identity, content-size disclosure, concatenated-frame policy, trailing-data policy, threading, memory ceiling, and determinism requirements.

**RM-ARCHIVE-CODEC-0003:** Decode never guesses among ambiguous formats unless an explicit bounded detection policy returns ranked evidence and requires the caller to accept the selected identity.

**RM-ARCHIVE-CODEC-0004:** Negotiation intersects ordered supported identities/profiles/parameters with security, interoperability, resource, licensing, determinism, and hardware/provider constraints; unavailable qualities are reported rather than silently weakened.

**RM-ARCHIVE-CODEC-0005:** Encoder tuning changes compressed bytes and performance but not decoded semantics. A reproducible profile pins all byte-affecting parameters and provider generation or declares cross-provider byte identity unsupported.

**RM-ARCHIVE-CODEC-0006:** Sync and async APIs share state and terminal semantics. Sync never creates a hidden runtime; async paths provide real backpressure and cancellation around source/sink I/O.
