---
title: "Product Brief: WRMS"
status: final
created: 2026-10-23
updated: 2026-10-23
---

# Product Brief: WRMS – Hệ thống tiếp nhận, phân công và xử lý phản ánh hiện trường tại phường Hòa Xuân

## Tóm tắt

WRMS giúp UBND phường Hòa Xuân (Đà Nẵng) xử lý phản ánh hiện trường của người dân: rác thải trái phép, lấn chiếm vỉa hè, đường hỏng, cống nghẹt, đèn đường hỏng. Người dân gửi phản ánh kèm ảnh và vị trí qua app mobile. Cán bộ phường duyệt, giao việc cho cán bộ phòng ban, theo dõi hạn chót và nghiệm thu bằng ảnh trước và sau trên web. AI gom các phản ánh trùng một hiện trường và sàng lọc ảnh không hợp lệ. Riêng lĩnh vực vệ sinh môi trường, AI gợi ý mức ưu tiên từ ảnh; đây là phần nghiên cứu của đồ án.

Đà Nẵng đã có kênh để người dân báo (Góp ý Đà Nẵng, 1022, Zalo), và WRMS không thay các kênh đó. WRMS nhắm vào phần việc sau khi phường nhận phản ánh qua app WRMS: bỏ gom trùng thủ công, bỏ đôn đốc việc bằng miệng, và khép kín vòng nghiệm thu để người dân biết kết quả.

WRMS là đồ án capstone SEP490 của nhóm 5 sinh viên FPT, thực hiện từ 01/01/2027 đến 30/04/2027, với mục tiêu để phường thật sự dùng sau khi bảo vệ. Hiện dự án mới là ý tưởng. Nhóm chưa làm việc với UBND phường, nên vấn đề phía phường vẫn là giả thuyết. Việc đầu tiên là gặp phường trước 01/01/2027 để trả lời bốn câu ở mục Cần xác minh.

## Vấn đề

Phần này là giả thuyết. Nhóm chưa làm việc với UBND phường Hòa Xuân, nên các nhận định về phía phường chưa được kiểm chứng.

**Phía người dân.** Người dân thường là người đầu tiên thấy rác thải trái phép, lấn chiếm vỉa hè, đường hỏng, cống nghẹt hay đèn đường hỏng. Đà Nẵng đã có kênh phản ánh cấp thành phố: app Góp ý Đà Nẵng, tổng đài 1022 và Zalo. Dù vậy, không ai trong nhóm 5 người từng gửi một phản ánh hiện trường, và trước khi viết bản brief này, nhóm cho rằng chưa có kênh nào. Vấn đề phía người dân có thể là không biết có kênh hoặc không tin phản ánh sẽ được xử lý, chưa chắc là thiếu kênh.

**Phía phường (giả thuyết).** Nhóm giả định phường nhận phản ánh qua nhiều đường: đến trực tiếp, gọi điện, nhắn tin, hoặc được chuyển từ kênh thành phố. Nhiều phản ánh có thể trùng một hiện trường, và cán bộ phải tự quyết định xử lý việc nào trước. Nhóm cũng giả định vòng xử lý chưa khép kín: khi phường cử người xuống hiện trường, không rõ ai báo lại kết quả, báo cho ai, và người dân có được biết không.

## Cần xác minh với phường

Trước ngày 01/01/2027, nhóm cần một buổi làm việc với UBND phường Hòa Xuân để trả lời bốn câu. Nếu câu trả lời ở bất kỳ câu nào khác với giả định của nhóm, phạm vi đề tài phải đổi.

1. **Lượng phản ánh.** Phường nhận bao nhiêu phản ánh hiện trường mỗi tháng, qua những kênh nào, và bao nhiêu phản ánh bị trùng? Ước lượng thô từ số liệu 1022 toàn thành phố là khoảng 9 phản ánh mỗi tháng cho mỗi đơn vị cấp xã. Nếu con số thật ở mức này, AI gom trùng và chấm ưu tiên có giá trị nghiên cứu nhưng chưa phải nhu cầu của phường.
2. **Người xử lý thật.** Với từng lĩnh vực (vệ sinh môi trường, trật tự đô thị, đường và thoát nước, chiếu sáng), ai xử lý ngoài hiện trường: phòng ban của phường, tình nguyện viên, hay đơn vị cấp thành phố? Nếu là cấp thành phố, phải xem lại hai mục đang để ngoài phạm vi: đơn vị phối hợp ngoài phường và chuyển phản ánh lên cấp thành phố.
3. **Báo lại kết quả.** Khi phường cử người xuống hiện trường, hiện nay ai báo lại kết quả, cho ai, bằng cách nào, và người dân có được biết không?
4. **Người dùng ở phường.** Ai trong UBND phường sẽ dùng WRMS hằng ngày, thuộc phòng ban nào, bao nhiêu người? Phường có người làm IT để giữ vai trò Admin không?

## Người dùng

WRMS phục vụ một phường: Hòa Xuân. Theo Nghị quyết 1659/NQ-UBTVQH15, phường gồm địa bàn cũ của phường Hòa Xuân, xã Hòa Châu và xã Hòa Phước. Người dùng chính là người làm việc tại UBND phường. Người dân là nguồn phản ánh và người nhận kết quả.

| Nhóm | Là ai | Cần gì |
| --- | --- | --- |
| Cán bộ phường (chính) | Cán bộ UBND phường điều phối phản ánh hiện trường. Phòng ban và số người chưa rõ. | Một chỗ để duyệt, xếp ưu tiên, giao việc, nghiệm thu và theo dõi mọi phản ánh gửi qua app WRMS |
| Cán bộ phòng ban | Cán bộ các phòng ban của phường, nhận việc và xuống hiện trường | Biết việc được giao và hạn chót, nộp ảnh minh chứng từ điện thoại |
| Người dân | Cư dân phường Hòa Xuân | Báo nhanh kèm ảnh và vị trí, biết phản ánh được xử lý tới đâu |
| Admin | Người làm IT tại UBND phường (IT helpdesk hoặc vai trò tương đương). Chưa rõ phường có người này (câu 4). | Quản lý tài khoản, danh mục, phòng ban |

## Giải pháp

WRMS là công cụ xử lý phản ánh hiện trường của UBND phường, từ lúc người dân gửi đến lúc nghiệm thu xong. Người dân và cán bộ phòng ban dùng app mobile; cán bộ phường và Admin dùng web.

1. Người dân gửi phản ánh: chọn loại, mô tả, chụp ảnh; vị trí lấy từ GPS, dữ liệu EXIF của ảnh hoặc ghim trên bản đồ.
2. Hệ thống sàng lọc ảnh không hợp lệ và gom các phản ánh cùng hiện trường. Cán bộ phường xem phản ánh rõ nhất của mỗi nhóm và tách nhóm gộp sai.
3. Cán bộ phường duyệt, đặt mức ưu tiên, giao việc cho một cán bộ phòng ban hoặc một nhóm, đặt hạn chót.
4. Người được giao chấp nhận hoặc từ chối kèm lý do, xử lý và nộp ảnh sau xử lý. Hệ thống báo trước khi quá hạn.
5. Cán bộ phường kiểm tra hiện trường và nghiệm thu bằng ảnh trước và sau. Người gửi, kể cả người gửi các phản ánh đã gộp, được báo ở mỗi lần đổi trạng thái.

AI chỉ đưa ra gợi ý; con người quyết định cuối cùng. Nếu AI lỗi, phản ánh vẫn được tiếp nhận.

**Phần nghiên cứu.** Chấm mức ưu tiên từ ảnh là phần nghiên cứu của đồ án, chưa phải nhu cầu đã được phường xác nhận. Đồ án thí điểm cho lĩnh vực vệ sinh môi trường: nhận diện loại rác trong ảnh, rồi suy ra mức Thấp, Trung bình hoặc Cao từ độ đa dạng của rác và việc có rác đặc biệt (nguy hại, y tế, xây dựng, cồng kềnh). Các lĩnh vực khác do cán bộ phường đặt mức ưu tiên.

**Dữ liệu.** Model huấn luyện trên dataset công khai và đánh giá trên ảnh nhóm tự chụp tại Hòa Xuân. Tiêu chí ưu tiên do nhóm viết, GVHD duyệt. Chi tiết ở addendum.

## Điểm khác biệt

Theo nguồn công khai, các kênh thành phố (Góp ý Đà Nẵng, 1022, Zalo) chuyển phản ánh cho "cơ quan liên quan" với hạn xử lý 3 ngày làm việc. Nhóm chưa tìm thấy mô tả về cách phường xử lý tiếp.

WRMS không thay các kênh đó và không nhận phản ánh từ chúng. WRMS tập trung vào ba việc sau khi phường nhận phản ánh qua app WRMS: gom trùng tự động, giao việc có hạn chót, và nghiệm thu bằng ảnh trước và sau (chi tiết ở mục Tiêu chí thành công).

WRMS không có lợi thế công nghệ độc quyền. Lợi thế dự kiến là thiết kế sát quy trình của một phường cụ thể, và điều này chỉ đúng sau khi nhóm làm việc với phường.

## Tiêu chí thành công

WRMS thành công khi UBND phường Hòa Xuân đồng ý thí điểm, và trong thời gian thí điểm cán bộ phường bỏ được ba việc làm tay. Hiện dự án mới là ý tưởng, chưa được phường duyệt.

| Kết quả | Hiện nay (giả thuyết) | Với WRMS | Đo bằng |
| --- | --- | --- | --- |
| Không gom trùng thủ công | Cán bộ tự rà và gộp các phản ánh cùng hiện trường | Hệ thống gom theo vị trí, loại và ảnh; cán bộ chỉ tách nhóm gộp sai | Thời gian rà soát mỗi phản ánh; tỷ lệ gom đúng |
| Không đôn đốc việc bằng miệng | Giao việc, nhắc hạn qua điện thoại hoặc gặp trực tiếp | Giao việc, hạn chót và trạng thái nằm trên hệ thống; cảnh báo sắp quá hạn | Tỷ lệ nhiệm vụ có hạn chót; tỷ lệ nhiệm vụ quá hạn được cảnh báo trước |
| Khép kín nghiệm thu | Không rõ ai báo lại kết quả | Nghiệm thu bằng ảnh hiện trường trước và sau; người dân tự tra cứu tiến độ | Tỷ lệ phản ánh hoàn thành có ảnh trước và sau; số lần người dân phải hỏi lại |

Mức mục tiêu cho từng chỉ số sẽ đặt sau buổi làm việc với phường, khi có số liệu về quy trình hiện tại. Các chỉ số nghiên cứu (độ khớp mức ưu tiên, độ chính xác sàng lọc và gom nhóm) nằm trong addendum.

## Phạm vi

**Trong phạm vi (01/01/2027 – 30/04/2027)**

- Phản ánh hiện trường gửi qua app WRMS tại phường Hòa Xuân.
- App mobile cho người dân và cán bộ phòng ban; web cho cán bộ phường và Admin.
- Sàng lọc và gom nhóm cho mọi loại phản ánh; AI chấm ưu tiên chỉ cho vệ sinh môi trường.
- Bản đồ điểm nóng, dashboard và thống kê cho cán bộ phường.

**Ngoài phạm vi**

- Nhận phản ánh từ Góp ý Đà Nẵng, 1022 hoặc Zalo.
- Chuyển phản ánh lên cấp thành phố; đơn vị phối hợp ngoài phường.
- Khiếu nại, tố cáo; hồ sơ thủ tục hành chính.
- Tình nguyện viên; tính năng cộng đồng (điểm, xếp hạng, phần thưởng).

## Rủi ro

| Rủi ro | Hệ quả | Hướng xử lý |
| --- | --- | --- |
| Chưa làm việc với UBND phường; phường chưa duyệt | Vấn đề phía phường chỉ là giả thuyết; không có thí điểm thật | Gặp phường trước 01/01/2027 với bốn câu ở mục Cần xác minh |
| Chưa có kế hoạch vận hành sau 04/2027 | Không ai chịu trách nhiệm server, chi phí, bảo trì; hỗ trợ chỉ dựa vào một thành viên nhóm | Chốt nơi đặt server và người chịu chi phí khi phường duyệt |
| Ít phản ánh đi qua WRMS | Lượng phản ánh có thể thấp (xem câu 1) và người dân đã quen kênh thành phố; cán bộ phải theo dõi hai nơi | Câu 1 ở mục Cần xác minh |
| Dữ liệu công khai khác ảnh đường phố Việt Nam | Model kém trên ảnh thật | Đánh giá trên ảnh nhóm tự chụp, báo độ chính xác đo được |
| Ảnh có mặt người, biển số xe | Vi phạm Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 | Xin đồng ý khi gửi; ẩn ảnh phản ánh bị từ chối và ảnh bị loại 90 ngày rồi xóa; cân nhắc làm mờ mặt và biển số |
| Lệch so với đơn đăng ký (bỏ tình nguyện viên, đổi kế hoạch dữ liệu) | Hội đồng hỏi vì sao làm khác đề tài đã đăng ký | Báo GVHD và xin xác nhận |
| Khối lượng lớn: 2 app, 3 thành phần AI, 5 người, 4 tháng | Trễ hạn hoặc làm nông | Cắt bản đồ điểm nóng trước, sau đó cắt AI sàng lọc; giữ gom nhóm và chấm ưu tiên |

## Tầm nhìn

Nhóm chưa xác định tầm nhìn dài hạn. Mục này sẽ bổ sung sau buổi làm việc với phường.
