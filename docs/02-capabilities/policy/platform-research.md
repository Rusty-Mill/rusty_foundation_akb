# Platform and provider research

## Language and decision evidence

- [Open Policy Agent policy language](https://www.openpolicyagent.org/docs/policy-language) exposes document-oriented declarative rules, undefined and conflict behavior, schemas, typed built-ins, partial evaluation, bundles, and [decision logs](https://www.openpolicyagent.org/docs/management-decision-logs) with bundle revisions and masking.
- [Cedar validation](https://docs.cedarpolicy.com/policies/validation.html) separates policy/schema validation from authorization evaluation over principal, action, resource, context, and entities with deny-by-default behavior.
- [Common Expression Language specification](https://github.com/google/cel-spec) demonstrates a typed, mutation-free, non-Turing-complete embedded expression language with ahead-of-time checking and host-supplied context/functions.
- [XACML 3.0](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html) distinguishes Permit, Deny, NotApplicable, Indeterminate, combining algorithms, obligations, advice, policy decision points, and enforcement points.

## Platform conclusions

Windows, Linux, and macOS provide native authorization and policy services for selected resources but no universal application business/authorization rule model. Native policy is composed through domain adapters and retains its own evidence and enforcement boundary.

**RM-POLICY-RESEARCH-0001:** Portability preserves typed requests/results, policy/input/data/function generations, unknown/error/default, combining, obligations, enforcement boundaries, and evidence—not identical language syntax, traces, optimizers, or provider extensions.

**RM-POLICY-RESEARCH-0002:** Providers disclose type/value/error/unknown semantics, validation soundness limits, determinism/cost, functions/data, conflicts/combining, partial evaluation/cache, obligations, distribution, logging, and isolation.

**RM-POLICY-RESEARCH-0003:** Rego/OPA, Cedar, CEL, XACML, native controls, and product rule engines remain selectable mappings; none becomes the abstract capability model.
