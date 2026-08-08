# Registration and resource generations

An I/O engine registration binds a native resource generation, interest/operation classes, provider engine generation, and delivery target. Registration is infrastructure state, not authority and not resource ownership by itself.

**RM-ASYNC-REG-0001:** Resource registrations MUST bind exact resource and engine generations and reject stale reuse.

**RM-ASYNC-REG-0002:** Registration, interest mutation, operation submission, close, and deregistration ordering MUST be explicit under concurrency.

**RM-ASYNC-REG-0003:** Native handle or descriptor reuse MUST NOT associate a late readiness/completion with a new logical resource.

**RM-ASYNC-REG-0004:** Fork, process replacement, handle inheritance, duplication/transfer, and provider restart MUST invalidate or explicitly reconstruct registrations; they MUST NOT be assumed portable.

**RM-ASYNC-REG-0005:** Deregistration completes only when the provider can no longer deliver an event that accesses reclaimed registration state, or when such delivery is safely generation-rejected.

One logical resource may restrict concurrent operation kinds even when the engine supports concurrency. Domain contracts decide whether simultaneous reads, writes, accepts, receives, seeks, control operations, or close are valid and how shared cursor/state is synchronized.
