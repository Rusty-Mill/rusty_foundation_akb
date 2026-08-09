# Catalogs, plans, subscriptions, trials, and add-ons

**RM-TENANT-GOV-PLAN-0001:** Catalog identity binds provider/product, market/region/currency/audience, offer/plan/add-on/price generations, publication state, effective period, terms reference, and supersession.

**RM-TENANT-GOV-PLAN-0002:** Features and quotas reference stable semantic identifiers. Display names, storefront product IDs, price IDs, invoice descriptions, or UI positions cannot become feature identity.

**RM-TENANT-GOV-PLAN-0003:** A subscription/agreement binds tenant and billing account, selected offers/quantities, term and billing cadence, effective periods, renewal/cancellation, trial, grace, commitment, discounts, contract overrides, and provider evidence.

**RM-TENANT-GOV-PLAN-0004:** Proposed, pending payment/approval, trialing, active, scheduled change, paused, grace, delinquent, canceled-at-period-end, ended, disputed, and provider-unknown are distinct states mapped loss-consciously.

**RM-TENANT-GOV-PLAN-0005:** Upgrade, downgrade, quantity change, add/remove add-on, renewal, pause/resume, cancellation, and reactivation declare effective instant, proration/nonfinancial service effects, queued operations, notification, rollback, and idempotency.

**RM-TENANT-GOV-PLAN-0006:** Provider webhooks are authenticated observations subject to duplication, reordering, delay, gaps, and reconciliation; they do not directly mutate resource authorization without policy evaluation.
