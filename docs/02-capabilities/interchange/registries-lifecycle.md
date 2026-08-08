# Registries and lifecycle

**RM-INTERCHANGE-REGISTRY-0001:** Registries store immutable schema/profile artifacts by content identity plus governed namespace/version aliases, ownership, status, compatibility policy/results, provenance/signatures, dependencies, and lifecycle metadata.

**RM-INTERCHANGE-REGISTRY-0002:** Registration separates validation, compatibility evaluation, identifier allocation, approval, publication, alias promotion, deprecation, revocation, retention, and deletion authority.

**RM-INTERCHANGE-REGISTRY-0003:** Consumers resolve an exact immutable generation and cache it under authenticated freshness/expiry/revocation policy; registry unavailability behavior and offline trust roots are explicit.

**RM-INTERCHANGE-REGISTRY-0004:** Schema/profile dependencies form bounded acyclic or explicitly recursive graphs with exact versions/content descriptors, namespace authority, license/supply-chain evidence, and resolution limits.

**RM-INTERCHANGE-REGISTRY-0005:** Revocation means the artifact must no longer be selected under specified policy; it cannot erase already encoded data and requires reader/quarantine/migration decisions.

**RM-INTERCHANGE-REGISTRY-0006:** Generated artifacts bind generator/toolchain/configuration and source schema/profile digests, supported platforms/languages, reproducibility, signatures/provenance, compatibility, and retirement.

**RM-INTERCHANGE-REGISTRY-0007:** Registry backup/restore/failover preserves immutable identities, allocation history/reservations, aliases, signatures, policy and audit without accepting rollback or equivocation.
