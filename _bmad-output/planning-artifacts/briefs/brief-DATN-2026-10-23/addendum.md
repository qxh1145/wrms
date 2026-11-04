---
title: "Addendum: Product Brief DATN (WRMS)"
created: 2026-10-23
updated: 2026-10-23
---

# Addendum: WRMS

Chi tiết dành cho PRD và architecture, không đưa vào brief. Mọi quy tắc dưới đây là bản đang áp dụng, đã gồm các thay đổi chốt ngày 23/10/2026.

## Nguồn

- Đơn đăng ký đề tài SP27_WRMS (Google Doc), bản trích: `inputs/SP27_WRMS_Dang_ky_de_tai.txt`.
- [WRMS – Tóm tắt nghiệp vụ](https://claude.ai/artifact/TCo4PkJ8LG8kGYh2rBBog2): 16 điểm chốt ngày 22/10/2026, đã cập nhật theo thay đổi ngày 23/10/2026.
- Khi các nguồn mâu thuẫn, addendum này và doc Tóm tắt nghiệp vụ được ưu tiên hơn đơn đăng ký.
- Nghiên cứu nền: `inputs/research-digest-2026-10-23.md`.

## Actor

| Actor | Loại | Nền tảng | Vai trò chính |
| --- | --- | --- | --- |
| Resident (người dân) | Chính | Mobile | Đăng ký, gửi và theo dõi phản ánh, bổ sung thông tin khi được yêu cầu |
| Task Assignee (người xử lý) | Chính | Mobile | Cán bộ phòng ban của phường; nhận hoặc từ chối nhiệm vụ, nộp ảnh minh chứng. Không có tình nguyện viên |
| Ward Officer (cán bộ phường) | Chính | Web | Điều phối toàn bộ: duyệt, từ chối, gom và tách nhóm, đặt mức ưu tiên cuối, giao việc, xét lý do từ chối, xác minh và kiểm tra hiện trường, nghiệm thu cuối, xem bản đồ điểm nóng, dashboard, thống kê |
| Admin (IT của UBND phường) | Chính | Web | Chỉ quản trị hệ thống: tài khoản, danh mục, phòng ban. Không xem bản đồ điểm nóng, dashboard, thống kê |
| AI Module | Phụ | Server | Dịch vụ riêng ngoài ranh giới hệ thống |
| Notification Service | Phụ | Bên ngoài | Thông báo đẩy |
| Map Service | Phụ | Bên ngoài | Bản đồ, ghim vị trí, đổi tọa độ thành địa chỉ |
| System Timer | Phụ | Server | Cảnh báo quá hạn, xóa dữ liệu hết hạn |

## Trạng thái

- Phản ánh: Submitted → Received → In Progress → Completed. Phản ánh không hợp lệ: Submitted → Rejected (kết thúc).
- Nhiệm vụ: Assigned → Accepted → Submitted → Approved hoặc Returned. Khi Returned, người xử lý làm lại và nộp lại (Submitted); phản ánh vẫn ở In Progress.
- Nhiệm vụ bị từ chối: Assigned → Declined. Nếu cán bộ phường chấp nhận lý do thì giao lại cho người khác, nếu không thì người được giao tiếp tục.

## Quyết định nghiệp vụ

Các điểm có ghi "(đổi 23/10)" đã thay bản chốt ngày 22/10.

1. Cán bộ phường kiểm tra hiện trường và nghiệm thu, là quyết định cuối. Admin không tham gia. (đổi 23/10)
2. Có trạng thái Rejected, chỉ từ Submitted.
3. Admin chỉ có sơ đồ use case Quản trị. Toàn bộ phần Điều phối thuộc Ward Officer. (đổi 23/10)
4. Không có tình nguyện viên. Task Assignee chỉ là cán bộ phòng ban của phường. (đổi 23/10)
5. AI chỉ gợi ý mức ưu tiên, cán bộ phường đặt mức cuối. Lưu riêng mức gợi ý và mức cuối kèm người đặt; chạy lại AI không ghi đè mức đã chỉnh tay.
6. Không có bật/tắt AI. Sàng lọc và gom nhóm luôn bật; chấm ưu tiên chỉ áp dụng cho lĩnh vực vệ sinh môi trường, đặt trong cấu hình.
7. Danh mục 2 cấp: Lĩnh vực → Loại phản ánh.
8. Không có bảng SLA. Cán bộ phường đặt hạn chót mỗi lần giao việc. (đổi 23/10)
9. Không có đơn vị phối hợp ngoài phường; chỉ có phòng ban của phường.
10. Bỏ: phòng ban xử lý mặc định, workflow template, minh chứng theo loại, hiển thị công khai, hỏi đáp chính sách.
11. Người xử lý được thông báo khi: được giao việc mới, có kết quả cán bộ phường xét lý do từ chối, bị trả lại (kèm lý do), sắp quá hạn (đề xuất 24 giờ trước hạn). Quá hạn thật thì báo cán bộ phường. (đổi 23/10)
12. Người dân chỉ bổ sung thông tin khi cán bộ phường yêu cầu, và chỉ khi phản ánh ở Received hoặc In Progress.
13. Cán bộ phường theo dõi tiến độ nhiệm vụ của phản ánh mình phụ trách, được báo khi có minh chứng. (đổi 23/10: bỏ giới hạn "chỉ xem")
14. AI Module là dịch vụ riêng, chạy khi có phản ánh mới.
15. Phản ánh bị từ chối và ảnh bị loại: ẩn ngay, sau 90 ngày xóa ảnh, mô tả, tọa độ chính xác; giữ loại, lý do, thời gian, khu vực. Không giữ làm dataset. Mốc 90 ngày theo thời hiệu khiếu nại của Luật Khiếu nại 2011. (đổi 23/10: thay cho xóa sau 48 giờ)
16. Nhiệm vụ giao cho nhóm: trưởng nhóm là người nhận việc duy nhất. Cán bộ phường chọn thành viên và trưởng nhóm. (đổi 23/10)

## Nhóm nghiệp vụ

- 11 nhóm, mỗi nhóm là một epic trên Jira với một người sở hữu fullstack (Leader, A, B, C, D).
- Ngày 23/10 bỏ nhóm Quản lý tình nguyện viên (nhóm 10 cũ). Bản đồ và thống kê thành nhóm 10, chuyển sang Ward Officer. Tác vụ tự động theo thời gian thành nhóm 11.
- B mất một nhóm, có thể cần chia lại việc.

## Dữ liệu và nghiên cứu

Kế hoạch chốt ngày 23/10/2026, thay cho phần dữ liệu, baseline và thử nghiệm trong đơn đăng ký.

- Model: pretrained do nhóm tinh chỉnh, chạy trên server của dự án, không dùng AI API bên ngoài. AI lỗi thì phản ánh vẫn được nhận.
- Huấn luyện: dataset công khai (Kaggle, Hugging Face...).
- Đánh giá: ảnh nhóm tự chụp ở nơi công cộng tại Hòa Xuân, mỗi điểm nhiều góc, không dùng khi huấn luyện. Dùng cho nhận diện rác và gom nhóm.
- Nhãn mức ưu tiên: nhóm viết tiêu chí và tự gán, GVHD duyệt tiêu chí. Cán bộ phường xác nhận lại nếu phường duyệt đề tài.
- Baseline gom nhóm: so gom chỉ theo vị trí với gom theo vị trí, loại và ảnh (giữ như đơn đăng ký).
- Baseline mức ưu tiên: so với nhãn của nhóm; so với đánh giá của cán bộ phường nếu phường duyệt đề tài.
- Baseline thời gian xử lý: so với quy trình hiện tại, chỉ khi phường duyệt và có số liệu.
- Metric: độ khớp mức ưu tiên, độ chính xác gom nhóm và sàng lọc, thời gian xử lý mỗi phản ánh, thời gian từ lúc gửi đến khi hoàn thành.
- Ngưỡng của model chỉnh theo góp ý của cán bộ phường nếu có thí điểm.

## Việc cần chốt

- Báo GVHD hai thay đổi so với đơn đăng ký: bỏ tình nguyện viên, và kế hoạch dữ liệu, baseline, thử nghiệm mới.
- 16 quyết định nghiệp vụ do nhóm tự chốt, chưa có ý kiến của phường. Cần phường xác nhận, nhất là điểm 5 (ai đặt mức ưu tiên cuối), điểm 8 (hạn chót, SLA) và điểm 9 (đơn vị phối hợp).
- Khi có nhiều cán bộ phường, ai chia phản ánh cho từng người.
- Ảnh không hợp lệ để huấn luyện bước sàng lọc lấy từ đâu, vì điểm 15 không giữ ảnh của phản ánh bị từ chối.
- GVHD hoặc phường xác nhận việc từ chối một phản ánh hiện trường có thuộc diện khiếu nại theo Luật Khiếu nại 2011 không. Đây là căn cứ của mốc 90 ngày ở điểm 15.
- Ảnh nhóm tự chụp có thể có mặt người, biển số xe; cần cách xử lý theo Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15.
