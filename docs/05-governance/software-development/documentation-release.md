# Documentation, compatibility, release, and maintenance

**RM-DEV-DOC-0001:** Public crates, modules, types, traits, functions, errors, features, examples, safety contracts, blocking/async behavior, authority, resource limits, platform variance, and compatibility are documented once code passes spike status.

**RM-DEV-DOC-0002:** Examples are minimal, tested where feasible, secure by default, accessibility/i18n aware when user-facing, and avoid `unwrap`/ambient authority patterns that consumers might copy without context.

**RM-DEV-DOC-0003:** Architecture/requirements remain linked rather than duplicated in API prose. Generated references link back to normative sources and identify generation/tool provenance.

**RM-DEV-COMPAT-0001:** Compatibility review uses the API-governance multidimensional model. SemVer classification includes behavioral/error/effect/order/performance/resource/security/platform/MSRV/feature changes, not only source compilation.

**RM-DEV-COMPAT-0002:** Deprecation names replacement, migration, support period, diagnostics, observed consumer readiness, and removal authority. A warning or elapsed date cannot independently authorize removal.

**RM-DEV-REL-0001:** Release candidates are built from reviewed immutable source with pinned inputs and produce artifacts, checksums, SBOM, provenance, licenses, signatures, conformance/benchmark/security evidence, compatibility notes, known exceptions, and recovery/revocation instructions.

**RM-DEV-REL-0002:** Publication identity and authority are separate from signing key possession and CI success. Promotion binds immutable digests and evidence; tags or mutable pages are not release authority.

**RM-DEV-MAINT-0001:** Each maintained component has owners, support/maturity, triage/security contact, dependency/unsafe inventory, platform/provider matrix, recovery plan, and archival/transfer criteria.

**RM-DEV-MAINT-0002:** Removal/archival preserves names, releases, decisions, advisories, provenance, migration, and security response for the supported retention window.
