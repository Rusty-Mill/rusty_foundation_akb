# Repository publication and security-response foundations

| Field | Value |
|---|---|
| Status | Draft ecosystem analysis |
| Purpose | Publish immutable releases, operate authenticated repositories and mirrors, promote channels, issue advisories, and execute emergency response without rewriting history |

```mermaid
flowchart LR
    Candidate["Verified release candidate digest"] --> Approve["Publication plan + role approvals"]
    Approve --> Upload["Upload immutable blobs + attestations"]
    Upload --> Snapshot["Signed repository snapshot"]
    Snapshot --> Channel["Versioned channel reference"]
    Channel --> Mirrors["Mirrors / CDN"]
    Snapshot --> Consumers["Package-management clients"]
    Report["Private vulnerability report"] --> Advisory["Revisioned advisory + affected products"]
    Advisory --> Response["Fix · mitigation · yank · revoke · emergency metadata"]
    Response --> Snapshot
```

## Conclusions

- Publishing, signing, approving, promoting, yanking, advising, revoking, mirroring, and deleting are separately attenuated roles.
- Published artifact identity is immutable. Corrections use new versions or signed metadata/advisory revisions; yanking and channel removal do not rewrite bytes or erase history.
- Channel promotion references the same accepted artifact digest and evidence set. Rebuilding or repackaging creates a different release candidate.
- Repository snapshots commit the complete visible metadata set so consumers can detect rollback, freeze, mix-and-match, and wrong-target attacks.
- Security advisories are signed revisioned evidence with exact product identities and ecosystem-native affected/fixed ranges; severity is contextual evidence, not automatic deployment policy.

## Documents

- [Roles, authority, and ceremonies](roles-authority.md)
- [Publication workflow and release records](publication-workflow.md)
- [Namespaces, ownership, and succession](namespaces-ownership.md)
- [Channels, promotion, yanking, and deprecation](channels-promotion.md)
- [Mirrors, availability, retention, and backup](mirrors-retention.md)
- [Advisory and vulnerability model](advisory-model.md)
- [Coordinated disclosure](coordinated-disclosure.md)
- [Revocation and emergency response](revocation-emergency.md)
- [Ecosystem research](ecosystem-research.md)
- [Conformance](conformance.md)
- [Benchmarks and operational objectives](benchmarks.md)

