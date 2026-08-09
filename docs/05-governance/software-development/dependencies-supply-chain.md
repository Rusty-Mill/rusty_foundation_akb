# Dependencies, build inputs, and supply chain

**RM-DEV-DEP-0001:** A new third-party runtime/build dependency requires a proposal stating problem, alternatives (including standard library/in-house/no dependency), maintenance and contributor cost, transitive graph, features, MSRV/targets, license, security history, provenance, release cadence, bus factor, and exit plan.

**RM-DEV-DEP-0002:** Dependencies are minimized and scoped behind narrow adapters where provider substitution, risk isolation, or semantic normalization is required. Wrappers without a real boundary are avoided.

**RM-DEV-DEP-0003:** Versions and features follow repository policy; lockfiles are committed for applications/tools and governed for libraries. Updates review changelog, source/provenance, semantic/security impact, transitive changes, MSRV, licenses, and benchmark/size effects.

**RM-DEV-DEP-0004:** Build scripts, proc macros, code generators, CI actions, package managers, compilers, linkers, SDKs, system libraries, containers, runners, and external services are supply-chain inputs with pinned identity and least-privilege execution.

**RM-DEV-DEP-0005:** Network access during release builds is denied unless the hermetic input/provenance policy explicitly permits and records it. Vendoring, caching, mirrors, and offline builds preserve origin/license/update evidence.

**RM-DEV-DEP-0006:** Vulnerability and license findings have owner, affected artifacts/targets/features, exploitability/reachability assessment, remediation/mitigation, disclosure policy, SLA, and release/advisory linkage.

**RM-DEV-DEP-0007:** Generated artifacts are reproducible from pinned inputs; generation commands, schemas/templates, tool versions, normalization, and review policy are documented. Generated output cannot hide unreviewed executable changes.

**RM-DEV-DEP-0008:** Release inputs produce SBOM and provenance evidence. Signing, publishing, registry, CI, and mirror credentials use scoped short-lived or hardware-backed mechanisms where available and tested rotation/recovery.
