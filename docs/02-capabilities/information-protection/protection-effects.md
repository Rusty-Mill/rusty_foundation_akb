# Marking, encryption, and rights protection

**RM-PROTECTION-EFFECT-0001:** A label may reference required protection intent, but effect plans independently bind exact subject generation, marking/encryption/rights/retention profile, recipients/principals, keys/templates/providers, policy, authority, limits, and rollback/recovery semantics.

**RM-PROTECTION-EFFECT-0002:** Headers, footers, watermarks, banners, filenames, icons, metadata, print markings, dynamic user identity, and accessibility announcements are distinct markings with format/layout/localization, tamper, duplication, visibility, and removal behavior.

**RM-PROTECTION-EFFECT-0003:** Markings communicate handling intent but do not enforce access and may be cropped, altered, omitted, hidden, inaccessible, duplicated, or rendered differently. Completion reports exact locations and unsupported/lost markings.

**RM-PROTECTION-EFFECT-0004:** Encryption and rights management bind content generation, cryptographic profile/key generation, issuer/owner, audience, permitted actions, authentication, offline lease, expiry, revocation, forwarding/printing/copy/export policy, provider, and recovery/escrow policy.

**RM-PROTECTION-EFFECT-0005:** Encryption does not enforce policy after authorized plaintext exposure and cannot prevent screenshots, photography, retyping, compromised endpoints, memory capture, or an authorized recipient's independent effects. Nonclaims are user/admin visible.

**RM-PROTECTION-EFFECT-0006:** Label metadata, visible markings, cryptographic envelope, rights policy, content bytes, container/service label, and retention record may diverge. Reconciliation reports every mismatch and never infers success from one component.

**RM-PROTECTION-EFFECT-0007:** Applying or changing protection creates a new artifact/object/message generation where bytes or envelope change, invalidates affected signatures/digests/caches, preserves lineage, and requires staged publication.
