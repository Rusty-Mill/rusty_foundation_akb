# Benchmarks

**RM-APP-AUTH-BENCH-0001:** Ceremony benchmarks report method/provider/platform, cold/warm state, interaction excluded and included distributions, challenge/verification/policy/session phases, network topology, cryptographic operations, requests, CPU, allocation, peak memory, and p50/p95/p99 latency.

**RM-APP-AUTH-BENCH-0002:** Password benchmarks report derivation algorithm/parameters/provider, concurrency, input bounds, verification and migration latency, CPU/memory, queueing, rate-limit overhead, denial-of-service behavior, and parameter-upgrade capacity without publishing credential-derived material.

**RM-APP-AUTH-BENCH-0003:** WebAuthn benchmarks report platform/roaming/synced/device-bound class, algorithms, attestation/extensions, transport, discovery, cold/warm broker state, registration/assertion phases, cancellation, user-interaction time separately, and verifier throughput/resources.

**RM-APP-AUTH-BENCH-0004:** Federation/token benchmarks report discovery/metadata/key cache state, authorization/token/introspection/revocation exchanges, token profile/size/signature, refresh rotation, connection behavior, issuer scale, fault/throttle modes, throughput, latency, and propagation.

**RM-APP-AUTH-BENCH-0005:** Session benchmarks report create/lookup/renew/revoke/logout mixes, session/token population, cache topology, concurrency, security-epoch fan-out, offline clients, revocation-to-deny convergence, storage/network amplification, and residuals.

**RM-APP-AUTH-BENCH-0006:** Recovery/lifecycle benchmarks report workload and system queue phases separately from human decision time, provider fan-out, notification channels, delays, authenticator/session/token reconciliation, partial faults, completion frontier, and security/privacy/accessibility instrumentation overhead.
