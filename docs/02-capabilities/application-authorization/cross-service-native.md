# Cross-service and native enforcement

**RM-APP-AUTHZ-BOUNDARY-0001:** Every service publishes protected resources/actions, accepted subject/actor/delegation evidence, policy dependency, enforcement location, native/domain secondary checks, obligation support, and effect milestones.

**RM-APP-AUTHZ-BOUNDARY-0002:** Gateway, sidecar, middleware, UI, or client checks are defense-in-depth and candidate filtering; the resource-owning service or native facility remains responsible for effect authorization.

**RM-APP-AUTHZ-BOUNDARY-0003:** Messages and RPC bind caller/subject/actor, audience, action/resource, request identity, authority or token proof, context, deadline, attempt, and policy frontier; intermediaries cannot broaden or retarget them.

**RM-APP-AUTHZ-BOUNDARY-0004:** Database row/column policy, object-store ACLs, filesystem permissions, broker ACLs, repository roles, CA/HSM policy, and cloud IAM remain provider-specific enforcement composed through explicit adapters and tested for drift.

**RM-APP-AUTHZ-BOUNDARY-0005:** Dual policy systems declare precedence and intersection/union semantics. Portable and native permits are never silently unioned, and disagreement produces observable denial or indeterminate behavior under product policy.

**RM-APP-AUTHZ-BOUNDARY-0006:** Asynchronous external effects use outbox/workflow/idempotency/fencing patterns that persist bounded authority and revalidate at each irreversible boundary; initial request authorization does not authorize arbitrary future retries.
