# Taxonomies, labels, and authority

**RM-PROTECTION-TAXONOMY-0001:** A taxonomy has immutable issuer/tenant/namespace and generation, labels with stable IDs and revisions, localized names/descriptions/tooltips, ordering or lattice relations where defined, scopes, applicability predicates, required markings/protections, lifecycle, and governing authority.

**RM-PROTECTION-TAXONOMY-0002:** Human display names such as Public, Internal, Confidential, Restricted, Secret, Personal, or Regulated are not globally interoperable identifiers and cannot be compared across issuers without an explicit mapping profile.

**RM-PROTECTION-TAXONOMY-0003:** Sensitivity, information type, legal/regulatory category, confidentiality/integrity/availability impact, retention, records status, export control, compartment, handling caveat, and audience are orthogonal dimensions unless a taxonomy explicitly composes them.

**RM-PROTECTION-TAXONOMY-0004:** A scalar ordering is used only where the issuer defines total order. Compartments, purposes, jurisdictions, integrity needs, and mixed obligations require a partial order/lattice or independent attributes; “highest label wins” is not universal semantics.

**RM-PROTECTION-TAXONOMY-0005:** Label policy publication binds eligible principals/apps/workloads, defaults/mandatory behavior, allowed transitions, classifier and protection mappings, offline policy, rollout/rollback, activation time, expiry, and supersession.

**RM-PROTECTION-TAXONOMY-0006:** Unknown, retired, malformed, foreign, conflicting, and unmapped labels remain visible evidence and default to the product's safe handling policy; they are never silently treated as unlabeled or public.

**RM-PROTECTION-TAXONOMY-0007:** Taxonomy administration, label publication, classification, downgrade approval, protection-template administration, DLP policy, incident review, and audit access are separately attenuated roles.
