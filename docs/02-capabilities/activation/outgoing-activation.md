# Outgoing brokered activation

`rm.activation.broker` asks an OS desktop/service broker to route one validated intent according to current user/system policy.

**RM-ACTIVATION-OUT-0001:** Submission MUST bind the exact intent, caller/app/session identity, explicit target capability/locator, interaction and handler-selection policy, foreground/activation token or parent surface, authority, deadline/cancellation, and correlation.

**RM-ACTIVATION-OUT-0002:** Default-handler, ask/open-with, exact-handler where platform/user policy permits, recommend/install fallback, and capability-only query are distinct modes. Exact-handler requests cannot silently weaken to arbitrary default selection.

**RM-ACTIVATION-OUT-0003:** The broker MUST apply current restrictions on executable/script/dangerous targets, background launches, remote/network references, sandbox crossing, writable file grants, custom schemes, and user interaction. A product cannot bypass denial through direct process spawn or shell execution.

**RM-ACTIVATION-OUT-0004:** URI and file activation use separate native paths where semantics differ. A file URI MUST NOT be substituted for a file capability when that would lose sandbox, identity, write-scope, or lifetime guarantees.

**RM-ACTIVATION-OUT-0005:** Batch activation reports whether the platform handled targets atomically, independently, or by provider-defined grouping and preserves partial/ambiguous outcomes.

**RM-ACTIVATION-OUT-0006:** Sync is complete only for queries or providers proven noninteractive/nonwaiting. Potential app chooser, consent, install, remote lookup, or launch work requires cancellable async without blocking the UI dispatcher.

**RM-ACTIVATION-OUT-0007:** Foreground activation is a user-attention request. The selected application/compositor remains authoritative; submission success cannot claim focus, visibility, window creation, or non-disruptive behavior.
