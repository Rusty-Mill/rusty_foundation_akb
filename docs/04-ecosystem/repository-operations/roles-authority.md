# Roles, authority, and ceremonies

**RM-REPOSITORY-AUTHORITY-0001:** Repository authority is divided among namespace administration, package ownership, candidate upload, signing, publication approval, metadata roles, channel promotion, yank/deprecation, advisory publication, emergency revocation, mirror operation, retention, and audit.

**RM-REPOSITORY-AUTHORITY-0002:** Every role binds organization/repository/package/channel scope, allowed operations, artifact/metadata classes, environment, authentication strength, approval threshold, time window, rate limit, and policy generation. Organization membership alone grants nothing.

**RM-REPOSITORY-AUTHORITY-0003:** Human and workload identities are distinct. Automation uses short-lived workload identity and least-privilege credentials; human approval is authenticated and plan-digest bound where required.

**RM-REPOSITORY-AUTHORITY-0004:** High-impact operations—new namespace owner, first stable publication, root/delegation rotation, stable promotion, destructive retention exception, advisory withdrawal, mass yank, emergency revocation, or policy downgrade—require configured separation of duties and quorum.

**RM-REPOSITORY-AUTHORITY-0005:** A ceremony record identifies immutable request, actors/roles, approvals, policy and trust generations, exact input/output digests, provider/workflow, timestamps, transparency evidence, result, overrides, and notifications without recording secrets.

**RM-REPOSITORY-AUTHORITY-0006:** Credential rotation, loss, compromise, suspension, owner departure, organization recovery, and provider outage have preauthorized bounded procedures. Recovery credentials cannot publish ordinary releases unless separately activated and audited.

**RM-REPOSITORY-AUTHORITY-0007:** Break-glass authority is narrow, expiring, quorum-controlled where feasible, prominently observable, and followed by credential rotation and independent review. It cannot erase its audit evidence.

