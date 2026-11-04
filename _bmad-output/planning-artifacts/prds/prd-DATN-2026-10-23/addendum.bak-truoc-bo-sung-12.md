---
title: "Addendum: PRD WRMS"
created: 2026-10-23
updated: 2026-10-23
---

# Addendum: PRD WRMS

Các chi tiết phục vụ kiến trúc, UX và chia việc mà PRD không đưa vào. Nguồn: addendum của brief, doc WRMS – Tóm tắt nghiệp vụ, đơn đăng ký đề tài.

## Ánh xạ tính năng, nhóm nghiệp vụ và người sở hữu

Mỗi nhóm nghiệp vụ là một epic trên Jira, có một người sở hữu fullstack từ database đến giao diện (doc Tóm tắt nghiệp vụ).

| Mục PRD | Nhóm nghiệp vụ | FR | Người sở hữu |
| --- | --- | --- | --- |
| §5.1 | 1. Quản lý tài khoản và danh mục | FR-1 đến FR-5 | B |
| §5.2 | 2. Gửi phản ánh | FR-6 đến FR-8 | A |
| §5.3 | 3. Phân tích tự động | FR-9 đến FR-12 | D |
| §5.4 | 4. Duyệt và tiếp nhận | FR-13 đến FR-18 | Leader |
| §5.5 | 5. Xử lý của cán bộ phường | FR-19 đến FR-22 | Leader |
| §5.6 | 6. Phân công nhiệm vụ | FR-23 đến FR-25, FR-43 | C |
| §5.7 | 7. Nhận hoặc từ chối nhiệm vụ | FR-26 đến FR-28, FR-42 | C |
| §5.8 | 8. Nghiệm thu | FR-29, FR-30 | Leader |
| §5.9 | 9. Theo dõi và thông báo | FR-31 đến FR-35, FR-44, FR-45 | A |
| §5.10 | 10. Bản đồ và thống kê | FR-36 đến FR-38 | D |
| §5.11 | 11. Tác vụ tự động theo thời gian | FR-39 đến FR-41 | C |

Leader sở hữu ba nhóm (4, 5, 8). B còn một nhóm sau khi bỏ nhóm Quản lý tình nguyện viên ngày 23/10; addendum của brief ghi có thể cần chia lại việc.

## Hướng kỹ thuật cho AI Module

Ghi lại từ đơn đăng ký và addendum của brief. Chi tiết do bước kiến trúc chốt.

- Sàng lọc: model ảnh pretrained, trả về hợp lệ hoặc gắn cờ kèm lý do.
- Gom nhóm: lọc theo vị trí và Loại phản ánh, rồi so sánh ảnh. Baseline: gom chỉ theo vị trí.
- Mức gợi ý: model ảnh pretrained nhận diện loại rác, cộng quy tắc ưu tiên do nhóm viết (độ đa dạng của rác, có rác đặc biệt hay không).
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
