# Notification replacement, progress, badges, and withdrawal

**RM-NOTIFY-STATE-0001:** Replacement/update MUST bind a stable product replacement key, expected prior content revision, and new relevance/expiry. Providers MUST disclose whether replacement is atomic, animated-as-new, best effort, or unsupported.

**RM-NOTIFY-STATE-0002:** Progress state MUST define determinate/indeterminate/completed/failed, numeric range/unit, status text, sequence/revision, terminal policy, and update-rate bound. Notification progress is a view of domain state, not its owner.

**RM-NOTIFY-STATE-0003:** Badge/count state MUST identify scope, meaning, source revision, clear/reconciliation policy, and supported range. A badge is not durable unread-count storage.

**RM-NOTIFY-STATE-0004:** Withdrawal/removal success MUST state only the provider scope affected. It MUST NOT claim that a banner already seen was unseen, a remote copy was recalled, or an activation cannot arrive later.

**RM-NOTIFY-STATE-0005:** Provider history enumeration/management, when selected, is sensitive user-attention data and MUST preserve application ownership, bounded scope, platform policy, and unknown/external modifications.

**RM-NOTIFY-STATE-0006:** Update loss, process restart, service restart, and external dismissal require reconciliation from domain state where possible; replay MUST not resurrect expired or completed notifications as new alerts without policy.
