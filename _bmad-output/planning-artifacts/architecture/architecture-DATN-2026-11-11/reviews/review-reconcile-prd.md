# Review: Spine vs PRD (what did not land)

Reviewer: independent. Inputs: ARCHITECTURE-SPINE.md (543 lines) and prd.md, both read from the working directory. Line refs: `S:` = spine, `P:` = PRD.

Verdict: the spine covers the PRD's main invariants well (state machines, row scope, outbox, signed URLs, purge), but it drops several quiet server-side gates and privacy constraints, and a few ADs go beyond or against specific FR/NFR text.

Counts: critical 0, high 2, medium 11, low 6 (19 total).

Capability to Architecture Map: all 12 group rows match PRD section 5 grouping. No FR is in the wrong group. Wrong-trace issues are only in individual Binds lines (finding 18).

---

## HIGH

### 1. DROPPED: consent and phone are gates on submit, but no AD says the server enforces them
- Severity: high
- PRD: FR-8 (P:372-378) "Người dân phải đồng ý ... trước khi gửi phản ánh đầu tiên", "Hệ thống lưu thời điểm và phiên bản", "đổi phiên bản thì phải đồng ý lại"; FR-1 (P:296) "Người dân từ chối thì không gửi được phản ánh" (phone required); section 8.1 (P:1024).
- Spine: ER has `CONSENT` (S:371) and AD-16 lists "nội dung đồng ý và phiên bản" as a setting (S:162). AD-6 stores `phoneVerified` (S:102). Nothing says `POST /resident/reports` is rejected unless the caller has a consent row for the current version and a phone number. Capability row 2 (S:448) does not bind any consent rule.
- Problem: the legal gate (consent for the current version, phone present) exists only as data, not as a backend rule, so a client bug or a stale Mini App can submit without consent (violates AD-1's own "backend giữ mọi quy tắc").
- Fix: add an AD (or extend AD-19/AD-1) "submit command rejects with a coded 409/403 unless consent.version = current setting and phone is set"; name the error code in `contracts`.

### 2. DROPPED: separation of real data from student-held accounts / council demo
- Severity: high
- PRD: section 8.1 (P:1026) "nhóm không được cấp cho mình vai trò Cán bộ phường hoặc Lãnh đạo trên dữ liệu thật"; section 2.1 (P:79) "demo trước hội đồng bằng dữ liệu mẫu và đóng vai".
- Spine: environment table (S:340-341) has only `local` (sample data) and `demo`, where `demo` = "Nơi duy nhất có dữ liệu thật khi thí điểm". AD-4 (S:90) only protects against Admin; R3 (S:539) mentions server access only.
- Problem: the same `demo` server hosts the council demo (role-play, student officer accounts) and real pilot data, so the 8.1 rule has no architectural home and one environment cannot satisfy both uses.
- Fix: add a `pilot` (real data) environment distinct from `demo` (sample data, role-play accounts), and state in AD-15/AD-4 that no student-held WARD_OFFICER or WARD_LEADER account exists in `pilot`.

---

## MEDIUM

### 3. CONTRADICTION: officer row scope vs FR-22 / FR-62 task-list scope
- Severity: medium
- PRD: FR-22 (P:566) tasks "thuộc các Nhóm mình phụ trách"; FR-62 (P:777) "Cán bộ phường xem trong phạm vi của FR-22; Lãnh đạo xem mọi Nhiệm vụ"; FR-61 (P:761) Leader list is "không giới hạn theo Cán bộ phụ trách như ở FR-22".
- Spine: AD-2 (S:78) "officer thấy mọi Nhóm" for the single `/officer` prefix shared by WARD_OFFICER and WARD_LEADER (S:77). AD-2 Binds lists FR-22 and FR-62.
- Problem: the row-scope function has no WARD_OFFICER vs WARD_LEADER distinction for the Task list, so the PRD's narrower officer task scope (and the Leader contrast) cannot be expressed by AD-2 as written.
- Fix: state in AD-2 that the Task list scope differs by role (officer: Groups where `ownerOfficer` = self; leader: all), while Hàng chờ and Group detail stay global (FR-18, P:526).

### 4. CONTRADICTION: Leader can read Cảnh báo đỏ and notification endpoints
- Severity: medium
- PRD: FR-61 (P:764) "Lãnh đạo không nhận thông báo và không thấy dải Cảnh báo đỏ trong v1".
- Spine: AD-3 (S:84) lets WARD_LEADER call every GET/HEAD under `/officer`; AD-10 (S:126) says the red alert is "web hỏi định kỳ danh sách Cờ PENDING" and that Cán bộ phường have web notifications. No exclusion for the Leader.
- Problem: the alert feed and officer notification list are `/officer` GETs, so the AD-3 guard admits the Leader, and nothing stops the notification command from generating rows for Leader accounts.
- Fix: in AD-3 list the `/officer` GET routes the Leader may not call (alert feed, notification list); in AD-10 restrict recipients to WARD_OFFICER (and Cán bộ phụ trách).

### 5. CONTRADICTION: AD-15 bans rejected data from "any export" but FR-37/FR-38 need it counted
- Severity: medium
- PRD: FR-37 (P:795, 800) stats include "phản ánh bị từ chối" and "Số liệu phản ánh bị từ chối vẫn đúng sau khi dữ liệu chi tiết đã bị xóa"; FR-38 (P:812, 809) logs view times "trước khi tiếp nhận hoặc từ chối" (SM-1) and exports history for SM-R4; SM-C1 (P:1165) counts rejection rate. FR-41 (P:864) only forbids use as training/evaluation data.
- Spine: AD-15 (S:156) "Phản ánh bị từ chối và ảnh bị loại không có trong bất kỳ tệp xuất nào".
- Problem: read literally, rejected Reports vanish from the CSV and history export, which biases SM-1, SM-C1 and SM-R4; the PRD only forbids their content (image, description, precise coordinates) in datasets.
- Fix: reword AD-15: no image, description or exact coordinates of hidden or purged data in any export; ids, counts, reasons, timestamps and Khu vực stay exportable.

### 6. DROPPED: SM-4 resident "first open" measurement vs "GET never writes"
- Severity: medium
- PRD: FR-38 (P:815) "Ghi lần đầu Người gửi mở phản ánh sau khi phản ánh sang Completed hoặc Closed (SM-4)".
- Spine: AD-3 (S:84) "GET không đổi dữ liệu nghiệp vụ, không ghi lịch sử, không ghi số đo"; its list of POST recording commands covers only officer-side views (FR-38 open/close detail, FR-41, CSV). `VIEW_LOG` is mentioned (S:399) but no resident-side writer.
- Problem: the natural implementation (record on GET of the resident detail) is forbidden by AD-3, and no explicit resident command exists, so SM-4 has no capture path.
- Fix: add a resident-side `POST` (e.g. mark-viewed) in AD-3/AD-20, or scope the "GET never writes" rule to WARD_LEADER only.

### 7. CONTRADICTION: bearer signed URLs vs NFR-5 "đường dẫn có kiểm tra quyền"
- Severity: medium
- PRD: NFR-5 (P:1010) "Ảnh chỉ tải được qua đường dẫn có kiểm tra quyền, không có đường dẫn công khai"; NFR-4 (P:1009) Admin and other roles must not read images.
- Spine: AD-14 (S:150) the URL "là quyền mang theo: ai có URL còn hạn thì tải được"; R5 (S:541) records it as a risk, not as a deviation from NFR-5.
- Problem: permission is checked only at issuance; a URL leaked through a screenshot, proxy log or chat is readable by anyone, including a role that NFR-4 excludes, until it expires. The deviation from NFR-5 is not flagged.
- Fix: keep unauthenticated signed URLs only for the AI Module (internal network); for clients require the session (cookie or Bearer) on `/files/:id` plus the signature, or explicitly list this as an accepted deviation of NFR-5 with the maximum lifetime stated.

### 8. CONTRADICTION: "hidden" row filter in every prefix vs reason that must stay visible
- Severity: medium
- PRD: FR-17 (P:518) and FR-31 (P:692) the resident sees the rejection reason, also after deletion (FR-41, P:861); FR-37 (P:800) rejected counts stay correct; FR-41 (P:859) hides only "ảnh, mô tả và tọa độ chính xác".
- Spine: AD-15 (S:156) "Hàm phạm vi dòng của mọi tiền tố lọc dữ liệu đang ẩn", with `hiddenAt` set "trên Phản ánh bị từ chối".
- Problem: a row-scope function removes rows, so the rejected Report (status, reason, Khu vực) would disappear from the resident list and from stats; the PRD hides fields, not the Report.
- Fix: make hiding field-level in AD-15 (projection drops description, images, exact lat/lng; row stays in scope) and say so in AD-2.

### 9. DROPPED: FR-15 and FR-21 side effects sit outside `core/lifecycle`
- Severity: medium
- PRD: FR-15 (P:499-500) cannot exclude a hazard-labelled image while the Flag is Chờ xác nhận; if all images of a Report are excluded the Group cannot be received; FR-21 (P:559) open Yêu cầu bổ sung "tự đóng khi Nhóm sang Closed".
- Spine: AD-7 Binds (S:106) omits FR-15 and FR-21; write-owner table (S:409) gives `image` to `core/storage` and `supplement_request` to a feature module. AD-7 locks the Group row only for lifecycle commands.
- Problem: image exclusion checks Flag state and Group readiness without taking the Group lock, so it can race with flag confirmation or receive; the Closed cascade to supplement requests has no owner.
- Fix: route "exclude image" and "close supplement requests on Closed" through lifecycle commands, add FR-15 and FR-21 to AD-7 Binds.

### 10. DROPPED: rule edits apply only to Groups received after the edit
- Severity: medium
- PRD: FR-57 (P:883) "Sửa bảng chỉ áp cho Nhóm tiếp nhận sau lúc sửa; Gợi ý phân luồng đã tạo không đổi"; FR-58 (P:892) suggestion recomputed on new AI result, merge, or category fix.
- Spine: AD-18 (S:174) pure function over the current rule table; AD-12 (S:138) recompute after AI result; no freeze point or rule versioning.
- Problem: as specified, any later recompute on a Received Group would use the edited table, contradicting FR-57.
- Fix: add to AD-18 that recompute stops at `RECEIVED` (or store a rule-table version on the suggestion), and say which.

### 11. WRONG IDIOM: AD-13 "once per deadline" does not fit FR-63 read reminder
- Severity: medium
- PRD: FR-63 (P:849, 851) "Mỗi Nhiệm vụ chỉ nhận một lần nhắc chưa đọc"; after On Hold return "Hạn đọc tính lại từ lúc trở lại; nếu đã được nhắc trước khi tạm dừng thì không nhắc lần hai"; label "quá hạn đọc" appears "Sau lần nhắc" (P:850).
- Spine: AD-13 (S:144) idempotence is "bằng cách lưu chính giá trị Hạn chót đã nhắc", and "quá hạn đọc" is a pure predicate with no stored column.
- Problem: the read reminder is once per Task, not per Hạn chót, and needs a resettable clock anchor and a "reminded" marker; a pure predicate would show the label before the reminder is sent and would reset wrongly after On Hold.
- Fix: add to AD-13/AD-20 two stored fields: read-clock start (reset on return from On Hold) and read-reminder-sent time; define the label from them.

### 12. DROPPED: the "Lĩnh vực có AI ảnh" scope has no home and is not in the AI request
- Severity: medium
- PRD: section 4 (P:173) and the matrix in 5.3 (P:386-393): image comparison and Nhãn ảnh scope by Lĩnh vực; FR-10 (P:418) no image comparison for the other three Domains.
- Spine: AD-11 (S:132) request carries only "có thuộc Lĩnh vực thí điểm không"; AD-16 (S:162) pins only the pilot Domain code (deployment config). The set of two image-AI Domains appears in none of the three config places.
- Problem: who decides whether `services/ai` compares images for a Report (backend flag or AI Module hard-code) is open, and the AD-11 "no divergence between runtime and offline eval" goal can be broken.
- Fix: add the image-AI Domain set to AD-16 (deployment config next to the pilot code) and pass an explicit `imageAiDomain` flag in the AD-11 request.

### 13. ASSUMPTION OVERRIDDEN: reuse of accepted images for training/evaluation (PRD open question)
- Severity: medium
- PRD: section 8.1 (P:1028) and section 14 Q10 (P:1201) leave open whether accepted reports' images may be used for training or evaluation.
- Spine: AD-15 (S:156) "Không có bản sao nào khác của dữ liệu thật: ... không xuất ảnh", while the tree has `services/ai/eval` (S:434) and AD-11 mentions "đánh giá offline".
- Problem: AD-15 decides "no" silently for accepted images (and for SM-R1 pilot comparison data) without marking it as resolving an open PRD question.
- Fix: tag it `[ASSUMPTION]` in AD-15 and list Q10 in "Điểm còn mở" (or Deferred).

---

## LOW

### 14. INCONSISTENCY: retention setting for non-rejected Reports
- Severity: low
- PRD: FR-8 (P:375) the consent text must state the retention period (24 months, temporary).
- Spine: Deferred (S:482) says "Số tháng giữ là setting", but AD-16 setting list (S:162) lacks it, and Deferred timing is "Trước thí điểm" while the consent text is needed before the first submit.
- Fix: add the retention months to the AD-16 settings and move that Deferred row's trigger to "before consent text is written".

### 15. DROPPED: catalog and account invariants that cross modules
- Severity: low
- PRD: FR-59 (P:908) an external-mode Unit cannot be Đơn vị chủ trì, but FR-57 (P:879) sets a default lead Unit per Domain; FR-4 (P:329) pilot Domain cannot be hidden; FR-3 (P:318-319) accounts with history are locked, never deleted, and the Cán bộ phụ trách is notified on lock.
- Spine: AD-8 (S:114) and AD-18 (S:174) do not state "lead must be IN_SYSTEM"; no rule on soft-hide only; lock notification is not an AD-10 event source.
- Fix: one sentence each in AD-8 (lead is IN_SYSTEM only; catalog and user rows are never hard-deleted) and AD-10 (account lock with open Tasks is a notification source).

### 16. CONFLICT: generic push title vs "thông báo ưu tiên cao" for On Hold
- Severity: low
- PRD: FR-33 (P:718) high-priority notification on On Hold with content "dừng xử lý, không tiếp xúc chất thải, rời hiện trường".
- Spine: AD-10 (S:126) FCM payload has "một tiêu đề chung" only; no priority class.
- Problem: the safety stop message is not visible on the lock screen and has no priority.
- Fix: allow a fixed, non-personal safety title and high-priority FCM delivery for the On Hold type.

### 17. SILENT NARROWING: fingerprint version mismatch disables "lặp lại"
- Severity: low
- PRD: FR-9 (P:403) "Lặp lại" = same image already in WRMS.
- Spine: AD-11 (S:132) "Dấu vân tay khác phiên bản bị coi như không có", with no re-fingerprint job.
- Fix: add a backfill job (AD-13) or state that duplicates are not detected across model versions.

### 18. WRONG TRACE (Binds lines)
- Severity: low
- AD-3 Binds FR-62 and lists "ghi Mốc đã đọc (FR-62)" among Leader-related POST commands (S:84), but that command is an `/assignee` action (AD-20, S:186), unusable by the Leader.
- AD-4 Binds `UJ-6` (S:89): a user journey, not an FR; FR-57 (Admin rule table) is not bound.
- AD-21 Binds FR-13 (S:190): FR-13's radius is a list filter (P:481), not a map feature.
- Fix: correct these three Binds lines.

### 19. WRITE-OWNER GAPS in "Ai ghi bảng nào"
- Severity: low
- Spine S:405-415 and convention "Mỗi bảng có đúng một module ghi" (S:236): `report_group` columns `finalPriority`, `ownerOfficer` and `task.deadline` have no listed writer, and `task.readAt` is written by an `/assignee` command (AD-20) while `task` is owned by lifecycle. The FR-19 precondition "có Mức cuối trước khi giao" (P:543) spans two modules.
- Fix: list a writer for each column (or state that lifecycle commands set them), and name the precondition in AD-7.
