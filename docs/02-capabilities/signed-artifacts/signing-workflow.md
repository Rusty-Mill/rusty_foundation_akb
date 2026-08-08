# Signing workflow and envelopes

**RM-SIGNED-WORKFLOW-0001:** A signing request is immutable and binds artifact digest/identity, signed-view profile, semantic purpose, signer role, key-generation selector, algorithm policy, timestamp/transparency/provenance requirements, requester, approvers, expiry, and correlation identifier.

**RM-SIGNED-WORKFLOW-0002:** Authorization to request, approve, sign, timestamp, log, and publish are separately attenuated. Possession of a signing-capable key handle does not imply authority to sign arbitrary content.

**RM-SIGNED-WORKFLOW-0003:** The signing service re-digests or receives digest evidence through an authenticated boundary, displays/reports the exact request to approvers, prevents digest substitution, and returns an evidence-bearing outcome.

**RM-SIGNED-WORKFLOW-0004:** Key operations use the cryptographic policy and opaque key model. Key purpose, signer role, identity/certificate generation, hardware/remote-provider evidence, user-presence policy, rate limits, and audit target are resolved before signing.

**RM-SIGNED-WORKFLOW-0005:** Signature envelopes carry or unambiguously reference content, signed attributes/claims, signer identifier, algorithms/parameters, signature value, certificate/key evidence, and envelope/profile versions. Critical unknown claims fail closed.

**RM-SIGNED-WORKFLOW-0006:** Randomized and deterministic signature schemes declare reproducibility behavior. Retrying never silently creates multiple publishable signatures or bypasses approval limits.

**RM-SIGNED-WORKFLOW-0007:** Cancellation distinguishes not-started, key operation possibly performed, signature produced, timestamp requested, logged, and published. Ambiguous remote outcomes require reconciliation by request identifier.

**RM-SIGNED-WORKFLOW-0008:** Batch signing preserves per-artifact identity, digest, result, failure, and authorization. One approved item cannot authorize another through archive, wildcard, or path substitution.

## Ceremony record

The durable ceremony record includes the request and policy generations, human/workload identities and authenticated channels, approvals, signer/key/certificate evidence, provider/module, timestamps, transparency submissions, provenance references, result digests, publication outcome, and every override. Secret key material, credentials, and sensitive source paths are excluded or redacted by schema.

