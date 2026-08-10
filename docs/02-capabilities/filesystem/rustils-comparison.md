# rustils filesystem comparison record

| Field | Value |
|---|---|
| Trial | [TRIAL-0002](../../05-governance/implementation-trials/rustils-trial-proposal.md), revision 4 (Authorized 2026-08-10) |
| Bound rustils commit | `b8bb862091e8af8dc484f8a8f2c4e76f54d37f16` |
| Reviewer | baileyrd (per RFC-0004, solo-maintainer sufficiency) |
| Produced | 2026-08-10, within the trial's 30-day authorized window |
| Status | Trial work complete — see each hypothesis's disposition below, and TRIAL-0002's own Closeout section for the trial-level outcome |

This record applies TRIAL-0002's bound Verification protocol (assertions, executable cases, comparison rules) to produce a disposition for each `RT-00N` hypothesis. Per `RM-RUSTILS-TRIAL-0003`/`0004`, nothing here is a Rusty-Mill conformance claim, and nothing here changes filesystem's promotion status by itself — only the domain's own promotion-review path can do that; this record is input to that path, not a substitute for it.

## `RT-001`: does rustils' `OsStr`-only path boundary satisfy ADR-0006's lossless-native-value requirement?

**Disposition: Inconclusive.**

Applying the bound comparison rule: "supported" requires the supporting-observation condition to hold *against the cited executable cases*. `RT-001` was bound to `rm.assertion.filesystem.resolve@1` (Verification protocol, TRIAL-0002) but, on direct inspection, **no executable case in rustils' own test suite exercises the hard cases this claim actually depends on**:

- No test in `crates/platform-linux/tests/` or `crates/platform-windows/tests/` creates, opens, or round-trips a path component containing non-UTF-8 bytes (permitted by POSIX, since Unix paths are arbitrary bytes excluding NUL and `/`) or a lone/unpaired UTF-16 surrogate (permitted by NTFS, and the specific case Rust's `OsString` uses WTF-8 internally to represent). A search across every test directory for `OsStrExt`/`OsStringExt`/`from_bytes`/`from_wide`/`encode_wide`/surrogate-adjacent constructs found exactly two incidental hits (`crates/platform-linux/tests/parity.rs:330,383`), both using `OsStrExt::as_bytes()` on an ordinary ASCII filename (`"f"`) to build a `CString` for a `libc::stat()` cross-check — unrelated to losslessness, not evidence for this claim.
- `docs/behavior/fs.md:19-20` states the claim as spec text ("names are `OsStr` and may be non-UTF-8 on unix") but rustils' own documented convention is that spec lines get a corresponding parity-suite assertion or a divergence entry; no such assertion exists for this line.
- rustils' own design rationale (`docs/rfc-v2.md` §7.3, decision O-1/D-11) is explicit that the `OsStr` choice was justified by API ergonomics and std-interop ("the entire extraction... shipped on `OsStr`/`OsString` without a boundary-level byte-manipulation need ever appearing... §5.1's std-interop works *because* `OsStr` is std's own boundary type") — **not** by a tested empirical losslessness guarantee. The rationale text makes no such claim.

Neither the refuting-observation condition holds (no counter-example was found either — no case where `OsStr` demonstrably loses information on either platform), nor is a supporting executable case available. Per the bound comparison rule, that is exactly the inconclusive condition as written ("no case distinguishing `OsStr` from ADR-0006's native value model is found on either platform").

**Worth recording separately, not as trial evidence:** Rust's own standard library documents `OsString`/`OsStr` as using WTF-8 on Windows (capable of representing any UTF-16 sequence, including unpaired surrogates, without loss) and raw bytes on Unix — a real, external, type-level guarantee. rustils inherits this by construction, simply by choosing not to layer a lossy `String`-based type on top. But that is a property of Rust's standard library, verified by Rust's own test suite, not something rustils' own repository demonstrates with its own evidence — and this trial's evidence rules (Verification protocol, "cited, not re-executed") are about what rustils itself has verified, not what an upstream dependency separately guarantees. Recording the distinction rather than blurring it is the point of an inconclusive disposition here.

## `RT-002`: does rustils' capability-style `Dir`/`File` satisfy ADR-0007's directory-relative-resolution security boundary, including disclosed protection strength?

**Disposition: Inconclusive — substantially supported for the tested scope, with a specific, named verification gap.**

**What is test-verified (supported for this slice):** `open_dir`/`create_dir`'s link-confinement claim is directly proven by four executable cases in rustils' own committed parity suite, all passing in rustils' own CI (rustils#122):

| Case | Backend |
|---|---|
| `linux_open_dir_rejects_a_symlink_in_an_intermediate_component` | Linux |
| `linux_create_dir_rejects_a_symlink_in_an_intermediate_component` | Linux |
| `windows_open_dir_rejects_a_reparse_point_in_an_intermediate_component` | Windows |
| `windows_create_dir_rejects_a_reparse_point_in_an_intermediate_component` | Windows |

ADR-0007 requires that "providers declare the strength of link, reparse, mount, and ancestor-race protections and expose weakened fallbacks" — rustils does this precisely: `docs/behavior/fs.md`'s Resolution safety section states R1 for most operations, R2 for `open_dir`/`create_dir` on Linux (5.6+ kernel, R1 fallback on `ENOSYS`), and R2-link-confinement-only for the same operations on Windows (no mount-confinement claim, since no NT flag equivalent to `RESOLVE_NO_XDEV` exists). This is disclosed strength, not an unstated assumption — the part of ADR-0007 that's about *disclosure* is met.

**What is not test-verified (the inconclusive condition, as bound):** the mount-confinement half of Linux's R2 claim (`RESOLVE_NO_XDEV`) has no committed test — rustils' own parity suite does not exercise a bind-mount crossing to confirm the flag actually rejects it (a real environment gap: a bind-mount fixture needs elevated CI privilege the harness doesn't assume, per `docs/divergences.md` #013's own disclosure). The claim rests on `openat2`'s documented kernel behavior for that flag, not on rustils' own executed evidence. This matches the bound Inconclusive condition exactly: "the parity suite still does not exercise a mount-crossing race on either backend, and Windows has no mount-confinement mechanism to test at all."

**Scope note, not a refutation:** `open`/`access`/`metadata`/`read_dir`/`rename`/etc. remain R1 (symlinks followed transparently) by deliberate design — this is not evidence against ADR-0007, since ADR-0007 requires disclosed strength, not universal R2+; R1 is disclosed as R1, not silently assumed stronger.

Because a real, named piece of the hypothesis (mount-confinement) has no executable evidence either way, "supported" would overclaim and "refuted" would misstate what was actually found (the tested link-confinement claim holds cleanly). Inconclusive, with the specific gap named, is the accurate disposition — consistent with `RM-TRIAL-MODEL-0003`'s "inconclusive is an equally valid learning outcome."

## Follow-on decision (per Closeout's own requirement)

**Explicit no-change decision for filesystem's Experimental promotion status.** Neither disposition refutes ADR-0006 or ADR-0007, and per `RM-RUSTILS-TRIAL-0004` a comparison finding cannot change promotion status unilaterally regardless. Filesystem's Experimental promotion (accepted 2026-08-10, scoped to the R2/D2 baseline already bound there) stands unchanged.

**Recorded, non-binding suggestions for rustils** (external repository, independently governed — this trial has no authority to request or require these, per Scope, limits, and nonclaims): a test exercising a non-UTF-8 (Linux) or lone-surrogate (Windows) path component would close `RT-001`'s gap; a bind-mount fixture (even one that skips gracefully in unprivileged CI, matching `tests/tun_parity.rs`'s own convention) would close `RT-002`'s remaining gap. Neither is requested or expected by this record — they are handed off as informative findings only.
