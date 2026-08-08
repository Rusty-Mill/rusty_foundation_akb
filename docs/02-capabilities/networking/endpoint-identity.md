# Endpoint and service identity

**RM-NETWORK-ENDPOINT-0001:** A service intent contains an application service identity, transport constraints, security-name policy, port/service selection, address-family policy, interface/path constraints, proxy policy, and network authority.

**RM-NETWORK-ENDPOINT-0002:** DNS names, internationalized display names, canonical ASCII lookup names, IP literals, scoped IPv6 addresses, local bind endpoints, and native endpoint extensions are distinct typed values.

**RM-NETWORK-ENDPOINT-0003:** An IP endpoint is an address, port, transport family, and required scope/zone context. Text formatting is canonical and locale independent; parsing rejects ambiguity and silent truncation.

**RM-NETWORK-ENDPOINT-0004:** Service identity survives candidate selection and redirects only under explicit higher-layer policy. The selected address cannot silently replace the identity used for authentication or authorization.

**RM-NETWORK-ENDPOINT-0005:** Local and peer endpoint observations record when they became valid and whether translation, proxying, or platform mediation makes them incomplete. They are not durable peer identities.

**RM-NETWORK-ENDPOINT-0006:** Interface names and indices are process/platform observations with an epoch; they can change or be reused and are not stable authorization identifiers.

