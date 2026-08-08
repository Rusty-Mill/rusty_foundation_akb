# Language, functions, and evaluation

**RM-POLICY-LANGUAGE-0001:** A language profile binds syntax/AST/bytecode generation, type/value model, equality/order/null/unknown/error, collections/entities, quantification, recursion, comprehensions, conditionals, pattern/time operations, imports/namespaces, and resource semantics.

**RM-POLICY-LANGUAGE-0002:** Policy languages are side-effect free by default and bound evaluation through finite input, restricted recursion or acyclic rules, fuel/steps, depth, collection/cardinality, regex/pattern, numeric/string, memory, output, and time limits.

**RM-POLICY-LANGUAGE-0003:** Parse, type, schema, reference, conflict, reachability, recursion, ambiguity, forbidden-function, resource-bound, and semantic lint results are distinct static-analysis evidence.

**RM-POLICY-FUNCTION-0001:** Functions bind stable identity/version, typed signature, null/unknown/error, determinism, purity, authority, cost model, limits, implementation, compatibility, and provenance.

**RM-POLICY-FUNCTION-0002:** Nondeterministic or external functions execute only through separately authorized adapters whose inputs/outputs are recorded in the decision context; they disable unsafe caching/partial evaluation and expose failure/freshness.

**RM-POLICY-EVAL-0001:** Evaluation binds exact compiled policy, schema, input, data, function registry, evaluator/version/configuration, time observations, limits, and requested entry point into one immutable context.

**RM-POLICY-EVAL-0002:** Undefined, unknown, indeterminate/error, false, empty collection, null, and not-applicable remain distinct according to the language and decision contract.

**RM-POLICY-EVAL-0003:** Optimizations, indexing, short circuit, memoization, parallelism, and ahead-of-time compilation preserve result, required obligations, error/unknown, explanation contract, resource limits, and security semantics.
