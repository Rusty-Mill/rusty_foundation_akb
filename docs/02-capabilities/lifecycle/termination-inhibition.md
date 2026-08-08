# Termination and inhibition

## Service boundary

Lifecycle termination requests may initiate the existing orderly-shutdown service. They do not redefine its phases or guarantee its completion.

**RM-LIFECYCLE-TERMINATE-0001:** Cooperative query, committed termination, forced termination indication, and disappearance without notification are distinct cases.

**RM-LIFECYCLE-TERMINATE-0002:** A cooperative query receives a prompt policy response: allow, request bounded deferral, or deny only where the platform and product policy permit. Cleanup is not performed inside the query callback.

**RM-LIFECYCLE-TERMINATE-0003:** After committed termination, the service quiesces new work and may invoke orderly shutdown within the remaining native deadline. Deadline expiry never implies arbitrary thread killing is safe.

**RM-LIFECYCLE-TERMINATE-0004:** Denial or inhibition requires explicit authority, stable human-readable reason, owner, monotonic deadline, renewal policy, and guaranteed release on completion/cancellation/drop where supported.

**RM-LIFECYCLE-TERMINATE-0005:** Inhibition is scoped separately for logout, shutdown, sleep, idle, display power, or platform-specific categories. One category cannot silently imply another.

**RM-LIFECYCLE-TERMINATE-0006:** User intent and administrator/system force policy ultimately prevail. Applications cannot claim prevention, only the native result and expiry actually observed.

**RM-LIFECYCLE-TERMINATE-0007:** User-facing blockers and recovery choices are keyboard and assistive-technology accessible, localized, and never conceal which data remains at risk.

