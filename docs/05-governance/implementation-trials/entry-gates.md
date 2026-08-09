# Trial entry gates

Authorization is conjunctive. `Unknown` blocks entry; a reviewed `not-applicable` or valid waiver is not the same as missing evidence.

| Gate | Required evidence |
|---|---|
| Subject | Exact capability/domain generation has explicit Experimental authorization |
| Learning value | Questions and falsifiable hypotheses justify implementation rather than further specification work |
| Bounds | Included and excluded behavior, platforms, providers, time/resource limits, and nonclaims |
| Ownership | Trial owner plus architecture, capability, security, and evidence reviewers as applicable |
| Repository | Current standards profile binds source, architecture, toolchain, targets, dependencies, and exceptions |
| Verification | Assertions, executable cases, benchmark scenarios, comparison rules, and evidence location |
| Cross-cutting | Security, privacy, accessibility, i18n, observability, performance, and operational review plans |
| Operations | CI trust, secrets, runners, artifacts, provenance, emergency authority, and disposal |

**RM-TRIAL-ENTRY-0001:** Trial authorization MUST identify every required gate as `pass`, `fail`, `unknown`, `not-applicable`, or `waived`, with exact evidence and reviewer.

**RM-TRIAL-ENTRY-0002:** Authorization MUST NOT be granted when any required gate is failed, unknown, expired, contradictory, or supported only by an aggregate score.

**RM-TRIAL-ENTRY-0003:** The authorizing record MUST bind the architecture model, capability contract, promotion decision, standards profile, toolchain, provider matrix, and active-exception generations.

**RM-TRIAL-ENTRY-0004:** A trial MUST NOT begin merely because a repository, prototype, funding allocation, or implementation team exists.

