# Handler discovery and association policy

`rm.activation.handler-observer` exposes a revisioned projection of handlers eligible for a typed intent under current user/session/package policy. It does not launch or set defaults.

**RM-ACTIVATION-HANDLER-0001:** A handler descriptor MUST include provider-scoped application identity/generation, package/artifact provenance, supported target types/schemes/content types/roles/verbs, sandbox/interaction constraints, multi-target behavior, display metadata, and evidence source/age.

**RM-ACTIVATION-HANDLER-0002:** Executable path, bundle/package/desktop-entry identity, application display name, process identity, store identity, and signing identity remain distinct. None alone establishes current installation or authority.

**RM-ACTIVATION-ASSOCIATION-0001:** An association snapshot MUST bind user/session/desktop scope, target classification, role/verb, eligible ordered handlers, default/preferred selection, user/admin/package/provider provenance, revision, and unavailable/ambiguous state.

**RM-ACTIVATION-ASSOCIATION-0002:** Registered, eligible, recommended, recently used, user preferred, administratively enforced, and provider fallback are independent states. Provider ordering MUST NOT be presented as user choice without evidence.

**RM-ACTIVATION-ASSOCIATION-0003:** Defaults and eligibility are observations that may change after query. Activation re-resolves at the broker boundary; cached selection keys exact scope/revision and never bypasses user policy.

**RM-ACTIVATION-ASSOCIATION-0004:** Setting/changing a default is a separate interactive privileged settings service. Silent takeover, repeated nagging, registry/config rewriting outside supported policy, and treating registration as consent are prohibited.

**RM-ACTIVATION-ASSOCIATION-0005:** Association notifications trigger reconciliation; install/uninstall/update, user/admin changes, desktop/session switch, package database restart, and lost events require complete re-query.
