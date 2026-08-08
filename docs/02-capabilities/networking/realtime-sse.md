# Server-sent events contract

**RM-REALTIME-SSE-0001:** An SSE subscription binds HTTP GET intent, original origin/resource, `text/event-stream` acceptance and response validation, credentials/CORS where applicable, cache and redirect policy, last-event cursor policy, reconnect budget, and authority.

**RM-REALTIME-SSE-0002:** Parsing is incremental UTF-8 with BOM, CR/LF variants, comments, field/value rules, blank-line dispatch, multi-line data joining, event type, identifier, and retry hint exactly modeled. Invalid encoding, line, event, buffer, and field sizes are bounded.

**RM-REALTIME-SSE-0003:** An emitted event contains data, optional type, current last-event identifier, receive/session generations, origin, and parse evidence. Empty/missing data, empty identifier reset, comments/heartbeats, unknown fields, and end-of-stream are distinct.

**RM-REALTIME-SSE-0004:** A server retry field is an untrusted delay hint constrained by client minimum/maximum, jitter, attempt/time budget, offline/path state, server overload, foreground/background policy, and explicit stop conditions. HTTP 204 or product policy can prohibit reconnect.

**RM-REALTIME-SSE-0005:** `Last-Event-ID` is an opaque application cursor sent only to the authorized original scope under privacy/length/character rules. It does not prove that earlier events were processed, retained, unique, or safe to skip.

**RM-REALTIME-SSE-0006:** Server flush/HTTP send completion, intermediary buffering, client byte receipt, event dispatch, application acknowledgment, and domain effect are separate. SSE provides no client-to-server application channel and no durable delivery guarantee.

**RM-REALTIME-SSE-0007:** Server/client implementations bound concurrent subscriptions, idle/heartbeat policy, response buffering/compression, proxy timeout, queue growth, slow consumers, reconnect storms, shutdown, and per-origin/tenant fairness.

