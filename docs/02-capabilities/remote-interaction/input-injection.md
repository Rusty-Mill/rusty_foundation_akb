# Input intent and injection

A `RemoteInputIntent` includes participant/session/authority revision, monotonically ordered event identity, device class and virtual-device generation, semantic event, remote observation revision, source coordinate/keymap context, sender timestamp, and provenance. It is validated into a short-lived `InjectionCommand` for a specific native adapter and local session generation.

**RM-REMOTE-INTERACTION-INJECT-0001:** Every remote event MUST be treated as untrusted intent and checked for session state, participant role, device/action allowance, generation, order, freshness, rate, focus/boundary policy, and local override before injection.

**RM-REMOTE-INTERACTION-INJECT-0002:** Admission validation MUST NOT replace execution-time validation. A queued command that becomes stale, revoked, out of bounds, or disallowed before native injection MUST be rejected.

**RM-REMOTE-INTERACTION-INJECT-0003:** Injection MUST preserve internal provenance, participant attribution, virtual-device generation, and decision reason even where the destination application or OS cannot distinguish injected input from physical input.

**RM-REMOTE-INTERACTION-INJECT-0004:** Native acceptance means only that a provider accepted all or part of the sequence. It does not prove delivery, target focus, application handling, resulting state, or semantic success.

**RM-REMOTE-INTERACTION-INJECT-0005:** Partial insertion, policy block, integrity mismatch, unsupported device/event, rate limit, state conflict, and unknown outcome MUST be distinct. Automatic retry is forbidden unless duplicate and state-transition safety are proven.

**RM-REMOTE-INTERACTION-INJECT-0006:** Remote events MUST NOT trigger secure attention, unlock, login, credential entry, consent, permission, elevation, trusted UI, or policy-management actions unless a separate platform-specific privileged contract explicitly proves that boundary.

**RM-REMOTE-INTERACTION-INJECT-0007:** The base contract MUST prefer constrained compositor/session brokers over unrestricted global injection where available and MUST disclose the effective native scope.
