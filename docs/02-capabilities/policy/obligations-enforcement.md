# Obligations, advice, and enforcement

**RM-POLICY-OBLIGATION-0001:** Obligations and advice are typed immutable values bound to the exact decision, policy/input/data generations, enforcement phase, target, parameters, order/dependencies, criticality, authority, deadline, idempotency, and audit policy.

**RM-POLICY-OBLIGATION-0002:** Unknown or unsupported critical obligations turn permit into enforcement failure/deny under the contract; advice may be ignored only when explicitly noncritical and has no hidden security/business effect.

**RM-POLICY-ENFORCE-0001:** The policy decision point and enforcement point are separate. Enforcement validates decision applicability/current generations, independently authorizes action and obligations, and records selected result.

**RM-POLICY-ENFORCE-0002:** Pre-, in-, post-, and compensating obligations declare transaction/effect boundary, failure semantics, retries, deduplication/fencing, partial progress, rollback/compensation, and reconciliation.

**RM-POLICY-ENFORCE-0003:** A permit with unmet pre-obligations cannot proceed; post-obligation failure cannot retroactively claim the domain effect did not occur and requires explicit response/reconciliation.

**RM-POLICY-ENFORCE-0004:** Data filtering/masking, rate/quota charging, step-up authentication, consent, logging, notification, retention, watermarking, approval, and routing obligations preserve domain-specific capabilities and authority rather than arbitrary callbacks.

**RM-POLICY-ENFORCE-0005:** Enforcement is race-safe against resource/principal/policy changes through generation preconditions, transactions, locks/fencing, or fresh reevaluation selected by risk.

**RM-POLICY-OBLIGATION-0003:** Obligation outputs never embed raw secrets/credentials unless the exact enforcement capability requires and protects them; references/handles are preferred.

**RM-POLICY-ENFORCE-0006:** Decision delivery failure, duplicate decisions, repeated enforcement, ambiguous obligation effects, and enforcement crash/restart have durable idempotency and audit identities where effects matter.
