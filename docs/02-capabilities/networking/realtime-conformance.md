# Real-time transport conformance specification

**RM-REALTIME-CONFORMANCE-0001:** Reports bind protocol/profile/draft and provider builds, client/server roles, origins/resources, HTTP/security/proxy/network topology, credentials/policy generations, limits, clocks, fixtures, impairment, and canonical session/event traces.

**RM-REALTIME-CONFORMANCE-0002:** Establishment tests cover malformed/rejected/redirected/challenged handshakes, wrong origin/host/accept/subprotocol/extensions/media type/settings, credentials, early data/replay, HTTP/1.1-/2-/3 mappings, proxy, pooling, cancellation at every milestone, and overload.

**RM-REALTIME-CONFORMANCE-0003:** WebSocket corpora cover masking, lengths, fragmentation/control interleaving, UTF-8, reserved opcodes/bits, compression negotiation/bombs/context takeover, message/queue bounds, ping/pong, partial transport loss, every close combination, and HTTP mapping differentials.

**RM-REALTIME-CONFORMANCE-0004:** SSE corpora cover BOM/UTF-8/chunk boundaries, CR/LF variants, comments/fields/unknown fields, multiline data, empty identifiers, retry hints, 204 stop, redirects/CORS/auth/cache/proxies, buffering/slow consumers, abrupt EOF, cursor privacy, reconnect/gap/duplicate/storm behavior, and bounds.

**RM-REALTIME-CONFORMANCE-0005:** WebTransport corpora cover exact draft/version negotiation, extended CONNECT/settings, session association, uni/bidirectional streams, resets/final sizes, datagram sizes/drop/reorder/duplicate, pre-session buffering, session/stream/data limits, pooling/fairness, migration, GOAWAY/drain, intermediary translation, and error scopes.

**RM-REALTIME-CONFORMANCE-0006:** Continuity tests cover sleep/suspend, network and proxy change, credential/policy rotation, server restart/deploy, state/cursor loss, gaps/duplicates/overlap, reconnect budgets/jitter, fleet storms, no implicit replay, late old-generation data, application reconciliation, and liveness-signal separation.

**RM-REALTIME-CONFORMANCE-0007:** Resource and adversarial tests enforce connection/session/stream/message/event/datagram/field/compression/queue/time limits, tenant fairness, slow peers, cancellation races, shutdown/drain, privacy redaction, accessible state/recovery, and bounded diagnostics under sustained load.

**RM-REALTIME-CONFORMANCE-0008:** Cross-platform/provider matrices compare canonical results across Windows, Linux, macOS, browser-mediated and native providers, IPv4/IPv6/proxy/VPN/constrained paths, and supported protocol revisions; unsupported or degraded behavior remains explicit.

