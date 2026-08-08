# Provenance and reproducibility

**RM-SIGNED-PROVENANCE-0001:** A provenance statement has typed subjects and digests, materials and resolved versions, builder/workflow identity, invocation parameters, build environment/isolation claims, timestamps, byproducts, and predicate/schema versions.

**RM-SIGNED-PROVENANCE-0002:** Provenance is an assertion whose signature and signer policy are verified independently. A well-signed false or incomplete statement remains possible.

**RM-SIGNED-PROVENANCE-0003:** Subject digests match the distributed artifacts exactly. References to source, dependency locks, toolchains, build definitions, SBOMs, test/conformance results, and benchmark reports are digest-bound rather than mutable links alone.

**RM-SIGNED-PROVENANCE-0004:** Builder identity, workflow source/revision, trigger, platform/runner, isolation level, privileged inputs, secrets exposure class, and dependency/network policy are preserved sufficiently for the consuming policy to evaluate the claim.

**RM-SIGNED-PROVENANCE-0005:** SBOM and provenance parsers apply size, depth, count, URI, decompression, and text bounds. Package names, URLs, annotations, and supplier claims are untrusted display and query input.

**RM-SIGNED-REPRODUCIBILITY-0001:** A reproducibility result binds two or more exact build plans, material sets, environments, output digests, normalizations, differences, and verifier identities. It is separate from provenance and signature validity.

**RM-SIGNED-REPRODUCIBILITY-0002:** Normalization cannot remove security-relevant output. Reproducible matching does not prove signer authority; a mismatch is evidence requiring explanation rather than automatic proof of compromise.

**RM-SIGNED-PROVENANCE-0006:** Redacted provenance declares omitted fields and redaction policy without claiming completeness. Private repositories, usernames, paths, environment values, and build topology are classified before publication.

