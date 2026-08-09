# Registry, generation, and release lifecycle

**RM-API-GOV-REGISTRY-0001:** The registry stores immutable source contracts, resolved dependencies, ownership, review/approval, compatibility results, policy generations, signatures/attestations, and derived-artifact provenance.

**RM-API-GOV-REGISTRY-0002:** Contract dependencies resolve by immutable identity with cycle and namespace controls; remote references are fetched under bounded authenticated policy and pinned before acceptance.

**RM-API-GOV-REGISTRY-0003:** Generators are hermetic, version-pinned, reproducible transformations. Output records source digest, generator/toolchain, options, target language/runtime, dependency lock, and semantic-loss warnings.

**RM-API-GOV-REGISTRY-0004:** Generated clients and servers are adapters. Domain types and policy do not depend on generator-specific wire models, hidden runtimes, ambient configuration, or transport errors.

**RM-API-GOV-REGISTRY-0005:** SDK review covers idiomatic naming, ownership/lifetimes, async and sync completeness, cancellation/deadlines, pagination, retries, streaming/backpressure, errors, documentation, examples, and upgrade behavior.

**RM-API-GOV-REGISTRY-0006:** Release promotion requires lint, reference resolution, compatibility analysis, conformance vectors, security/privacy review, generated-artifact verification, documentation, rollout plan, and accountable approval.
