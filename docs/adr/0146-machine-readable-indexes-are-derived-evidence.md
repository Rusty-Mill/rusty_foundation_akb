# ADR-0146: Machine-readable indexes are derived evidence

**Status:** Accepted  
**Date:** 2026-08-08

## Context

The knowledge base now contains thousands of normative requirements. Automated validation and traceability need structured records, but a second manually maintained authority would drift from the Markdown model.

## Decision

Markdown remains normative. Machine-readable indexes are deterministically generated, content-addressed derived evidence whose records link to exact Markdown sources. A stale or malformed index fails validation; it never amends, overrides, or repairs a normative source.

## Alternatives considered

- Make structured metadata authoritative now: rejected because the contract schema and authoring workflow have not been proven.
- Maintain Markdown and metadata independently: rejected because disagreement would create ambiguous authority.
- Avoid structured evidence: rejected because repository-scale traceability cannot be reviewed reliably by navigation alone.

## Consequences

- Automation can inventory and validate the model without creating competing prose.
- Generated diffs can be large and require deterministic formatting.
- Future RFCs may promote a structured format only after round-trip and review evidence exists.
