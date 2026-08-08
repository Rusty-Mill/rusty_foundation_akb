# Lifecycle and session conformance specification

| Area | Required evidence |
|---|---|
| Launch | reason/provenance matrix, readiness milestones, malformed inputs, process epoch |
| Activation | file/URI/reopen/notification cases, duplicates, concurrent routing, no implicit authority/focus |
| Multi-instance | simultaneous starts, stale coordinator, crash/restart, forwarding authentication and bounds |
| Session | lock/unlock, local/remote disconnect/reconnect, missing/unknown observations |
| Power | suspend/resume, repeated transitions, clock discontinuity, resource reconciliation |
| Termination | allow/deny/defer, committed end, timeout, force kill, absent callback, shutdown composition |
| Inhibition | scope, deadline, renewal/release, permission denial, user-visible accessible reason |
| Restoration | periodic checkpoint, atomic replacement, version migration, corruption, stale references, display/locale/accessibility changes |
| Lifecycle | overflow, cancellation, reentrancy, affinity, startup/shutdown races |

Tests use sacrificial applications and controlled test accounts/sessions. A harness records native input, portable events, replies, deadlines, process exit, archive state, and resource cleanup. Destructive shutdown/suspend tests run only in isolated virtual machines or dedicated hosts with explicit recovery procedures.

