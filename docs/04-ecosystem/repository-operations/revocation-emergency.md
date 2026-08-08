# Revocation and emergency response

**RM-REPOSITORY-EMERGENCY-0001:** Emergency triggers include signing/publishing/root/owner credential compromise, malicious or corrupted release, repository/mirror compromise, active critical exploitation, dependency takeover/confusion, metadata rollback/freeze/equivocation, or unsafe updater behavior.

**RM-REPOSITORY-EMERGENCY-0002:** Incident declaration binds severity, scope, affected identities/digests/keys/metadata generations/channels, commander, responders, communication classification, containment authority, evidence preservation, and next review time.

**RM-REPOSITORY-EMERGENCY-0003:** Containment actions—pause publication/promotion, freeze namespace, revoke credentials/delegations, yank/exclude targets, rotate roots, disable mirrors, issue mitigations, force update/disable—are independently authorized, reversible where safe, and recorded as signed policy changes.

**RM-REPOSITORY-EMERGENCY-0004:** Revocation identifies exact compromised or disallowed key/certificate, signer, artifact, package version/range, repository snapshot/delegation, namespace owner, workflow, or channel membership plus reason, effective/known-compromise time, scope, replacement, and policy generation.

**RM-REPOSITORY-EMERGENCY-0005:** Clients distinguish emergency metadata freshness from ordinary release cadence, persist monotonic state, verify recovery/root transitions, and declare fail-open/closed/degraded behavior by risk class when responders or clocks are unavailable.

**RM-REPOSITORY-EMERGENCY-0006:** Artifact exclusion does not rewrite bytes. Repository metadata and advisories make the release unavailable or rejected; retained evidence supports investigation, locked deployments, and recovery under controlled access.

**RM-REPOSITORY-EMERGENCY-0007:** Recovery requires clean identities/credentials/builders, root/delegation and repository reconstruction, independent artifact/provenance review, affected consumer inventory under privacy policy, safe replacement release, staged rollout, and heightened monitoring.

**RM-REPOSITORY-EMERGENCY-0008:** Communications distinguish confirmed facts, suspected scope, user action, mitigations, fixed versions, unsupported products, detection/IOC guidance, and unknowns; updates are revisioned and accessible.

**RM-REPOSITORY-EMERGENCY-0009:** Post-incident review validates timeline, authority use, detection/containment/recovery, consumer impact, key and repository integrity, residual risk, notification obligations, control changes, drills, and public disclosure boundaries.

