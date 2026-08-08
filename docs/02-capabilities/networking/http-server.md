# HTTP server lifecycle and request dispatch

**RM-HTTP-SERVER-0001:** A listener policy binds accepted transports/protocols, authority and virtual-host routing, secure-channel policy, connection/request/resource limits, timeouts, proxy-trust policy, overload behavior, and graceful shutdown.

**RM-HTTP-SERVER-0002:** Request parsing and validation complete before domain dispatch to the declared milestone. Routing uses normalized typed components while retaining original evidence needed for signature and security policy.

**RM-HTTP-SERVER-0003:** Handler authority is derived from listener/route policy and authenticated application context, never from Host, forwarded fields, certificate presence, socket locality, or connection identity alone.

**RM-HTTP-SERVER-0004:** Admission control distinguishes connection, stream, request-head, body, handler, response, tenant, and global budgets. Overload is bounded and fair and does not require reading an unbounded body before rejection.

**RM-HTTP-SERVER-0005:** Graceful shutdown stops admission, advertises/drains according to protocol, bounds completion, cancels remaining work with failure evidence, and closes transports. It is not proof that handlers committed or clients received responses.

**RM-HTTP-SERVER-0006:** Forwarded client identity, scheme, host, and address are accepted only from explicitly trusted intermediary hops with a declared parsing and overwrite policy.

