# Login sessions and security contexts

A login session is a lifecycle/namespace relationship between a principal, a host/session provider, and an interactive or service environment. A security-context snapshot describes the credentials and policy-relevant attributes currently presented by an execution context.

**RM-IDENTITY-SESSION-0001:** A session reference MUST carry provider, provider-local session identity, generation, principal reference, class, lifecycle state, interaction availability, namespace/seat hints when known, and observation revision.

**RM-IDENTITY-SESSION-0002:** Console, remote, service, batch, container, graphical, unlocked, active, foreground, and interactive are independent attributes. No single `is_interactive` flag may imply all of them.

**RM-IDENTITY-SESSION-0003:** Lock, unlock, disconnect, reconnect, fast-user switch, logoff, sleep/resume, provider restart, and seat/namespace migration MUST invalidate or revise affected observations. Missed notifications trigger complete reconciliation.

**RM-IDENTITY-CONTEXT-0001:** A security-context snapshot MUST distinguish subject/effective/filesystem identities where native semantics differ, group/claim sets, privilege/capability/entitlement states, integrity/label/sandbox evidence, credential/keyring references, provider generation, and unavailable dimensions.

**RM-IDENTITY-CONTEXT-0002:** A snapshot is observation, not a promise that a future operation will succeed. Authorization advice uses the exact target and policy context; the native operation remains the authorization point.

**RM-IDENTITY-CONTEXT-0003:** Process and thread contexts MUST remain distinguishable. Code MUST NOT infer the effective context of future work from process identity or from the context observed on another thread.

Session observation does not create or terminate OS login sessions. Account provisioning, login-window integration, desktop-session management, remote session brokering, and service managers remain separate privileged services.
