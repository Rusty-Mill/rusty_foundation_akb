# Platform research

This research informs adapter contracts; native package managers and vendor policy remain authoritative.

## Windows

- MSIX separates package identity, manifest, dependencies/framework packages, staging/registration, in-use deferral or shutdown, and update versions. Block maps enable differential transfer without changing the target package identity.
- Deployment capability varies by Windows version and distribution channel. Store, App Installer, enterprise management, MSIX APIs, MSI, and executable installers expose different transaction and policy evidence.
- Classic MSI/custom-action and arbitrary installer behavior cannot inherit MSIX atomicity or isolation claims.

Primary sources: [MSIX deployment overview](https://learn.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-overview), [MSIX differential updates](https://learn.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-update), [Windows App SDK deployment architecture](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/deploy-overview).

## Linux

- Debian/dpkg explicitly models unpacked, configured, half-installed, and error-unwind states. Maintainer scripts run at multiple old/new package phases and are required to be idempotent for recovery.
- RPM transactions include scriptlets and triggers whose failure and transaction effects vary by slot. Higher-level dependency solvers and repository managers add policy not supplied by the archive format alone.
- Distribution-native package databases, version ordering, dependency semantics, configuration policy, service integration, offline roots, and locks remain native adapter concerns.

Primary sources: [Debian installation and maintainer-script procedure](https://www.debian.org/doc/debian-policy/ch-maintainerscripts.html), [RPM scriptlets and triggers](https://rpm.org/docs/latest/manual/triggers.html).

## macOS

- Application bundles, disk images, signed installer packages, Mac App Store distribution, managed-device package declarations, and third-party updaters are different mechanisms.
- Distribution packages may include component choices, target/volume requirements, authorization levels, scripts, services, and multiple nested signed containers. Package installation success is separate from code-signing/notarization and application health.

Primary sources: [Packaging Mac software for distribution](https://developer.apple.com/documentation/xcode/packaging-mac-software-for-distribution), [Distribution XML reference](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/DistributionDefinitionRef/Chapters/Distribution_XML_Ref.html).

## Secure-update metadata

The Update Framework demonstrates independent root, targets, snapshot, and timestamp roles; threshold/delegated trust; consistent repository snapshots; metadata versioning/expiration; bounded downloads; and defenses against rollback, freeze, mix-and-match, wrong-target, and key-compromise attacks. Rusty Mill defines the required properties but does not select TUF as the only profile without an RFC.

Primary source: [The Update Framework specification](https://theupdateframework.github.io/specification/).

