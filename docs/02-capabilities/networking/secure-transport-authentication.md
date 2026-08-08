# Peer authentication and credentials

**RM-SECURE-AUTH-0001:** Server authentication binds the original typed service reference, presented certificate/key evidence, proof within the current handshake transcript, selected trust purpose/profile, verification time/clock, trust/algorithm/status/network generations, pins/overrides, and negotiated protocol.

**RM-SECURE-AUTH-0002:** Presented certificates are an untrusted candidate bag. Path construction/validation and exact DNS/IP/URI/service matching use the PKI-validation contract; a valid signature or chain without reference-identity match is not authenticated service evidence.

**RM-SECURE-AUTH-0003:** Certificate, raw-public-key, PSK, external PSK, token-bound, attested, or protocol-specific authentication are separately selected profiles. Their identities, provisioning, rotation, compromise, anonymity, and forward-secrecy claims cannot substitute for one another.

**RM-SECURE-AUTH-0004:** Local credentials are selected by role, original service/listener, acceptable issuer/signature schemes, purpose, peer request, policy, availability, user presence, privacy, and authority. Provider heuristics cannot send an unintended client identity.

**RM-SECURE-AUTH-0005:** Client authentication distinguishes not requested, requested/optional, required, no credential, declined, credential sent, proof verified, mapped principal, post-handshake, and failed. Certificate authentication does not itself map or authorize an application account.

**RM-SECURE-AUTH-0006:** Private-key operations use opaque key capabilities and bind channel/handshake transcript, algorithm, credential generation, principal, interaction, deadline, and provider evidence. Exporting the private key is never required by the channel API.

**RM-SECURE-AUTH-0007:** Credential/trust changes during a handshake yield a generation-bound result or restart according to policy. A certificate revoked or distrusted after establishment does not retroactively rewrite evidence; long-lived-channel revalidation/reconnect policy is explicit.

**RM-SECURE-AUTH-0008:** Authentication callbacks receive bounded immutable evidence and return a scoped decision. They cannot perform hidden event loops, unbounded network I/O, bypass critical checks, retain secrets, or convert unknown/error into trust silently.

