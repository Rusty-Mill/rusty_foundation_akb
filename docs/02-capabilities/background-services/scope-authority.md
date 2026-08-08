# Execution scopes, principals, and authority

**RM-BACKGROUND-SCOPE-0001:** Machine/system, boot, user, login session, graphical session, container, and application-private scopes MUST be modeled independently; no `background=true` flag may collapse them.

**RM-BACKGROUND-SCOPE-0002:** Every definition and attempt MUST identify principal/security-context provenance, credential source, group/privilege/capability restrictions, filesystem/network namespace, sandbox/label, home/profile availability, interaction state, and unknowns.

**RM-BACKGROUND-SCOPE-0003:** Installation authority, configuration authority, start/stop/control authority, execution authority, resource authority, secret/credential use, and result-read authority MUST be separately attenuated.

**RM-BACKGROUND-SCOPE-0004:** A system service MUST NOT assume an interactive user, desktop, home directory, profile, clipboard, display, keychain session, network identity, locale, or mapped storage. A user agent MUST bind a specific user/session generation.

**RM-BACKGROUND-SCOPE-0005:** Interactive authentication and permission prompting are prohibited in headless/service execution unless a separately selected out-of-band broker contract exists; lack of authority is a bounded explicit outcome.

**RM-BACKGROUND-SCOPE-0006:** Credentials and secrets MUST be opaque, purpose/audience/principal-bound, non-exportable where possible, fetched just in time, and invalidated on context or policy change. They MUST NOT be embedded in definitions, arguments, environment, logs, or scheduler payloads.

**RM-BACKGROUND-SCOPE-0007:** Privilege transition and helper delegation MUST use a narrow authenticated IPC operation boundary; a privileged long-lived service cannot become an ambient execution proxy.
