# Platform and standards research

## Neutral privacy-risk architecture

- The [NIST Privacy Framework](https://www.nist.gov/privacy-framework) treats privacy as enterprise risk from data processing and organizes Identify-P, Govern-P, Control-P, Communicate-P, and Protect-P outcomes.
- NIST defines data processing across collection, retention, logging, generation, transformation, use, disclosure, sharing, transmission, and disposal, supporting an end-to-end action model rather than a consent-only API.
- [NIST Privacy Engineering Program](https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering) distinguishes predictability, manageability, and disassociability objectives and publishes risk-assessment resources.

## Legal-policy sources illustrating variance

- The official [EU General Data Protection Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj) defines principles such as purpose limitation, minimization, accuracy, storage limitation, rights, controller/processor duties, transfer rules, and multiple lawful bases/exceptions. Rusty Mill does not encode their legal interpretation.
- California's official [CCPA overview](https://oag.ca.gov/privacy/ccpa) describes rights to know, delete, opt out of sale/sharing, correct, limit sensitive-information use, and nondiscrimination, with business duties and exceptions distinct from GDPR.
- The [Global Privacy Control specification](https://globalprivacycontrol.org/) illustrates a user-agent preference signal whose legal effect and mapping remain jurisdiction/product policy rather than intrinsic protocol semantics.

## Platform/product evidence

- Apple [privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files) declare SDK/app data categories, collection purposes, tracking domains, and required-reason API use for App Store policy; declarations are supply-chain evidence, not runtime legal authorization.
- Windows, Linux, and macOS provide permissions, sandboxing, account identity, device management, encryption, storage, browser preferences, application manifests, and deletion mechanisms, but no OS supplies a complete cross-jurisdiction controller/processor, purpose, rights, or lineage service.
- Cloud/SaaS privacy portals and data maps vary in resource coverage, identity matching, deletion semantics, backup handling, regions, processors, exports, and audit. Provider adapters preserve exact scope and residuals.

## Architectural inference

Rusty Mill standardizes lifecycle evidence, authority separation, orchestration, and testable boundaries. Product legal/privacy owners select definitions, bases, notices, deadlines, exceptions, transfer mechanisms, and response content through versioned policy and RFCs.
