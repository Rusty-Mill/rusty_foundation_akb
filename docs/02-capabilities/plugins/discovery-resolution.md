# Discovery and selection

## Capability identity

`rm.plugin.catalog` produces immutable catalog snapshots from explicitly authorized sources.

**RM-PLUGIN-DISCOVERY-0001:** Sources are ordered and scoped directory/package-store authorities. Ambient current-directory, PATH, loader search paths, registry-wide enumeration, and network discovery are prohibited by default.

**RM-PLUGIN-DISCOVERY-0002:** Discovery parses metadata and verifies package evidence without mapping executable code, running constructors, resolving imports, or invoking plugin callbacks.

**RM-PLUGIN-DISCOVERY-0003:** A catalog snapshot records revision, source plan, package identities/versions/digests, verification state, conflicts, rejected entries, and observer continuity.

**RM-PLUGIN-DISCOVERY-0004:** Selection consumes exact interface ranges, workload/isolation requirements, trust policy, authority ceiling, platform constraints, resource budgets, and conformance evidence. It returns one evidence-bound plan or complete unsatisfied diagnostics.

**RM-PLUGIN-DISCOVERY-0005:** Duplicate identity/version with different content is a conflict, never last-writer-wins. Downgrade, publisher change, or trust-policy change requires explicit policy.

**RM-PLUGIN-DISCOVERY-0006:** Source changes trigger catalog reconciliation. Overflow or ambiguous replacement forces full rescan; an active generation is unaffected until a new plan is verified and committed.

