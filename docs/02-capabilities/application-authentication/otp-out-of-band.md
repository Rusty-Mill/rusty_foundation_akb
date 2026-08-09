# OTP, recovery codes, and out-of-band methods

**RM-APP-AUTH-OTP-0001:** HOTP/TOTP profiles bind algorithm, secret generation and protection, digit count, moving factor or time step, accepted window, drift/resynchronization, single-use replay state, issuer/account display, and lifecycle generation.

**RM-APP-AUTH-OTP-0002:** OTP secrets are opaque and non-exportable after enrollment where provider capabilities permit. Bootstrap transfer is protected, short-lived, purpose-bound, user-confirmed, and excluded from logs and screenshots by default.

**RM-APP-AUTH-OTP-0003:** Recovery codes are independently random, hashed at rest, individually single-use, count- and generation-bound, replenished through a strong lifecycle ceremony, and never presented as phishing-resistant.

**RM-APP-AUTH-OTP-0004:** Out-of-band and push plans bind the primary ceremony, subject/account, receiving endpoint generation, human-readable transaction context, nonce, expiry, attempt limits, and response. Generic approve/deny prompts are insufficient for high-risk transactions.

**RM-APP-AUTH-OTP-0005:** Number matching, context display, rate limits, device enrollment, channel authentication, and fatigue detection reduce but do not transform manual or push approval into verifier-bound phishing resistance.

**RM-APP-AUTH-OTP-0006:** SMS, voice, email, push, and provider-specific channels expose their rerouting, interception, device sharing, availability, privacy, and recovery limitations. Fallback requires explicit policy and user-visible method identity.
