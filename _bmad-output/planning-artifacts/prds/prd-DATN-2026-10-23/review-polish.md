# Polish — PRD WRMS (bmad-review lenses=structure,prose)

Ngày: 2026-10-23. Đọc trước: PRD giúp nhóm SEP490, GVHD và các bước UX, kiến trúc, epic chốt phạm vi WRMS. Mô hình cấu trúc: Strategic/Context (Pyramid). Thứ tự: structure rồi prose; PRD trước, addendum sau.

Bất biến đã kiểm sau khi sửa: mọi ID (FR, UJ, NFR, SM, RQ, §, số câu hỏi §14) và mọi thẻ `[ASSUMPTION]`, `[NOTE FOR PM]`, `[NON-GOAL for MVP]`, `[CXM-n]` giữ nguyên nội dung; 61 thẻ ASSUMPTION inline khớp 61 mục ở §15; tiêu đề mục không đổi. Số từ: PRD 15.203 → 15.230; addendum 852 → 878 (tăng nhẹ vì thêm tham chiếu chéo và tách câu).

## Structure — PRD (2 sửa)

| Vị trí | Sửa | Lý do |
| --- | --- | --- |
| §2, dòng CXM-2, cột "Yêu cầu mang nhãn" | Thêm §5.6, §5.7 | Mô tả §5.6 và §5.7 mang `[CXM-2]` inline nhưng bảng không liệt kê |
| §2, dòng CXM-3, cột "Yêu cầu mang nhãn" | Thêm §5.8 | Mô tả §5.8 mang `[CXM-3]` inline nhưng bảng không liệt kê |

Giữ nguyên có chủ đích: lặp lại "không gọi AI API bên ngoài" ở §5.3, §8.2, NFR-8, §9 (mỗi mục được đọc độc lập); §13 tóm tắt rủi ro; câu nhắc thuật ngữ ở §0 và §4; thứ tự FR-42..FR-44 (đã giải thích ở §0).

## Structure — addendum (2 sửa)

| Vị trí | Sửa | Lý do |
| --- | --- | --- |
| Kế hoạch dữ liệu và đánh giá, câu mở | Thêm "(thay đổi 6 ở §11 của PRD)" | Nối với danh sách thay đổi cần báo GVHD |
| Quy trình phân tích use case | Tách câu dài một đoạn thành danh sách 5 bước | Quy trình tuần tự, dễ quét hơn; "Ward Officer" đổi thành "Cán bộ phường (Ward Officer)" theo §4 |

## Prose — PRD (28 sửa)

- §0: "Khi mâu thuẫn, brief, addendum…" → "Khi có mâu thuẫn, brief, addendum của brief…" (tránh nhầm với addendum của PRD). Tương tự ở §4 câu mở.
- §2 CXM-1: thêm "cho thấy" để câu ước lượng có động từ.
- §2 CXM-2: "thu hẹp Lĩnh vực trong phạm vi còn những lĩnh vực…" → "thu hẹp Lĩnh vực trong phạm vi, chỉ giữ những Lĩnh vực…"; "có thể tích hợp" → "có thể cần tích hợp".
- §2 CXM-4: sắp lại câu giả định về người làm IT cho gọn.
- §2.2: "điểm 5/8/9" → "quyết định 5/8/9" (khớp cách gọi trong toàn PRD); "mức ưu tiên cuối" → "Mức cuối"; "hạn chót" → "Hạn chót"; bỏ "là" thừa; "Tại các FR này PRD ghi" → "Các FR này ghi".
- UJ-2: "AI gộp hai phản ánh…; anh tách thành hai nhóm" → "AI đề xuất gom…; anh bác đề xuất gom" (khớp định nghĩa Đề xuất gom và FR-10: AI không tự gộp).
- UJ-3: "trước hạn 24 giờ" → "24 giờ trước hạn chót" (bỏ nghĩa nước đôi).
- §4: "đặt mức ưu tiên cuối" → "đặt Mức cuối"; Lĩnh vực thí điểm: "gợi ý mức ưu tiên từ AI" → "Mức gợi ý".
- §5.1: "không có tự đăng ký cho cán bộ" → "cán bộ không tự đăng ký".
- FR-2, FR-7, FR-8, NFR-7: chuẩn hóa tham chiếu "câu hỏi mở N" → "§14, câu N" như phần còn lại của PRD (4 chỗ).
- FR-3: viết lại hệ quả khóa tài khoản thành câu điều kiện "Khi Admin khóa…".
- FR-9 Notes: thêm chủ ngữ "Sàng lọc".
- FR-15: tách rõ hai trường hợp (Nhóm một phần tử, Nhóm còn Phản ánh hợp lệ), giữ nguyên các lựa chọn.
- FR-34: "cán bộ" → "Cán bộ phường".
- §5.6: "tính năng này dựa trên giả định cán bộ phòng ban…" → "nhóm nghiệp vụ này giả định Cán bộ phòng ban…".
- §5.10: "nhóm này" → "nhóm nghiệp vụ này" (tránh nhầm với Nhóm phản ánh).
- FR-38: làm rõ "ghi thời điểm của lần nộp Minh chứng được duyệt, để so với Hạn chót".
- RQ-2: "nhãn của người" → "nhãn do người gán".
- §10.3: "FR chia ba tầng" → "Các FR chia thành ba tầng".
- §11: viết lại câu "thay đổi thứ bảy" để không lẫn với danh sách sáu thay đổi so với đơn đăng ký.
- §11 Vận hành: "nhận hỗ trợ" → "nhận lời hỗ trợ"; "Đây là điều kiện" → "Kế hoạch vận hành là điều kiện".
- §15: "Các mục cần phường nên đưa vào…" → "Nên đưa các mục cần phường xác nhận vào…".

Giữ nguyên có chủ đích: thuật ngữ viết thường trong UJ và §1–§3 (văn kể chuyện); bị động tự nhiên trong tiếng Việt ở §6 và §12 (đổi sang chủ động sẽ phải thêm người thực hiện mà PRD không nêu).

## Prose — addendum (5 sửa)

- Câu mở: "Chi tiết cho kiến trúc, UX và chia việc, không đưa vào PRD" → "Các chi tiết phục vụ kiến trúc, UX và chia việc mà PRD không đưa vào".
- Hướng kỹ thuật cho AI Module: "Kiến trúc chốt chi tiết" → "Chi tiết do bước kiến trúc chốt".
- Bảng kế hoạch dữ liệu: "Ảnh cùng một điểm cùng nhãn hiện trường" → "Ảnh chụp cùng một điểm mang cùng nhãn hiện trường" (khớp §6 của PRD).
- Bảng kế hoạch dữ liệu, hai dòng: viết hoa "Mức ưu tiên", "Cán bộ phường" theo §4 (cột "Đơn đăng ký ghi" giữ nguyên vì trích đơn).

## Hoãn lại (cần quyết định nội dung, không sửa)

1. SM-R4 nằm trong nhóm "Chính (cần thí điểm)" dù tiền tố R gợi ý nhóm nghiên cứu; không đổi được ID, còn chuyển nhóm là quyết định nội dung.
2. Câu 20 ở §14 gộp ba quyết định không liên quan (Cancelled, đổi SM, phản hồi sau Completed); tách ra sẽ đổi số câu hỏi.
3. Lời dẫn FR-38 hứa số liệu cho SM-R4 nhưng không có hệ quả nào cho SM-R4; thêm hệ quả là thêm yêu cầu.
4. "Nhóm phản ánh đang mở" được dùng (FR-10, FR-13, Đề xuất gom) nhưng §4 chỉ định nghĩa "Nhiệm vụ đang mở"; thêm mục thuật ngữ là thêm định nghĩa.
5. §1, việc thứ ba trong "ba việc làm tay" ("khép kín vòng báo lại kết quả") là một kết quả, không phải một việc làm tay; sửa nghĩa là phát biểu lại luận điểm.
6. Addendum, mục "Quy trình phân tích use case" là quy trình làm việc của nhóm, không phải chi tiết cho kiến trúc hay UX; giữ hay chuyển sang tài liệu khác do nhóm quyết.
