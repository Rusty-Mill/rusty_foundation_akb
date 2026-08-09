# Delegation, attenuation, and confused deputies

**RM-APP-AUTHZ-DELEGATE-0001:** Delegation identifies subject, actor, issuer, recipient/audience, resource/scope/actions, conditions, lifetime, purpose, delegation depth, proof/capability generation, and revocation semantics.

**RM-APP-AUTHZ-DELEGATE-0002:** Derived authority can only narrow every operation, resource, time, audience, condition, budget, and redelegation dimension. Incomparable or broader derivation is rejected rather than approximated.

**RM-APP-AUTHZ-DELEGATE-0003:** On-behalf-of requests preserve subject and actor chains through logs, tokens, messages, policy evaluation, obligations, and effects. Impersonation, delegation, service identity, and user authentication remain distinguishable.

**RM-APP-AUTHZ-DELEGATE-0004:** Services accept authority only for their own audience and requested resource/action, bind callbacks and redirected effects to original intent, and never substitute ambient service privilege for caller authority.

**RM-APP-AUTHZ-DELEGATE-0005:** Batch, queue, scheduled, retry, webhook, plugin, and background work carries bounded persisted authority with expiry and generation; resumption or replay revalidates current applicability.

**RM-APP-AUTHZ-DELEGATE-0006:** Cancellation, transfer failure, recipient rejection, partial effect, and revocation report authority ownership and possible downstream use without guessing or duplicating transferable authority silently.
