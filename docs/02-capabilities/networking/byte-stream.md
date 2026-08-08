# Connected byte streams

## Capability identity

`rm.network.byte-stream` is an owned full-duplex connected transport preserving byte order independently in each direction.

**RM-NETWORK-STREAM-0001:** A successful creation returns one stream resource with observed local/peer endpoints, transport/provider identity, connection epoch, selected path evidence, and negotiated option claims.

**RM-NETWORK-STREAM-0002:** Reads and writes may complete partially and report exact progress. A write completion means bytes were accepted by the local transport, not received, processed, or durably stored by the peer.

**RM-NETWORK-STREAM-0003:** The stream preserves byte order but no application write boundaries. Consumers supply framing at a higher layer.

**RM-NETWORK-STREAM-0004:** Graceful write shutdown, peer EOF, local close, reset/abort, timeout, unreachable, and indeterminate failure remain distinct. EOF follows all readable accepted bytes.

**RM-NETWORK-STREAM-0005:** Backpressure is bounded. Async operations do not occupy an executor thread solely to block where native readiness/completion exists; sync operations never nest a hidden runtime.

**RM-NETWORK-STREAM-0006:** Cancellation reports completed progress, confirmed cancellation, or indeterminate outcome. It cannot roll back bytes accepted by the transport.

**RM-NETWORK-STREAM-0007:** Concurrent read/write is supported; concurrent same-direction ordering and fairness are explicit provider claims. Drop/close does not promise protocol-level graceful shutdown.

**RM-NETWORK-STREAM-0008:** Keepalive, no-delay, buffer sizes, traffic class, interface binding, zero-copy, and native handles are separately negotiated options or escape contracts, never silently enabled semantics.

