# Directory objects, aliases, and correlation

**RM-IDENTITY-GOV-DIRECTORY-0001:** Directory schemas identify object kind, tenant, stable local identity, provider identity, generation, attributes, extension namespaces, lifecycle state, provenance, and sensitivity. Unknown extensions remain losslessly observable where safe.

**RM-IDENTITY-GOV-DIRECTORY-0002:** Correlation uses an explicit versioned rule and records candidate evidence, ambiguity, conflicts, reviewer or automated policy, and outcome. Email address, display name, or login-name equality is insufficient by default.

**RM-IDENTITY-GOV-DIRECTORY-0003:** Recreated provider objects receive a new generation even if the provider reuses a name or external key. Tombstones prevent stale events from resurrecting retired objects.

**RM-IDENTITY-GOV-DIRECTORY-0004:** Service and workload accounts declare owner, purpose, environment, credential policy, review schedule, expiry, interactive-login policy, and orphan response.

**RM-IDENTITY-GOV-DIRECTORY-0005:** Attribute access is projected by purpose and caller authority; secrets, authenticators, recovery data, protected characteristics, and high-risk identifiers never appear in general directory projections.
