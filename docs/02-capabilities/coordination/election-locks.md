# Leader election, locks, semaphores, and barriers

**RM-COORDINATION-ELECTION-0001:** Election candidacy binds role, participant incarnation, configuration, eligibility, priority policy, campaign generation, campaign value, lease/session, deadline, and authority. Elected evidence includes term/epoch/revision and fencing token.

**RM-COORDINATION-ELECTION-0002:** Candidate, elected by provider, leadership observed, externally fenced, application-ready, resigning, superseded, and lost are distinct. A participant performs protected leader work only after downstream fencing and product readiness succeed.

**RM-COORDINATION-LOCK-0001:** A distributed lock binds resource name/generation, holder incarnation, mode, fairness/queue policy, lease, fencing token, reentrancy policy, deadline, and authority. It is not a process mutex and cannot guard memory or resources that ignore fencing.

**RM-COORDINATION-LOCK-0002:** Acquisition returns acquired/not-acquired/timed-out/cancelled/lost-session/stale-configuration/fenced/unknown distinctly. Cancellation may leave a queued or granted acquisition that must be reconciled by attempt identity.

**RM-COORDINATION-LOCK-0003:** Reentrancy is off by default; when selected it binds exact logical owner and depth within one lease generation. Thread ID, address, task-local state, or reused process identity cannot establish distributed ownership.

**RM-COORDINATION-SEMAPHORE-0001:** Semaphore capacity, weighted permits, fairness, overcommit, lease/fence semantics, partial acquisition, resize, and recovery are explicit. Permit count is coordination state, not proof of downstream capacity.

**RM-COORDINATION-BARRIER-0001:** A barrier binds participant set/configuration, generation, arrival payload, quorum/all policy, deadline, failure/withdrawal, release state, and cleanup. Reusing a name creates a new generation and late arrivals cannot cross it.

**RM-COORDINATION-ELECTION-0003:** Leader transfer/resignation is an ordered coordination request, not a no-leader guarantee. Old authority is fenced before or atomically with new authority according to the selected protocol.

