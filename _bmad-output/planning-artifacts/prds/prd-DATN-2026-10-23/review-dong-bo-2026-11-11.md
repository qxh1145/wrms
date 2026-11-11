# Review: đồng bộ PRD với quyết định 1, 4, 6, 7 (11/11/2026)

Reviewer độc lập (critic) rà bản diff của `prd.md` và `addendum.md` so với `chot-2026-10-29.md`. Kết luận: **REVISE**, 1 high, 6 medium, 5 low. Mọi phát hiện đã xử lý trong cùng ngày; cột cuối ghi cách xử lý.

| # | Mức | Phát hiện | Xử lý |
| --- | --- | --- | --- |
| 1 | High | §8.1: sinh viên giữ Admin tạo được tài khoản Lãnh đạo và đọc được mọi dữ liệu, vượt rào "không tự cấp vai trò Cán bộ phường" | §8.1 cấm thêm vai trò Lãnh đạo trên dữ liệu thật |
| 2 | Medium | FR-60 chạy Nhãn ảnh trên mọi ảnh, trái câu "chỉ áp cho hai Lĩnh vực" ở §4, §5.3; addendum suy nhãn "rác" từ nhận diện rác vốn chỉ chạy ở Lĩnh vực thí điểm | §4, §5.3 viết lại: AI chỉ nhận ra hai loại hiện trường, nhưng kiểm hai nhãn trên mọi ảnh; FR-60 gắn thẻ giả định; addendum tách bộ phân loại ba lớp khỏi nhận diện loại rác |
| 3 | Medium | Nhãn ảnh vừa là điều kiện quy tắc (FR-57, FR-60, §4), vừa "chỉ gợi ý sửa loại" (FR-58, file đề xuất phân luồng §3); không quy tắc mặc định nào dùng | Bỏ Nhãn ảnh khỏi điều kiện của FR-57; chỉ còn gợi ý sửa Loại phản ánh. Sửa §4, FR-60, §10.3 bước 8, addendum |
| 4 | Medium | Mốc đã trả lời công dân không xác định khi Nhóm Completed qua FR-55 không có Nhiệm vụ, khi Nhiệm vụ chủ trì đã đóng, và khi Nhóm Closed | Mốc ghi trên Nhóm (Completed hoặc Closed), hiện ở chi tiết Nhóm và trên dòng chủ trì nếu có |
| 5 | Medium | Bỏ sót "hạn trả lời công dân" của câu 7 trong file chốt; Nghiệm thu chậm không ai được nhắc | FR-62 ghi rõ v1 không có hạn trả lời riêng (giả định); thêm vào §14 câu 33 |
| 6 | Medium | "Lãnh đạo không ghi được gì" trái FR-2 (đổi mật khẩu, hồ sơ) | NFR-4, FR-61: chỉ cấm ghi dữ liệu nghiệp vụ, danh mục, cấu hình |
| 7 | Medium | Tên tiếng Anh "Leader" trùng mã trưởng nhóm sinh viên trong addendum | Đổi thành Ward Leader; ghi chú ở §4 và addendum |
| 8 | Low | Danh sách Nhiệm vụ toàn phường cho Lãnh đạo chưa có chỗ quy định; addendum sót nhóm 3 và 12; tham chiếu sai FR-51 | FR-61 nêu rõ danh sách toàn phường; addendum sửa phạm vi; tham chiếu đổi sang FR-13 |
| 9 | Low | FR-57 vô tình cấm điều kiện Cờ nguy hại ở ba Lĩnh vực | Bỏ gạch đầu dòng đó |
| 10 | Low | FR-62, FR-63 thiếu chặt: nhãn quá hạn đọc không mất khi Nhiệm vụ bị thu hồi; 4 giờ chưa rõ giờ đồng hồ hay giờ làm việc; Nhiệm vụ trở lại từ On Hold; Mốc đã xử lý còn sót sau Cancelled; chấp nhận mà chưa có Mốc đã đọc | Viết lại các gạch đầu dòng tương ứng |
| 11 | Low | Ví dụ còn sót: §8.3 và câu 23 (đường, đèn), UJ-8 (ống cấp nước); §8.2 "cả ba thành phần"; SM-R2; "sáu thay đổi" ở §11, §13 | Đã sửa từng chỗ; UJ-8 đổi sang cá chết trên sông |
| 12 | Low | FR-60 ghi Realizes UJ-2 nhưng UJ-2 không có bước Nhãn ảnh; "người phụ trách" ở §4 viết như sự thật; "Mốc chưa đọc" là khoảng thời gian trong khi các "Mốc" khác là thời điểm; số quyết định ở §11 thiếu "ngày 29/10" | UJ-2 thêm một bước; §4 trỏ về giả định ở FR-62; đổi tên thành Hạn đọc; thêm hậu tố |

Câu hỏi reviewer để ngỏ: nhãn "thoát nước" có thể bật trên ảnh kênh mương ô nhiễm, nhãn "rác" trên ảnh đốt rác. Đã ghi vào Notes của FR-60 và §14 câu 30.

Đã kiểm, không có vấn đề: 11 thẻ giả định mới lúc rà đều có dòng ở §15 (sau khi sửa theo review là 12); nhãn CXM khớp bảng §2; dải FR-1 đến FR-63, bảng ánh xạ addendum, §14 câu 30 đến 33 và các tầng §10.3 nhất quán; FR-63 khớp FR-39, FR-40, FR-59.

Chưa làm: lượt polish toàn văn (structure, prose) và lượt rà lại sau khi sửa theo review.

## Rà lại sau khi sửa (11/11/2026)

Reviewer rà lại 12 phát hiện: 1 đến 7, 9, 11, 12 đã xong. Còn ba điểm nhỏ, đã sửa tiếp:

- §10.1 và mô tả §5.3 còn ghi Nhãn ảnh "chỉ cho hai Lĩnh vực": viết lại thành hai giá trị, kiểm trên ảnh của mọi Phản ánh.
- "Danh sách Nhóm nguy hại" chưa được định nghĩa ở đâu: thêm định nghĩa vào FR-13 (giả định, có dòng ở §15).
- FR-63: một lần nhắc so với Hạn đọc tính lại sau On Hold: ghi rõ không nhắc lần hai.

Ba điểm sửa cuối này chưa qua lượt rà độc lập.
