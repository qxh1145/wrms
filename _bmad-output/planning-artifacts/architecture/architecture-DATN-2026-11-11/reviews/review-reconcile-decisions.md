# Review: does ARCHITECTURE-SPINE honour the decision and input documents

Reviewed: ARCHITECTURE-SPINE.md (working copy, 543 lines) against chot-2026-10-29.md (sections 1, 2.2, 4, 5, 6, 7), prd addendum.md, de-xuat-phan-luong-2026-10-29.md.
Short names: chot = chot-2026-10-29.md; addendum = prds/prd-DATN-2026-10-23/addendum.md; routing = de-xuat-phan-luong-2026-10-29.md.

Verdict: A1..A7 are all answered and traceable and A2 is respected, but the spine mishandles the Zalo Mini App environment and login assumptions, flattens the per-domain AI scope into one boolean, and leaves the group-12 shared interface (lifecycle commands, table writers) unspecified.

Counts: critical 0, high 4, medium 5, low 5 (14 total).

## 1. A1..A7 check (no separate findings unless listed in section 2)

- A1, A2, A3, A4, A5, A6, A7 each have an AD or Stack row. A2 (Android first) is respected: iOS is in Deferred, FCM only, no iOS-only or APNs path.
- No answer conflicts with the notes column. Remaining nits are F12 and F15.

## 2. Findings

### F1 (high) Demo environment contradicts Mini App Development/Testing limits and decision 11
- Source: chot decision 9 (Dev/Testing build, demo account must be Developer/Admin), decision 11 (demo first, no go-live), section 4 (Dev/Testing opens only for Developer/Admin; deploy quota 300/month Development, 60/month Testing).
- Spine: Structural Seed, environment table, row `demo`: "Mini App bản Development hoặc Testing ... Nơi duy nhất có dữ liệu thật khi thí điểm"; AD-6 (accounts created for any successful exchange).
- Problem: real residents cannot open a Development/Testing Mini App, so the spine's pilot-with-real-data claim contradicts section 4 and decision 11; the Developer/Admin restriction and deploy quotas are not mentioned anywhere (ignored).
- Fix: state that demo users must be Developer/Admin of the Mini App, move "real data / pilot" to a published Mini App gated on OA/KYB (Deferred row), and add the 300/60 deploy quota to the risks.

### F2 (high) Login depends on an unchecked path and drops the alternative the source offers
- Source: chot section 4 (identity via `getUserID`, OR `getAccessToken` + `graph.zalo.me/v2.0/me` + `appsecret_proof`); spike list covers only upload, `getLocation`/`getPhoneNumber`, tunnel.
- Spine: AD-6 (only `getAccessToken` + `/v2.0/me`; forbids `getUserID` ids), AD-24 header claim that each check has a fallback inside four touch points; risks S1..S9.
- Problem: S1..S9 never check that `getAccessToken` (and its consent prompt) works on an unreviewed Development app, yet every FR depends on it; AD-6 forbids the only other path in chot, so AD-24's "every spike dependency has a fallback" is false for authentication. S4 covers only `appsecret_proof`.
- Fix: add a check S10 (`getAccessToken` + `/v2.0/me` on Development build, consent behaviour) with a stated fallback (for example `getUserID` accepted only behind a demo flag in `integrations/zalo`), and say that AD-6 assumes this check passes.

### F3 (high) AI scope per domain collapsed into one boolean
- Source: chot decision 22 (drainage: image labels + image comparison only; Mức gợi ý only for waste); addendum "Hướng kỹ thuật cho AI Module" (labels for all reports; waste-type recognition only for pilot domain; image comparison only for two domains, other three group by location + type + time).
- Spine: AD-11 request ("có thuộc Lĩnh vực thí điểm không"), AD-16 (3) "mã Lĩnh vực thí điểm" as deployment config.
- Problem: three different domain scopes (labels: all; image comparison: waste + drainage; priority: waste) cannot be expressed by one "is pilot" flag, and nothing says the backend omits image fingerprints from the comparison set for the three non-image domains.
- Fix: put per-domain capability flags (`imageLabels`, `imageCompare`, `priority`) in the catalog or config, have the backend send them in the AD-11 request, and state that non-image domains group by location + Loại phản ánh + time window.

### F4 (high) Group-12 shared interface not actually specified; core ownership open
- Source: addendum ("cần thống nhất giao diện giữa các nhóm này trước sprint đầu", groups 12 touching 1,3,4,6,7,8,9,10; owner table: group 12 B proposed, groups 6/7/11 C, group 9 A).
- Spine: AD-7 (all state change via `core/lifecycle`), "Ai ghi bảng nào", Capability map rows 3, 9, 11, 12, open point M2, Deferred row "từng endpoint, từng schema".
- Problem: the shared mechanism exists but its interface (the list of lifecycle commands, their inputs and consequences) is not enumerated and M2 says nobody owns `core/`; the writer table omits `task` content, `task.readAt` (AD-20 writes it from `tasks` and from lifecycle), `deadline`, `group.citizenAnsweredAt`, and Task creation, so `task` has unassigned or multiple writers, contradicting "mỗi bảng đúng một module ghi". Row 12 also maps `core/lifecycle` to group 12 only, and `jobs` appears under both groups 3 and 11.
- Fix: add a lifecycle command list (name, caller module, state changes, side effects) and a complete writer row for every table, and name an owner for `core/` and `jobs/` before sprint 1.

### F5 (medium) "Đã trả lời công dân" is automatic, so decision 7 cannot be measured or nagged
- Source: chot decision 7 (track assignee: read, handled, answered citizen; overdue gets a reminder); routing section 1 item 4 (lead unit is the contact point); chot question 8 open.
- Spine: AD-20 (`group.citizenAnsweredAt` set by lifecycle when the result notification row is inserted), AD-13, M7.
- Problem: the milestone is stamped by the system at COMPLETED/CLOSED, so it is always on time and no person ever "answers"; the lead unit's role as responder is not modelled.
- Fix: either mark this as a known reduction of decision 7 in Open points, or add a person-attributed answer command by the lead Task recipient or `ownerOfficer`, with a Hạn for it that jobs can remind on.

### F6 (medium) Mini App size limits (10 MB app, 3 MB per file) not budgeted or checked
- Source: chot section 4 (10 MB / 3 MB limits).
- Spine: Stack (MapLibre GL JS 6 in Mini App, zod 4 contracts, zmp-ui, React 18), risks S6/S7; no mention of the limits.
- Problem: the constraint is ignored; MapLibre GL plus zod and zmp-ui in one bundle may breach a single-file 3 MB cap, and no check or fallback covers it.
- Fix: add a bundle-size check (S10-style) with code splitting or Leaflet as the fallback, and keep the boundary GeoJSON served from `/config` rather than bundled.

### F7 (medium) Several unverified Zalo facts are written as invariants; fallbacks escape AD-24
- Source: chot section 4 (CORS origin `h5.zdn.vn`; spike not done).
- Spine: AD-22 ("mọi Mini App của Zalo dùng chung origin đó", origin not named), AD-21 and Stack (MapLibre in Mini App) vs S5 and S6; AD-24 header claim "mỗi điểm có phương án dự phòng nằm gọn trong AD-24"; S6, S7, S8.
- Problem: AD-22 and AD-21 state as fact what S5 and S6 say is unchecked; the fallbacks for S6 (Leaflet, breaks AD-21's "một họ thư viện"), S7 (move `apps/mini-app` out of the workspace) and S8 (draft behaviour, AD-19) are not inside the four AD-24 touch points, so the claim is false; CORS allowed headers (`Authorization`, `X-Client`, `X-App-Version`, `Idempotency-Key`) are not stated although all trigger preflight.
- Fix: mark AD-21, AD-22 and the Stack map line `[ASSUMPTION pending spike]`, name `https://h5.zdn.vn` in AD-22 as the provisional origin, list the allowed headers, and reword the AD-24 claim to list which fallbacks are outside it.

### F8 (medium) Label-driven category correction (FR-60) has no mechanism
- Source: addendum (labels only to suggest fixing Loại phản ánh, not routing input); routing section 3 notes (suggest category fix, then rules re-run).
- Spine: AD-11 (labels stored; "tính lại Gợi ý phân luồng qua lifecycle"), AD-18 (labels not an input), Consistency rule "Giá trị của AI và của người lưu cột riêng", "Ai ghi bảng nào" (`routing_suggestion` written by `modules/routing`).
- Problem: there is no `suggestedCategory` column or event, no trigger that recomputes routing after an officer accepts a corrected category, and AD-11 says lifecycle recomputes routing while the writer table says `modules/routing` does.
- Fix: add a suggested-category field (separate from final) and name the command that applies it and re-runs the AD-18 function; fix the writer of `routing_suggestion`.

### F9 (medium) Routing function misses the default-lead rule and several inputs of the rule table
- Source: chot decision 12 (KTHTDT lead by default); routing section 3 ("Luôn luôn" rows, "không khớp quy tắc nào thì chỉ đi KTHTDT", keyword matching on normalised text, night window 22:00-06:00).
- Spine: AD-18, AD-16 settings list.
- Problem: no home for the default lead unit or the unconditional and fallback rows; AD-18 normalises the description but not the stored keywords; a Nhóm has several Reports and the function does not say which description and send time apply; a window that crosses midnight is not mentioned.
- Fix: state the default lead as a setting or a rule row type, specify keywords stored normalised, define Nhóm-level aggregation of descriptions and times, and add a midnight-crossing test row.

### F10 (low) AD-3 contradicts itself on what a Leader can POST
- Source: chot decision 6 (Lãnh đạo chỉ xem); addendum FR-62 owner group 7 (C).
- Spine: AD-3 (Leader GET/HEAD only under `/officer`, yet lists POST commands "Mốc đã đọc (FR-62)", mở/đóng chi tiết FR-38, mở lại FR-41, xuất CSV FR-38), AD-20 (`/assignee/tasks/:id/read`).
- Problem: AD-3 lists the read-mark as a Leader-view POST while AD-20 puts it on `/assignee`, and a Leader cannot call any of the other listed POSTs, so Leader views and exports are undefined for FR-38.
- Fix: state which of those commands the Leader may call (carve-out) or that Leader views are deliberately unlogged.

### F11 (low) Mapping Mini App id to OA user_id only reserved as an empty column
- Source: chot section 5 ("giao cho kiến trúc"), section 2.2 (two different ID types).
- Spine: Deferred row 1 (`zaloOaUserId`, source "idByOA của getUserInfo"), AD-6.
- Problem: the source `idByOA` is not in any input document, is client-supplied (conflicts with AD-6's "never trust client ids"), and S9 admits ids may change.
- Fix: label the source as unverified and say it must be re-read server-side (not taken from the client) when OA is added.

### F12 (low) A7 and A3 details have no config home or token type
- Source: chot section 6 A3, A7.
- Spine: A7 row ("/config trả phiên bản app tối thiểu"), AD-16 (three config places), AD-10, Stack (`expo-notifications` + `firebase-admin`).
- Problem: the minimum app version is in none of the three config locations of AD-16, and A3 does not say the device token is the native FCM token (default `expo-notifications` yields an Expo push token, which `firebase-admin` cannot send to).
- Fix: put `minAppVersion` in AD-16 (2) and state "native device token via getDevicePushTokenAsync" in AD-10.

### F13 (low) AI trigger latency and baseline mode not stated
- Source: addendum (service triggered when a new report arrives; baseline = group by location only); PRD NFR-2.
- Spine: AD-12, AD-13, AD-11, M10.
- Problem: trigger is a sweep with no stated interval or concurrency, so NFR-2 (2 minutes) cannot be reasoned about, and no location-only baseline mode exists in the pipeline or eval.
- Fix: add the sweep interval as a setting and a `baseline` flag in the AI contract and `eval`.

### F14 (low) Mandatory photo (decision 21) not enforced in the spine
- Source: chot decision 21 (photo mandatory for every Loại phản ánh; no blur).
- Spine: AD-14, AD-16 ("số ảnh tối đa" only), Deferred (blur).
- Problem: only a maximum is configured; the minimum of one photo per Report is not stated, and unblurred photos are reachable through a bearer signed URL (R5) without a note linking the two.
- Fix: state "ít nhất một ảnh" in the AD-14 or contract rule and cross-reference R5 under decision 21.

## 3. Checked and fine (not findings)

Decisions 9 (no OA API; AD-22 outbound list), 13 (EXTERNAL mode, no account), 15 (settings), 19 (WEB_CAPTURE), 20 (GeoJSON, AD-17), 23 (CANCELLED kept, no reopen), section 5 "read on open" (AD-20), AI separate service on project server with no external AI API (AD-11, AD-22), "AI only suggests" and image label not selecting units (AD-18), config-driven units and modes (AD-16, AD-18).
