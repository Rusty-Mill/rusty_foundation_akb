# Platform research

## Standards and risk categorization

- [FIPS 199](https://csrc.nist.gov/pubs/fips/199/final) categorizes information and systems by confidentiality, integrity, and availability impact; these are independent dimensions rather than a universal document-label ladder.
- [NIST SP 800-60](https://csrc.nist.gov/pubs/sp/800/60/v1/r1/final) maps information types to provisional impact categories and requires organization-specific adjustment and rationale.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) and [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) frame data processing, protection, audit, media, transfer, and privacy controls without defining a cross-product label format.

## Windows and Microsoft ecosystem

- [Microsoft Purview sensitivity labels](https://learn.microsoft.com/purview/sensitivity-labels) are tenant-specific cleartext metadata assertions that can drive markings, encryption, access restrictions, automatic labeling, and user policy tips.
- [DLP label conditions](https://learn.microsoft.com/purview/dlp-sensitivity-label-as-condition) vary by workload, item type, policy-tip availability, and enforcement coverage; encrypted content can restrict content-based evaluation.
- [Office label behavior](https://learn.microsoft.com/purview/sensitivity-labels-office-apps) documents platform/application differences in when metadata, markings, and encryption apply, plus independent pre-existing rights protection.
- Windows Information Protection is not a universal future foundation; endpoint DLP, application/container policy, file encryption/rights systems, Defender, and Purview have product/licensing/management boundaries that providers must disclose.

## Apple platforms

- [Managed Open In](https://support.apple.com/guide/deployment/managed-open-in-dep8b081c79b/web) separates managed and unmanaged document flows under device-management policy; it is channel/application management, not content classification proof.
- Apple platform data protection, managed pasteboard, per-app VPN, document providers, sharing restrictions, file protection, and rights-bearing application formats are separate mechanisms without one portable sensitivity-label service.

## Linux and cross-platform environments

- Linux distributions/desktops expose MAC labels, extended attributes, document metadata, application sandboxes, print/clipboard portals, enterprise agents, cryptographic containers, and server-side gateways independently. Semantics depend on security module, filesystem, desktop, management, and application support.
- Common document/email/cloud labeling and rights-management systems are application/service formats, not kernel or freedesktop guarantees. Unknown metadata may be lost during copy, conversion, archive, sync, or tool editing.

## Architectural inference

Rusty Mill standardizes the evidence and effect boundaries while products select organizational taxonomies, protection providers, management systems, covered channels, and legal policy. Platform presence never implies equivalent enforcement or prevention.
