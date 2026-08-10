# Trial review checklist

The authorization record names the person filling each applicable role; one person may fill multiple roles while conflicts and independence limitations remain visible.

- [ ] Capability owner confirms exact Experimental subject and contract frontier.
- [ ] Architecture reviewer confirms bounded questions, dependencies, nonclaims, and no accidental precedent.
- [ ] Standards reviewer validates repository profile, tooling, exceptions, and evidence mapping.
- [ ] Security reviewer approves authority, unsafe/FFI, secrets, runner, supply-chain, and data risks.
- [ ] Quality reviewers confirm performance, accessibility, i18n, privacy, observability, and operational applicability.
- [ ] Evidence reviewer confirms assertions, cases, scenarios, environments, retention, and reproducibility.
- [ ] Trial owner accepts limits, pause/stop conditions, cleanup, disposal, and closeout duties.
- [ ] Authorizing maintainer records gate states and decision for the exact generation.

**RM-TRIAL-REVIEW-0001:** Required reviewers MUST explicitly approve, reject, or qualify their gate; silence is `unknown`.

**RM-TRIAL-REVIEW-0002:** A reviewer MUST disclose when they authored the evidence they independently assess; the authorization records accepted independence limitations.

**RM-TRIAL-REVIEW-0003:** Open blocking findings, expired waivers, or unresolved reviewer qualifications prevent authorization.

**RM-TRIAL-REVIEW-0004:** Per [RFC-0004](../../rfc/0004-solo-maintainer-review-sufficiency.md), while solo-maintainer mode is active for a role, that role's independent-reviewer expectation is satisfied by the sole accountable person's own disclosed self-review; RM-TRIAL-REVIEW-0002's disclosure duty still applies without exception, and this does not substitute for any gate's substantive evidence.

