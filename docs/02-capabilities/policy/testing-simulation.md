# Testing, simulation, and change analysis

**RM-POLICY-TEST-0001:** Unit tables bind policy/schema/data/function/evaluator generations, typed inputs, expected decision/error/unknown, obligations/advice, matched policy IDs, and resource bounds.

**RM-POLICY-TEST-0002:** Property tests cover invariants such as no cross-tenant permit, monotonic attenuation, explicit deny precedence, obligation completeness, default behavior, and decision determinism over generated boundary inputs.

**RM-POLICY-TEST-0003:** Static analysis detects unreachable/shadowed/conflicting/duplicate rules, unconstrained variables, unsafe defaults, forbidden functions, cycles, missing schema/data, excessive cost, sensitive output, and compatibility issues with declared soundness limits.

**RM-POLICY-SIM-0001:** Simulation/shadow evaluation is side-effect free, uses explicit historical/synthetic/current snapshots with privacy authority, and never performs obligations or changes enforcement.

**RM-POLICY-SIM-0002:** Old/new comparison reports allow-to-deny, deny-to-allow, not-applicable/indeterminate/error, typed-result, obligation/advice, cost, dependency, explanation, and population/segment deltas.

**RM-POLICY-SIM-0003:** Historical replay accounts for missing/stale attributes, changed schemas/entities/functions, sampling/selection bias, survivorship, policy feedback, and inability to reconstruct original context.

**RM-POLICY-SIM-0004:** Approval gates define required tests, formal/static checks, risk owners, sampled change thresholds, exceptions/waivers, rollout guardrails, and evidence retention.

**RM-POLICY-TEST-0004:** Fuzzing targets parser/compiler/evaluator, type/value boundaries, entity graphs, collections/regex, recursion/comprehension, unknown/error propagation, combining algorithms, and explanation/log redaction.
