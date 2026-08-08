# Delegated and presigned access

**RM-OBJECT-DELEGATE-0001:** A delegated request capability binds provider/account/namespace, exact key or constrained prefix, optional exact generation, allowed operation/method, maximum bytes/range/content type/checksum, required headers/conditions, audience/network, not-before/expiry, signer/credential generation, and nonce/use policy.

**RM-OBJECT-DELEGATE-0002:** Delegated URLs/forms/tokens are bearer-like secrets. They are minimized, short-lived, transmitted only over authorized secure channels, excluded from logs/referrers/history/analytics, redacted in UI, and never embedded in durable public metadata by default.

**RM-OBJECT-DELEGATE-0003:** Canonical signing binds exact scheme/host/path/query/header normalization, credential scope, clock region/service, payload policy, and provider protocol revision. Parser/canonicalization differentials, duplicate parameters, alternate hosts, redirects, and proxy rewriting are rejected.

**RM-OBJECT-DELEGATE-0004:** Delegation cannot exceed issuer authority and cannot be broadened by recipient-supplied metadata, copy source, redirect, multipart continuation, content type, or encryption fields. Required preconditions remain signed.

**RM-OBJECT-DELEGATE-0005:** Issued, first used, provider accepted, bytes transferred, object committed/read, expired, credential rotated/revoked, and audited are separate. Offline signatures may not support immediate revocation; that limitation and emergency response are explicit.

**RM-OBJECT-DELEGATE-0006:** Upload delegation binds a create-only/exact-generation target and whole-object integrity/size constraints where the provider supports them. Otherwise content is quarantined and independently verified/promoted before trusted use.

**RM-OBJECT-DELEGATE-0007:** Browser/CORS use separately constrains origins, exposed/required headers, methods, credentials, cache/referrer policy, redirects, preflight, filename/content disposition, and cross-site upload/download risks.

