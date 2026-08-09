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
| Conformance assertion | stable assertion identifier (closure gate CR-001) | one or more requirements |
| Benchmark scenario | stable scenario identifier (closure gate CR-005) | performance claim and native baseline |
| Profile | profile name and version | required/optional capabilities and quality levels |
| Provider claim | provider/version/platform tuple | passing evidence and known exceptions |
| Release claim | artifact digest | profiles, provider claims, provenance, SBOM |

## Rules

- A stable requirement cannot exist without a planned verification method.
- A passing test cannot establish a guarantee unless it links to a normative requirement.
- A benchmark result states the environment, workload, baseline, and contract version.
- Waivers are explicit, owned, time-bounded, and visible in release claims.
- Source records and structural links are validated by the [derived machine-readable consistency index](consistency-readiness/README.md). Direct requirement-to-assertion and requirement-to-scenario links remain explicit closure gates and MUST NOT be inferred from artifact presence.

## Documentation behavior

Markdown remains the human-readable normative source of architectural intent. Structured indexes may derive and validate records, but generated views link back to the normative source and cannot fork, repair, or override its wording ([ADR-0146](../adr/0146-machine-readable-indexes-are-derived-evidence.md)).
