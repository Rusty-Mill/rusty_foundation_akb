# Specification and evidence traceability

**Status:** Accepted foundation model  
**Authority:** [Authoritative architecture model](../01-architecture/architecture-model.md) and [RFC-0001](../rfc/0001-capability-specification-system.md)

> This document elaborates the evidence chain in the [authoritative architecture model](../01-architecture/architecture-model.md). The authoritative model governs if wording conflicts.

Traceability ensures that architecture promises survive implementation and release.

```text
Charter / Principle
        |
       ADR
        |
       RFC
        |
Capability requirement --- Profile requirement
        |                         |
Conformance assertion      Profile conformance
        |
Backend evidence --- Benchmark result --- Security evidence
        |
     Release claim
```

## Traceable records

| Record | Stable key | Must link to |
|---|---|---|
| Capability | `rm.<domain>.<name>@<version>` | specification, owner, graph |
| Requirement | `RM-<DOMAIN>-<CAPABILITY>-<NNNN>` | capability, decision source |
| Conformance assertion | future test identifier | one or more requirements |
| Benchmark scenario | future benchmark identifier | performance claim and native baseline |
| Profile | profile name and version | required/optional capabilities and quality levels |
| Provider claim | provider/version/platform tuple | passing evidence and known exceptions |
| Release claim | artifact digest | profiles, provider claims, provenance, SBOM |

## Rules

- A stable requirement cannot exist without a planned verification method.
- A passing test cannot establish a guarantee unless it links to a normative requirement.
- A benchmark result states the environment, workload, baseline, and contract version.
- Waivers are explicit, owned, time-bounded, and visible in release claims.
- Trace links are validated automatically once machine-readable metadata exists.

## Documentation behavior

Markdown remains the human-readable source of architectural intent. Future structured metadata may index and validate it, but generated views must link back to the normative source rather than fork its wording.
