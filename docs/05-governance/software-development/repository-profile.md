# Repository standards profile contract

Each implementation repository publishes a profile at a conventional reviewed path chosen by ecosystem RFC. The syntax remains open; this document defines required information before choosing YAML/TOML/JSON or generated metadata.

| Field | Meaning |
|---|---|
| Profile identity/version | Stable policy generation and compatibility |
| Repository/components | Exact governed scope and ownership |
| Architecture/domain inputs | Model, ADR/RFC, capability/profile generations |
| Trial/maturity | Approved trial class and nonclaims |
| Toolchain | Edition, stable channel policy, MSRV, targets, SDKs/linkers |
| Rules | Inherited standards version, strengthened rules, applicability |
| Unsafe/FFI | Crates/modules, budgets, owners, invariants, audits |
| Dependencies | Policy, lock/vendor strategy, licenses, advisories, update cadence |
| Verification | Required assertions/cases, features, platforms/providers, fuzz/model tests |
| Performance | Scenarios, baselines, budgets, environments |
| Cross-cutting | Security/privacy/accessibility/i18n/observability/operations evidence |
| CI/release | Pinned gates, runner trust, artifacts, provenance, publication authority |
| Exceptions | Active exception IDs, expiry, affected claims |

**RM-DEV-PROFILE-0001:** A repository profile MUST bind exact standards, architecture, domain, toolchain, target, and ownership generations and MUST fail validation when required information is absent or contradictory.

**RM-DEV-PROFILE-0002:** Local policy MAY strengthen inherited rules or classify reviewed non-applicability; it MUST NOT silently weaken foundation safety, authority, evidence, or release rules.

**RM-DEV-PROFILE-0003:** Tool/lint/CI configuration MUST be derived from or cross-validated against the profile. Unenforced normative rules remain visible manual-review gates rather than assumed pass.

**RM-DEV-PROFILE-0004:** Profile changes receive the same protected review as the rules/gates they affect and preserve prior generations for release-evidence interpretation.

**RM-DEV-PROFILE-0005:** A repository without a current valid profile cannot host an authorized implementation trial or publish a Rusty Mill conformance/release claim.
