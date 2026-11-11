---
title: 'Recheck of revised ARCHITECTURE-SPINE (WRMS)'
target: '../ARCHITECTURE-SPINE.md (719 lines, AD-1..AD-26)'
ground_truth: 'prd.md §4, §4.1, §5, §7, §8.2; chot-2026-10-29.md §7'
date: '2026-11-11'
---

# Recheck of the revised spine

**Verdict:** ready with minor fixes. 21 of the 23 critical/high findings are closed with an enforceable rule; 2 are partial; none are open. The revision introduced one high problem (revealed hidden images cannot be fetched) and about ten medium ones, all fixable by a sentence or two each.

Tally for the critical+high set: **CLOSED 21, PARTIAL 2, OPEN 0.**

## 1. Status of the 23 critical/high findings

| # | Source finding | Status | Closed by / what is missing |
| --- | --- | --- | --- |
| A1 | Lifecycle and modules may not call routing; submit writes `ai_analysis` (C) | CLOSED | Routing moved to `core/routing` (diagram, AD-18.1-3, table); AD-12.1 submit writes no `ai_analysis`; AD-6.1 moved Zalo use case into `modules/accounts` |
| A2 | Lifecycle unowned, bounded by column (C) | CLOSED | AD-7.1 (single writer of every column of 7 tables), AD-7.2, "Ai ghi bảng nào"; owner = M2 assumption plus Structural Seed paragraph |
| A3 | Late/repeated AI results hit changed group (H) | CLOSED | AD-12.4-5 (`applyAnalysis`: lock both groups, latest attempt once, proposal only if alone in SUBMITTED and target open, Cờ only on open group), AD-7.8 |
| A4 | Merged-away group still accepts commands (H) | CLOSED | AD-7.7 (`MERGED`, `GROUP_MERGED`, enum in Conventions) |
| A5 | Derived group transitions implemented per command (H) | CLOSED | AD-7.4 `settleGroup` |
| A6 | Nobody owns the transaction (H) | CLOSED | AD-25.1-2 (see N8 for an ordering conflict) |
| A7 | Purge follows a closed list (H) | CLOSED | AD-15.5 (ownership-based `purge` per module, address included), AD-15.6, AD-10.2, AD-19.2 (hash plus id only, no stored body) |
| A8 | Row scope removes rows that must stay; stateful reveal leaks (H) | CLOSED | AD-15.2-3 (field-level hiding, stateless reveal); see N1 for a new image problem |
| A9 | Idempotency scope/cached errors/drift (H) | CLOSED | AD-19.2-3, AD-19.5, AD-14.2 `UPLOAD_EXPIRED` |
| A10 | Admin reaches content through accounts (H) | CLOSED | AD-4.3 (ACCOUNT events readable by officers and leaders, forced password change), M12 states it is detective |
| R1 | Diagram contradicts ADs (H) | CLOSED | Diagram redrawn; AD-6.1; schema-location gap is N10 |
| R2 | No shared-transaction rule (H) | CLOSED | AD-25 |
| R3 | Actor authorization unassigned (H) | CLOSED | AD-7.3 (actor checked per "Ai" column inside the command; guard checks role only) |
| R4 | Structural rules have no automation (H) | PARTIAL | Import-direction CI check exists (diagram paragraph, Conventions "Git và CI"). Still missing: any automated check for single-writer ("mỗi bảng đúng một nơi ghi", AD-7.1). Fix: add a CI lint that insert/update/delete on the seven lifecycle tables is imported only from `core/lifecycle`, or export those table objects as write-capable only there |
| R5 | Schema and migration ownership (H) | CLOSED | Conventions "Schema và migration" row |
| R6 | "Ai ghi bảng nào" incomplete (H) | PARTIAL | Table is now full, but `image.hiddenAt/purgeAfter` has no stated writer (`core/storage` owns `image`, yet `decideFlaggedImage` and `rejectReport` must set it) and `user` has two writers (`modules/accounts`, `core/auth`) against the Conventions line "đúng một nơi ghi". Fix: say lifecycle sets image hide columns through a `core/storage` function with `tx`, and note `user` is column-split by design or move password/counters to a `credential` table |
| P1 | Consent and phone gate on submit (H) | CLOSED | AD-1.2 |
| P2 | Real data separated from student accounts (H) | CLOSED | `pilot` environment, AD-26.1-2 |
| D1 | Demo env vs Mini App Developer/Testing limits (H) | CLOSED | Environment table (`demo` Developer/Admin only, `pilot` needs OA), R2 quotas |
| D2 | Login depends on unchecked path, no alternative (H) | CLOSED | AD-6.5 and S0 state there is no fallback (`getUserID` is client-supplied and cannot satisfy FR-1); explicit stop-and-ask |
| D3 | AI scope collapsed to one boolean (H) | CLOSED | AD-11.2 (two backend-computed flags), AD-16.4 (image-AI Domain codes) |
| D4 | Group-12 interface/command list/writers (H) | CLOSED | Lifecycle command table, writer table, M2, R5 (see N6, N7 for missing commands) |
| W1 | `@node-rs/argon2` version wrong (H) | CLOSED | Stack row now `2 (2.2.2)` |

## 2. Medium findings from the earlier reviews still PARTIAL or OPEN (cross-epic risk only)

| Source | Status | Problem | Fix |
| --- | --- | --- | --- |
| A11 `/files` both role-guarded and session-less | PARTIAL | AD-14.5 says no session check, but AD-2.3 (default-deny prefix guard), AD-3.1 (Leader uses only `/auth`, `/me`, `/config` plus GET `/officer`) and AD-4.1 never exempt `/files`; a literal guard author blocks the Leader from images, which FR-61 forbids | AD-2.3: "`/files` and `/health` are outside the role guard; HMAC is the only credential" |
| Dec F8 / FR-60 label-to-category suggestion | OPEN | No rule says who turns Nhãn ảnh plus the confidence threshold into a "suggest fix Loại phản ánh" (FR-60), where it is shown, or that it is a read-time derivation; epic 3 and epic 12 owners can each build one | Add to AD-18 or AD-11: derived at read time from stored labels and the threshold setting, never stored, never a routing input |
| Rubric F13 / view recording | PARTIAL | AD-3.3 lists measured views but not that the POST is idempotent per (user, group, kind) | Add one clause |
| Dec F7 | PARTIAL | AD-22.2 still states "mọi Mini App dùng chung origin đó" as fact while S5 says unchecked; AD-24.3 says S1,S2,S4,S5 fallbacks stay in the four touch points but S5's fix is CORS in deployment config | Tag AD-22.2 `[ASSUMPTION pending S5]`; add CORS config to AD-24.3's list |

## 3. NEW problems introduced by the revision

| ID | Sev | Location | Problem | Minimal fix |
| --- | --- | --- | --- | --- |
| N1 | high | AD-15.3 vs AD-14.5 | FR-41 reveal returns hidden fields "chỉ trong response của POST", but `/files` refuses images that are hidden at fetch time, so the officer can never see the revealed images | The reveal POST mints URLs carrying a signed `reveal` flag and a very short expiry that `/files` honours for hidden (not purged) images |
| N2 | medium | AD-10.1 | "At most one row per recipient per command, final state" drops notices PRD requires: manual Cờ takes tasks On Hold then Cancelled in one command, so the assignee never gets the high-priority stop notice (FR-33); confirming a Cờ on a Received group owes Người gửi both an In Progress notice and the Cờ-confirmed safety advice (FR-32) | One row per (recipient, notice type), or define that the hazard-cancel type carries the safe fixed title and high priority and that `HAZARD_CONFIRMED` subsumes the status notice |
| N3 | medium | AD-13.6 vs AD-25.1/25.4, AD-7.3 | `pg_try_advisory_xact_lock` lives only as long as one transaction; a sweep that holds it while calling the AI Module or FCM keeps a pooled connection for minutes inside a transaction, or the job opens an outer transaction plus per-item use-case transactions | State that the lock tx only claims work (for example inserts the attempt row) and that no external call runs inside it |
| N4 | medium | AD-3.2 vs AD-5.1/5.4 | Every GET runs in a read-only transaction, yet NFR-5 needs a sliding 8-hour inactivity timeout, which writes `session` on every request | Exempt the session touch: `core/auth` updates last-activity in its own short statement outside the handler's read-only tx |
| N5 | medium | AD-2.3, AD-3.1, AD-4.1 | `/files` and `/health` are listed as shared prefixes but not exempted from the default-deny role guard (see section 2) | As A11 fix |
| N6 | medium | AD-25.3, lifecycle command list | FR-20 (field check), FR-21 (send and answer supplement request), FR-45 (rating) write module tables under state preconditions (Received/In Progress, Completed), but no lifecycle command locks and checks the group first, so the AD-25.3 pattern cannot be followed and they race with split, close and merge | Add a lifecycle guard such as `assertGroupState(tx, groupId, states)` that locks the group, and require those module use cases to call it first |
| N7 | medium | AD-18.5, lifecycle command list, FR-23 | "Danh sách đơn vị cuối cùng lưu riêng" (SM-R6) has no table, writer or command; FR-23 "đổi chủ trì khi Nhiệm vụ chủ trì cũ đóng" has no command (`isLead` is lifecycle-only) | Derive the final list from created tasks (no storage), and add `setLeadTask` or state `assignTask` may carry `isLead` for an existing open task |
| N8 | medium | AD-12.4, sequence diagram vs AD-25.3 | The job transaction is "lưu kết quả, rồi `applyAnalysis`" (module write first) while AD-25.3 requires lifecycle first; "nhận một lần" needs an applied marker on `ai_analysis` (owned by `modules/analysis`) that lifecycle may not write | Order: `applyAnalysis` first, then analysis stores result and `appliedAt`; or let `applyAnalysis` take the result as input and write the marker through an analysis function |
| N9 | medium | AD-3.3 vs FR-41/FR-35 | The reveal is logged to `view_log` (a metrics table owned by `modules/insights`), but FR-41 requires it in history (FR-35, append-only) | Reveal also appends a `CASE` history event (`HIDDEN_DATA_REVEALED`, ids only) |
| N10 | medium | Dependency diagram and import check vs Conventions "Schema" | `apps/api/drizzle/schema` is imported by `core`, `modules`, `jobs` but is not a node in the diagram, so the CI import check is undefined for it | Add a `SCHEMA` node that all three may import |
| N11 | medium | AD-2.7 vs FR-42, NFR-4 | Assignee row scope returns only the assignee's own tasks, but FR-42 and NFR-4 require the detail to list the other Đơn vị working on the same Nhóm and the lead/support role | Allow a scope-exempt projection of "other units on this Nhóm" (unit names and role only) in the assignee output schema |
| N12 | medium | AD-7.3, Conventions "Test" | AD-7.3 enforces state and actor only; FR-level preconditions in the Binds list (no reject or image exclusion while Cờ is pending, FR-19 Mức cuối before assign, FR-52 lock while proposals pending, FR-53 locks, deadline not in the past) have no rule and no test requirement | AD-7.3: "commands also enforce the preconditions in the Consequences of the FRs in Binds"; Test row: negative test per such precondition |
| N13 | low | AD-20.1 | "báo chất thải nguy hại" stamps `readAt`, but any Nhóm xử lý member may report hazard (FR-51) while FR-62 stamps only for the Người nhận | Stamp only when the actor is the Người nhận |
| N14 | low | AD-16.3 | Setting list omits values other ADs say are settings: signed-URL TTL (AD-14.6), orphan-upload TTL (AD-14.2), AI attempt timeout and retry spacing (AD-12.2-3) | Add them |
| N15 | low | Capability row 9 | Column omits AD-13 although AD-13 binds FR-34, against the stated "mọi AD" generation rule | Add AD-13 |
| N16 | low | ERD | No `SUPPLEMENT_REQUEST` to `IMAGE`, no `HISTORY_EVENT` to `REPORT` link (AD-9.3 per-report timeline), no `USER` to `TASK`/`TASK_MEMBER` | Add the three edges |
| N17 | low | Stack | Row "expo-notifications, ..." has "Theo SDK 58", not a number | Name the SDK-58 versions or accept as pinned by SDK |
| N18 | low | AD-11.2 | Does not say the "nhận diện loại rác" flag also gates hazard/medical labels (FR-50; PRD FR-60 says so) | Add three words |
| N19 | low | AD-18.2, AD-8.3 | A default lead Unit in the rule set can be switched to `EXTERNAL` mode by Admin | Catalog write rejects it |
| N20 | low | M2, R5 | `jobs/` framework (lock-id enum, `job_run`) has no owner, though epics 3 and 11 both add jobs | Name the owner in M2 |

## 4. Check of the three "not changed" claims

- **(a) Mốc đã trả lời công dân stamped by the system (FR-62): fair.** PRD §4 and FR-62 define it as the time the system sends the result notice at Completed/Closed, state that no written answer or answer deadline exists, and park the question in §14 q32-33; the spine mirrors it and lists q32 in "Điểm còn mở".
- **(b) AI retried only while the group is Submitted (FR-12): fair.** FR-12 conditions re-analysis on the Phản ánh still being in Submitted, and its last bullet makes the officer flag hazards by hand when AI is down; AD-12.2 keeps the "chưa phân tích" label alive after receipt. It is a PRD choice, though §8.2 treats missing hazard detection as the unsafe side, so a one-line open question to the PM would be prudent.
- **(c) Login lockout per account (NFR-5): fair.** NFR-5 says "tài khoản bị khóa đăng nhập 15 phút sau 5 lần nhập sai", which is per account; the denial-of-service-on-staff concern is real but is a PRD matter.

## 5. Frontmatter and lint contract

- Frontmatter has name, type, purpose, altitude, paradigm, scope, status, created, updated, binds, sources, companions; `.memlog.md` exists next to the spine.
- All 26 `### AD-n` blocks have Binds, Prevents and Rule (AD-23 has an inline Rule); ids are unique and ascending 1 to 26 (scripted check).
- Every row of the Stack table has a version containing a digit, except the "Theo SDK 58" row (N17).
- No TODO, TBD, XXX, placeholder or lorem text found.
- AD cross-references (AD-3→AD-20, AD-6, AD-10→AD-13, AD-14→AD-2, AD-11→AD-14, AD-24 to the risk table, S6 to AD-21 rules 1 and 2, M12 to AD-26 rule 2, A3-A7 rows) point to the right AD and rule. Chot decision numbers 17-24 resolve to §7.
- Capability map FR coverage checked row by row against the Binds fields: only row 9 omits an AD (N15).
