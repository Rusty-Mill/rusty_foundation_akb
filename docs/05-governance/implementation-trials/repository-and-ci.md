# Trial repository and CI

A trial may use a dedicated repository or an isolated workspace only when its accepted contract explains the boundary. Repository shape is an experimental variable unless already governed elsewhere.

**RM-TRIAL-REPO-0001:** Trial code MUST live behind an unmistakably experimental boundary with protected review, a valid [repository standards profile](../software-development/repository-profile.md), and no automatic production publication path.

**RM-TRIAL-REPO-0002:** CI MUST pin or record toolchain, target SDK/linker, dependencies, feature set, configuration, runner trust class, platform/provider versions, and evidence retention location.

**RM-TRIAL-REPO-0003:** Secrets and privileged runners MUST use least authority, prohibit untrusted-code exposure, record approval and use, and define emergency revocation.

**RM-TRIAL-REPO-0004:** Trial artifacts MUST carry experimental status, source/profile identity, intended audience, expiry or retention, and explicit non-release language.

**RM-TRIAL-REPO-0005:** Trial code MUST be disposable; reuse requires a later reviewed decision and ordinary standards, compatibility, and release gates.

