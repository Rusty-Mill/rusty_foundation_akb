# Update and rollback

**RM-PLUGIN-UPDATE-0001:** Install verifies an immutable versioned package into a content-addressed/staged location. It never overwrites an active generation's executable files.

**RM-PLUGIN-UPDATE-0002:** Activation uses prepare, optional state migration, readiness, atomic routing switch, old-generation quiescence, and retirement. Failure before commit leaves the old generation active.

**RM-PLUGIN-UPDATE-0003:** State schemas and migrations are independently versioned, bounded, transactional, and tested for forward/backward policy. Executable rollback does not imply state rollback is safe.

**RM-PLUGIN-UPDATE-0004:** Downgrade protection, revocation, publisher/key rotation, emergency disable, staged rollout, rollback window, and retained-version cleanup follow signed host policy.

**RM-PLUGIN-UPDATE-0005:** In-process native replacement normally requires host restart unless exact platform/ABI/lifetime evidence proves generation coexistence. Unload/reload is not the baseline update mechanism.

**RM-PLUGIN-UPDATE-0006:** Supply-chain evidence includes source/build provenance, SBOM, licenses, vulnerability status, signatures, attestations, transparency where selected, verification-tool versions, and conformance results.

