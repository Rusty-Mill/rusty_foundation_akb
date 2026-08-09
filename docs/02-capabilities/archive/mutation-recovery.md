# Mutation, update, repair, and recovery

**RM-ARCHIVE-MUTATE-0001:** In-place update is not a generic guarantee. Providers declare append-only, rewrite-and-replace, index-only mutation, or unsupported, including crash and space-amplification behavior.

**RM-ARCHIVE-MUTATE-0002:** Logical add/remove/replace produces a new immutable creation plan and output generation. Existing signatures, digests, offsets, indexes, encryption, multipart layout, and reproducibility evidence are invalidated unless explicitly recomputed.

**RM-ARCHIVE-MUTATE-0003:** Update mode never loads unbounded metadata/content into memory and never overwrites the only accepted generation before the replacement passes validation and publication policy.

**RM-ARCHIVE-REPAIR-0001:** Repair and salvage are forensic operations producing a new artifact plus an evidence report. They never silently relabel recovered bytes as the original valid container.

**RM-ARCHIVE-REPAIR-0002:** Salvage records skipped ranges, inferred headers, missing volumes, duplicate choices, checksum/authentication state, truncated entries, synthetic metadata, and confidence limits.

**RM-ARCHIVE-RECOVERY-0001:** Journals and staging identify operation/source/destination generations, planned effects, completed steps, integrity state, cleanup authority, expiry, and compatible recovery code.

**RM-ARCHIVE-RECOVERY-0002:** Recovery chooses resume, complete, roll forward, restore prior generation, quarantine, or abandon with residuals; rollback is not claimed when externally visible overwrites cannot be reversed.
