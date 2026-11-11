# WRMS

Hệ thống tiếp nhận, phân công và xử lý phản ánh hiện trường về môi trường sống tại phường Hòa Xuân. Đồ án tốt nghiệp SEP490.

## Cấu trúc monorepo

| Thư mục | Nội dung |
| --- | --- |
| `apps/api` | Backend |
| `apps/web` | Web cho Cán bộ phường, Lãnh đạo, Admin |
| `apps/mini-app` | Zalo Mini App cho Người dân |
| `apps/mobile` | App mobile cho Cán bộ phòng ban |
| `services/ai` | AI Module |
| `packages/contracts` | Hợp đồng dùng chung giữa backend và client |
| `config` | Ranh giới Khu vực, dữ liệu seed |
| `deploy` | Triển khai, sao lưu |

Các thư mục hiện chỉ có README giữ chỗ; chưa có code.

## Branch

- `main`: chỉ có code của dự án.
- `develop`: code cùng tài liệu làm việc với AI: BMAD (`_bmad`, các thư mục skill), tài liệu planning (`_bmad-output`: PRD, kiến trúc) và `HUONG-DAN-BMAD.md`.

Làm việc hằng ngày trên `develop` hoặc branch tách từ `develop`.

## Đưa code từ develop về main

Không merge `develop` vào `main`: merge sẽ kéo tài liệu AI theo. Chỉ lấy các thư mục code:

```bash
git switch main
git checkout develop -- apps services packages config deploy README.md .gitignore
git commit -m "chore: sync code from develop"
```

Lệnh này không xóa file đã bị xóa trên `develop`. Nếu `develop` có xóa file code, xóa tay trên `main` trước khi commit.
