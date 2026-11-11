# Hướng dẫn làm việc với BMAD sau khi pull dự án

Dành cho thành viên nhóm WRMS vừa clone hoặc pull repo này. BMAD đã cài sẵn trong repo (bản 6.12.4, hai module `core` và `bmm`), bạn không phải cài lại.

## 1. Cần có trên máy

- Git.
- [uv](https://docs.astral.sh/uv/): các script của BMAD chạy bằng `uv run`. Kiểm tra: `uv --version`.
- Một trong các công cụ AI mà repo đã cấu hình skill: Claude Code, Codex, hoặc Antigravity.

## 2. Việc làm một lần sau khi clone

File cấu hình cá nhân bị gitignore (`*.user.toml`), nên máy bạn chưa có. Thiếu file này, BMAD gọi bạn là "BMad" và nói tiếng Anh.

Tạo file `_bmad/custom/config.user.toml`:

```toml
[core]
user_name = "Tên của bạn"
communication_language = "Vietnamese"
```

Kiểm tra cấu hình đã nhận:

```bash
uv run _bmad/scripts/resolve_config.py --project-root .
```

Kết quả phải có `user_name` và `communication_language` bạn vừa đặt. `document_output_language` đã là `Vietnamese` cho cả nhóm.

## 3. Repo có gì

| Đường dẫn | Là gì | Sửa tay? |
| --- | --- | --- |
| `_bmad/config.toml` | Cấu hình do bộ cài sinh ra | Không. Bị ghi đè khi cài lại |
| `_bmad/custom/config.toml` | Cấu hình chung của nhóm, có commit | Có, khi cả nhóm thống nhất |
| `_bmad/custom/config.user.toml` | Cấu hình riêng của bạn, không commit | Có |
| `_bmad/scripts/` | Script dùng chung (`memlog.py`, `resolve_config.py`…) | Không |
| `.claude/skills/`, `.agents/skills/`, `.agent/skills/` | Cùng một bộ 29 skill BMAD, mỗi thư mục cho một công cụ AI | Không |
| `_bmad-output/planning-artifacts/` | Tài liệu planning: brief, PRD, research, file chốt | Qua skill, xem mục 5 |
| `_bmad-output/implementation-artifacts/` | Story, sprint status (chưa có) | Qua skill |

## 4. Cách gọi BMAD

Mở công cụ AI ở thư mục gốc của repo rồi gọi skill theo tên. Trong Claude Code gõ `/tên-skill`, ví dụ `/bmad-help`.

Không biết làm gì tiếp: gọi `bmad-help`. Nó đọc trạng thái repo và gợi ý skill kế tiếp.

Các skill theo thứ tự của dự án:

| Bước | Skill | Kết quả |
| --- | --- | --- |
| Ý tưởng | `bmad-brainstorming`, `bmad-forge-idea`, `bmad-deep-recon` | Ghi chú, research |
| Brief | `bmad-product-brief` | `briefs/…/brief.md` |
| PRD | `bmad-prd` (tạo, sửa, validate) | `prds/…/prd.md` |
| Kiến trúc | `bmad-architecture` | Tài liệu kiến trúc |
| UX | `bmad-ux` | `DESIGN.md`, `EXPERIENCE.md` |
| Epic, story | `bmad-create-epics-and-stories` | Danh sách epic và story |
| Sprint | `bmad-sprint-planning` | Kiểm tra readiness, `sprint-status` |
| Code | `bmad-build` | Code đã review |
| Review | `bmad-code-review`, `bmad-review` | Phát hiện đã phân loại |
| Đổi hướng | `bmad-correct-course` | Đề xuất thay đổi sprint |
| Hết epic | `bmad-retrospective` | Retro |

Muốn nói chuyện với một vai: `bmad-agent-pm` (John), `bmad-agent-architect` (Winston), `bmad-agent-analyst` (Mary), `bmad-agent-ux-designer` (Sally), `bmad-agent-dev` (Amelia).

## 5. Dự án đang ở đâu

Tính đến 11/11/2026:

- Xong: brief, PRD (58 FR, 11 NFR), research phòng ban, bảng phân luồng.
- Đang làm: kiến trúc.
- Chưa có: UX, epic và story, sprint status, code.

Đọc theo thứ tự này trước khi làm gì:

1. `_bmad-output/planning-artifacts/prds/prd-DATN-2026-10-23/prd.md`. §4 là thuật ngữ bắt buộc; §14 là câu còn mở; §14.1 là câu đã chốt.
2. `_bmad-output/planning-artifacts/chot-2026-10-29.md`: sổ quyết định của nhóm.
3. `_bmad-output/planning-artifacts/prds/prd-DATN-2026-10-23/addendum.md`: chia việc theo người, hướng kỹ thuật AI.

## 6. Quy ước khi sửa tài liệu

- Sửa PRD qua `bmad-prd` (nói rõ "update"), không sửa tay rồi quên ghi lại. Skill sẽ ghi `.memlog.md` và cập nhật §14, §15.
- `.memlog.md` chỉ ghi thêm bằng script, không sửa hay xóa dòng cũ:

  ```bash
  uv run _bmad/scripts/memlog.py append --workspace _bmad-output/planning-artifacts/prds/prd-DATN-2026-10-23 --type decision --text "nội dung, kèm lý do"
  ```

- Quyết định mới của nhóm: ghi vào `chot-2026-10-29.md` (hoặc file chốt mới theo ngày), rồi mới đưa vào PRD.
- ID của FR, UJ, NFR không đổi và không dùng lại. FR mới lấy số kế tiếp (hiện tới FR-63).
- Chỗ tự suy ra phải gắn `[ASSUMPTION: …]` và có dòng trong §15 của PRD.
- Dùng đúng thuật ngữ ở §4 của PRD, kể cả trong code và story.

## 7. Quy ước git

- `git pull` trước khi chạy skill sửa tài liệu. PRD dài và các dòng rất dài, conflict khó gỡ.
- Mỗi lúc chỉ một người sửa `prd.md`. Báo nhóm trước khi sửa.
- Làm trên branch riêng, không commit thẳng lên `main`.
- Commit cả `.memlog.md` và file review đi kèm lần sửa.
- Không commit `*.user.toml`, `.omc/`, `.env`.

## 8. Lỗi hay gặp

| Hiện tượng | Nguyên nhân | Cách xử lý |
| --- | --- | --- |
| BMAD gọi bạn là "BMad", trả lời tiếng Anh | Thiếu `_bmad/custom/config.user.toml` | Làm mục 2 |
| `uv: command not found` | Chưa cài uv | Cài uv, mở lại terminal |
| Gõ `/bmad-…` không thấy skill | Mở công cụ AI sai thư mục | Mở ở thư mục gốc repo |
| Skill tạo thư mục PRD mới thay vì sửa bản cũ | Không nói rõ là update | Nêu đường dẫn `prd.md` và nói "update" |
