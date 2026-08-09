# Rate, reputation, and abuse controls

**RM-COMMS-ABUSE-0001:** Admission combines tenant/account/sender/provider/channel/recipient/topic/campaign/global quotas, throughput, concurrency, burst, daily/rolling frequency, cost budget, reputation, and provider limits without confusing them with consent.

**RM-COMMS-ABUSE-0002:** Per-recipient frequency caps define counted milestones, rolling/calendar window, time zone, channel/topic aggregation, transactional/security exceptions, queued messages, retries/fallbacks, and race consistency.

**RM-COMMS-ABUSE-0003:** Abuse controls detect enumeration, list bombing, snowshoe distribution, compromised tenants/credentials/templates, phishing, smishing, malware, spam traps, anomalous bounce/complaint, link/domain reputation, and provider evasion.

**RM-COMMS-ABUSE-0004:** Hold, throttle, challenge, require review, disable sender/template/campaign/tenant, rotate credentials, withdraw queued work, notify, and report are scoped authorized effects with evidence and appeal/recovery.

**RM-COMMS-ABUSE-0005:** Retry uses outcome-specific eligibility, bounded attempts/backoff/jitter/deadline, provider guidance, cost budget, and deduplication; permanent failures, suppression, expiry, and policy denial are not retried.

**RM-COMMS-ABUSE-0006:** Reputation and deliverability scores are provider/time/population-qualified observations, not universal truth; remediation never bypasses recipient protections or misrepresents sender identity.
