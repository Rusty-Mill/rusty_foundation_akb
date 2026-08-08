# Protocols, delivery, and installation

**RM-PKI-PROTOCOL-0001:** Enrollment protocol selection binds protocol/profile/version, endpoints/CA label/directory, server trust and authorization, account/bootstrap/client authentication, redirect/proxy/network policy, replay/idempotency, polling, rate limits, interaction, and bounds.

**RM-PKI-PROTOCOL-0002:** ACME account, order, authorization, challenge, finalize, certificate, revocation, key-change, nonce, and renewal-information resources map to distinct lifecycle evidence. Challenge success is identifier authorization, not certificate issuance or application identity.

**RM-PKI-PROTOCOL-0003:** EST initial enrollment, reenrollment, CSR attributes, CA certificates, full-CMC, and server-key-generation operations retain their authentication/bootstrap and POP differences. SCEP and CMP pending/polling/resynchronization and message-protection semantics remain explicit.

**RM-PKI-PROTOCOL-0004:** Redirects, alternate endpoints, proxies, enrollment web services, MDM relays, RA/CA separation, and out-of-band transfer preserve authenticated server/RA identity, request/response binding, destination allowlist, and confidentiality. SSRF and credential forwarding are prohibited.

**RM-PKI-PROTOCOL-0005:** Responses are bounded and parsed before trust. They bind transaction/request/public key, issued certificate, candidate chain/CA certificates, status/error/pending/retry, protocol protection, server/RA evidence, and receipt time.

**RM-PKI-DELIVERY-0001:** Certificate delivery proves response retrieval only. Installation separately verifies certificate syntax/profile, public-key match, issuer/path under enrollment purpose, request/issued differences, validity/status, and target store/scope/ownership.

**RM-PKI-DELIVERY-0002:** Installation associates certificate with the exact opaque private-key generation, applies intended access/usage/export/user-presence policy, stores required chain/evidence without trusting supplied order, and reports store/provider identifiers and persistence.

**RM-PKI-DELIVERY-0003:** Activation and distribution to services, load balancers, users, devices, trust stores, directories, or relying parties are separate generation switches with readiness, overlap, rollback, cache/session, and access-control policy.

**RM-PKI-PROTOCOL-0006:** Offline/manual enrollment exports a signed request package and imports a response package with exact transaction/public-key/policy binding, media custody, expiry, duplicate detection, and audit; filenames and operator memory are insufficient correlation.

