# Platform research

## Shared and protocol identities

- The [IANA media-types registry](https://www.iana.org/assignments/media-types/media-types.xhtml) provides registered names and specification references, not content detection or safety verdicts.
- The [WHATWG MIME Sniffing Standard](https://mimesniff.spec.whatwg.org/) specifies contextual browser sniffing and documents security consequences when declared and interpreted types diverge.
- The [freedesktop.org Shared MIME-info specification](https://specifications.freedesktop.org/shared-mime-info/latest-single/) combines weighted filename globs, magic, XML roots, aliases, inheritance, user/application overrides, and security guidance; it can yield conflicts rather than intrinsic truth.

## Windows

- [`IAttachmentExecute::CheckPolicy`](https://learn.microsoft.com/windows/win32/api/shobjidl_core/nf-shobjidl_core-iattachmentexecute-checkpolicy) evaluates filename/path/source/referrer evidence into enable, prompt, or disable for attachment execution policy.
- [Antimalware Scan Interface](https://learn.microsoft.com/windows/win32/amsi/antimalware-scan-interface-portal) exposes provider-backed buffer/string/session assessment and operation notification; result codes remain provider/policy evidence rather than general file safety.
- Windows file associations, perceived types, property handlers, thumbnail providers, SmartScreen/reputation, Defender, Mark-of-the-Web/zone evidence, and code-signing policy are separate facilities with different scope and availability.

## macOS

- [Gatekeeper and runtime protection](https://support.apple.com/guide/security/gatekeeper-and-runtime-protection-sec5599b66df/web) compose downloaded-software provenance, identified-developer signatures, notarization, known-malware checks, user approval, and runtime controls.
- [`quarantinePropertiesKey`](https://developer.apple.com/documentation/foundation/urlresourcekey/quarantinepropertieskey) exposes quarantining agent and origin metadata with documented hard-link inconsistency.
- [Quick Look](https://developer.apple.com/documentation/quicklook) uses system and extension providers to generate previews for declared content types; preview support is not content acceptance or activation authority.

## Linux desktop

- Shared MIME-info, application associations, desktop thumbnailers, sandboxing frameworks, extended attributes, package signatures, and malware scanners are independently deployed and policy-controlled.
- The [Thumbnail Managing Standard](https://specifications.freedesktop.org/thumbnail/latest-single/) defines source-URI/time-associated preview caches and provider-specific failure records, illustrating that previews and failures require generation-aware cache policy.

## Architectural inference

No platform provides one authoritative “safe content” service. Rusty Mill composes typed evidence and purpose-specific decisions while retaining native results, gaps, privacy costs, and policy authority.
