---
title: 'Adversarial review: ARCHITECTURE-SPINE (WRMS)'
target: '../ARCHITECTURE-SPINE.md'
ground_truth: 'prd.md §4, §4.1, §5, §7; addendum.md ownership table'
lens: 'Build two units one level down that each obey every AD and still do not fit together'
date: '2026-11-11'
---

# Adversarial review: ARCHITECTURE-SPINE (WRMS)

**Verdict.** The spine names the right mechanisms: a lifecycle aggregate, a transactional outbox, scopes per audience, derived predicates and DB uniqueness. Its boundaries are drawn at the wrong grain, though. AD-7 bounds lifecycle by *column* where it should bound it by *row*. The dependency rule forbids calls that AD-11, AD-12 and AD-18 require. Several rules list what they cover ("purge deletes X, Y", "lifecycle owns status") when they should state a principle. As a result, five owners can each follow the spine to the letter and still ship tasks with three writers, routing suggestions computed by nobody, AI results applied to groups that have since changed, and personal data that survives purge.

**Count:** 2 critical, 8 high, 9 medium, 1 low (20 holes).

Owner names follow the addendum: A, B, C, D, and Leader (the student owner of groups 4, 5 and 8, not the WARD_LEADER role).

| # | Hole | Units | Sev. | Tighten |
| --- | --- | --- | --- | --- |
| 1 | Lifecycle and modules may not call routing; submit may not write `ai_analysis` | A↔B, A↔D, core↔modules/routing | Critical | dependency rule, AD-12, AD-18 |
| 2 | Lifecycle is unowned and bounded by column, so `task` and `report_group` have 2–3 writers | Leader↔C↔B | Critical | AD-7, "Ai ghi bảng nào", M2 |
| 3 | Late or repeated AI results land on a group that has changed | D↔Leader↔B | High | AD-11, AD-12 |
| 4 | A merged-away group stays `SUBMITTED` and still accepts commands | Leader↔any officer command | High | AD-7 |
| 5 | Each command implements the derived group transitions itself, so groups get stuck In Progress | Leader↔C↔B | High | AD-7 |
| 6 | Nobody owns the transaction, so module writes and lifecycle commit separately | Leader/B↔lifecycle | High | AD-7 |
| 7 | Purge follows a closed list and misses copies the spine itself creates | C↔A, Leader, D, B | High | AD-15 |
| 8 | "Row scope filters hidden data" removes rows that must stay visible; stateful reveal leaks to WARD_LEADER | core scope↔A↔D↔Leader | High | AD-15 |
| 9 | Idempotency records: scope, cached errors and payload drift are undefined | core↔C↔A | High | AD-19, AD-8 |
| 10 | Admin reaches report content through account management | B↔AD-4 | High | AD-4 |
| 11 | `/files` is both role-guarded and session-less | core/auth↔core/storage↔D↔A | Medium | AD-14, AD-2 |
| 12 | Jobs change tasks without the group lock, and the read clock cannot be derived | C↔B↔Leader | Medium | AD-13 |
| 13 | Notification rows: unit of uniqueness, stored prose, push state | A↔B/C/Leader↔C | Medium | AD-10 |
| 14 | History payloads are untyped and point at one object, so merge and split break timelines and metrics | Leader↔A↔D↔B | Medium | AD-9 |
| 15 | The resident scope has no rule for result images; shared prefixes have no scope | A↔Leader/B | Medium | AD-2, AD-4 |
| 16 | Open supplement requests are stored state that lifecycle cannot close | Leader↔B | Medium | AD-7/AD-20 |
| 17 | Setting keys and the `/config` payload are not part of contracts | B↔C↔clients | Medium | AD-16, AD-1 |
| 18 | Contract drift goes undetected (AI fixtures, enum additions, old APKs, Mini App copy) | D↔D, backend↔C, contracts↔A | Medium | AD-1, A7 |
| 19 | Each client shell has several owners | all five | Medium | Conventions |
| 20 | "Giờ gửi" is undefined for queued drafts | A↔B↔D | Low | AD-18 |

---

## Critical

### 1. Lifecycle and modules may not call routing, and submit may not write `ai_analysis` — Critical

- **Units:** A (`modules/submission`) and B (`modules/routing`); A and D (`modules/analysis`); `core/lifecycle` and `modules/routing`.
- **Scenario:** AD-12 says the submit transaction commits the Report, the Nhóm, the Gợi ý phân luồng and an `ai_analysis` row in `PENDING`. "Ai ghi bảng nào" gives `routing_suggestion` only to `modules/routing` and `ai_analysis` only to `modules/analysis`. The dependency diagram has no MOD→MOD arrow ("Không có mũi tên thì không được"). A complies by leaving both rows out, or by copying the matcher into submission. B complies by keeping the matcher private.
  - Worse, AD-11 and FR-58 require the suggestion to be recomputed when groups merge, when the Cờ changes (Cờ state is a routing input, AD-18) and when the officer edits the Loại phản ánh. Merge and Cờ changes happen inside `core/lifecycle`, which may not import modules.
  - The category edit (FR-58, B) also has to write `report.categoryId`, which belongs to A's table.
  - Result: nobody computes the suggestion at submit time, and it goes stale after every merge or Cờ change. The Hàng chờ filter "Đơn vị chủ trì gợi ý" (FR-13) and SM-R6 (FR-38) then read wrong data.
- **Fix (dependency rule, AD-12, AD-18):**
  - Modules never import modules; anything that two modules or lifecycle need lives in core. Move the routing matcher to `core/routing`, and have lifecycle recompute the suggestion in every command that changes membership, category or Cờ state. Keep `routing_suggestion` append-only and tagged with the rule-set version. The latest row is the suggestion; the "final list" for SM-R6 is derived from the Nhiệm vụ created, not stored.
  - Make "AI pending" derived: the AI job selects reports in `SUBMITTED` groups that have no current attempt, so submission writes no `ai_analysis` row.

### 2. Lifecycle is unowned and bounded by column, so `task` and `report_group` have 2–3 writers — Critical

- **Units:** Leader, C and B, each writing different columns of the same rows:
  - Leader: casework FR-22 changes the deadline, FR-19 sets `finalPriority`, FR-18 transfers `ownerOfficer`, and intake sets the representative report.
  - C: assignment FR-23 creates the task and its deadline, `POST /assignee/tasks/:id/read` writes `readAt` (AD-20), and jobs write the reminder markers (AD-13).
  - B: FR-52 un-hold sets a new deadline and restores the pre-hold status, and Cờ confirmation sets `ownerOfficer`.
- **Scenario:** AD-7 only forbids modules from writing "cột trạng thái, quan hệ Phản ánh với Nhóm, quyết định trên Đề xuất gom, hay Cờ". The following writes are therefore all legal:
  - Leader's casework updates `task.deadline` directly, without the group lock.
  - B's `removeFlag` in lifecycle sets `task.deadline` and restores the pre-hold status under the lock.
  - C's sweep writes `remindedDeadline` on the same row.
  - `readAt` is written both by modules/tasks and by lifecycle (AD-20).

  Officer X un-holds T and sets deadline D2 while officer Y's casework edit writes D3. The last write wins, and the reminder marker is compared against whichever value survived. The Conventions also say "Mỗi bảng có đúng một module ghi", while the ownership table splits `task` and `report_group` by column, so the spine contradicts itself. With M2 open, all five owners will add their own commands to one transition table in parallel PRs.
- **Fix (AD-7, ownership table, M2):** `core/lifecycle` is the only writer of every column of `report_group`, `task`, `task_member`, `hazard_flag`, `hazard_source` and `merge_proposal`, including deadline, recipient and members, `readAt`, `ownerOfficer`, `finalPriority`, the representative report and the reminder markers. Modules own controllers, read queries and their own child tables, and change these rows only through named lifecycle commands. Close M2 before sprint 1 by naming one owner of `core/lifecycle` (Leader, who owns most §4.1 rows); that owner reviews every command PR.

---

## High

### 3. Late or repeated AI results land on a group that has changed — High

- **Units:** D (`modules/analysis` and the AI job), Leader (intake: merge, reject, receive) and B (hazard).
- **Scenario:** FR-12 explicitly lets officers act while a report is "đang phân tích", so late results are routine.
  - **(a) Late hazard on a rejected report.** The officer rejects R, which becomes a hidden singleton group in `REJECTED`. The in-flight result carries a hazard label. §4.1 sets no group-state precondition for an AI-sourced Cờ, so lifecycle creates a `PENDING` Cờ on the `REJECTED` group. The polled Cảnh báo đỏ (AD-10) now points at a group that the `/officer` scope hides (AD-15). Nobody can confirm or remove it, so the banner stays forever.
  - **(b) Proposal to a merged-away group.** The result proposes R→G3, but G3 has meanwhile been merged into G4 and is now a tombstone. The ownership table lets `modules/analysis` insert proposals directly, contradicting AD-11's "qua lifecycle", so there is no lock or state check. Under FR-52, the pending proposal locks confirm and remove on R's `PENDING` Cờ. If an officer confirms the proposal, R moves into the hidden tombstone and disappears from every list.
  - **(c) Duplicate results.** A timed-out attempt is retried and both responses arrive. This creates two AI hazard sources. If the officer removed the Cờ between the two, the second result raises it again and puts the tasks back On Hold (FR-51, "nguồn mới").
- **Fix (AD-11, AD-12, ownership table):**
  - Applying an AI result is one lifecycle command. It locks the report's current group and the target group, and accepts only the latest attempt, once. It creates a proposal only if the report is still alone in a `SUBMITTED` group and the target is open and not merged away. It creates or extends a Cờ only on groups in `SUBMITTED`, `RECEIVED` or `IN_PROGRESS`.
  - Every merge, split and reject drops pending proposals that touch the moved report or the merged-away group. Remove "đề xuất mới trong merge_proposal" from `modules/analysis` in the ownership table.

### 4. A merged-away group stays `SUBMITTED` and still accepts commands — High

- **Units:** Leader (intake merge) and any other command owner (receive, B's manual Cờ, C's assign); two officers working at the same time.
- **Scenario:** FR-14 only merges a `SUBMITTED` source. AD-7 keeps the empty group with `mergedIntoId` and leaves its status unchanged; the group enum in Conventions has no terminal value for it.
  1. Officer X merges G1 into G2.
  2. Officer Y, on a stale G1 page, clicks "Tiếp nhận".
  3. Lifecycle locks G1, finds `SUBMITTED→RECEIVED` valid, receives an empty group and makes Y its Cán bộ phụ trách.
  4. Y sets a Mức cuối and assigns a Nhiệm vụ to a group with no reports. The assignee opens a task with no photos and no location.

  Every step obeys the ADs.
- **Fix (AD-7):** Merging sets the source group to a terminal internal status `MERGED`, declared in the contracts enum and never shown to residents. Every lifecycle command on a `MERGED` group returns 409 `GROUP_MERGED` with the target id.

### 5. Each command implements the derived group transitions itself, so groups get stuck In Progress — High

- **Units:** Leader (approve, FR-30), C (decline review FR-28, cancel FR-43) and B (external result FR-59, Cờ removal FR-52, FR-55).
- **Scenario:** §4.1 attaches In Progress→Completed to FR-30 and FR-59 (FR-43 adds it in prose). C implements FR-28 "chấp nhận lý do" by closing the task; that §4.1 row has no group consequence.
  - **Accepted decline.** A group has T1 Approved and T2 Declined. The officer accepts T2's reason. Every task is now closed, at least one is Approved and the group is not hazardous, so it should be Completed. It stays In Progress: residents never get the result notice, `citizenAnsweredAt` is never written, and no command can complete the group.
  - **Removed confirmed Cờ.** Confirming the Cờ cancelled the only open task; later B's "gỡ Cờ Đã xác nhận" runs. §4.1 only says "Nhóm quay về luồng thường", so the group again stays In Progress.
  - **Received→In Progress** is spread across four commands owned by three people (FR-26, FR-28, FR-59, FR-52).
- **Fix (AD-7):** The two derived group transitions are evaluated by one `settleGroup` step that ends every lifecycle command, and no command implements them itself:
  - Received→In Progress when any Nhiệm vụ is Accepted or a Cờ is confirmed.
  - In Progress→Completed under the §4.1 conditions, including `citizenAnsweredAt` and the result notifications.

### 6. Nobody owns the transaction, so module writes and lifecycle commit separately — High

- **Units:** Leader (acceptance inserts the `evidence` row and its images, then calls `lifecycle.submitEvidence`) and whoever writes lifecycle. B's hazard report (photo and note) and the casework field notes have the same shape.
- **Scenario:** AD-7 says each lifecycle command "chạy trong một giao dịch". It does not say the caller's writes share that transaction. In Drizzle, a command that calls `db.transaction()` opens a separate transaction on another pooled connection unless it is passed the caller's `tx`.
  - **Lifecycle commits, module write fails.** Leader inserts Evidence in its own transaction. Lifecycle's transaction commits task→`SUBMITTED`. Leader's transaction then fails on an expired `uploadId`. The task is `SUBMITTED` with no Evidence: Mốc đã xử lý (derived from Evidence, AD-20) is empty, the officer approves without an after-photo, and the Completed notice to residents (FR-30) has no photo.
  - **Module write commits, lifecycle fails.** In the reverse order, the Evidence row is committed while lifecycle returns 409 for `ON_HOLD`.
- **Fix (AD-7):** The controller opens exactly one transaction through a shared core helper, and every lifecycle command and module write takes that `tx` as its first argument. Lifecycle locks and checks first, and the module writes in the same `tx` afterwards. Nothing below a controller opens a transaction.

### 7. Purge follows a closed list and misses copies the spine itself creates — High

- **Units:** C (the purge job) against the owners of other copies:
  - A: the reverse-geocoded address (AD-21) and idempotency records (AD-19).
  - Leader: supplement answers, text and photos (FR-21).
  - D: the raw `ai_analysis` result (AD-11 "lưu nguyên kết quả").
  - `core/notification`: prose stored at insert time.
  - B: `routing_suggestion` reasons such as "từ khóa: karaoke".
- **Scenario:** AD-15's purge deletes "file; mô tả và tọa độ chính xác; kết quả và dấu vân tay AI của ảnh đó", and C implements exactly that list. The following survive:
  - The address string that AD-21 stores on the Report. It is the exact location in words, which contradicts FR-36 and FR-41.
  - A resident's supplement answer text and photos. This is reachable: answer while the group is Received, split to `SUBMITTED` (FR-14), then reject (FR-17).
  - The raw `ai_analysis` JSON, including per-image fingerprints. D's comparison set may keep reading them.
  - The idempotency record's stored first response body (AD-19, "trả lại kết quả đầu tiên"), which contains the description and coordinates.
  - Any prose a command wrote into its notification rows.
- **Fix (AD-15):** Define purge by ownership, not by a list. Every module that holds report-derived data exposes `purge(reportId)`, which removes every free-text, location (including address) and file field it holds for that report, including supplement answers and raw AI results. The purge job calls all of them. Idempotency and notification rows may hold only ids, codes and status values.

### 8. "Row scope filters hidden data" removes rows that must stay visible; a stateful reveal leaks to WARD_LEADER — High

- **Units:** The author of the per-prefix row-scope functions (core), A (resident tracking, FR-31 and FR-17), D (insights, FR-36 and FR-37) and Leader (FR-41 reveal).
- **Scenario:** AD-15 says "Hàm phạm vi dòng của mọi tiền tố lọc dữ liệu đang ẩn". Read literally, as a row-scope function, it adds `hidden_at IS NULL` on reports.
  - **Resident.** The rejected report disappears from the resident's list, so they never see the rejection reason. FR-17 and FR-41 require that they do.
  - **Insights.** D's dashboard loses the rejected counts (FR-37) and the dots by Khu vực (FR-36). To get those numbers back, D bypasses the scope with a raw query, and now a drill-down returns hidden descriptions.
  - **Reveal.** If Leader implements FR-41 as a stored `revealedAt` that the `/officer` scope honours, WARD_LEADER shares that same scope (AD-2) and sees revealed data, which FR-61 and NFR-4 forbid.
- **Fix (AD-15):**
  - Hiding is field-level. Rows stay in every scope, and every output schema blanks the hidden fields (images, description, coordinates, address) while category, Khu vực, reason and timestamps remain.
  - The FR-41 reveal is stateless: hidden fields appear only in the response to that POST, never in a later GET.

### 9. Idempotency records: scope, cached errors and payload drift are undefined — High

- **Units:** The author of the idempotency interceptor (core), C (the mobile evidence queue, A5) and A (the Mini App report queue).
- **Scenario:** AD-19 says "lưu khóa với ràng buộc duy nhất và trả lại kết quả đầu tiên", and the interceptor records every first result, errors included.
  - **Cached 409.** A recipient's evidence draft is sent while the task is `ON_HOLD`, so a 409 is recorded under key K. The Cờ is then removed and the task returns to Accepted (FR-52). C's queue keeps one key per draft and resends K, which returns the cached 409 forever. The draft can never be submitted, and this is the UJ-9 demo path.
  - **Global key.** The key is unique globally (AD-8), not per user and command. A client that reuses the draft id as the key for both "báo chất thải nguy hại" and "nộp Minh chứng" gets the hazard result back for the evidence call.
  - **Edited draft.** If the first attempt actually committed and the user edited the draft before retrying, the edit is silently dropped.
  - **Expired uploads.** The orphan-upload TTL (AD-13) is unspecified, while drafts keep only `uploadId`s (S8). A draft retried after the TTL fails with no specific error code.
- **Fix (AD-19, AD-8):**
  - The key is unique per (user, command). The record stores a request hash and the id of the created resource. Only 2xx outcomes are recorded, and replays re-read that resource through the normal output schema. The same key with a different hash returns 409 `IDEMPOTENCY_KEY_REUSED`, and the key check runs before any state check.
  - The orphan-upload TTL is a setting no shorter than the client draft lifetime, and an expired upload returns `UPLOAD_EXPIRED`.

### 10. Admin reaches report content through account management — High

- **Units:** B (`modules/accounts`, implementing FR-3 to the letter) and AD-4 (the `/admin` output schemas).
- **Scenario:** AD-4 strips content from `/admin`. FR-3, however, lets Admin create `WARD_LEADER` and `WARD_OFFICER` accounts and reset any officer's password. A student holding Admin creates "leader-test", or resets a real officer's password, then logs in on the web. Everything is readable through `/officer`, and every step complies with AD-2 to AD-5. The only trace is an ACCOUNT-scope history event, and the spine gives no non-admin reader for those (AD-9). AD-4's "Prevents" line, which PRD §8.1 relies on as the only safeguard, overclaims.
- **Fix (AD-4):** ACCOUNT events that create, change the role of, unlock or reset a `WARD_OFFICER` or `WARD_LEADER` account are listed read-only to every `WARD_LEADER`, and a password set by Admin must be changed at first login. AD-4 should state that it is detective, not preventive.

---

## Medium

### 11. `/files` is both role-guarded and session-less — Medium

- **Units:** The `core/auth` guard author, `core/storage`, D (the AI integration) and A (Mini App `<img>` tags).
- **Scenario:** AD-2 puts `/files` under the global prefix-to-role guard, which denies by default. AD-3 and AD-4 list `/files` among the prefixes each role may use, which implies a session check. AD-14, however, makes the URL a bearer capability, and two consumers cannot send a session: the AI Module has no account, and Mini App `<img>` tags cannot send `Authorization`.
  - **Session required.** If the guard author requires a session for `/files`, every AI download returns 401, every report ends up "chưa phân tích", and Mini App images break.
  - **Public URL.** The serializer emits the public `https://…/api/v1/files/…` URL, which the AI container can only reach by hairpinning through Caddy.
  - **Stale access.** Hidden state is checked only when a URL is issued, so a URL issued just before an image is rejected keeps working until its TTL ends.
- **Fix (AD-14, AD-2):** `/files` is the only route outside the session guard. The HMAC over (image id, expiry) is its only credential, and at fetch time it re-checks that the image is neither hidden nor purged. File URLs in output schemas and AI requests are relative paths, and each consumer prefixes its own base URL.

### 12. Jobs change tasks without the group lock, and the read clock cannot be derived — Medium

- **Units:** C (the FR-39, FR-40 and FR-63 sweeps), B (hazard hold and un-hold) and Leader (deadline changes).
- **Scenario:**
  - **(a) Conflicting pushes.** The due-soon sweep reads T (Accepted, deadline D1) holding only its advisory lock. A team member reports hazard: T goes `ON_HOLD` and the high-priority "dừng xử lý" push is committed (FR-33). The sweep then commits its "sắp quá hạn" reminder. The recipient is told both "stop" and "hurry" for the same task.
  - **(b) No stored read clock.** AD-13 defines "quá hạn đọc" as a predicate of deadline, status and the current time. FR-63, however, restarts the read clock "từ lúc trở lại" after On Hold, and no column stores when the clock restarted. C computes from `assignedAt`, so a task resumed after two days is immediately overdue-to-read and is labelled that way for leaders.
  - **(c) Lock ids.** Advisory lock ids, and whether locks are session-level or transaction-level, are unspecified. A session lock on a pooled connection can leak and silently stop a job.
- **Fix (AD-13):**
  - A job's action on a task or group is a lifecycle command: it takes the group lock and re-checks its predicate inside it.
  - The read predicate uses a stored `readClockStartedAt`, which lifecycle sets on assignment and on resume to `ASSIGNED`.
  - Jobs use `pg_try_advisory_xact_lock` with ids taken from one enum in `jobs/`.

### 13. Notification rows: unit of uniqueness, stored prose, push state — Medium

- **Units:** A (`core/notification` and the list UIs), the command authors (Leader, B, C) and C (the push job and the mobile app).
- **Scenario:**
  - **Unit of uniqueness.** AD-10 makes rows unique per (event, recipient). B's "confirm Cờ on a `SUBMITTED` group" emits three history events (Received, In Progress, Cờ confirmed), so residents get three notices for one click. A built the list assuming one per command, as AD-10's "Prevents" line suggests.
  - **Stored prose.** "Nội dung dựng ở server" does not say when the text is built. B stores Vietnamese prose in the row at insert time, while A renders text from the type at read time; the list shows the text twice or not at all. Stored prose that includes addresses escapes purge (hole 7). The Completed notice must carry an after-photo, but a stored row cannot hold a signed URL.
  - **Push state.** "Đẩy lỗi không làm đổi dòng" leaves the push job nowhere to record attempts. It either re-pushes on every sweep or adds a column that A's module treats as immutable.
  - **Device tokens.** Tokens bound per user keep receiving pushes on a phone after logout or lock.
- **Fix (AD-10):**
  - A row holds `type` (an enum in contracts), object ids and a typed params object, never prose or file keys. Text and image URLs are rendered at read time by the endpoint of each audience prefix.
  - Uniqueness is per (lifecycle command, recipient), and the notice reflects the final state.
  - The push job owns `pushedAt` and `pushAttempts`.
  - A device token is unique per token, re-bound at login and deleted at logout or lock.

### 14. History payloads are untyped and point at one object, so merge and split break timelines and metrics — Medium

- **Units:** Leader (intake events for merge, split and reject), A (the resident timeline, FR-31), D (the FR-37 and FR-38 metrics) and B (Cờ sources).
- **Scenario:** AD-9 fixes the event envelope (type, scope, group id, one object id, actor, payload) but not the payload of each type.
  - **Merge and split.** Leader logs "merged" as {group: target, object: source group}. A builds a resident's "mốc thời gian" by filtering on `groupId = current group`. A report merged in loses its milestones from before the merge, and a report split out of a Received group shows Received and then Submitted again.
  - **Cờ sources.** D counts Cờ "theo nguồn" from `payload.source`, while B wrote `payload.sources[]`.

  Each owner complies with AD-9.
- **Fix (AD-9):** The payload of each event type is a discriminated-union schema in contracts that `core/history` parses on insert. Every CASE event lists all affected `reportIds`, so per-report timelines and per-group metrics are queries over the same events.

### 15. The resident scope has no rule for result images; shared prefixes have no scope — Medium

- **Units:** A (`/resident` and the notification list), and Leader (acceptance Evidence) or B (the FR-55 closing photo).
- **Scenario:**
  - **Result images.** AD-2's resident scope is "own reports". FR-30, FR-32 and FR-55 require residents to see the lead unit's approved Evidence photo or the hazard closing photo, and those belong to Evidence or FieldNote, not to the resident's report. A widens the scope to "images of my group", and the resident now sees other senders' before-photos, which FR-31 forbids.
  - **Shared prefix.** Serving one notification table to three clients, A builds `GET /me/notifications`. `/me` is a shared prefix with no per-audience schema and no row scope, and AD-4 says only the three audience prefixes may emit image URLs. The Completed notice either loses its photo or leaks signed URLs through a prefix that ADMIN and WARD_LEADER can call.
- **Fix (AD-2):** The resident scope is the resident's own reports, plus the group's result images (approved lead-task Evidence and the FR-55 note) once the group is COMPLETED. It never includes other reports' content. Shared prefixes (`/auth`, `/me`, `/config`, `/uploads`, `/files`) never return case data or signed URLs, so notification lists live under each audience prefix.

### 16. Open supplement requests are stored state that lifecycle cannot close — Medium

- **Units:** Leader (casework owns `supplement_request`), B (FR-56 close as out of jurisdiction) and Leader's intake (split, FR-14).
- **Scenario:** FR-21 says "Yêu cầu bổ sung đang mở tự đóng khi Nhóm sang Closed". That is a consequence of a lifecycle command, but on a table lifecycle may not write (ownership table) and core may not import (diagram).
  - **Close.** B's close command complies and leaves the request open. The Mini App keeps showing "Bổ sung" on a Closed report, and A's endpoint accepts the answer.
  - **Split.** A report with an open request can be split out of a Received group into a `SUBMITTED` singleton. It then holds an open request in a state where FR-21 forbids one.
- **Fix (AD-20, derive instead of store):** A supplement request is "open" if it is unanswered and its report's group is `RECEIVED` or `IN_PROGRESS`. With no status column, there is no cascade to implement.

### 17. Setting keys and the `/config` payload are not part of contracts — Medium

- **Units:** B (the admin settings UI and the seed), C (jobs reading Hạn đọc and the reminder offsets) and the clients reading `/config`.
- **Scenario:**
  - **Key mismatch.** AD-16 says "khóa định kiểu", but the contracts list in AD-1 (schemas, state enums, roles, error codes) does not include the key registry. B seeds `readDeadlineMinutes: 240`, while C reads `read_deadline_hours` and gets `undefined`. C either falls back to a hard-coded constant, which AD-16 forbids, or computes with NaN and the FR-63 reminders never fire.
  - **`/config` shape.** No one owns the shape of `/config`. Each of the three clients guesses where the boundary, tile source, `minAppVersion`, maximum image count and consent version live, and whether residents receive the AI thresholds.
- **Fix (AD-16, AD-1):** Setting keys and their value schemas are one zod map in contracts, which `core/settings` validates on every read and write; an unknown key fails at boot. `/config` returns a projection per role, declared in contracts.

### 18. Contract drift goes undetected (AI fixtures, enum additions, old APKs, Mini App copy) — Medium

- **Units:** D's pydantic models and the zod schema in contracts; the backend and installed APKs (C); contracts and the Mini App (A, under the S7 fallback).
- **Scenario:**
  - **AI fixtures.** D adds `fingerprintVersion` to the pydantic response and to a fixture but not to the zod schema. Zod strips unknown keys (Conventions: "trường không khai báo bị bỏ"), so both fixture tests still pass. The backend stores fingerprints without a version, and AD-11 ("khác phiên bản bị coi như không có") silently turns grouping into location-only.
  - **Enum additions.** Leader adds a task status or notification type. The mobile app parses responses with the same zod enum, so an installed APK throws on the whole list until someone bumps `minAppVersion` (A7). Only the client enforces that version.
  - **Mini App copy.** If S7 forces the Mini App out of the workspace, it consumes a built copy of contracts that nobody re-publishes.
- **Fix (AD-1, A7):**
  - The AI contract is strict on both sides (zod `.strict()`, pydantic `extra="forbid"`), and the fixtures cover every optional field.
  - Clients parse response enums with an `UNKNOWN` fallback. Any PR that adds a response enum value bumps `minAppVersion`, and the backend answers 426 `APP_VERSION_TOO_OLD` to older versions.
  - A Mini App outside the workspace builds contracts from the same commit in CI.

### 19. Each client shell has several owners — Medium

- **Units:** All five owners in `apps/web`; C (the mobile shell and its A5 queue) and Leader (the FR-29 Evidence screen in the same app).
- **Scenario:** The addendum makes every owner full-stack, so groups 1, 4, 5, 6, 8, 9, 10 and 12 all add screens to `apps/web`, and groups 7, 8 and 12 add screens to `apps/mobile`. Nothing names who owns each client's HTTP layer: the `X-Client` and `X-App-Version` headers, `Idempotency-Key` generation, the mapping from error code to message, 401 handling, and the retry queue that Leader's Evidence screen depends on but C builds.
  - Two owners write two fetch wrappers. One forgets `X-Client` on non-GET requests (AD-5), so the web CSRF check rejects only that owner's screens.
  - Leader's Evidence screen keys drafts differently from C's queue.
- **Fix (Consistency Conventions):** Each client app has one shell owner who owns its HTTP client, auth handling, notification list and retry queue. Feature owners add routes and screens only, and call that client.

---

## Low

### 20. "Giờ gửi" is undefined for queued drafts — Low

- **Units:** A (the Mini App queue, AD-19), B (the routing night window, AD-18) and D (the FR-37 durations).
- **Scenario:** A resident records karaoke noise at 23:30 while offline, and the queue sends it at 07:10. A posts the draft's `createdAt`, while B's routing uses the server's receive time. Whether the night-window rule (Công an phối hợp) fires, and where the report sorts in the Hàng chờ, depends on which owner you ask.
- **Fix (AD-18):** "Giờ gửi" means the server's receive time everywhere: routing, Hàng chờ order and statistics. A capture time declared by the client is stored separately and is informational only.

---

## Attacks the spine withstood

- **Duplicate records under concurrency.** Two officers creating a second open task for the same unit, a second lead task, a second Cờ or a duplicate rating are stopped by AD-8's partial unique indexes plus the group `FOR UPDATE` lock.
- **Merge collisions.** Merging two groups that both hold tasks is impossible: FR-14 only merges a `SUBMITTED` source, so AD-8's indexes cannot collide on merge.
- **WARD_LEADER writes.** The guard allows only GET and HEAD under `/officer`, and every recorded view, the reveal and the CSV export are POSTs (AD-3).
- **Officer cookie from the Mini App origin.** `SameSite=Strict`, CORS without credentials and `X-Client` on non-GET requests block it (AD-5, AD-22).
- **Spoofed Zalo id or phone.** Only the backend exchanges tokens with Zalo Graph, and a client-sent id is never accepted (AD-6, AD-24).
- **Personal data leaving the system.** FCM payloads carry only ids and a generic title, the AI Module is internal-only, and only coordinates reach the map provider (AD-10, AD-11, AD-21, AD-22).
- **Backup restore resurrecting purged data.** Restore runs purge before the API opens, and backups expire after 14 days (AD-15). This holds only within the closed list; see hole 7.
- **Divergent derived values.** "Đang phân tích", overdue, Mốc đã xử lý and the Cảnh báo đỏ are derived rather than stored (AD-12, AD-13, AD-20), so different units cannot disagree about them. The exception is the read clock; see hole 12.
