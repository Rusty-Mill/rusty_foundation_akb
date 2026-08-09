# Change design, review, CI, and merge gates

**RM-DEV-CHANGE-0001:** Changes are focused and reviewable. A nontrivial change states problem, contract/requirements, alternatives, risks, compatibility, platform/profile impact, tests, benchmarks, documentation, rollout/recovery, and unresolved questions before or with implementation.

**RM-DEV-CHANGE-0002:** Public API, unsafe/FFI, authority/security, persistence/schema, protocol, dependency/toolchain, performance budget, release, or standards changes require designated specialist review and linked ADR/RFC when durable architecture changes.

**RM-DEV-REVIEW-0001:** Review assesses semantics and failure modes, not only style. Authors respond by changing code/evidence, explaining disagreement, or recording a governed decision; unresolved blocking findings prevent merge.

**RM-DEV-REVIEW-0002:** No author is the sole approving reviewer for a protected change. Emergency changes record retrospective review, evidence gaps, containment, and follow-up deadline.

**RM-DEV-CI-0001:** Required CI is defined as versioned policy and includes source/license/provenance checks, formatting, lints, build/feature/MSRV matrices, tests, documentation links/examples, unsafe/dependency policy, conformance, and relevant benchmarks/security scans.

**RM-DEV-CI-0002:** Required gates run from pinned reviewed definitions on trusted runners with least privilege and protected secrets. Pull-request code from untrusted contexts cannot access release credentials.

**RM-DEV-CI-0003:** CI results bind commit/tree, workflow/tool/configuration versions, target/provider/environment, artifacts, and logs. Reruns preserve prior failures and create new attempt evidence.

**RM-DEV-CI-0004:** Branch protection requires current passing gates and required reviews; bypasses are explicit emergency authority with immutable audit and retrospective closure.

**RM-DEV-CI-0005:** Merge queues/rebases revalidate the integrated tree. A passing stale head or unrelated branch cannot authorize merge.

**RM-DEV-CI-0006:** CI resource/time budgets are measured. Test selection/caching may optimize feedback but cannot silently omit release-required evidence; omitted gates remain visible and run before affected claims.
