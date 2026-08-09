# Platform and standards research

- NIST [SP 800-144](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-144.pdf) discusses cloud multi-tenancy, shared infrastructure, isolation, and provider risk. Rusty Mill expresses isolation as an evidence vector rather than a deployment label.
- Kubernetes [multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/) and [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) guidance demonstrate namespace/resource separation, aggregate hard limits, admission rejection, and the important limitation that quota does not itself isolate nodes or retroactively affect existing resources.
- Stripe's [meter configuration](https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure) makes aggregation over billing periods explicit; its subscription and entitlement APIs illustrate provider lifecycle evidence rather than portable application authority.
- The FinOps Foundation [FOCUS specification](https://focus.finops.org/focus-specification/) defines normalized billing/cost-and-usage data including account, billing and charge periods, quantities, currencies, charges, credits, discounts, and reconciliation-oriented fields.
- OpenTelemetry's [metric semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/metrics/) define metric instruments, units, and semantic naming, while noting cardinality implications. Operational telemetry and billable metering remain separate pipelines unless explicitly reconciled.

**RM-TENANT-GOV-RESEARCH-0001:** Provider subscription, entitlement, quota, meter, and billing objects map loss-consciously into the logical model and never silently strengthen native guarantees.

**RM-TENANT-GOV-RESEARCH-0002:** Windows, Linux, and macOS provide local identity, resource controls, storage, telemetry, licensing/commerce integrations, and isolation mechanisms but no shared tenant-commercial governance contract; product/provider selection remains an RFC decision.
