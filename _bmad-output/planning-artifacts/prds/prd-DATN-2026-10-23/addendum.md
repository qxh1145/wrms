---
title: "Addendum: PRD WRMS"
created: 2026-10-23
updated: 2026-11-11
---

# Addendum: PRD WRMS

Các chi tiết phục vụ kiến trúc, UX và chia việc mà PRD không đưa vào. Nguồn: addendum của brief, doc WRMS – Tóm tắt nghiệp vụ, đơn đăng ký đề tài.

## Ánh xạ tính năng, nhóm nghiệp vụ và người sở hữu

Mỗi nhóm nghiệp vụ là một epic trên Jira, có một người sở hữu fullstack từ database đến giao diện (doc Tóm tắt nghiệp vụ).

| Mục PRD | Nhóm nghiệp vụ | FR | Người sở hữu |
| --- | --- | --- | --- |
| §5.1 | 1. Quản lý tài khoản, danh mục và Đơn vị xử lý | FR-1 đến FR-5 | B |
| §5.2 | 2. Gửi phản ánh | FR-6 đến FR-8 | A |
| §5.3 | 3. Phân tích tự động | FR-9 đến FR-12, FR-50, FR-60 | D |
| §5.4 | 4. Duyệt và tiếp nhận | FR-13 đến FR-18 | Leader |
| §5.5 | 5. Xử lý của cán bộ phường | FR-19 đến FR-22 | Leader |
| §5.6 | 6. Phân công nhiệm vụ | FR-23 đến FR-25, FR-43 | C |
| §5.7 | 7. Nhận hoặc từ chối nhiệm vụ | FR-26 đến FR-28, FR-42 | C |
| §5.8 | 8. Nghiệm thu | FR-29, FR-30 | Leader |
| §5.9 | 9. Theo dõi và thông báo | FR-31 đến FR-35, FR-44, FR-45, FR-61, FR-62 | A |
| §5.10 | 10. Bản đồ và thống kê | FR-36 đến FR-38 | D |
| §5.11 | 11. Tác vụ tự động theo thời gian | FR-39 đến FR-41, FR-63 | C |
| §5.12 | 12. Phân luồng, ngoài thẩm quyền, chất thải nguy hại | FR-51 đến FR-53, FR-55 đến FR-59 | B (đề xuất) |

FR-46 đến FR-49 và FR-54 đã bỏ ngày 29/10/2026.

FR-60 đến FR-63 thêm ngày 11/11/2026 theo quyết định 4, 6, 7 trong `../../chot-2026-10-29.md`; người sở hữu ghi theo nhóm nghiệp vụ, nhóm chốt lại nếu cần. Các FR này đụng nhiều nhóm: vai trò Lãnh đạo phường (FR-61; tên tiếng Anh trong PRD là Ward Leader, không phải "Leader" trưởng nhóm sinh viên ở bảng trên) cần quyền chỉ xem trên mọi API đọc mà Cán bộ phường dùng (nhóm 3 đến 10 và 12) và thêm một loại tài khoản ở nhóm 1 (B); Mốc đã đọc (FR-62) ghi ở màn hình chi tiết Nhiệm vụ của nhóm 7 (C) và hiển thị ở danh sách Nhiệm vụ của nhóm 5; FR-63 dùng chung System Timer với FR-39, FR-40.

Leader sở hữu ba nhóm (4, 5, 8). B còn một nhóm sau khi bỏ nhóm Quản lý tình nguyện viên ngày 23/10; addendum của brief ghi có thể cần chia lại việc. Nhóm 12 đề xuất giao B vì B đang ít việc nhất, nhóm chốt (§14 của PRD, câu 27). Nhóm 12 đụng vào nhóm 1 (Đơn vị xử lý FR-5, của B), nhóm 3 (nhãn ảnh FR-50, của D), nhóm 4 (Hàng chờ, tiếp nhận, của Leader), nhóm 6 và 7 (giao nhiều Nhiệm vụ song song, khóa giao việc, On Hold, của C), nhóm 8 (điều kiện Completed khi đủ mọi Nhiệm vụ, FR-30, của Leader), nhóm 9 (thông báo, của A) và nhóm 10 (FR-37, FR-38, của D); cần thống nhất giao diện giữa các nhóm này trước sprint đầu. Thay đổi lớn nhất cho mô hình dữ liệu: một Nhóm có nhiều Nhiệm vụ song song, mỗi Nhiệm vụ một Đơn vị xử lý.

## Phân luồng

Bảng quy tắc mặc định, danh mục Đơn vị xử lý và lý do thiết kế ở `../../de-xuat-phan-luong-2026-10-29.md`. Căn cứ phòng ban cấp phường ở `../../research/domain-phong-ban-ubnd-phuong-hoa-xuan-2026-10-29/research.md`. Gợi ý cách làm: một bảng cấu hình (Lĩnh vực, Loại phản ánh, từ khóa, khung giờ, Cờ nguy hại, Đơn vị) và một hàm so khớp thuần, có bộ test bảng; không cần dịch vụ riêng.

## Hướng kỹ thuật cho AI Module

Ghi lại từ đơn đăng ký và addendum của brief. Chi tiết do bước kiến trúc chốt.

- Sàng lọc: model ảnh pretrained, trả về hợp lệ hoặc gắn cờ kèm lý do.
- Gom nhóm: lọc theo vị trí và Loại phản ánh, rồi so sánh ảnh. Baseline: gom chỉ theo vị trí.
- Mức gợi ý: model ảnh pretrained nhận diện loại rác, cộng quy tắc ưu tiên do nhóm viết (độ đa dạng của rác, có rác đặc biệt hay không).
- Nhãn ảnh (FR-60, thêm 11/11): một bộ phân loại ảnh ba lớp (rác, thoát nước, khác), chạy cho ảnh của mọi Phản ánh; chỉ dùng để gợi ý sửa Loại phản ánh, không vào bảng quy tắc phân luồng. Nhận diện loại rác cho Mức gợi ý (FR-11, FR-50) là bước riêng, chỉ chạy cho Phản ánh thuộc Lĩnh vực thí điểm. Nhãn "thoát nước" chưa có dataset; nếu không tìm được thì cắt theo bước 8 ở §10.3 của PRD.
- Phạm vi theo Lĩnh vực (bảng ở §5.3 của PRD): so ảnh khi Gom nhóm chỉ chạy cho hai Lĩnh vực có AI ảnh; ba Lĩnh vực còn lại gom theo vị trí, Loại phản ánh và khoảng thời gian.
- AI Module là dịch vụ riêng, kích hoạt khi có phản ánh mới (quyết định 14). Model chạy trên server của dự án, không gọi AI API bên ngoài.

## Kế hoạch dữ liệu và đánh giá

Kế hoạch chốt ngày 23/10/2026, thay phần dữ liệu, baseline và thử nghiệm trong đơn đăng ký. Cần báo GVHD (thay đổi 6 ở §11 của PRD).

| Mục | Kế hoạch hiện tại | Đơn đăng ký ghi |
| --- | --- | --- |
| Dữ liệu huấn luyện | Dataset công khai (Kaggle, Hugging Face…) | Ảnh phản ánh thu tại Hòa Xuân, bổ sung bằng dữ liệu công khai |
| Dữ liệu đánh giá | Ảnh nhóm tự chụp ở nơi công cộng tại Hòa Xuân, mỗi điểm nhiều góc | Phản ánh thu tại Hòa Xuân, không dùng khi phát triển |
| Nhãn Mức ưu tiên | Nhóm viết tiêu chí và tự gán, GVHD duyệt tiêu chí; một người ngoài nhóm gán độc lập một phần; Cán bộ phường xác nhận nếu phường duyệt | Cán bộ phường đánh giá thủ công |
| Nhãn hiện trường và hợp lệ | Ảnh chụp cùng một điểm mang cùng nhãn hiện trường; nhóm tự dựng ảnh không hợp lệ cho tập đánh giá Sàng lọc | Ảnh phản ánh thu tại Hòa Xuân, gán nhãn loại, điểm, hợp lệ |
| Baseline Mức ưu tiên | Nhãn của nhóm; Cán bộ phường nếu có thí điểm | Cán bộ phường |
| Baseline gom nhóm | Chỉ theo vị trí | Chỉ theo vị trí (giữ nguyên) |
| Baseline thời gian xử lý | Quy trình hiện tại, chỉ khi phường duyệt và có số liệu | Quy trình hiện tại nếu có hồ sơ |

Ứng viên dataset theo nghiên cứu nền 23/10: TACO (khoảng 1.500 ảnh, rác ngoài trời), TrashNet (khoảng 2.527 ảnh nền phòng lab, 6 lớp; không phải ảnh đường phố), UrbanDumpSight (hơn 4.000 ảnh bãi rác đường phố, 2025). Chưa có benchmark trên ảnh đường phố Việt Nam. Cần kiểm tra giấy phép từng bộ trước khi dùng.

## Quy trình phân tích use case

Doc Tóm tắt nghiệp vụ mô tả cách nhóm viết use case trước khi viết SRS:

1. Mỗi người phân tích một actor; Leader và D chia đôi Cán bộ phường (Ward Officer).
2. Mọi người dùng chung một mẫu: tên, mô tả, actor khác, điều kiện trước và sau, luồng chính 3–6 bước.
3. Nhóm ghép use case trong một buổi workshop.
4. Review chéo theo cặp có tương tác: Leader với C, A với Leader, D với Leader.
5. Leader và A chốt; B đưa vào SRS; C chuyển thành story trên Jira.

Use case nên dùng thuật ngữ ở §4 của PRD.

## Mẫu biểu

Mẫu PC-01, BB-01, BB-02 và bộ ảnh nghiệm thu đã bỏ ngày 29/10/2026 cùng FR-48, FR-54 (quyết định 2, 3 trong `chot-2026-10-29.md`). Bản cũ ở `addendum.bak-truoc-phan-luong.md`.
