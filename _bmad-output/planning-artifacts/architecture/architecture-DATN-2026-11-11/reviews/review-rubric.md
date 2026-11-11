# Review (rubric walk): ARCHITECTURE-SPINE.md (WRMS, 2026-11-11)

Reviewer scope: 8-item good-spine checklist. Line numbers refer to ARCHITECTURE-SPINE.md as read from the working directory. Stack versions were not researched; only internal consistency was checked.

**Gate verdict:** Not ready to hand to the 12 epic owners. Six high findings (a dependency diagram its own ADs break, no transaction or actor-authorization mechanism, no enforcement of the boundary rules, no schema/migration rule, and an incomplete single-writer table) must be fixed first. The rest is fixable in one revision.

**Counts:** critical 0, high 6, medium 16, low 9 (31 total).

## Checklist summary

| # | Item | Result |
| --- | --- | --- |
| 1 | Real divergence points covered | Partial. F2, F3, F5, F6, F7, F13, F14, F16, F22 are uncovered. |
| 2 | Rules enforceable and prevent their "Prevents" | Partial. AD-8, AD-9 and AD-5 are strong. AD-2, AD-3, AD-7 and the dependency rules have no enforcement mechanism (F4, F21). |
| 3 | Deferred cannot cause divergence | Fails on 3 rows (F7, F9, F15). |
| 4 | Stack versions, internal consistency | Mostly OK. Minor items in F23. |
| 5 | Capability map vs PRD | FR ranges and NFR 1..11 are complete and correct. The "Chịu ràng buộc" column is inconsistent with the ADs' Binds (F20). |
| 6 | Operational envelope | Deployment and environments are present. Secrets, migrations, CI, observability and off-host backup are silent or thin (F5, F8 to F11). |
| 7 | Internal consistency | Fails: F1, F6, F12, F13. |
| 8 | Clarity for student readers | Partial (F21, F27, F29). |

## Findings

### High

**F1. High. The dependency diagram contradicts the ADs and the Capability map.**
- Location: lines 47-64 vs AD-6 (line 98), AD-11/AD-12, Capability row 1 (line 447), AD-12 and the sequence diagram (line 355), "Ai ghi bảng nào" (lines 401-415).
- Problem: The diagram allows `core` to depend only on `contracts` and gives `modules` no arrow to other `modules`. Yet (a) `core/auth` is mapped together with `integrations/zalo` and calls Zalo Graph (AD-6); (b) AD-11 and the sequence diagram say the backend recomputes the Gợi ý phân luồng "qua lifecycle", while `routing_suggestion` is written only by `modules/routing`, so `core/lifecycle` would import a module; (c) `submission` must produce the routing suggestion in its submit transaction (AD-12), which is a module-to-module call; (d) `core/auth`, `core/lifecycle` and `core/notification` read `user`, `report`, `task` and `unit`, tables owned by `modules/*`. The paragraph at line 64 ("core không import modules hay integrations") is therefore false in practice.
- Fix: Redraw the diagram to match reality. Options: move the pure routing function and `routing_suggestion` write into `core/routing`; let `modules/accounts` own the Zalo exchange and hand the result to `core/auth`; or allow an explicit `CORE -> INT` arrow for `zalo` only. State where the Drizzle schema lives (see F5) so tables are shared by schema import, not by importing modules.

**F2. High. No rule for how a feature module and a lifecycle command share one transaction.**
- Location: AD-7 (line 108), AD-12 (line 138), AD-9, AD-10, the submit sequence diagram (line 355).
- Problem: AD-7 says each lifecycle command "chạy trong một giao dịch". AD-12 needs one transaction covering Report, Group, routing suggestion, `ai_analysis` and history. Feature writes such as the rejection reason (FR-17), Mức cuối (FR-19), a supplement request (FR-21) and a rating (FR-45) must be atomic with the transition. Two owners can implement this as nested transactions, as sequential commits, or by passing a `tx` handle, and the results are incompatible.
- Fix: Add one rule: the module service opens the transaction and passes the `tx` handle to every `core/*` command (lifecycle, history, notification, storage). Core commands never open their own transaction and never commit. Add one test that fails if a core command is called without a `tx`.

**F3. High. Who may perform a transition is not assigned to any layer.**
- Location: AD-2 (line 78), AD-7 (line 108), PRD §4.1 "Ai" column.
- Problem: The global guard checks role by route prefix only. Lifecycle "kiểm điều kiện" is not stated to include the actor. PRD §4.1 and the Người nhận / Trưởng nhóm / Nhóm xử lý rules need per-object checks: only the Người nhận accepts, declines or submits; a Nhóm xử lý member only views, except hazard reporting (FR-51); the Người nhận of a task must be on that task. Epics 6, 7, 8 and 12 will each put this check in a controller or in the service, and some will omit it.
- Fix: State that every lifecycle command takes `actor` and enforces the PRD §4.1 "Ai" column and Người nhận membership inside the command. Controllers do only the role-prefix check. Add a negative test per transition row: right state, wrong actor, expect 403 or 404.

**F4. High. The spine's central structural rules have no automated enforcement.**
- Location: dependency rules (lines 45-64), "Ghi dữ liệu" convention (line 236), AD-7 "Module tính năng không ghi cột trạng thái", Git row (line 243).
- Problem: "Không có mũi tên thì không được", "mỗi bảng có đúng một module ghi" and "module không ghi cột trạng thái" are checkable only by human review across five students and 12 epics. The only CI line is "lint, kiểm kiểu, test cho phần bị đổi". The point of a spine is that a test can tell compliant from non-compliant code.
- Fix: Add an AD or convention: the import graph in the diagram is enforced by an ESLint `no-restricted-imports` config or dependency-cruiser in CI. Table definitions are exported write-capable only from the owning module, so other modules get read-only views. CI fails on violations. Note the 5 mutating tables in `core/*`.

**F5. High. DB schema and migration ownership is not decided.**
- Location: source tree line 429 (`drizzle/` under `apps/api`), Stack (drizzle-kit 0.31), R1 (line 537), no AD or Deferred row.
- Problem: Twelve epics, five people, one schema directory. Nothing says whether there is one schema file per module or one shared file, who generates migrations, how conflicting migrations are resolved (drizzle-kit snapshots conflict on every parallel branch), whether migrations run at API start or in deploy, whether they are forward-only, and how seed relates to migration. This is the single most likely collision point in a 4-month, 5-person build and is silent in all of Decisions, Deferred and Open questions.
- Fix: Add an AD: schema files live under each owning module (`modules/<x>/schema.ts`, `core/<x>/schema.ts`) and are aggregated in one index; migrations are forward-only, generated on `main` only after merge; migrations run as a separate deploy step, not on app start. Name who resolves snapshot conflicts.

**F6. High. "Ai ghi bảng nào" is incomplete and its own exception breaks the single-writer rule.**
- Location: lines 401-415, AD-15 (line 156), AD-19, AD-20 (line 186), AD-8, FR-8/FR-18/FR-19.
- Problem: No owner is named for `task` creation and `task_member`, `task.readAt` (AD-20 says both the tasks module endpoint and lifecycle write it), `group.finalPriority` and `ownerOfficer`, `idempotency_key`, `view_log` beyond a generic row, `hiddenAt`/`purgeAfter` on `report` and `image`, and `consent` (owned by `modules/accounts` but written at submit, FR-8). The purge job (AD-15) deletes content of `report`, `image_ai_result` (owned by `analysis`) and `image` (`core/storage`), which contradicts "mỗi bảng có đúng một module ghi" unless the job calls each owner. The last row ("module tính năng tương ứng ở bảng Capability") is not a table; it points to a map that is not keyed by table.
- Fix: Replace the last row with one row per table or column group. Resolve each: assignment owns task and task_member creation, lifecycle owns state only; `readAt` is written by one function in `modules/tasks`, called by lifecycle when needed; the purge job calls owner functions (`analysis.purgeImage`, `storage.purge`).

### Medium

**F7. Medium. Command endpoint shape and list conventions are left to "per story".**
- Location: Deferred row "Tên cột, từng endpoint, từng schema" (line 486); Conventions "API" (line 233); AD-20 (`POST /assignee/tasks/:id/read`).
- Problem: AD-2 fixes prefixes, but nothing fixes how a state-changing command is expressed (`POST /tasks/:id/accept` vs `PATCH /tasks/:id {status}`), plural or singular nouns, error code when a unique index fires (AD-8), or list filter and sort parameters. The three clients are built by the same people epic by epic, so this will diverge across epics.
- Fix: Add one convention: commands are `POST /<prefix>/<resource>/:id/<verb>` mapped one to one to a lifecycle command; filter and sort use `?filter[...]` with a documented shape in `contracts`; a unique-index violation maps to 409 `ALREADY_EXISTS` or a named code.

**F8. Medium. Secrets management is not decided.**
- Location: AD-6 ("App secret chỉ có ở backend"), AD-16 (3) (line 162), AD-14 (HMAC), AD-10 (FCM), AD-15 (backup encryption), M6.
- Problem: Secrets are named (Zalo app secret, HMAC key, FCM service-account, backup key, DB password) but nowhere says where they live, that they are never in git, how they reach the container, who holds them, or how rotation works (HMAC rotation invalidates live URLs; backup key loss makes backups unreadable). M6 only asks whose name the accounts are under.
- Fix: Add one rule: secrets come only from environment or Compose secrets files outside the repo, are listed by name in `deploy/` (names only), and the backup key is held by two named people. State rotation per secret in one line.

**F9. Medium. Observability and operational alerting are Deferred but NFR-9, NFR-2 and backups need them now.**
- Location: Deferred row "Triển khai tự động, giám sát và cảnh báo vận hành" (line 484), Conventions "Log" (line 241), AD-13, AD-15.
- Problem: Nothing says who learns that the sweep jobs stopped, the nightly backup failed, the AI Module is down, or the disk is filling (the image store is a directory on the server's disk). There is `GET /health` only on the AI Module. Log destination and retention are unspecified (stdout only).
- Fix: Move a minimal slice out of Deferred: backend `/health`, each job writes a `last_run` row, backup script exits non-zero and posts to one channel, and a daily check reads these. Leave full monitoring deferred.

**F10. Medium. Backup design has gaps against NFR-11 and its own goals.**
- Location: AD-15 (line 156), deployment diagram `BK` inside `SRV` (line 321), NFR-11.
- Problem: (a) Backups sit inside the same server box in the diagram; a disk loss destroys data and backup together, and AD-15's "không có bản sao nào khác" forbids copying elsewhere. (b) NFR-11 requires "chạy thử khôi phục một lần trước thí điểm" and the spine has only the restore procedure, no drill step or owner. (c) The encryption key custody is not stated (see F8).
- Fix: Name one off-host target for encrypted backups (it still expires at 14 days, so the AD-15 retention claim holds), add "một lần chạy thử khôi phục, có người chịu trách nhiệm, trước thí điểm" to AD-15, and add the key custody line.

**F11. Medium. CI and deploy procedure are one line.**
- Location: Conventions "Git" (line 243), `deploy/` (line 440), env table (lines 338-341).
- Problem: No CI platform, no required gates beyond lint/typecheck/test, no contract-fixture test gate (AD-1 relies on it), no rule on how demo is deployed (manual `docker compose up`? from which branch?), no rollback. Only two environments exist and demo is also the only one with real data, so there is no place to rehearse a migration.
- Fix: Add to Conventions: CI platform name, required checks (including the F4 boundary check and the AD-1 fixture test on both sides), deploy = a single script from `main`, and one rule that a migration is rehearsed against a restored backup copy on a local machine only for schema, not data (see AD-15 no-copy rule).

**F12. Medium. The risk table's fallbacks break AD-21 and AD-24, and the header claim is false.**
- Location: "Rủi ro và điểm cần kiểm" intro (line 521), S3, S5, S6, S7, S8 (lines 527-532), AD-21 (line 192), AD-24 (line 210).
- Problem: The section says each fallback "nằm gọn trong các chỗ nêu ở AD-24". S6 swaps the Mini App map to Leaflet with raster tiles, contradicting AD-21 ("một họ thư viện"), and the `/config` map "style" for MapLibre is not the same kind of value as a raster tile URL. S7 moves `apps/mini-app` out of the workspace and consumes `contracts` through a build, breaking the AD-1 import rule. S5 changes backend CORS and S3 changes the dev environment; neither is in the four touch points.
- Fix: Reword the intro to "phần lớn". Add to AD-21 that `/config` returns a map descriptor `{kind: 'vector-style'|'raster-tiles', url}` so S6 is a client-only swap, and add to AD-1 how a non-workspace Mini App consumes `contracts`.

**F13. Medium. Recording of views for the success metrics is undecided, and AD-3 is incomplete about it.**
- Location: AD-3 (line 84), AD-9, FR-38 (SM-1, SM-4), Capability row 10.
- Problem: AD-3 lists POST commands only in the Leader context. FR-38 SM-4 needs "lần đầu Người gửi mở phản ánh sau khi Completed/Closed", a read by a Người dân; nothing says whether the Mini App's GET writes it (violating the spirit of AD-3 and AD-2's GET rules) or a separate POST does. The same is open for the officer open/close timing.
- Fix: State one rule for all roles: reads never write; a measured view is a POST to `/<prefix>/views` writing `view_log`, idempotent per (user, group, kind). Assign this to the owner of epic 9 or 10.

**F14. Medium. Idempotency and notification dedupe are under-specified.**
- Location: AD-19 (line 180), AD-8 (line 114), AD-10 (line 126).
- Problem: "Một bản ghi cho mỗi khóa idempotency" does not say the key is scoped by (user, endpoint), how long keys live, or what happens when the same key arrives with a different payload (return first result silently, or 422). AD-10's uniqueness "theo cặp sự kiện và người nhận" does not define "sự kiện" (history event id? a dedupe key built by the command?).
- Fix: AD-19: unique on (userId, command, key), 24 h retention, mismatched payload hash returns 409 `IDEMPOTENCY_MISMATCH`. AD-10: the unique key is `(historyEventId, recipientId)`, so a notification is always derived from one history event.

**F15. Medium. Deferred retention and deletion rows can cause schema divergence now.**
- Location: Deferred row 2 from the bottom region (line 482), AD-8, FR-3 ("chỉ khóa, không xóa"), FR-4/FR-5.
- Problem: "Xóa hoặc ẩn danh Phản ánh không bị từ chối; Người dân rút đồng ý hoặc xóa tài khoản" is Deferred, but FK behavior is decided at the first migration. The first epic to write `user` and `report` picks `ON DELETE CASCADE`, `SET NULL`, or `RESTRICT`. Catalog deactivation (retire a Loại phản ánh or Đơn vị used by existing reports) has no rule at all, and unique indexes (AD-8) interact with it.
- Fix: Decide the default now: no hard deletes of `user`, `unit`, `domain`, `category`; they get `disabledAt`; all FKs are `RESTRICT`. Leave the anonymization policy Deferred.

**F16. Medium. The device token type for push is not fixed.**
- Location: AD-10 (line 126), A3 (line 219), Stack row for `expo-notifications` (line 293), `firebase-admin`.
- Problem: A3 says the backend sends FCM HTTP v1 directly "tới token thiết bị", and the mobile stack includes `expo-notifications`. That library returns an Expo push token by default; an FCM v1 send needs the native FCM registration token. Mobile and backend owners can pick different ones and find out only at integration.
- Fix: State in AD-10 that `device_token` stores the native FCM token obtained from `getDevicePushTokenAsync`, and name the invalidation behavior on `UNREGISTERED` (delete the row).

**F17. Medium. The central module (`core/lifecycle`) has no owner, no delivery order, and no extension rule.**
- Location: M2 (line 495), AD-7, Capability rows 4 to 9 and 12.
- Problem: Seven of the 12 epics depend on `core/lifecycle`, and the spine says it must be built before feature sprints, but M2 only asks who owns it, with no default. Adding a transition (for example the open question on PRD §14 q.16, "thêm một chuyển trạng thái") requires editing one shared table, which is a merge-conflict point and a single-person bottleneck.
- Fix: Convert M2 into a decision: one named owner for `core/*`, delivered in sprint 0, with the three transition tables as data in one file and a rule that any epic adds a row by pull request reviewed by that owner.

**F18. Medium. No rate-limit or quota rule although the throttler and the 429 code are in the spine.**
- Location: Stack (`@nestjs/throttler`, line 273), Conventions "Lỗi" (line 234), AD-14, AD-5.
- Problem: `@nestjs/throttler` is named and 429 exists, but nothing says what is throttled, per what key, or that `/uploads` has a per-user quota. Uploads go to the server's own disk (AD-14), so an authenticated Zalo user can fill the disk. Orphan upload expiry (AD-14, "chưa quá hạn") has no stated default.
- Fix: Add to AD-14: per-user upload count and byte cap per day (settings), global throttle on `/auth/*` and `/uploads`, and an orphan expiry setting with a default.

**F19. Medium. AD-12 stops AI retries when the Group leaves SUBMITTED, which can silently drop hazard detection.**
- Location: AD-12 (line 138), FR-12, FR-50, PRD §8.2.
- Problem: If the AI Module is down for an hour and an officer receives the Nhóm meanwhile, retries stop. A Nhóm that never got FR-50 hazard analysis proceeds to Received, and PRD §8.2 treats missing hazard detection as the safer-default case. Check whether FR-12 accepts this.
- Fix: Keep retrying hazard detection (FR-50) until a result or a configured maximum, regardless of Nhóm status; stop only the gom nhóm and Mức gợi ý parts.

**F20. Medium. The Capability map's "Chịu ràng buộc của" column is not derived from the ADs' Binds.**
- Location: lines 445-468 vs Binds in AD-7, AD-14, AD-16, AD-19, AD-20, AD-21.
- Problem: An epic owner reads only their row. Examples: AD-19 binds FR-21 and FR-51 but rows 5 and 12 do not list it; AD-14 binds FR-51, FR-52 and FR-55 but row 12 omits it; AD-21 binds FR-42 but row 7 omits it; AD-7 binds FR-10 and FR-50 but row 3 omits it; AD-16 binds FR-13 but row 4 omits it; AD-20 binds FR-63 but row 11 omits it. Coverage of FR ranges (FR-1..63 minus 46..49 and 54) and of NFR-1..11 is complete and correct.
- Fix: Regenerate the column from the Binds fields of the ADs, or add a one-line generation check in `bmad` validation.

**F21. Medium. AD-2 and AD-3 enforcement is described but not specified.**
- Location: AD-2 (line 78), AD-3 (line 84).
- Problem: "Một hàm phạm vi dòng áp cho mọi truy vấn của nó" does not say how: a mandatory parameter on repositories, a query builder wrapper, an RLS policy? A reviewer cannot tell compliant from non-compliant code. "GET không đổi dữ liệu nghiệp vụ" is a policy; GET handlers can still write (see F13).
- Fix: Say that repository functions for prefixed reads require a `Scope` argument with no default, and that GET handlers run inside a read-only DB transaction (`SET TRANSACTION READ ONLY`) so a write attempt fails in tests.

**F22. Medium. Concurrency control covers only lifecycle commands.**
- Location: AD-7 (line 108), AD-8.
- Problem: AD-7 prevents officers overwriting each other only through the `FOR UPDATE` on lifecycle commands. Non-lifecycle updates (Mức cuối, `ownerOfficer`, catalog edits by Admin, setting edits) have no rule, so two epics will choose last-write-wins or optimistic version columns differently.
- Fix: One convention: every mutable row edited by users carries a `version` column; updates send `If-Match`-style version and return 409 `STALE_VERSION` when stale.

### Low

**F23. Low. Stack items worth verifying or tightening.**
- Location: Stack (lines 265-304).
- Problem: (a) `@nestjs/schedule 12.0.3` tracks the Nest core major while `@nestjs/throttler 6.7.1` does not; verify the former is a real published line. (b) The workspace holds three React lines (Mini App 18.2, web 19.3.1, Expo 19.3.0) plus two Vite lines in one pnpm workspace; S7 already doubts this works. (c) "TypeScript 6.0 cho mọi mã TypeScript" is not confirmed for the Mini App toolchain (zmp-vite-plugin on Vite 5.4) or for zod 4 consumption there. (d) The test runner, linter, PostgreSQL driver and the pytest/Python lint tools are not named, though Conventions require tests and lint. (e) "Ghim đúng dòng lớn" pins majors only; lockfile policy is unstated.
- Fix: Add the missing rows, state "lockfile committed, exact versions via lockfile", and add a Mini App row for the TypeScript version it actually builds with.

**F24. Low. AD-23's license allowlist leaves common cases undecided.**
- Location: AD-23 (line 204).
- Problem: Only Apache-2.0, MIT and BSD are allowed; AGPL and "giấy phép riêng" need a written decision. GPL, LGPL, CC-BY-NC and research-only weights are neither allowed nor routed to the decision path.
- Fix: State "mọi giấy phép ngoài Apache-2.0, MIT, BSD cần quyết định bằng văn bản".

**F25. Low. Path and host ambiguities between AD-2, Conventions, AD-22 and AD-11.**
- Location: AD-2 (line 78), Conventions "API" (line 233), AD-22 (line 198), AD-11 and the signed URL.
- Problem: AD-2 writes prefixes as `/resident` and `/files`, Conventions say `/api/v1` prefix, Caddy exposes `/api`. The signed `/files` URL given to the AI Module must use an internal host while URLs for clients use the public host; the spine states only one.
- Fix: Write AD-2 prefixes with the `/api/v1` base and add `FILES_INTERNAL_BASE_URL` and `FILES_PUBLIC_BASE_URL` to the deployment config list in AD-16 (3).

**F26. Low. AD-17 does not specify point-on-boundary or overlap handling.**
- Location: AD-17 (line 168).
- Problem: The ward boundary is the union of three features; a point on a shared edge or in a tiny overlap matches two `areaCode`s and the code that picks "first match" is implementation-defined.
- Fix: One line: features must not overlap; a point matching more than one takes the lowest code alphabetically; a CI check asserts non-overlap.

**F27. Low. Some rules over-specify implementation or restate PRD numbers.**
- Location: AD-5 (argon2id, 5 attempts, 15 min, 8 h restate NFR-5); AD-11 (full field list of the AI request, but both sides belong to the epic 3 owner); AD-18 ("mô tả đã viết thường và bỏ dấu"); AD-15 (what the purge keeps restates FR-41); AD-10 FCM payload keys.
- Problem: These belong in code and `contracts`, add reading load, and make a later PRD change look like a spine violation.
- Fix: Cut to the invariant (for example AD-5: "server-side session, hashed token, lock enforced in DB per NFR-5 values"); leave field lists to `contracts`.

**F28. Low. AD-3 leaves the Leader's CSV export and views ambiguous.**
- Location: AD-3 (line 84), FR-38, FR-61.
- Problem: Leader is GET/HEAD-only under `/officer`, but CSV export is a POST (AD-3 itself), so the Leader cannot export, while FR-61 does not say whether the Leader may. FR-61 also hides the red-alert strip and notifications from the Leader, which the guard does not mention.
- Fix: One sentence: the Leader has no export and no view-log writes; the red-alert and notification endpoints are not under any Leader-allowed GET.

**F29. Low. Readability for the target readers.**
- Location: AD-5, AD-11, AD-14 and AD-15 (each is one paragraph of 8 to 14 rules).
- Problem: Several rules are folded into one paragraph without numbering, so a student cannot cite "AD-14 rule 4" in review; Vietnamese prose mixes camelCase identifiers (`hiddenAt`, `purgeAfter`) inside sentences. Phrases like "quyền mang theo" and "tập quét" are unexplained.
- Fix: Split long Rules into numbered sub-rules (AD-14.1, AD-14.2) so reviews and tests can reference them, and add a two-line glossary of the few coined terms.

**F30. Low. AD-13's "ghi dấu đã làm trong cùng giao dịch" cannot hold for external pushes.**
- Location: AD-13 (line 144), AD-10 (line 126).
- Problem: A push to FCM is an external call; marking done before the call loses the push on a crash, marking after can duplicate it. AD-10 says "một lần thử" but not which.
- Fix: State at-least-once for push (mark after send; duplicates are acceptable because the client dedupes by notification id) and exactly-once only for DB rows.

**F31. Low. AD-5 lockout and client declaration.**
- Location: AD-5 (line 96).
- Problem: A per-account lock after five failures lets anyone lock out a named officer (denial of service on staff). The platform check relies on the client-sent `X-Client` header, which any caller can fake; it is a usability guard, not a security control, but the text reads as a security rule.
- Fix: Count failures per (account, source IP) with a backoff and note in the rule that `X-Client` is advisory for CSRF and wrong-platform messages only.

## Divergence points not covered by any AD, convention or Deferred row

- Transaction/unit-of-work pattern (F2).
- Actor-level authorization location (F3).
- Schema and migration process (F5).
- Command endpoint shape, list filter/sort (F7).
- Optimistic concurrency outside lifecycle (F22).
- View recording for success metrics (F13).
- Soft-delete and FK behavior for users and catalog (F15).
- Rate limits and upload quotas (F18).
- Push token type (F16).

## Items checked and found sound

- AD-8 (unique indexes), AD-9 (append-only with trigger), AD-12 (async AI) and AD-13 (sweep jobs, advisory lock) are enforceable and match their "Prevents".
- Capability map FR ranges and the NFR rows 1 to 11 are complete; FR-46..49 and FR-54 are correctly excluded.
- Cross-references between ADs, chot decision numbers (8, 9, 12, 14 to 18, 20, 24) and PRD sections were spot-checked and resolve correctly.
