# Security and isolation

**RM-POLICY-SECURITY-0001:** Policy source, bytecode/AST, schemas, data, functions/extensions, bundles, residual policies, caches, explanations, test corpora, and evaluator input are untrusted or privileged according to explicit supply-chain and authority policy.

**RM-POLICY-SECURITY-0002:** Evaluation has no ambient filesystem/network/process/clock/random/credential access and runs with memory/time/steps/depth/output limits, safe arithmetic/text/regex, stack protection, and tenant isolation.

**RM-POLICY-SECURITY-0003:** Dynamic code, native plugins, WASM, remote calls, templates, and provider built-ins require separate trust/isolation classes, capability attenuation, deterministic/replay rules, and failure handling; they are not implied by a policy language.

**RM-POLICY-SECURITY-0004:** Policy and data namespace ownership prevents injection, shadowing, import confusion, identifier collision, path traversal, ambiguous case/Unicode, dependency substitution, and cross-tenant reference.

**RM-POLICY-SECURITY-0005:** Evaluator errors, timing, cache hits, explanations, reason codes, missing-data fetches, and obligation behavior are analyzed for existence/attribute/policy/tenant side channels.

**RM-POLICY-SECURITY-0006:** Break-glass decisions require authenticated emergency authority, narrow scope, expiry, prominent audit/notification, obligation enforcement, post-use rotation/review, and cannot be created by ordinary policy inputs.

**RM-POLICY-SECURITY-0007:** Compromised distribution/control planes cannot silently roll back, mix, or widen policy generations; clients reject invalid signatures, dependencies, schemas, and revoked artifacts.

**RM-POLICY-SECURITY-0008:** Denial of service controls bound policy complexity, inputs/data/entity graphs, concurrency, partial evaluation, compile storms, cache cardinality, explanations/logs, and update churn.
