# Listeners and accepted connections

## Capability identity

`rm.network.listener` binds explicit local network authority and accepts inbound byte-stream transports.

**RM-NETWORK-LISTENER-0001:** Bind policy distinguishes exact address/interface, loopback, wildcard, dual-stack, ephemeral port, reuse, and activation/inherited endpoint. Wildcard binding is never the secure default by implication.

**RM-NETWORK-LISTENER-0002:** Bind/listen returns an immutable effective-endpoint snapshot and option-quality report or fails without exposing an indeterminate listener.

**RM-NETWORK-LISTENER-0003:** Each accepted connection is a separately owned stream with local/peer observations, listener generation, accept time, and inherited policy. Peer address is untrusted input, not identity.

**RM-NETWORK-LISTENER-0004:** Backlog is a provider hint/claim, not an exact portable queue capacity. Overload policy, admission limits, handshake deadlines, and resource budgets are explicit.

**RM-NETWORK-LISTENER-0005:** Cancellation, listener close, accepted-late race, transient accept failure, resource exhaustion, and terminal provider failure remain distinguishable. Late accepted streams are closed or delivered exactly once under policy.

**RM-NETWORK-LISTENER-0006:** Port/address reuse and multi-process distribution are optional platform-specific qualities requiring hijack/isolation analysis; a common flag name does not imply common semantics.

