# Conformance

**RM-APP-AUTH-CONFORMANCE-0001:** Ceremony histories cover discoverable and identified subjects, method selection/fallback, fresh/replayed/swapped/expired challenges, origin/verifier/audience mismatch, cancellation/timeouts, provider ambiguity, account enumeration, policy changes, and session/effect separation.

**RM-APP-AUTH-CONFORMANCE-0002:** Password suites cover breached-value policy, Unicode and length boundaries, password-manager/paste/accessibility, verifier migration, constant-time behavior, rate/lockout/DoS controls, change/reset, logging exclusion, generic failures, and concurrent attempts.

**RM-APP-AUTH-CONFORMANCE-0003:** WebAuthn suites use official and adversarial vectors across registration/assertion, algorithms, origins/RP IDs, user presence/verification, discoverable credentials, extensions, attestation forms, counters, backup state, synced/device-bound credentials, conditional mediation, duplicate credentials, and provider differentials.

**RM-APP-AUTH-CONFORMANCE-0004:** OTP/OOB suites cover HOTP/TOTP windows/drift/replay, bootstrap protection, recovery-code single use, SMS/voice/email/push routing, number matching, fatigue/rate attacks, shared/replaced devices, offline/unavailable channels, fallback, and phishing-resistance nonclaims.

**RM-APP-AUTH-CONFORMANCE-0005:** Lifecycle/recovery histories cover enrollment, duplicate/add/replace/overlap/revoke/loss/compromise, administrator action, independent notifications, circular recovery, cooling-off, session/token reconciliation, support social engineering, federation outage, appeal, and no stale resurrection.

**RM-APP-AUTH-CONFORMANCE-0006:** Federation/token suites cover exact OIDC/OAuth/SAML profiles, issuer/audience/nonce/state/PKCE/redirect/mix-up, key/metadata rollover, claims and subject mapping, token substitution/replay/exchange/downscope, refresh rotation/family reuse, introspection/revocation freshness, and logout gaps.

**RM-APP-AUTH-CONFORMANCE-0007:** Session/risk suites cover fixation/rotation, idle/absolute/renewal, concurrent sessions, account/authenticator/security-epoch revocation, step-up/transaction binding, signal staleness/model changes, local/federated logout frontiers, caches/offline clients, and cross-tenant isolation.

**RM-APP-AUTH-CONFORMANCE-0008:** Reports bind synthetic identities, provider/authenticator/client/verifier/issuer/trust/key/schema/policy/risk/session generations, clocks, algorithms, platform/browser/device, network, limits, expected histories, accessibility/privacy mode, and every skipped/degraded/unsupported assertion without production credentials or tokens.
