# Trust, authority, and isolation

| Isolation class | Trust/failure implication |
|---|---|
| In-process native | Shares memory, privileges, runtime, loader, allocator, threads, crash, and compromise domain with host |
| Restricted process | OS-enforced process boundary; capabilities transferred or brokered explicitly; serialization and supervision required |
| Portable component | Runtime-mediated interfaces and memory separation according to exact engine/component profile; host imports remain authority boundary |

**RM-PLUGIN-ISOLATION-0001:** Selection states the isolation class and exact provider quality. Code signing/provenance never upgrades in-process loading into sandbox isolation.

**RM-PLUGIN-ISOLATION-0002:** In-process native plugins are limited to host-trusted publishers/build pipelines and receive all ambient host privileges that native code can reach, regardless of manifest claims.

**RM-PLUGIN-ISOLATION-0003:** Restricted hosts begin with minimum inherited handles, environment, filesystem, network, identity, memory, CPU, process, and device authority. Grants are explicit, attenuated, revocable only within stated scope, and auditable.

**RM-PLUGIN-ISOLATION-0004:** Resource limits cover memory, CPU/time, threads/tasks, handles/descriptors, storage, network, message size/rate, recursion, and diagnostic volume. Exhaustion cannot destabilize the host beyond declared residual risks.

**RM-PLUGIN-ISOLATION-0005:** Secrets are not configuration or generic plugin values. Secret/key operations use separately granted broker interfaces and redacted diagnostics.

**RM-PLUGIN-ISOLATION-0006:** Host callbacks validate plugin-controlled identifiers, lengths, ordering, reentrancy, lifetime, and cancellation. Trust in publisher does not remove input validation at the boundary.

