# Deidentification and reidentification risk

**RM-PRIVACY-DEID-0001:** A deidentification plan binds source generation/population, purpose, recipient/adversary model, auxiliary-data assumptions, direct/quasi/sensitive identifiers, transformation algorithms/parameters/keys, utility goals, risk thresholds, provider, and policy authority.

**RM-PRIVACY-DEID-0002:** Removal, masking, pseudonymization, tokenization, hashing, generalization, suppression, perturbation, aggregation, sampling, synthetic generation, differential privacy, secure computation, and encryption are distinct techniques with different reversibility and threat models.

**RM-PRIVACY-DEID-0003:** Pseudonymized/tokenized/encrypted data remains linkable/reversible under named capabilities and is never relabeled anonymous solely because direct identifiers are hidden.

**RM-PRIVACY-DEID-0004:** Risk evaluation covers singling out, linkability, inference, membership, attribute disclosure, reconstruction, differencing, longitudinal joins, rare groups, location/temporal trails, model memorization, composition across releases, and privileged/recipient auxiliary data.

**RM-PRIVACY-DEID-0005:** Privacy budgets bind mechanism/profile, neighboring relation, epsilon/delta or other exact metric, contribution bounds, query/release composition, population/partition, ledger generation, authorized analyst, expiry, and failure behavior; the word “differential privacy” without parameters is prohibited.

**RM-PRIVACY-DEID-0006:** Outputs are new generations with lineage, utility/loss, risk evaluation, residual classifications, recipient/use restrictions, release history, and independent validation. A one-time assessment cannot cover future auxiliary data or combined releases indefinitely.

**RM-PRIVACY-DEID-0007:** Reidentification testing uses controlled restricted environments, approved datasets and adversary models, ethical/legal review, bounded access, no production subject exposure, incident handling, and destruction evidence.
