# Security, privacy, and accessibility

**RM-IDENTITY-SECURITY-0001:** Principal enumeration, session observation, attribute expansion, authentication, credential use/export, impersonation, and delegation use separate least-authority grants and native enforcement.

**RM-IDENTITY-SECURITY-0002:** Identity and authentication telemetry is sensitive. Default events omit names, addresses, identifiers, group/claim values, credential metadata, prompt text, target paths, and biometric/device details; stable correlation requires explicit governed pseudonymization.

**RM-IDENTITY-SECURITY-0003:** Prompts MUST be bound to the requesting product, foreground/session, purpose, target, and trusted provider surface. Products MUST prevent prompt flooding, background surprise, lookalike fallback, and secret collection by plugins or remote content.

**RM-IDENTITY-ACCESS-0001:** Every interactive ceremony MUST support keyboard-only operation, screen readers, zoom/high contrast, reduced motion, localized and bidirectionally correct content, sufficient timeout/retry, and a clear accessible cancellation path.

**RM-IDENTITY-ACCESS-0002:** Method selection MUST offer a viable accessible alternative where policy permits. Biometric, camera, fine-motor, audio, memory, or time-sensitive interaction MUST NOT be the only product-designed path without a documented system-policy requirement.

**RM-IDENTITY-ACCESS-0003:** Errors explain purpose and recovery without exposing whether an untrusted account name exists, which factor failed, sensitive policy internals, or another user's session state.

**RM-IDENTITY-ACCESS-0004:** Headless/service contexts prohibit interactive prompting unless a separately selected out-of-band broker contract exists; failure is explicit and bounded.
