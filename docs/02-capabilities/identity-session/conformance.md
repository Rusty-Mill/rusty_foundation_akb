# Credential and identity-session conformance specification

| Area | Required evidence |
|---|---|
| Principal | local/service/managed subjects, realm collisions, rename/reuse, ambiguous/missing attributes, group/claim changes, disclosure denial |
| Session | console/remote/service/headless, lock/unlock, disconnect/reconnect, switch/logoff, provider restart, missed-event reconciliation |
| Authentication | success/cancel/timeout/deny/unavailable, fresh/cached/silent, method/assurance variance, foreground/session binding, spoof resistance |
| Credentials | opaque lifetime, purpose/audience selection, expiry/revocation, export denial, secret canaries, owner/provider retirement |
| Context | process/thread distinction, UID/SID/group/privilege/capability/label vectors, stale snapshots, native use-time denial |
| Delegation | attenuation, scope/use/lifetime, restoration on every exit, nesting policy, cross-thread/async leakage, plugin/callback isolation |
| Privacy/accessibility | identifier redaction, prompt rate/purpose, localization/bidi, keyboard/screen reader/zoom, accessible alternatives, headless behavior |

Adversarial tests attempt realm confusion, account-name reuse, `is_admin` flattening, stale-session retargeting, cached-evidence replay, credential extraction, unauthorized prompt creation, delegation amplification, context leakage through executor thread reuse, failure during native revert, and policy change between advice and operation.

Reports bind OS/kernel/build, identity/session/authentication provider, realm/directory configuration, local/remote/container/sandbox state, principal/session/context generation, method/assurance claims, interaction policy, privilege/elevation state, provider versions, and every unavailable or degraded dimension. Fixtures use synthetic accounts and credentials; artifacts never contain reusable secrets.
