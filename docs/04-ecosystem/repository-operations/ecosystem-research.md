# Ecosystem research

This research informs repository profiles; provider behavior and ecosystem rules remain authoritative.

## GitHub

- Releases associate tags/commits, notes, and assets. Immutable releases lock release tags/assets and produce release attestations, but provider-generated source archives have separate reproducibility/verification limits.
- Artifact attestations use signed provenance and transparency evidence. Repository security advisories support private collaboration, publication, and CVE coordination.

Primary sources: [GitHub immutable releases](https://docs.github.com/en/enterprise-cloud@latest/code-security/concepts/supply-chain-security/immutable-releases), [artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations), [repository security advisories](https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories).

## Rust and crates.io

- Cargo packages and publishes to registries with registry-specific ownership. crates.io acts as a permanent archive: versions are not replaced or deleted through ordinary correction; yanking affects new resolution while supporting locked dependencies under ecosystem rules.
- Registry/source identity and exact package checksums are essential to dependency-confusion resistance.

Primary sources: [Cargo publishing](https://doc.rust-lang.org/cargo/reference/publishing.html), [Cargo registries](https://doc.rust-lang.org/cargo/reference/registries.html).

## Content-addressed registries

OCI Distribution demonstrates immutable digest-addressed blobs/manifests, mutable references/tags, resumable upload, content-digest receipts, and subject/referrer relationships for attestations and SBOMs. Tags are not artifact identity.

Primary source: [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec/blob/main/spec.md).

## Vulnerability interchange

OSV models ecosystem packages and affected version/source ranges, aliases, publication/withdrawal, severity, and database/ecosystem extensions. CSAF models product trees, affected/not-affected/under-investigation status, threats, and remediation categories. CVE identifiers and records provide cross-provider vulnerability identity but do not replace product-specific advisory detail.

Primary sources: [OSV schema](https://ossf.github.io/osv-schema/), [CSAF 2.0](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html), [CVE CNA rules](https://www.cve.org/ResourcesSupport/AllResources/CNARules).

