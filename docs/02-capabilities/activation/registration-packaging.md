# Registration, packaging, and updates

Handler registration is packaging/deployment metadata evaluated by the platform, not a runtime mutation API in the base capability.

**RM-ACTIVATION-REGISTER-0001:** A registration manifest MUST declare stable application/package identity, supported file/content types and schemes, verbs/roles, executable/entry point, argument/activation contract, icons/display resources, install scope, platform/version constraints, trust/signing evidence, and ownership/contact.

**RM-ACTIVATION-REGISTER-0002:** Applications register only types/schemes they can handle safely and completely under the advertised role. Overbroad wildcard, executable/script, reserved/system scheme, or unrelated type claims are prohibited.

**RM-ACTIVATION-REGISTER-0003:** Custom schemes require collision/ownership/spoofing analysis and versioned payload grammar. Verified web associations require domain-controlled evidence and safe browser fallback; they are not equivalent to custom schemes.

**RM-ACTIVATION-REGISTER-0004:** Install/update/uninstall are transactional with generation identity. Failed updates preserve or restore the prior usable registration where the platform supports it; stale entries are detected and reconciled.

**RM-ACTIVATION-REGISTER-0005:** Version compatibility covers old/new sender and receiver payloads, side-by-side installations, downgrade, rollback, per-user/per-machine scope, roaming/sync, and unknown fields. Handler changes never imply data migration authority.

**RM-ACTIVATION-REGISTER-0006:** Registration evidence and conformance are release gates. Runtime code MUST NOT edit native association stores to force defaults or repair packaging silently.

**RM-ACTIVATION-REGISTER-0007:** Default-setting UX uses supported OS settings/chooser paths with accessible explanation and user control. Products remember only their own prompt policy, not a claim that they remain default.
