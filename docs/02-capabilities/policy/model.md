# Model, entities, and milestones

**RM-POLICY-MODEL-0001:** A policy domain binds purpose, request/decision schemas, policy modules/bundle, data snapshot, function registry, combining and default rules, evaluator, enforcement contract, distribution, security/privacy, and lifecycle generations.

**RM-POLICY-MODEL-0002:** Distinct entities include policy source/module/set/bundle, schema, static analysis, compiled plan, input request, subject/resource/action/context entities, policy data, function, evaluation, decision, obligation/advice, enforcement attempt, and domain effect.

**RM-POLICY-MODEL-0003:** Milestones distinguish parse, type/schema validation, static analysis, compilation, bundle validation/signature, distribution acceptance, local activation, request validation, data resolution, evaluation, decision delivery, enforcement, obligation completion, and domain effect.

**RM-POLICY-MODEL-0004:** Outcomes preserve domain/policy/schema/data/function/evaluator generations, request and decision identity, matched/failed policies where permitted, missing/unknown/error evidence, obligations/advice, cache/partial state, time/dependencies, and enforcement/reconciliation requirements.

**RM-POLICY-MODEL-0005:** Evaluation does not mutate ambient state or perform domain I/O. External data and nondeterministic observations enter as explicit versioned inputs or constrained recorded function results.

**RM-POLICY-MODEL-0006:** Async data acquisition/distribution is bounded and cancellation-safe; pure evaluation has bounded deterministic cancellation/fuel/deadline behavior. Sync equivalents never create hidden runtimes.
