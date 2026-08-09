# Passwords and shared-secret verification

**RM-APP-AUTH-PASSWORD-0001:** Password policy is versioned and distinguishes enrollment, verification, change, administrative reset, breached-value rejection, rate limiting, lockout, and migration. The portable layer does not impose arbitrary composition rules.

**RM-APP-AUTH-PASSWORD-0002:** Password verifiers store only salted, parameterized password-derivation results plus algorithm/policy generation and migration state. Plaintext and reversible password storage are prohibited.

**RM-APP-AUTH-PASSWORD-0003:** Verification uses bounded work, constant-time comparison where applicable, generic external outcomes, per-account and abuse-context throttling, monitored resource limits, and defenses against user enumeration and denial-of-service amplification.

**RM-APP-AUTH-PASSWORD-0004:** Password entry uses protected accessible controls, prevents framework logging/telemetry/clipboard persistence by default, supports password managers and paste, and does not reveal arbitrary policy or account details before appropriate verification.

**RM-APP-AUTH-PASSWORD-0005:** Password change requires current policy-defined evidence, invalidates the old verifier generation, evaluates session/token consequences, notifies through independent channels, and records recovery/admin exceptions.

**RM-APP-AUTH-PASSWORD-0006:** Passwords are neither replay-resistant nor phishing-resistant. Combining a password with another knowledge factor does not create independent multi-factor evidence.
