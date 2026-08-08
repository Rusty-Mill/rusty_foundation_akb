# Security, privacy, and accessibility

**RM-PRINT-SECURITY-0001:** Destination discovery/status, capability query, interactive selection, silent submission, job observation/control, queue administration, accounting, secure release, and artifact file output use separate least-authority grants and native enforcement.

**RM-PRINT-SECURITY-0002:** Documents, previews, thumbnails, titles, owner names, destination/location, job tickets, accounting codes, release secrets, spool files, job histories, and device responses are sensitive. Logging and diagnostics use classified metadata and content-free identifiers by default.

**RM-PRINT-SECURITY-0003:** Temporary render/spool data is access-restricted, encrypted when policy requires and support is evidenced, lifetime-bounded, cleaned on every terminal path, and covered by crash/restart recovery. Deletion does not claim physical erasure without proof.

**RM-PRINT-SECURITY-0004:** Untrusted documents, fonts, images, ICC profiles, tickets, driver data, and device protocols are size/complexity bounded and isolated according to risk. Print submission never executes embedded active content.

**RM-PRINT-ACCESS-0001:** Destination and option UI exposes semantic labels, current/effective values, conflicts/substitutions, status, page range, preview, cost/privacy consequences, and progress through keyboard and assistive technology with localized/bidirectional correctness.

**RM-PRINT-ACCESS-0002:** Status and errors do not rely on color, animation, spatial preview, or device jargon alone. Held/secure-release, paper/media conflicts, cancellation ambiguity, and partial/duplicate-output risk have accessible recovery guidance.

**RM-PRINT-ACCESS-0003:** Accessible document output is independently verified. Native print-dialog accessibility does not prove the produced artifact or printed content is accessible.
