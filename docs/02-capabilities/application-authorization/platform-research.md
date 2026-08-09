# Platform and standards research

## Primary references

- [NIST SP 800-162](https://csrc.nist.gov/pubs/sp/800/162/upd2/final) defines ABAC using subject, object, operation, and environment attributes evaluated against policy, rules, or relationships.
- [XACML 3.0](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-cos01-en.html) defines policy administration/information/decision/enforcement concepts, permit/deny/not-applicable/indeterminate outcomes, combining algorithms, obligations, and advice.
- [Zanzibar](https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/) documents a large-scale relationship tuple model, namespace configuration, checks/expansion, causal consistency tokens, caching, and external consistency constraints.
- [Cedar authorization](https://docs.cedarpolicy.com/auth/authorization.html) models typed principal/action/resource/context requests evaluated with entity data and separately validated policy/schema.

## Platform families

| Family | Relevant facilities | Architectural consequence |
|---|---|---|
| Windows | access tokens, SIDs, ACLs/security descriptors, privileges, AuthZ APIs, application/cloud IAM | native access checks use exact object/security context and remain final for protected native objects |
| Linux | UIDs/GIDs, capabilities, POSIX/NFS ACLs, namespaces, LSMs, seccomp, polkit and service policy | multiple intersecting kernel/user-space mechanisms prevent one universal permission abstraction |
| macOS | credentials, POSIX ACLs, sandbox/entitlements, Authorization Services, TCC and app-scoped controls | user authorization, sandbox entitlement, privacy consent, and resource ACL are separate gates |

## Conclusion

The portable layer standardizes typed semantics, decision/enforcement boundaries, derivation evidence, consistency, and loss. Product policy and native adapters retain their own authority and enforcement truth.
