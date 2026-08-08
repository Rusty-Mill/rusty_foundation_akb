# Network retrieval and caching

**RM-PKI-NETWORK-0001:** Intermediate, CRL, OCSP, trust-list, and transparency retrieval MUST be independently authorized and constrained by purpose, scheme, host/port, proxy, redirect, DNS/network context, size, time, concurrency, and privacy policy.

**RM-PKI-NETWORK-0002:** Certificate-provided locators are untrusted. Retrieval MUST prevent local-file access, loopback/link-local/private-network reach contrary to policy, credential leakage, downgrade, redirect escape, decompression bombs, and recursive trust-validation deadlock.

**RM-PKI-NETWORK-0003:** Offline, no-network-authority, metered/constrained, captive, proxy-auth-required, unavailable, timeout, and policy-denied states MUST be distinguishable and flow into selected hard/soft-fail policy.

**RM-PKI-NETWORK-0004:** Caches MUST key exact object identity, issuer/responder, policy/provider, verification/status time, trust generation, network partition where relevant, and signed freshness. URL alone is insufficient.

**RM-PKI-NETWORK-0005:** Cache entries MUST retain source, validation, freshness, negative-result, rollback, partitioning, size, eviction, and privacy evidence. Cached intermediates remain untrusted candidates; cached status remains time-bounded evidence.

**RM-PKI-NETWORK-0006:** Concurrent retrieval MUST deduplicate safely, bound waiter and response fanout, propagate cancellation without invalidating other consumers, and prevent one hostile certificate from monopolizing global resources.

**RM-PKI-NETWORK-0007:** Validation callbacks and UI/realtime contexts MUST never perform hidden blocking network I/O. Async is primary; sync uses explicit offline/cache policy or finite deadline and reports network use.
