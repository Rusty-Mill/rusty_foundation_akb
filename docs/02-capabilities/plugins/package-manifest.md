# Package identity and manifest

**RM-PLUGIN-PACKAGE-0001:** A package has stable namespaced identity, package version, publisher identity/provenance, content digest, target formats/platform constraints, declared interfaces, dependencies, requested capabilities, isolation requirements, resource budgets, lifecycle policy, and update channel.

**RM-PLUGIN-PACKAGE-0002:** Manifest bytes use a canonical versioned format with bounded size/depth/count. Unknown critical fields reject the package; unknown noncritical fields remain preserved or diagnosed according to schema policy.

**RM-PLUGIN-PACKAGE-0003:** Package name, filesystem name, module name, publisher display name, signature identity, and interface identity are distinct and cannot substitute for one another.

**RM-PLUGIN-PACKAGE-0004:** Integrity digest, signature validity, certificate/trust decision, transparency/provenance evidence, malware/notarization assessment, and user/admin approval are separate results with time and policy context.

**RM-PLUGIN-PACKAGE-0005:** Native libraries and dependencies are enumerated before activation where tooling permits. Runtime dependency search cannot use ambient current directory or unrestricted process paths.

**RM-PLUGIN-PACKAGE-0006:** Requested authority is descriptive input, never self-granted. The host resolves an attenuated grant or rejects activation.

