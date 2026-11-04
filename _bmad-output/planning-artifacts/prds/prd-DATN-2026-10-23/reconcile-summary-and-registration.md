# Đối chiếu đầu vào: Tóm tắt nghiệp vụ + Đơn đăng ký so với PRD và addendum

Ngày: 23/10/2026. Không sửa PRD. Nguồn đã đọc đủ: doc "WRMS – Tóm tắt nghiệp vụ" (summary), đơn đăng ký SP27 (đơn), `prd.md` (786 dòng), `addendum.md`.
Quy ước: summary và addendum của brief ưu tiên hơn đơn. Mức độ: critical / high / medium / low.

## 1. Kết luận ngắn

- Không có gap critical. PRD phủ tốt 16 quyết định, 11 nhóm nghiệp vụ và hầu hết use case trong bảng quyết định.
- PRD không giữ lại quy tắc nào của đơn đã bị thay thế (tình nguyện viên, Admin điều phối, Admin nghiệm thu, hotspot map cho Admin, 4 trạng thái, giữ dữ liệu ẩn danh). Đã kiểm tra từng mục.
- Gap chính: (a) mâu thuẫn nội bộ FR-15 và FR-21; (b) phần nghiên cứu thiếu "sản phẩm đầu ra" và kế hoạch gán nhãn tập đánh giá cho gom nhóm và sàng lọc; (c) danh sách thay đổi cần báo GVHD chưa đủ; (d) thiếu FR cho Cán bộ phòng ban xem nhiệm vụ.

## 2. Các gap

### G-1 (high) FR-15 trái FR-21 và quyết định 12
- Nguồn: summary quyết định 12: Yêu cầu bổ sung "chỉ mở khi phản ánh ở Received hoặc In Progress".
- PRD: FR-15 nói nếu mọi ảnh của Phản ánh bị loại thì Cán bộ phường phải từ chối hoặc "gửi Yêu cầu bổ sung" trước khi tiếp nhận. Lúc đó Phản ánh còn ở Submitted, mà FR-21 cấm gửi Yêu cầu bổ sung cho Phản ánh ở Submitted. Dòng này cũng nằm trong §15 chỉ mục giả định.
- Sửa: bỏ nhánh "gửi Yêu cầu bổ sung" khỏi FR-15 (chỉ còn: từ chối), hoặc nêu đây là ngoại lệ có chủ ý của quyết định 12 và gắn `[NOTE FOR PM]` để nhóm quyết định. Khuyến nghị bỏ nhánh này.

### G-2 (high) Sản phẩm đầu ra và dataset của phần nghiên cứu không được ghi
- Nguồn đơn: 3.3.4 Expected research outputs (thành phần sàng lọc, gom nhóm, nhận diện rác và kết quả đánh giá; dataset ảnh có nhãn loại, điểm, hợp lệ, loại rác, mức ưu tiên; tiêu chí ưu tiên và phương pháp gom nhóm có ngưỡng đã đánh giá; báo cáo đồ án) và 3.4 Expected outputs (app mobile, web, module phân tích, dataset và báo cáo đánh giá). Kế hoạch dữ liệu mới (addendum) đổi nguồn dataset nhưng không bỏ việc nhóm tạo bộ ảnh Hòa Xuân có nhãn.
- PRD: §6 và §10.1 chỉ có RQ, dữ liệu, quy tắc đánh giá. Không có mục "Sản phẩm bàn giao". §10.1 không nêu dataset đánh giá, báo cáo đánh giá, tiêu chí ưu tiên đã chốt, báo cáo đồ án.
- Sửa: thêm tiểu mục "Sản phẩm đầu ra của nghiên cứu" ở §6 và dòng tương ứng ở §10.1: (1) module sàng lọc, gom nhóm, nhận diện rác; (2) bộ ảnh đánh giá tự chụp ở Hòa Xuân kèm nhãn; (3) tiêu chí ưu tiên và ngưỡng gom nhóm đã đánh giá; (4) báo cáo đánh giá và báo cáo đồ án. Ghi rõ bộ ảnh đánh giá có công bố hay không là câu hỏi mở (quyền riêng tư, §8.1).

### G-3 (medium) Kế hoạch gán nhãn tập đánh giá chưa phủ gom nhóm và sàng lọc
- Nguồn đơn: dataset gắn nhãn loại, địa điểm (site) và tính hợp lệ; loại rác và mức ưu tiên cho lĩnh vực thí điểm. Metric: độ chính xác gom nhóm và sàng lọc (SM-R2, SM-R3).
- PRD §6: chỉ nói "Nhãn mức ưu tiên" và "Dùng cho nhận diện rác và gom nhóm". Không nêu ai gán nhãn site (điểm nào thuộc cùng hiện trường) và nhãn hợp lệ hay không hợp lệ. RQ-4 và SM-R3 (sàng lọc) không có dữ liệu đánh giá nào được mô tả; chỉ có nguồn huấn luyện ảnh không hợp lệ ở câu hỏi mở 9.
- Sửa: thêm vào "Dữ liệu" một dòng về nhãn site (từ cách chụp "mỗi điểm nhiều góc"), nhãn hợp lệ (nhóm tự dựng ảnh không hợp lệ: ảnh chụp màn hình, mờ, lặp), và gắn câu hỏi mở 9 với cả tập đánh giá chứ không chỉ tập huấn luyện.

### G-4 (high) Danh sách thay đổi cần báo GVHD chưa đủ
- Nguồn: summary ghi 23/10 đổi lớn so với đơn: cán bộ phường điều phối toàn bộ và nghiệm thu cuối, Admin chỉ quản trị hệ thống, bỏ tình nguyện viên. Đơn còn ghi: 4 trạng thái; người xác minh AI là Admin; phản ánh bị từ chối "giữ dạng ẩn danh"; Admin dùng web để duyệt, giao việc, duyệt kết quả, xem hotspot.
- PRD: §11 và câu hỏi mở 14 chỉ nêu "hai thay đổi" (bỏ tình nguyện viên; kế hoạch dữ liệu, baseline, thử nghiệm). §3.2 chỉ nhắc tình nguyện viên.
- Sửa: sửa §11, câu hỏi mở 14 và §3.2 thành danh sách đầy đủ, ít nhất 6 thay đổi: (1) bỏ tình nguyện viên; (2) vai trò Admin và Cán bộ phường (Admin chỉ quản trị); (3) thêm trạng thái Rejected (5 trạng thái); (4) bảng AI Use Declaration: người kiểm chứng là Cán bộ phường; (5) lưu trữ phản ánh bị từ chối: xóa dữ liệu chi tiết sau 48 giờ thay cho "ẩn danh"; (6) kế hoạch dữ liệu, baseline, thử nghiệm. Đơn cũng cần sửa mô tả "web cho Admin và cán bộ phường" cho khớp.

### G-5 (medium) Thiếu FR cho Cán bộ phòng ban xem nhiệm vụ và hộp thông báo
- Nguồn: bảng quyết định 11 liệt kê use case "Task Assignee: View Notifications"; actor table: Task Assignee nhận hoặc từ chối, xử lý, nộp minh chứng; thành viên nhóm "chỉ xem".
- PRD: FR-26 đến FR-29 là hành động, FR-33 là thông báo. Không có FR "xem danh sách và chi tiết nhiệm vụ của tôi" (ảnh, vị trí, hạn chót, kết quả xác minh hiện trường, lịch sử trả lại). FR-24 và FR-20 chỉ nhắc ngầm. Hộp thông báo của người dùng chỉ có ở NFR-6 và FR-34 (riêng cán bộ phường).
- Sửa: thêm FR "Cán bộ phòng ban xem nhiệm vụ của mình" (danh sách lọc theo trạng thái nhiệm vụ, quá hạn; chi tiết nhiệm vụ; chế độ chỉ xem cho thành viên nhóm) và nêu hộp thông báo trong app cho người dân và cán bộ phòng ban (có thể gộp vào NFR-6 nhưng nên có FR để story).

### G-6 (medium) Ba actor phụ không có trong thuật ngữ §4
- Nguồn: actor table liệt kê Notification Service, Map Service, System Timer là actor phụ cùng AI Module, kèm trách nhiệm cụ thể.
- PRD §4 Vai trò chỉ có Người dân, Cán bộ phường, Cán bộ phòng ban, Admin, AI Module. Map Service xuất hiện ở FR-7 và NFR-8, Notification Service ở NFR-8, System Timer ở mô tả §5.11, nhưng không định nghĩa. §0 nói thuật ngữ §4 là bắt buộc.
- Sửa: thêm vào §4 ba actor phụ, mỗi actor một dòng theo đúng trách nhiệm trong actor table: Notification Service (đẩy thông báo cho người dân khi trạng thái đổi; cho người xử lý và cán bộ phường theo sự kiện nhiệm vụ); Map Service (bản đồ, ghim vị trí, chuyển tọa độ thành địa chỉ; nêu cả bản đồ hotspot nếu dùng chung); System Timer (nhắc sắp quá hạn cho người xử lý, báo quá hạn cho cán bộ phường, xóa dữ liệu sau 48 giờ). Đổi chủ ngữ "Hệ thống" ở FR-39 đến FR-41 thành System Timer.

### G-7 (medium) Phản ánh gom vào nhóm đã Received hoặc In Progress phá bất biến "mọi phản ánh trong Nhóm cùng trạng thái"
- Nguồn: summary: "Mỗi lần trạng thái đổi, người gửi được thông báo, kể cả người gửi các phản ánh đã gộp nhóm"; quyết định 12: thông tin bổ sung "kể cả khi đã gộp nhóm".
- PRD: §4 Nhóm phản ánh nói mọi Phản ánh trong Nhóm cùng trạng thái. FR-10 lại để Phản ánh mới gộp vào Nhóm đã Received/In Progress vẫn ở Submitted đến khi Cán bộ phường xác nhận. Trong thời gian đó Người gửi không được thông báo trạng thái của Nhóm và FR-21 không cho gửi Yêu cầu bổ sung cho Phản ánh ở Submitted dù nó nằm trong nhóm đang xử lý. Mâu thuẫn nội bộ chưa được ghi nhận, dù có tag ASSUMPTION.
- Sửa: sửa câu định nghĩa Nhóm phản ánh ở §4 ("trừ Phản ánh mới gộp đang chờ xác nhận") hoặc đổi thiết kế FR-10: Phản ánh gộp vào Nhóm đang xử lý nhận trạng thái của Nhóm ngay và nhãn "chờ xác nhận gộp" chỉ là cờ riêng. Cần PM chọn.

### G-8 (medium) Quy tắc xóa 48 giờ còn mơ hồ ở hai điểm
- Nguồn: summary nhóm 11: System Timer "xóa ảnh bị gắn cờ và phản ánh bị từ chối theo quy định lưu trữ"; actor table và quyết định 15: "sau 48 giờ xóa ảnh, mô tả, tọa độ của phản ánh bị từ chối". Đơn: ảnh bị gắn cờ "removed 48 hours after upload".
- PRD: FR-15 và FR-41 chỉ xóa Ảnh bị gắn cờ "đã bị loại" sau 48 giờ từ lúc tải lên. Hai điểm chưa nêu: (a) ảnh bị gắn cờ nhưng Cán bộ phường chưa quyết định sau 48 giờ thì sao (đọc summary nhóm 11 có thể hiểu là xóa mọi ảnh bị gắn cờ); (b) Cán bộ phường loại ảnh ở giờ thứ 60 thì xóa ngay hay không. FR-41 cũng không nói mốc 48 giờ của phản ánh bị từ chối tính từ lúc từ chối hay lúc gửi (summary ngầm hiểu từ lúc bị từ chối, và §8.1 gắn với chính sách đồng ý).
- Sửa: ghi rõ mốc bắt đầu của hai quy tắc và ca ảnh bị gắn cờ chưa quyết định. Đề xuất: ảnh gắn cờ chưa quyết định cũng bị xóa sau 48 giờ nên hàng chờ cần cảnh báo cán bộ; phản ánh bị từ chối tính 48 giờ từ lúc từ chối. Gắn `[ASSUMPTION]` hoặc đưa vào câu hỏi mở.

### G-9 (low) FR-33 nói "bốn sự kiện" nhưng liệt kê năm
- Nguồn: quyết định 11: 4 sự kiện (giao việc mới; kết quả xét lý do từ chối; bị trả lại kèm lý do; sắp quá hạn).
- PRD: FR-33 thêm sự kiện thứ năm "Hạn chót đổi" (từ FR-22, ASSUMPTION của PRD) nhưng consequence vẫn viết "Bốn sự kiện theo quyết định 11".
- Sửa: tách rõ "4 sự kiện theo quyết định 11, cộng 1 sự kiện bổ sung do FR-22 `[ASSUMPTION]`" và đưa dòng này vào §15.

### G-10 (low) Notification Service chỉ đẩy cho người dân và người xử lý, còn PRD hạ cán bộ phường xuống thông báo trong web
- Nguồn: actor table: Notification Service đẩy thông báo "cho người xử lý và cán bộ phường theo sự kiện nhiệm vụ".
- PRD: FR-34 giả định cán bộ phường chỉ nhận thông báo hiển thị trong web, không email, không SMS; có tag ASSUMPTION nên không mâu thuẫn, nhưng lệch nhẹ với "đẩy". Khi cán bộ không mở web thì quá hạn không ai biết.
- Sửa: giữ assumption, thêm ghi chú rằng đây là chỗ nhóm có thể nâng (email hoặc web push) nếu phường cần, và hỏi ở CXM-4.

### G-11 (low) Các điểm nhỏ khác
- FR-3: Admin được tạo tài khoản Admin; summary chỉ nói "tài khoản cán bộ do Admin tạo". Gắn ASSUMPTION hoặc bỏ.
- FR-24: Nhóm xử lý "hai Cán bộ phòng ban trở lên" là ràng buộc PRD tự thêm, quyết định 16 không nêu. Gắn ASSUMPTION.
- FR-30: summary nhóm 8 và quyết định 1 nói cán bộ phường "kiểm tra hiện trường" rồi nghiệm thu. PRD chỉ cho "ghi" kết quả kiểm tra (ASSUMPTION), không nêu kiểm tra hiện trường có bắt buộc trước khi duyệt không. Nên hỏi lại nhóm hoặc ghi rõ "không bắt buộc".
- FR-4 và §4 Lĩnh vực thí điểm: Admin được đổi tên, ẩn Lĩnh vực nhưng "Vệ sinh môi trường" cố định trong cấu hình; chưa nêu cơ chế khóa (ví dụ khóa theo mã Lĩnh vực, không cho Admin xóa hoặc đổi mã).
- Summary phần "Còn mở: khi có nhiều cán bộ phường, ai chia phản ánh". FR-18 đã nêu là NOTE FOR PM, hợp lý; chỉ cần bảo đảm FR-18 không bị đọc như quyết định đã chốt.

## 3. Phủ use case trong bảng quyết định

| Use case (summary) | FR trong PRD | Nhận xét |
| --- | --- | --- |
| Inspect Site After Handling | FR-30 | Có; xem G-11 (bắt buộc hay không) |
| Approve or Return Task Result | FR-30 | Đủ |
| Contact Residents | FR-21 | Đủ |
| Provide Additional Info | FR-21 | Đủ (cùng FR; xem G-1, G-7) |
| Monitor Task Progress | FR-22, FR-34 | Đủ |
| Review Declined Task | FR-28 | Đủ |
| View Overdue Alerts | FR-34, FR-40, FR-22 | Phủ qua thông báo, nhãn, bộ lọc; không có FR riêng, chấp nhận được |
| Manage Domains, Manage Categories | FR-4 | Đủ |
| Manage Departments | FR-5 | Đủ |
| Analyze Report | FR-9, FR-10, FR-11, FR-12 | Đủ; kích hoạt khi gửi nêu ở §4 và §5.3 |
| Review Reports, Reject Report, Assign Task | FR-13 đến FR-17, FR-23 đến FR-25 | Đủ |
| Set or Adjust Report Priority | FR-19 | Đủ |
| Accept Task, Reject Task, Complete Assigned Task | FR-26, FR-27, FR-29 | Đủ; quy tắc trưởng nhóm ở FR-24 |
| View Dashboard and Statistics | FR-36, FR-37 | Đủ |
| Task Assignee: View Notifications | FR-33, NFR-6 | Thiếu FR xem nhiệm vụ và hộp thông báo, xem G-5 |
| Enable/Disable AI, Manage SLA, Volunteer…, Policy Q&A… | không có (đúng) | Đã bỏ đúng; liệt kê ở §9 |

## 4. Phủ 11 nhóm nghiệp vụ

Đủ FR cho cả 11 nhóm, ánh xạ đúng với addendum (người sở hữu khớp summary). Các ý "Nội dung chính" đều có FR tương ứng: tự đăng ký và Admin tạo tài khoản cán bộ (FR-1, FR-3); ảnh nhiều, GPS, EXIF, ghim (FR-6, FR-7); AI lỗi vẫn tiếp nhận (FR-12); phản ánh rõ nhất, tách nhóm, ảnh gắn cờ, từ chối (FR-13 đến FR-17); giao cá nhân hoặc nhóm, quá hạn báo cán bộ (FR-23, FR-24, FR-40); nghiệm thu bắt buộc ảnh (FR-29, FR-30); thông báo kể cả nhóm gộp (FR-32); thống kê đủ 7 chiều (FR-37); cảnh báo quá hạn và xóa dữ liệu (FR-39 đến FR-41). Gap duy nhất của nhóm: xem G-5 (nhóm 7 và 9, phía Cán bộ phòng ban) và G-8 (nhóm 11).

## 5. Phủ nội dung đơn đăng ký còn hiệu lực

| Mục trong đơn | Trạng thái trong PRD |
| --- | --- |
| Mục tiêu 1 đến 4, phạm vi, ngoài phạm vi | Có (§1, §9, §10) |
| Hướng tiếp cận (sàng lọc, gom nhóm, ưu tiên từ độ đa dạng và rác đặc biệt) | Có (FR-9 đến FR-11, addendum) |
| Baseline gom nhóm chỉ theo vị trí; baseline thời gian xử lý | Có (SM-R2, SM-R4) |
| Metric: khớp mức ưu tiên, chính xác gom nhóm và sàng lọc, thời gian xử lý, thời gian đến Completed | Có (SM-R1 đến SM-R4) |
| Thiết lập thử nghiệm: ngưỡng chỉnh theo góp ý cán bộ khi thí điểm | Có (§6) |
| Mục tiêu nghiên cứu: nhận diện loại rác, tiêu chí ưu tiên, gom nhóm, sàng lọc | Có (RQ-1 đến RQ-4) |
| Sản phẩm nghiên cứu và sản phẩm bàn giao (3.3.4, 3.4) | Thiếu, xem G-2 |
| Nhãn dataset (site, hợp lệ, loại rác, mức ưu tiên) | Thiếu một phần, xem G-3 |
| Khai báo AI: hai dòng chọn dùng AI trong sản phẩm và nghiên cứu | Có (§6, §8.2); bảng người kiểm chứng đổi sang Cán bộ phường, cần báo GVHD (G-4) |
| AI 3.6.3: model pretrained tinh chỉnh, server riêng, không AI API ngoài; lỗi AI vẫn tiếp nhận; quyền dùng dữ liệu theo giấy phép | Có (§8.2, NFR-8, addendum) |
| Quy tắc 48 giờ | Có nhưng còn mơ hồ, xem G-8 |

## 6. Quy tắc cũ của đơn bị thay thế: PRD có giữ lại không?

Không. PRD không còn tình nguyện viên, Admin điều phối hay nghiệm thu, Admin xem hotspot, 4 trạng thái, "đề xuất người xử lý" của cán bộ phường, phản ánh bị từ chối giữ ẩn danh, hay Admin là người kiểm chứng AI. Quy tắc 48 giờ cho ảnh bị gắn cờ được giữ từ đơn nhưng đã tag ASSUMPTION ở FR-15 và nằm trong §15; xem G-8.
