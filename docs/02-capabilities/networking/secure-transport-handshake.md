# Handshake and lifecycle

**RM-SECURE-HANDSHAKE-0001:** Handshake is an async-first, cancellation-safe state machine over explicit transport I/O with deadlines, byte/message/amplification/flight/retry bounds, backpressure, and executor separation. Sync operation never creates a hidden runtime or nested event loop.

**RM-SECURE-HANDSHAKE-0002:** Progress distinguishes needs read, needs write, credential/trust/interaction pending, timer/retransmit, transport blocked, peer flight received, authentication complete, confirmed, ready, and terminal failure without busy polling.

**RM-SECURE-HANDSHAKE-0003:** Handshake transcripts, messages, extensions, certificates, alerts, QUIC crypto frames, and provider errors are untrusted and bounded before allocation or callback. Unknown critical/incompatible semantics fail according to protocol and policy.

**RM-SECURE-HANDSHAKE-0004:** Cancellation/timeout reports whether any ClientHello, identity, early data, credential proof, ticket use, server response, or application data may have crossed the boundary. It closes/abandons safely and does not claim peer nonreceipt.

**RM-SECURE-HANDSHAKE-0005:** Server admission applies address validation/amplification, handshake concurrency/memory/CPU, certificate/key-operation, authentication, pending-interaction, per-source/account, and global budgets before expensive work.

**RM-SECURE-HANDSHAKE-0006:** Key updates are generation transitions with direction, trigger/limits, request/response, bytes/records/time, pending I/O, completion, peer behavior, and failure evidence. Applications cannot assume an update occurred merely because it was requested.

**RM-SECURE-HANDSHAKE-0007:** Legacy renegotiation is disabled by default and, if selected for a bounded legacy profile, changes channel/authentication generation, disables incompatible binding assumptions, and cannot silently weaken policy. TLS 1.3 post-handshake authentication is separately selected.

**RM-SECURE-HANDSHAKE-0008:** Suspend/resume, network change, clock change, provider/policy/credential rotation, process fork/snapshot, and peer address change trigger declared continue/revalidate/key-update/migrate/reconnect/close behavior.

