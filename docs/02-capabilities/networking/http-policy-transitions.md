# HTTP redirects, authentication, retries, and replay

**RM-HTTP-POLICY-0001:** Redirect handling is an explicit state machine recording status, source and resolved target, origin change, method/content transformation, credential/referrer/header disposition, loop/limit, downgrade, and user/policy decision.

**RM-HTTP-POLICY-0002:** Cross-origin, cross-scheme, local/private-network, and less-secure redirects require policy authorization. Sensitive fields and capabilities never follow solely because a field name is unrecognized.

**RM-HTTP-POLICY-0003:** Authentication challenges are parsed as untrusted inputs. Credential selection binds scheme, origin/proxy, realm/scope, channel, audience, freshness, interaction, secret provider, and retry count; origin and proxy credentials are isolated.

**RM-HTTP-POLICY-0004:** A retry decision binds failure/status evidence, method and domain idempotency, body replayability, bytes-sent state, attempt lineage, idempotency key, deadline/budget, backoff/jitter, server guidance, and duplicate-effect risk.

**RM-HTTP-POLICY-0005:** Automatic retry is disabled when effect is unknown unless a domain contract proves replay safety or deduplication. Retrying creates a new attempt, not a continuation that erases the prior outcome.

**RM-HTTP-POLICY-0006:** Hedging and racing are separate duplicate-operation authorities with bounded concurrency, loser cancellation, response selection, billing/load implications, and server-side deduplication requirements.

