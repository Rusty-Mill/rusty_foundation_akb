# Trial contract

The approved contract is the boundary of authority.

## Required record

- stable trial identity, revision, status, owner, reviewers, and decision dates;
- exact subject and upstream generations;
- questions, falsifiable hypotheses, and decision each result can support;
- in-scope and excluded behavior, platforms/providers, workloads, data, and users;
- public-surface, production, portability, performance, security, and release nonclaims;
- time, cost, dependency, unsafe/FFI, privilege, data, and operational limits;
- assertion, case, benchmark, cross-cutting, and standards evidence plan;
- stop, pause, disposal, retention, and follow-on/promotion conditions.

**RM-TRIAL-CONTRACT-0001:** Each hypothesis MUST name the observation that supports it, the observation that refutes it, and the uncertainty that can leave it inconclusive.

**RM-TRIAL-CONTRACT-0002:** Scope expansion requires a new reviewed contract revision; an implementation discovery cannot silently enlarge trial authority.

**RM-TRIAL-CONTRACT-0003:** Trial interfaces MUST be marked unstable and MUST NOT be represented as supported public contracts.

**RM-TRIAL-CONTRACT-0004:** Native-provider selection MUST be treated as a tested mapping for an exact platform generation, not as the capability identity.

