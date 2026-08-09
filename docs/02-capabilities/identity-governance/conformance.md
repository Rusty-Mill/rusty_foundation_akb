# Conformance

**RM-IDENTITY-GOV-CONFORMANCE-0001:** Identity suites cover creation/recreation, aliases, ambiguous correlation, merge/split, tombstones, provider identifier reuse, tenant move, source conflicts, stale observations, privacy projections, and every object kind.

**RM-IDENTITY-GOV-CONFORMANCE-0002:** Mapping suites use official and adversarial SCIM/LDAP/native fixtures for absent/null/unknown, case/normalization, uniqueness, mutability, cardinality, extensions, unsupported operations, lossy round trips, conditional writes, bulk partial results, and hostile values.

**RM-IDENTITY-GOV-CONFORMANCE-0003:** Query/change suites cover coherent and weak snapshots, pagination mutation, ordering scopes, duplicate/out-of-order/missing events, expired cursors, tombstones, checkpoint crashes, snapshot-plus-delta recovery, authorization changes, and anti-enumeration.

**RM-IDENTITY-GOV-CONFORMANCE-0004:** Group suites cover direct/dynamic/nested/external/temporary membership, cycles, depth/fan-out, exclusions, stale attributes, cross-tenant edges, rule rollout, invalidation, provider disagreement, and no implicit entitlement or authority.

**RM-IDENTITY-GOV-CONFORMANCE-0005:** Lifecycle histories cover joiner/mover/leaver/rehire/correction, invitations/guests/federation, future and retroactive dates, cancellation, concurrent sources, dormant/orphan accounts, ownership, credential/session/resource reconciliation, and partial provider outage.

**RM-IDENTITY-GOV-CONFORMANCE-0006:** Governance histories cover requests, approvals, delegation/quorum/conflicts, separation of duties, fulfillment, expiry, access reviews/nonresponse, privilege/JIT/emergency use, changed evidence, rollback, appeal, and verified revocation.

**RM-IDENTITY-GOV-CONFORMANCE-0007:** Deprovisioning fault injection interrupts every directory/group/entitlement/session/token/credential/device/resource/ownership/downstream-provider boundary and verifies bounded retry, honest residuals, no stale resurrection, and new-generation restoration.

**RM-IDENTITY-GOV-CONFORMANCE-0008:** Reports bind datasets, source/provider/schema/mapping/policy/workflow generations, tenant/subject/account scopes, clocks, limits, expected histories, privacy mode, authorization boundary, and every skipped, degraded, unsupported, or unknown assertion without production identity data.
