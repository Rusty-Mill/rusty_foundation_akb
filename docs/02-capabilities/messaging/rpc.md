# Unary RPC lifecycle

**RM-MESSAGING-RPC-0001:** An RPC call binds service/method revision, exact request/response/error schemas, target selection policy, principal/authority, immutable metadata, deadline budget, cancellation, compression, size/resource limits, retry/hedge policy, idempotency evidence, and attempt identity before dispatch.

**RM-MESSAGING-RPC-0002:** Resolution, channel/session ready, request metadata sent, request content partially/fully sent, server admitted, handler started, response metadata/message/status received, local completion, and domain effect are separate. Client and server may reach different terminal observations.

**RM-MESSAGING-RPC-0003:** Deadlines use an overall monotonic budget. Cross-process propagation sends remaining duration with elapsed-time deduction and uncertainty bounds rather than trusting unsynchronized absolute clocks. Servers reject hopeless work and propagate bounded remaining budgets downstream.

**RM-MESSAGING-RPC-0004:** Cancellation communicates loss of interest and requests cooperative stop. It can race handler execution, durable commit, response, and downstream calls; it does not roll back prior effects or prove peer receipt.

**RM-MESSAGING-RPC-0005:** Status distinguishes transport, protocol, authentication, authorization, admission/overload, invalid input, conflict/precondition, not found, unavailable, deadline, cancellation, application rejection, internal fault, partial result, and unknown effect. Typed details are bounded/versioned and untrusted.

**RM-MESSAGING-RPC-0006:** Metadata is a typed multimap with reserved namespaces, encoding/size/count limits, sensitive-field classification, forwarding policy, hop/end-to-end scope, signature coverage, and duplicate handling. Ambient process context never flows implicitly.

**RM-MESSAGING-RPC-0007:** Load balancing, failover, service discovery, proxy/mesh routing, and connection reuse are policy inputs preserving original service/audience, tenant/credential partition, locality, health freshness, attempt lineage, and no semantic weakening.

**RM-MESSAGING-RPC-0008:** Server dispatch validates schema, authority, deadline, admission, idempotency token, tenant budgets, and domain preconditions before invoking a handler. Handler return is not proof that durable effects committed or the client received a reply.

