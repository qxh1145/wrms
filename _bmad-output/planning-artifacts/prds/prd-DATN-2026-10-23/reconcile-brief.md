# Đối chiếu đầu vào: Brief (brief.md, addendum.md, .memlog.md) so với PRD (prd.md, addendum.md)

Ngày: 2026-10-23. Chỉ đối chiếu, không sửa PRD. Ký hiệu nguồn: B = brief.md, BA = addendum của brief, M = .memlog.md (mục theo thứ tự dòng), P = prd.md, PA = addendum của PRD.

## Kết luận nhanh

- 16 quyết định nghiệp vụ: 16/16 đã có trong PRD, đúng bản 23/10 (điểm 1, 3, 4, 8, 11, 13, 16 đều theo bản mới). Không có chỗ nào quay lại bản 22/10.
- Bốn câu "Cần xác minh": giữ đủ, có nhãn CXM-1..4 gắn vào FR/SM/NFR. Còn sót vài chỗ phụ thuộc chưa gắn nhãn (G-8).
- Khung trung thực (giả thuyết phía phường, AI chấm ưu tiên là nghiên cứu, WRMS chỉ xử lý phản ánh qua app của nó, phường chưa duyệt): có ở P §1, §6, §9, §11, §12. Nhưng bị yếu đi ở §3.1 và §3.3 (G-5).
- Bảy rủi ro, thứ tự cắt, phạm vi trong/ngoài: giữ đúng. Thứ tự cắt có hệ quả chưa nêu (G-4).
- Bị bỏ lặng lẽ: mục tiêu của nhóm "phường thật sự dùng sau bảo vệ", "tầm nhìn dài hạn chưa xác định", "không có lợi thế công nghệ độc quyền" (G-1, G-2, G-3).

## Danh sách khoảng trống

### G-1 [HIGH] Mục tiêu của nhóm "phường thật sự dùng sau khi bảo vệ" không có trong PRD
- Nguồn: B Tóm tắt đoạn 3 ("với mục tiêu để phường thật sự dùng sau khi bảo vệ"); M dòng 20 ("không chỉ đạt điểm"; brief phải trả lời ai vận hành, phường cam kết gì).
- PRD: grep "bảo vệ|thật sự|thực sự" chỉ ra "Luật Bảo vệ dữ liệu" và "Hội đồng bảo vệ". Không có câu nào nêu mục tiêu này. P §12 chỉ ghi "điều kiện đầu tiên: phường đồng ý thí điểm". P §11 nêu vận hành sau 04/2027 như một dòng chưa có kế hoạch, không gắn với mục tiêu.
- Hệ quả: PRD đọc như tài liệu cho đồ án đạt điểm; mất ý "dùng thật" vốn quyết định nhiều lựa chọn (đo bằng mức sử dụng thật, hỗ trợ sau bàn giao).
- Sửa: thêm 1-2 câu vào P §1 (hoặc §12 đầu): "Mục tiêu của nhóm không dừng ở bảo vệ đồ án: nhóm muốn UBND phường thật sự dùng WRMS sau bảo vệ và có người hỗ trợ sau 04/2027 (hiện một thành viên nhóm nhận hỗ trợ khi phường liên hệ)." Nối với §11 và câu hỏi mở 12.

### G-2 [MEDIUM] Mục "Tầm nhìn" của PRD thay cho "tầm nhìn chưa xác định" của brief
- Nguồn: B mục Tầm nhìn ("Nhóm chưa xác định tầm nhìn dài hạn. Sẽ bổ sung sau buổi làm việc với phường"); M dòng 62.
- PRD: §1 mang tên "Tầm nhìn" nhưng chỉ mô tả sản phẩm hiện tại; không nói tầm nhìn dài hạn còn bỏ ngỏ. Hạng mục "deferred vision" bị mất, người đọc sau (UX, kiến trúc) có thể coi §1 là tầm nhìn đã chốt.
- Sửa: đổi tên §1 thành "Tổng quan sản phẩm" hoặc thêm một câu cuối §1 và một mục trong §14: "Tầm nhìn dài hạn chưa xác định; bổ sung sau buổi làm việc với phường (theo brief)".

### G-3 [MEDIUM] Bỏ mất định vị trung thực "không có lợi thế công nghệ độc quyền"
- Nguồn: B Điểm khác biệt ("WRMS không có lợi thế công nghệ độc quyền. Lợi thế dự kiến là thiết kế sát quy trình của một phường cụ thể, và điều này chỉ đúng sau khi nhóm làm việc với phường"); M dòng 59.
- PRD: §1 chỉ giữ "WRMS không phải thêm một kênh báo" và không thay các kênh thành phố. Hai câu trung thực còn lại không có.
- Sửa: thêm vào P §1 đoạn "Luận điểm": WRMS không có lợi thế công nghệ độc quyền; lợi thế dự kiến là bám quy trình của một phường, chỉ đúng sau khi làm việc với phường (gắn CXM).

### G-4 [MEDIUM] Thứ tự cắt giảm: hệ quả lên đo lường và nghiên cứu chưa ghi
- Nguồn: B Rủi ro dòng cuối ("Cắt bản đồ điểm nóng trước, sau đó cắt AI sàng lọc; giữ gom nhóm và chấm ưu tiên"); M dòng 61.
- PRD §10.3 đúng thứ tự. Thiếu: (a) cắt FR-9 làm mất luôn RQ-4 và SM-R3 (P §6, §12) và FR-12 mô tả "AI Module" vẫn dựa vào ba thành phần; (b) FR-41 vẫn xóa "Ảnh bị gắn cờ đã bị loại" dù FR-15 bị cắt; (c) brief gộp "Bản đồ điểm nóng, dashboard và thống kê" thành một dòng phạm vi, PRD tự quyết giữ dashboard khi cắt bản đồ (hợp lý nhưng là suy ra, chưa gắn [ASSUMPTION]).
- Sửa: thêm vào §10.3 bước 2: "Khi cắt: RQ-4, SM-R3 bỏ theo; bỏ phần xóa ảnh bị loại ở FR-41"; gắn [ASSUMPTION] cho việc giữ FR-37 khi cắt FR-36.

### G-5 [MEDIUM] Khung "giả thuyết" yếu đi ở JTBD và hành trình
- Nguồn: B Vấn đề ("Phần này là giả thuyết"), Giải pháp ("Phần nghiên cứu... chưa phải nhu cầu đã được phường xác nhận"); M dòng 27, 49, 51.
- PRD:
  - §3.1 JTBD cán bộ phường viết ở thể khẳng định ("tôi muốn thấy ngay các phản ánh đã gom... và mức ưu tiên gợi ý, để duyệt...") không có thẻ [ASSUMPTION]. Mức gợi ý AI được trình bày như nhu cầu của cán bộ, trái với brief (chấm ưu tiên là phần nghiên cứu, chưa phải nhu cầu phường). §3.3 có thẻ giả định nhưng §3.1 thì không.
  - §3.3 UJ-2 đặt "mức gợi ý Cao" làm trọng tâm buổi sáng của cán bộ; UJ-1 đến UJ-6 có tên, tuổi, nghề cụ thể ("Chị Lan, 41 tuổi, bán hàng ở chợ"; "anh Minh", "anh Tuấn", "chị Hà"). Đã gắn thẻ giả định ở đầu §3.3, chấp nhận được, nhưng nhân vật trông như dữ liệu thật.
  - §1 ý "Ba là tự tìm cách báo lại kết quả cho người dân" trình bày như việc cán bộ đang làm. Brief (Vấn đề, câu 3) nói chưa rõ ai báo lại, người dân có biết không: đây là câu hỏi chưa trả lời, không phải việc làm tay đã biết.
- Sửa: gắn [ASSUMPTION] hoặc CXM-1/CXM-3 vào JTBD cán bộ; thêm cụm "(thành phần nghiên cứu, chưa phải nhu cầu phường đã xác nhận)" vào mô tả mức gợi ý trong JTBD và UJ-2; sửa câu ba ở §1 thành "khép kín vòng báo lại kết quả: hiện chưa rõ ai báo, báo cho ai (CXM-3)".

### G-6 [MEDIUM] Quyết định 5, 8, 9 "cần phường xác nhận" chưa được đánh dấu tại FR
- Nguồn: BA "Việc cần chốt" dòng 81 (nhất là điểm 5, 8, 9); M dòng 29.
- PRD §2 đoạn cuối hứa "ghi số điểm tương ứng ở các FR liên quan". FR-19 (điểm 5) chỉ ghi "Quyết định 5", không có nhãn chờ phường. FR-23 (điểm 8) mang CXM-2 nhưng không gắn với việc "hạn chót thay SLA cần phường xác nhận". FR-5 (điểm 9) mang CXM-2 (trùng ý nhưng không nêu rõ là quyết định chưa được xác nhận). Không có nhãn riêng cho "16 quyết định chờ phường".
- Sửa: thêm nhãn [PENDING-WARD: Q5/Q8/Q9] (hoặc dùng [NOTE FOR PM]) tại FR-19, FR-23, FR-5, FR-22 (Q13).

### G-7 [MEDIUM] Quy tắc xóa "Ảnh bị loại" là điều PRD tự bịa, mở rộng quyết định 15
- Nguồn: BA điểm 15 (chỉ phản ánh bị từ chối: sau 48 giờ xóa ảnh, mô tả, tọa độ chính xác; giữ loại, lý do, thời gian, khu vực. Không giữ làm dataset). Không có quy tắc nào cho ảnh bị loại của phản ánh được tiếp nhận.
- PRD: FR-15 và FR-41 xóa "Ảnh bị gắn cờ đã bị loại" sau 48 giờ kể từ khi tải lên; FR-15 có [ASSUMPTION] nhưng FR-41 (và dòng "Ảnh bị loại" trong FR-41) không có thẻ, và §15 Chỉ mục chỉ ghi ở dòng FR-15. Quy tắc này xóa luôn nguồn ảnh không hợp lệ có thể dùng huấn luyện Sàng lọc (BA dòng 83 đang hỏi nguồn này).
- Sửa: gắn [ASSUMPTION] vào FR-41 và thêm một dòng ở §15; nêu trong câu hỏi mở 9 rằng quy tắc này cản trở nguồn ảnh huấn luyện.

### G-8 [LOW] Nhãn CXM còn sót
- Nguồn: B Cần xác minh câu 1 (lượng thấp thì "AI gom trùng và chấm ưu tiên có giá trị nghiên cứu nhưng chưa phải nhu cầu"), câu 2 (đơn vị cấp thành phố xử lý thì xem lại hai mục ngoài phạm vi), câu 4 (Admin).
- PRD: FR-39, FR-40 (nhắc/báo quá hạn gửi cho "Người nhận" là cán bộ phòng ban của phường) phụ thuộc CXM-2 nhưng không gắn nhãn; FR-35 (lịch sử) và FR-9 (Sàng lọc, phụ thuộc lượng phản ánh) cũng không; FR-2, FR-4 (Admin) phụ thuộc CXM-4 nhưng chỉ FR-3 có nhãn. NFR-3 đặt 50 phản ánh/ngày (khoảng 1.500 mỗi tháng), cao gấp rất nhiều lần ước lượng 9/tháng của brief; có nhãn CXM-1 nhưng không giải thích đây là mức dự phòng.
- Sửa: bổ sung nhãn vào FR-39, FR-40 (CXM-2), FR-2, FR-4 (CXM-4); ghi vào NFR-3 "mức dự phòng, ước lượng brief là khoảng 9 phản ánh mỗi tháng".

### G-9 [LOW] "Cuộc vận hành sau 04/2027" mất chi tiết quy trách nhiệm
- Nguồn: B Rủi ro dòng 2 ("hỗ trợ chỉ dựa vào một thành viên nhóm"; hướng xử lý: chốt nơi đặt server và người chịu chi phí khi phường duyệt); M dòng 46, 48.
- PRD: §11 có nội dung này nhưng không ghi hướng xử lý "chốt khi phường duyệt" và việc phụ thuộc vào phê duyệt (có câu "phụ thuộc vào việc phường duyệt", đủ). §13 chỉ trỏ tới §11. Không có FR/NFR nào nói tới vận hành, bàn giao, tài liệu hướng dẫn (có thể ngoài phạm vi PRD).
- Sửa: bổ sung §13 một cột "Hướng xử lý" (xem G-10), hoặc ghi một dòng trong §11.

### G-10 [LOW] Bảng rủi ro §13 tham chiếu thay vì nêu lại
- Nguồn: B bảng Rủi ro (7 dòng, cột hệ quả và hướng xử lý).
- PRD §13 ghi "bảy rủi ro vẫn giữ nguyên" và chỉ liệt kê chỗ xử lý. Người đọc PRD không biết hệ quả của từng rủi ro nếu không mở brief. Đủ 7 rủi ro, không mâu thuẫn.
- Sửa: thêm cột "Hệ quả" tóm tắt một dòng; ghi rõ rủi ro 7 (khối lượng) là 2 app, 3 thành phần AI, 5 người, 4 tháng.

### G-11 [LOW] Bối cảnh bằng chứng về phía người dân bị lược
- Nguồn: B Vấn đề, đoạn "Phía người dân" (không ai trong nhóm từng gửi phản ánh hiện trường; trước đó nhóm cho rằng chưa có kênh nào); M dòng 28.
- PRD: §3.1 chỉ giữ "vấn đề có thể là không biết kênh hoặc không tin phản ánh được xử lý". Mất sự kiện "không ai trong nhóm từng báo phản ánh" và việc nhóm từng tin là chưa có kênh, là phần cho thấy giả thuyết yếu đến đâu.
- Sửa: thêm một câu ở §3.1 hoặc §2.

### G-12 [LOW] Brief liệt kê "ba kết quả" thành công; SM-3 được đặt lại, ghi chú có chỗ sai nhỏ
- Nguồn: B bảng Tiêu chí thành công: kết quả 2 đo bằng "Tỷ lệ nhiệm vụ có hạn chót; tỷ lệ nhiệm vụ quá hạn được cảnh báo trước".
- PRD: [NOTE FOR PM] dưới SM-5 nói "PRD thay bằng SM-3". Thực tế SM-3 là chỉ số thứ hai của brief, còn chỉ số thứ nhất (tỷ lệ có hạn chót) bị bỏ vì luôn 100% theo FR-23. Việc bỏ là hợp lý và đã nêu, nhưng câu chữ ngụ ý thay thế chứ không phải rút bớt.
- Ngoài ra §12 gộp SM-R4 vào nhóm "Nghiên cứu (đo trên tập đánh giá, không cần thí điểm)" trong khi chính SM-R4 cần thí điểm/quy trình hiện tại (BA dòng 74); mâu thuẫn nội bộ nhẹ với câu đầu §12 (chỉ SM-R1..R3 đo được khi phường không đồng ý).
- Sửa: sửa câu note thành "bỏ chỉ số tỷ lệ có hạn chót, giữ chỉ số cảnh báo trước (SM-3)"; chuyển SM-R4 sang nhóm "cần thí điểm".

### G-13 [LOW] Nội dung PRD tự thêm, không có trong nguồn và chưa gắn thẻ
Các mục dưới đây không mâu thuẫn nguồn nhưng không có [ASSUMPTION]; nên gắn thẻ hoặc đưa vào §15.
- FR-9: ba lý do gắn cờ (không phải cảnh thật, không đọc được, lặp lại) và "đúng một lý do". Brief chỉ nói "ảnh không hợp lệ".
- FR-26: phản ánh sang In Progress khi nhiệm vụ đầu được chấp nhận (PRD §4.1 bảng vòng đời). BA không nêu điều kiện kích hoạt.
- FR-16, FR-17: tiếp nhận theo Nhóm; từ chối một phản ánh trong nhóm thì tách ra khỏi nhóm.
- FR-24: nhóm xử lý tối thiểu hai người.
- FR-33: thêm sự kiện "Hạn chót đổi" ngoài bốn sự kiện của điểm 11 (có nêu rõ, chấp nhận được).
- FR-36, FR-37: mọi định nghĩa chi tiết hiển thị.
- Khái niệm "Nhóm phản ánh có trạng thái chung" (P §4) và FR-10 ("phản ánh gom vào nhóm đã Received vẫn ở Submitted") mâu thuẫn nhau trong nội bộ PRD ("mọi Phản ánh trong Nhóm cùng trạng thái" so với "vẫn ở Submitted"). Đây là lỗi nội bộ, không phải lệch nguồn, nhưng ảnh hưởng đến epic nhóm 4/6.

### G-14 [LOW] Thiếu tham chiếu pháp lý/địa bàn
- Nguồn: B Người dùng ("Theo Nghị quyết 1659/NQ-UBTVQH15, phường gồm Hòa Xuân, Hòa Châu, Hòa Phước"); M dòng 17.
- PRD: Khu vực (§4) và câu hỏi mở 6 nhắc ba địa bàn cũ nhưng không dẫn NQ 1659; ranh giới phường là câu hỏi mở 7. Không sai.
- Sửa: dẫn NQ 1659/NQ-UBTVQH15 ở câu hỏi mở 7 hoặc §8.

## Đã kiểm tra, không có vấn đề

- Quyết định 1-16 (bản 23/10): đã phản ánh ở FR-30 (1), FR-17 (2), §4 vai trò Admin và NFR-4 (3), §3.2 và §9 (4), FR-11/FR-19 (5), FR-4 và FR-11 (6), FR-4 (7), FR-23 (8), FR-5 (9), §9 (10), FR-33/34/39/40 (11), FR-21 (12), FR-22 (13), §4 và FR-12 (14), FR-41 (15), FR-24 (16).
- Cắt giảm đúng thứ tự (bản đồ điểm nóng, rồi AI sàng lọc; giữ gom nhóm, chấm ưu tiên). Có ghi chú PM hợp lý về CXM-1.
- Trong/ngoài phạm vi khớp brief (khiếu nại, TTHC, tình nguyện viên, tính năng cộng đồng, đơn vị phối hợp ngoài phường, chuyển lên cấp thành phố, nhận phản ánh từ kênh thành phố).
- Dữ liệu: dataset công khai để huấn luyện, ảnh tự chụp ở Hòa Xuân để đánh giá, nhãn nhóm tự gán và GVHD duyệt, baseline gom nhóm giữ, không dùng AI API ngoài: khớp.
- Phường chưa duyệt; nhóm chưa làm việc với phường; AI chấm ưu tiên là phần nghiên cứu: có ở §1, §6, §11, §12.
- Việc báo GVHD hai thay đổi: có ở §11 và câu hỏi mở 14.
