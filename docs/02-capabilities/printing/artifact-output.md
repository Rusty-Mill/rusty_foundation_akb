# Artifact and virtual destinations

File/PDF output is a document-artifact service that may share pagination and rendering with printing, but its authority, durability, metadata, signing, and lifecycle differ.

**RM-PRINT-ARTIFACT-0001:** Artifact output MUST bind destination file authority, exact format/profile, overwrite/atomic-replace policy, metadata/privacy policy, resource embedding, encryption/signing intent, and durability requirement.

**RM-PRINT-ARTIFACT-0002:** Render completion, encoded-byte completion, file replacement, file synchronization, directory synchronization, upload, and consumer acceptance are distinct milestones.

**RM-PRINT-ARTIFACT-0003:** “Print to PDF” presented by an OS queue and direct PDF export are distinct provider paths. A product MUST NOT infer file authority, format profile, metadata, accessibility tagging, or durability from a destination display name.

**RM-PRINT-ARTIFACT-0004:** Accessible reading order, structure/tag tree, language, alternative text, forms, links, and document metadata require an explicit accessible-document contract; visual page fidelity alone does not satisfy it.

**RM-PRINT-ARTIFACT-0005:** Digital signatures, certified documents, archival profiles, encryption/permissions, redaction, and sanitization are separate services with their own threat models and conformance evidence.

Email, cloud print, fax, and remote document delivery are application protocols, not aliases for local file or queue submission.
