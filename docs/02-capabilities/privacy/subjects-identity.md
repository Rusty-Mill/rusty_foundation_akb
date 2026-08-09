# Personal-data subjects, identity, and linkage

**RM-PRIVACY-SUBJECT-0001:** Subject kinds may include identified person, pseudonymous person, household, account, employee/contractor, minor/dependent, authorized agent, device/browser, location, group, organization contact, or unknown/unresolved under product policy; these are not globally interchangeable legal definitions.

**RM-PRIVACY-SUBJECT-0002:** Subject references are tenant/issuer scoped and may use direct identifiers, account IDs, pseudonyms, keyed tokens, device/session IDs, household links, or probabilistic linkage; each exposes provenance, confidence, expiry, collision, and unlinking behavior.

**RM-PRIVACY-SUBJECT-0003:** Authentication, account ownership, data-subject identity, authority to act, parental/guardian authority, authorized-agent delegation, and authority over another affected subject are separately evidenced.

**RM-PRIVACY-SUBJECT-0004:** Rights verification is proportional to request risk and available data, minimizes new collection, avoids requesting sensitive information the system would not otherwise hold, supports accessible alternatives, and never stores raw credentials as case evidence.

**RM-PRIVACY-SUBJECT-0005:** Failed or excessive verification cannot leak whether a subject or record exists. Rate limits, anti-enumeration, fraud review, appeal, and safe human escalation are explicit.

**RM-PRIVACY-SUBJECT-0006:** Identity resolution preserves ambiguity and conflicts. Merging subject graphs requires authority, evidence, reversible/fenced workflow where possible, impact review, and correction/unmerge semantics.

**RM-PRIVACY-SUBJECT-0007:** One record may concern multiple people or entities with competing rights and confidentiality. Projection/redaction and decision policy resolve request-specific disclosure; one request does not grant another subject's data.
