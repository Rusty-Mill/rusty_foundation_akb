# Models, analytics, logs, and backups

**RM-PRIVACY-DERIVED-0001:** Analytics, indexes, embeddings/features, profiles, model training/evaluation, prompts/outputs, logs/traces/metrics, support artifacts, caches, reports, and backups appear in the data inventory with purpose, subjects/linkability, lineage, retention, recipients, and rights policy.

**RM-PRIVACY-DERIVED-0002:** Model datasets and checkpoints bind source snapshots/consents or other policy evidence, filters, subject populations, lineage coverage, preprocessing, provider/region, training runs, evaluations, release/deployment generations, retention, and deletion/unlearning strategy.

**RM-PRIVACY-DERIVED-0003:** Removing a training record does not prove removal from a trained model. Products explicitly choose retrain, exact/inexact unlearning with validation, suppress outputs, restrict/deploy-new generation, retain under policy, or disclose an unsupported residual.

**RM-PRIVACY-DERIVED-0004:** Logs and security/audit evidence minimize personal data at schema/source, use purpose-separated stores and access, and define conflicts between privacy requests, integrity, incident response, fraud/security, legal hold, and retention without silently choosing priority.

**RM-PRIVACY-DERIVED-0005:** Backup erasure uses indexed selective deletion where proven, cryptographic compartment/key destruction, expiry without restore, or restore-time suppression/re-erasure. Production deletion never claims immediate absence from immutable backups.

**RM-PRIVACY-DERIVED-0006:** Restore, replay, reindex, rebuild, retrain, cache fill, replica catch-up, and disaster recovery consume deletion/restriction/correction tombstones before exposing resurrected data and prove convergence afterward.

**RM-PRIVACY-DERIVED-0007:** Aggregated metrics and reports retain threshold, suppression/noise, population, release-composition, small-group, drill-down, export, and reidentification evidence; aggregate naming alone does not remove privacy obligations.
