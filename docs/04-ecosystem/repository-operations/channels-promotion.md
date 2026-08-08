# Channels, promotion, yanking, and deprecation

**RM-REPOSITORY-CHANNEL-0001:** A channel is a versioned signed policy view over immutable release digests, not mutable artifact storage. It declares maturity, audience, compatibility/support window, promotion gates, rollout policy, and downgrade/retention rules.

**RM-REPOSITORY-CHANNEL-0002:** Promotion input binds source release digest/evidence, source/target channel generations, required conformance/benchmarks/security review, soak/health evidence, compatibility, advisory state, approvals, effective time, and rollback policy.

**RM-REPOSITORY-CHANNEL-0003:** Promotion changes only authenticated metadata referencing the same artifact digest and evidence set. Rebuild, repack, resign with changed claims, or provider-generated archive change creates a new candidate and publication ceremony.

**RM-REPOSITORY-CHANNEL-0004:** Demotion, hold, pause, end-of-support, and channel closure are explicit metadata revisions with reason, scope, effective time, replacement guidance, and consumer impact. Clients retain monotonic history to resist replay.

**RM-REPOSITORY-CHANNEL-0005:** Yanking prevents new dependency resolution under declared policy but preserves artifact bytes, historical lockfile resolution where ecosystem permits, release/advisory evidence, and exact reason. Yank is not deletion, revocation, or proof of vulnerability.

**RM-REPOSITORY-CHANNEL-0006:** Deprecation identifies replacement/migration and support timeline without changing installability unless separate channel/yank policy says so. It is reversible only through a new signed revision.

**RM-REPOSITORY-CHANNEL-0007:** Release revocation or emergency exclusion is stronger than yank and is consumed through signed security/update policy. It cannot be represented solely by hiding a web page or deleting an asset.

**RM-REPOSITORY-CHANNEL-0008:** Channel aliases/tags are convenience references. Critical automation resolves and records immutable digest plus metadata generation and rejects silent tag movement outside policy.

