# Name and service resolution

## Capability identity

`rm.network.resolve` converts an explicit service intent into an immutable candidate set.

**RM-NETWORK-RESOLVE-0001:** Resolution inputs specify lookup name, service/port, transport, family policy, flags, network authority, deadline, cache policy, and desired metadata. Ambient resolver policy is disclosed in the result.

**RM-NETWORK-RESOLVE-0002:** Results carry candidate endpoints, ordering/grouping, source/provenance class, canonical-name status, expiry or unknown lifetime, negative-result status, network/path epoch, and resolver/provider identity.

**RM-NETWORK-RESOLVE-0003:** Candidate ordering is resolver and connection-policy input, not a permanent priority or authenticated preference. Consumers cannot persist resolved addresses as service identity without separate policy.

**RM-NETWORK-RESOLVE-0004:** Success with zero usable candidates, name-not-found, temporary failure, policy denial, malformed name, unsupported family/service, timeout, cancellation, and provider failure are distinct outcomes.

**RM-NETWORK-RESOLVE-0005:** Async resolution is cancellable and deadline bounded. Sync resolution is complete but discloses blocking and never creates a hidden runtime.

**RM-NETWORK-RESOLVE-0006:** Cancellation may race completion; completed candidate ownership and cache effects are reported. Cancellation does not revoke already issued results.

**RM-NETWORK-RESOLVE-0007:** Resolution is not authentication, authorization, reachability proof, or protection against rebinding. Security policy validates the original service identity at connection/use time.

