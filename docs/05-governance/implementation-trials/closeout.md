# Trial closeout

| Outcome | Meaning | Permitted next step |
|---|---|---|
| Success | Named observations support hypotheses within the exact frontier | propose contract/ADR/RFC change or further review |
| Failure | Named observations refute one or more hypotheses | revise or reject approach; preserve negative evidence |
| Inconclusive | Evidence cannot distinguish outcomes within limits | refine question, method, or bounds in a new trial |
| Terminated | Safety, authority, cost, or governance stop condition fired | contain, retain evidence, and require explicit restart decision |

**RM-TRIAL-CLOSE-0001:** Closeout MUST record outcome per hypothesis, all findings/limitations, evidence inventory, unresolved uncertainty, spent authority, cleanup, disposal/retention, and recommended decisions.

**RM-TRIAL-CLOSE-0002:** Closing a successful trial MUST NOT automatically promote capability maturity, stabilize an interface, select a provider, merge trial code, or authorize release.

**RM-TRIAL-CLOSE-0003:** Negative and inconclusive evidence MUST be retained under the same integrity and provenance rules as successful evidence.

**RM-TRIAL-CLOSE-0004:** Disposal MUST revoke credentials/privileges, remove temporary publication paths, account for data/artifacts, and preserve the minimum governed evidence needed to interpret decisions.

