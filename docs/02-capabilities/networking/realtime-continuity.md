# Real-time reconnect, resume, replay, and liveness

**RM-REALTIME-CONTINUITY-0001:** Reconnect is a policy decision triggered by typed closure/path/session/application evidence and constrained by original service, credentials, privacy, foreground/background, network cost, deadline, attempt budget, exponential backoff/jitter, server hints, and fleet-storm controls.

**RM-REALTIME-CONTINUITY-0002:** Every reconnect creates a new secure/HTTP/protocol session generation, reauthenticates, reauthorizes subscriptions/streams, renegotiates extensions/subprotocols/limits, and rejects old-generation late data. Transport resumption or connection reuse cannot preserve application authority silently.

**RM-REALTIME-CONTINUITY-0003:** Resume state is typed application evidence containing scope, stream/subscription generation, opaque cursor or sequence, acknowledgment meaning, freshness, retention window, integrity/confidentiality, single-/multi-use policy, and fallback. It is not a transport guarantee.

**RM-REALTIME-CONTINUITY-0004:** Gap, duplicate, overlap, reset, expired cursor, unknown cursor, server state loss, reordered datagram, and complete replay are distinct. Product policy selects fail, snapshot/reconcile, replay bounded history, or restart—not silent continuation.

**RM-REALTIME-CONTINUITY-0005:** Re-sending a client message/stream operation follows the HTTP/domain replay boundary: attempt lineage, effect ambiguity, idempotency/deduplication key, body availability, authorization, and duplicate handling are explicit. Reconnect alone never replays queued application data.

**RM-REALTIME-CONTINUITY-0006:** Transport ping/pong, SSE comment bytes, QUIC path validation, HTTP activity, application heartbeat, domain freshness, and peer process health are separate liveness signals with source, deadline, clock, false-positive, cost, and suspension policy.

**RM-REALTIME-CONTINUITY-0007:** Sleep, hibernation, process suspension, network change, address migration, proxy rebinding, credential rotation, server deploy, and clock discontinuity trigger evidence-based revalidation rather than assumed continuity.

