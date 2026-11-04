---
title: "PRD: WRMS"
status: final
created: 2026-10-23
updated: 2026-10-23
---

# PRD: WRMS – Hệ thống tiếp nhận, phân công và xử lý phản ánh hiện trường tại phường Hòa Xuân

## 0. Mục đích tài liệu

PRD này dành cho nhóm 5 sinh viên SEP490, giảng viên hướng dẫn (GVHD) và các bước tiếp theo trong chuỗi BMad: thiết kế UX (`bmad-ux`), kiến trúc (`bmad-architecture`), epic và story (`bmad-create-epics-and-stories`). PRD dựa trên product brief đã chốt ngày 23/10/2026 và không lặp lại phần lập luận của brief:

- Brief: `_bmad-output/planning-artifacts/briefs/brief-DATN-2026-10-23/brief.md`
- Addendum của brief (actor, trạng thái, 16 quyết định nghiệp vụ, kế hoạch dữ liệu): `.../brief-DATN-2026-10-23/addendum.md`
- Doc [WRMS – Tóm tắt nghiệp vụ](https://claude.ai/artifact/TCo4PkJ8LG8kGYh2rBBog2) (11 nhóm nghiệp vụ, bảng điểm đã chốt)
- Đơn đăng ký đề tài: `.../brief-DATN-2026-10-23/inputs/SP27_WRMS_Dang_ky_de_tai.txt`. Khi có mâu thuẫn, brief, addendum của brief và doc Tóm tắt nghiệp vụ được ưu tiên hơn đơn đăng ký.

Cách đọc:

- Thuật ngữ ở §4 là bắt buộc. Mọi FR, UJ, SM dùng đúng các thuật ngữ đó.
- Tính năng ở §5 xếp theo 11 nhóm nghiệp vụ, mỗi nhóm là một epic trên Jira. FR đánh số toàn cục, từ FR-1 đến FR-45. Các FR thêm sau bản nháp đầu (FR-42 đến FR-45) mang số nối tiếp và nằm trong nhóm nghiệp vụ của chúng, để giữ ID ổn định.
- `[ASSUMPTION: …]` đánh dấu chỗ PRD tự suy ra, chưa ai xác nhận. Tất cả có trong Chỉ mục giả định ở §15, chia theo người cần xác nhận. `[NOTE FOR PM: …]` đánh dấu điểm căng cần nhóm quyết định; mỗi điểm có một dòng ở §14. Thẻ giữ tiếng Anh để công cụ ở bước sau tìm được.
- `[CXM-1]` đến `[CXM-4]` đánh dấu yêu cầu phụ thuộc vào câu trả lời của UBND phường cho bốn câu ở mục "Cần xác minh với phường" của brief. Xem §2.

## 1. Tầm nhìn (v1)

WRMS là công cụ để UBND phường Hòa Xuân xử lý phản ánh hiện trường của người dân, từ lúc người dân gửi qua app đến lúc cán bộ phường nghiệm thu xong. Người dân chụp ảnh rác thải trái phép, đường hỏng, cống nghẹt hay đèn đường hỏng, gửi kèm vị trí, và biết phản ánh của mình đang ở bước nào. Cán bộ phường có một chỗ duy nhất để duyệt, đặt mức ưu tiên, giao việc có hạn chót cho cán bộ phòng ban, rồi nghiệm thu bằng ảnh trước và sau.

Luận điểm của sản phẩm: với các phản ánh đi qua app WRMS, cán bộ phường bỏ được ba việc làm tay. Một là gom các phản ánh trùng một hiện trường. Hai là đôn đốc việc bằng miệng. Ba là khép kín vòng báo lại kết quả; hiện chưa rõ ai báo lại, báo cho ai, và người dân có biết không `[CXM-3]`. WRMS không phải thêm một kênh báo. Đà Nẵng đã có Góp ý Đà Nẵng, tổng đài 1022 và Zalo, và WRMS không thay hay nhận phản ánh từ các kênh đó. WRMS cũng không có lợi thế công nghệ độc quyền. Lợi thế dự kiến là thiết kế sát quy trình của một phường cụ thể, và điều này chỉ đúng sau khi nhóm làm việc với phường.

Luận điểm này hiện là giả thuyết. Nhóm chưa làm việc với UBND phường, và dự án mới là ý tưởng chờ phường duyệt. Phần AI chấm mức ưu tiên từ ảnh cho lĩnh vực vệ sinh môi trường là phần nghiên cứu của đồ án, chưa phải nhu cầu phường đã xác nhận. Mục tiêu của nhóm không dừng ở bảo vệ đồ án: nhóm muốn UBND phường thật sự dùng WRMS sau khi bảo vệ, và điều đó kéo theo câu hỏi ai vận hành sau 04/2027 (§11).

Mục này chỉ mô tả sản phẩm v1. Tầm nhìn dài hạn chưa xác định; nhóm bổ sung sau buổi làm việc với phường.

## 2. Điều kiện để phạm vi đứng vững: bốn câu cần xác minh

Trước 01/01/2027 nhóm cần một buổi làm việc với UBND phường Hòa Xuân để trả lời bốn câu dưới đây (theo brief). Bảng ghi giả định PRD đang dùng, điều phải đổi nếu câu trả lời khác, và các yêu cầu mang nhãn tương ứng.

| Nhãn | Câu hỏi | Giả định PRD đang dùng | Nếu câu trả lời khác | Yêu cầu mang nhãn |
| --- | --- | --- | --- | --- |
| CXM-1 | Lượng phản ánh mỗi tháng, qua kênh nào, bao nhiêu phản ánh trùng | Đủ phản ánh trùng để gom nhóm và xếp ưu tiên có ích cho phường. Ước lượng thô từ số liệu 1022 cho thấy chỉ khoảng 9 phản ánh mỗi tháng cho mỗi đơn vị cấp xã | Nếu lượng thấp như ước lượng: gom nhóm và chấm ưu tiên chỉ còn giá trị nghiên cứu; bản đồ điểm nóng và dashboard ít dữ liệu; mục tiêu SM phải hạ; nên xem lại thứ tự cắt giảm ở §10.3 | §3.1, FR-10, FR-11, FR-13, FR-14, FR-36, FR-37, NFR-3, SM-1, SM-2, SM-R4 |
| CXM-2 | Ai xử lý ngoài hiện trường theo từng lĩnh vực | Cán bộ phòng ban của phường xử lý mọi lĩnh vực trong phạm vi | Nếu đèn đường, thoát nước, đường sá do đơn vị cấp thành phố xử lý: hoặc thu hẹp Lĩnh vực trong phạm vi, chỉ giữ những Lĩnh vực phường tự xử lý, hoặc đưa lại hai mục đang ngoài phạm vi (đơn vị phối hợp ngoài phường, chuyển phản ánh lên cấp thành phố). Thu hẹp rẻ hơn nhiều: chỉ đổi danh mục; còn chuyển cấp thành phố cần thêm vai trò, trạng thái và có thể cần tích hợp `[NOTE FOR PM: chọn sẵn hướng thu hẹp nếu buổi làm việc sát 01/01/2027]` | §3.2, §5.6, §5.7, FR-3, FR-5, FR-23, FR-24, FR-25, FR-26, FR-27, FR-28, FR-29, FR-30, FR-33, FR-39, FR-40, FR-42, FR-43, SM-3, UJ-3, UJ-4, UJ-7, §9 |
| CXM-3 | Hiện nay ai báo lại kết quả, cho ai, bằng cách nào, người dân có biết không | Vòng xử lý chưa khép kín; người dân không biết kết quả | Nếu phường đã có cách báo lại ổn: giá trị của nghiệm thu bằng ảnh và tra cứu tiến độ giảm; SM-4, SM-5 không còn là kết quả chính | §1, §3.1, §5.8, FR-29, FR-30, FR-31, FR-32, SM-4, SM-5, UJ-1, UJ-5 |
| CXM-4 | Ai trong UBND phường dùng WRMS hằng ngày, phòng ban nào, bao nhiêu người; phường có người làm IT cho vai trò Admin không | Có một hoặc vài cán bộ phường điều phối; có một người làm IT, khác với cán bộ phường, giữ vai trò Admin | Nếu nhiều cán bộ phường: cần quy tắc chia phản ánh. Nếu không có người IT: vai trò Admin do cán bộ phường hoặc nhóm giữ. Khi đó một người cần hai tài khoản hoặc một tài khoản nhiều vai trò (§4 đang giả định mỗi tài khoản một vai trò). Nếu sinh viên giữ Admin, NFR-4 là thứ duy nhất ngăn nhóm đọc dữ liệu cá nhân của người dân; rủi ro vận hành sau 04/2027 tăng | §3.1, FR-2, FR-3, FR-4, FR-18, FR-22, FR-34, NFR-3, NFR-4, §8.1, UJ-2, UJ-6, §11 |

### 2.1 Nếu chưa có câu trả lời hoặc phường không duyệt

UX và kiến trúc khởi động từ 01/01/2027 dù đã có buổi làm việc với phường hay chưa. Hướng mặc định dưới đây do PRD đề xuất; nhóm và GVHD quyết định. `[ASSUMPTION: nhóm và GVHD chấp nhận hướng mặc định này]`

- Nếu đến 01/01/2027 chưa có buổi làm việc: nhóm thiết kế theo cột "Giả định PRD đang dùng" ở bảng trên. Phòng ban, Lĩnh vực, Loại phản ánh, Lĩnh vực thí điểm và mốc nhắc hạn nằm trong danh mục hoặc cấu hình, không viết cứng, để đổi được khi có câu trả lời.
- Sau một mốc nhất định thì không đổi phạm vi theo câu trả lời của phường nữa. `[NOTE FOR PM: nhóm và GVHD đặt mốc cuối được đổi phạm vi]`
- Nếu phường không duyệt thí điểm: nhóm vẫn xây phạm vi MVP ở §10.1, đánh giá phần nghiên cứu trên tập ảnh tự chụp (SM-R1 đến SM-R3), và demo trước hội đồng bằng dữ liệu mẫu và đóng vai. Các lựa chọn khác là thu hẹp về phần nghiên cứu, hoặc tìm phường khác.

### 2.2 Quyết định nghiệp vụ chờ phường xác nhận

Cả 16 quyết định nghiệp vụ trong addendum của brief do nhóm tự chốt, chưa có ý kiến của phường. Ba quyết định cần xác nhận nhất: quyết định 5, ai đặt Mức cuối (FR-19); quyết định 8, Hạn chót thay cho bảng SLA (FR-22, FR-23); quyết định 9, không có đơn vị phối hợp (FR-5). Các FR này ghi "chờ phường xác nhận".

## 3. Người dùng

### 3.1 Jobs To Be Done

- **Cán bộ phường (người dùng chính).** `[CXM-1]` `[CXM-3]` `[CXM-4]` Khi có phản ánh mới gửi qua app WRMS, tôi muốn thấy ngay các phản ánh đã gom theo hiện trường, để duyệt và giao việc mà không phải tự rà từng tin. Khi đã giao việc, tôi muốn biết việc nào sắp quá hạn mà không phải gọi điện hỏi. Khi việc xong, tôi muốn nghiệm thu bằng ảnh trước và sau, và để hệ thống báo kết quả cho người dân. Ba nhu cầu này là giả thuyết của brief, chưa được phường xác nhận. Mức gợi ý của AI là phần nghiên cứu; chưa biết cán bộ phường có cần không.
- **Cán bộ phòng ban.** Khi được giao việc, tôi muốn biết rõ việc gì, ở đâu, hạn chót khi nào, và nộp ảnh minh chứng ngay từ điện thoại ở hiện trường. Khi việc không đúng chuyên môn, tôi muốn từ chối kèm lý do thay vì bỏ ngỏ.
- **Người dân.** Khi thấy một vấn đề ở nơi công cộng, tôi muốn báo trong vài phút bằng ảnh và vị trí, rồi biết phản ánh được xử lý tới đâu mà không phải hỏi lại. Theo brief, vấn đề phía người dân có thể là không biết có kênh hoặc không tin phản ánh được xử lý, chưa chắc là thiếu kênh. Không ai trong nhóm từng gửi phản ánh hiện trường, và trước khi viết brief nhóm cho rằng chưa có kênh nào.
- **Admin (IT của UBND phường).** `[CXM-4]` Tôi muốn tạo tài khoản cán bộ, quản lý danh mục và phòng ban mà không phải đụng vào nghiệp vụ xử lý phản ánh.

### 3.2 Không phải người dùng (v1)

- Tình nguyện viên. Đã bỏ hẳn ngày 23/10; đây là một trong sáu thay đổi so với đơn đăng ký cần báo GVHD (§11).
- Đơn vị cấp thành phố và đơn vị phối hợp ngoài phường. `[CXM-2]`
- Cán bộ tiếp nhận phản ánh của Góp ý Đà Nẵng, 1022, Zalo. WRMS không nhận phản ánh từ các kênh này.
- Người dân xem phản ánh của người khác. Không có hiển thị công khai (quyết định 10).

### 3.3 Hành trình chính

Các hành trình dưới đây dựng lại từ luồng 5 bước trong brief. Chưa có cán bộ phường thật kể lại một phiên làm việc, và nhân vật là hư cấu. `[ASSUMPTION: UJ-1 đến UJ-7 là hành trình giả định; cần kiểm lại sau buổi làm việc với phường]`

**UJ-1. Chị Lan báo một đống xà bần đổ trộm và biết nó đã được dọn.** `[CXM-3]`
Chị Lan bán hàng ở chợ. Chị đi ngang bãi đất trống gần nhà và thấy một đống xà bần lẫn nệm cũ mới đổ trộm. Chị đã có tài khoản Người dân. Chị mở app, chọn lĩnh vực Vệ sinh môi trường, loại "Rác thải trái phép", chụp hai ảnh, gõ một dòng mô tả. App lấy vị trí từ GPS và hiện ghim trên bản đồ để chị xác nhận. Chị đồng ý cho phường xử lý ảnh và vị trí, rồi gửi. App báo đã nhận ngay, không chờ AI. Hai ngày sau chị nhận thông báo phản ánh chuyển In Progress, rồi Completed kèm ảnh hiện trường sau khi dọn. **Edge case:** chị gửi một ảnh chụp từ hôm qua khi GPS đang tắt; app lấy vị trí từ EXIF của ảnh, và nếu ảnh không có EXIF thì yêu cầu chị ghim trên bản đồ. Nếu vị trí nằm ngoài phường Hòa Xuân, app không cho gửi và giải thích lý do.
Realizes FR-1, FR-6, FR-7, FR-8, FR-31, FR-32, FR-44.

**UJ-2. Anh Minh duyệt hàng chờ buổi sáng.** `[CXM-4]`
Anh Minh là cán bộ UBND phường được giao điều phối phản ánh hiện trường. Đầu giờ sáng anh mở WRMS trên web. Hàng chờ có sáu nhóm phản ánh mới, sắp theo mức ưu tiên. Nhóm đầu có ba phản ánh về cùng đống xà bần, gồm phản ánh của chị Lan; AI gợi ý mức Cao vì phát hiện rác xây dựng và rác cồng kềnh (Mức gợi ý là phần nghiên cứu; anh có thể bỏ qua). Anh xem phản ánh đại diện, lướt hai phản ánh còn lại, giữ mức Cao. Ở một nhóm khác, AI đề xuất gom hai phản ánh cống nghẹt cách nhau hai con hẻm; anh bác đề xuất gom. Một phản ánh có ảnh bị gắn cờ vì là ảnh chụp màn hình; anh từ chối kèm lý do. Với nhóm xà bần, anh tiếp nhận, rồi giao nhiệm vụ cho một nhóm xử lý hai người của một phòng ban, chọn anh Tuấn làm trưởng nhóm, hạn chót sau hai ngày. **Edge case:** AI Module lỗi lúc đêm; các phản ánh mới vẫn có trong hàng chờ với nhãn "chưa phân tích", và anh tự đặt mức ưu tiên.
Realizes FR-9, FR-10, FR-11, FR-12, FR-13, FR-14, FR-15, FR-16, FR-17, FR-18, FR-19, FR-24.

**UJ-3. Anh Tuấn dọn xong và bị trả lại một lần.** `[CXM-2]`
Anh Tuấn là cán bộ một phòng ban của phường, làm việc ngoài hiện trường bằng điện thoại. Anh nhận thông báo có nhiệm vụ mới, mở app, xem ảnh và vị trí, hạn chót, thành viên nhóm. Anh chấp nhận; phản ánh chuyển In Progress và chị Lan được báo. Chiều hôm sau, 24 giờ trước hạn chót, app nhắc anh nhiệm vụ sắp quá hạn. Anh cho người dọn, chụp ba ảnh sau xử lý và nộp minh chứng. Anh Minh xem và trả lại vì còn sót nệm cũ ở góc bãi. Anh Tuấn nhận thông báo kèm lý do, quay lại dọn nốt, nộp lại. Thành viên còn lại của nhóm chỉ xem và nhận thông báo.
Realizes FR-26, FR-29, FR-30, FR-33, FR-39, FR-42, FR-44.

**UJ-4. Anh Tuấn từ chối một nhiệm vụ không đúng chuyên môn.** `[CXM-2]`
Anh Tuấn được giao sửa một đèn đường hỏng. Phòng của anh không có thiết bị làm việc trên cao. Anh từ chối nhiệm vụ và ghi lý do. Anh Minh nhận thông báo, xét lý do, chấp nhận và giao lại cho cán bộ phòng ban khác. Anh Tuấn được báo kết quả xét. **Edge case:** nếu anh Minh không chấp nhận lý do, nhiệm vụ trở về anh Tuấn và anh phải tiếp tục.
Realizes FR-23, FR-25, FR-27, FR-28, FR-33, FR-34.

**UJ-5. Anh Minh nghiệm thu và cả ba người gửi đều được báo.** `[CXM-3]`
Anh Minh nhận thông báo có minh chứng nộp lại cho nhóm xà bần. Anh xem ảnh trước (từ các phản ánh) và ảnh sau (từ minh chứng) cạnh nhau, ghé hiện trường trên đường đi làm, rồi duyệt. Nhiệm vụ chuyển Approved, phản ánh chuyển Completed. Chị Lan và hai người gửi khác trong nhóm nhận thông báo kèm ảnh sau xử lý.
Realizes FR-30, FR-32, FR-34.

**UJ-6. Chị Hà thêm tài khoản cho cán bộ mới.** `[CXM-4]`
Chị Hà làm IT tại UBND phường. Một cán bộ phòng ban mới chuyển về; chị tạo tài khoản vai trò Cán bộ phòng ban, gán vào phòng ban, và giao thông tin đăng nhập ban đầu cho cán bộ đó. Cùng buổi, chị thêm một Loại phản ánh dưới lĩnh vực Trật tự đô thị theo đề nghị của anh Minh. Chị không xem được nội dung phản ánh, bản đồ hay thống kê.
Realizes FR-2, FR-3, FR-4, FR-5.

**UJ-7. Anh Minh xử lý một nhiệm vụ quá hạn.** `[CXM-2]`
Anh Minh mở danh sách nhiệm vụ, lọc theo quá hạn. Một nhiệm vụ cống nghẹt giao cho chị Thu đã quá hạn một ngày mà vẫn ở Assigned: chị Thu chưa chấp nhận cũng chưa từ chối. Anh gọi không được, nên thu hồi nhiệm vụ kèm lý do và giao lại cho anh Tuấn với hạn chót mới. Chị Thu và anh Tuấn đều nhận thông báo. Người gửi không nhận thông báo vì trạng thái phản ánh không đổi.
Realizes FR-22, FR-23, FR-25, FR-40, FR-43.

## 4. Thuật ngữ

Mọi phần còn lại của PRD dùng đúng các thuật ngữ này. Tên vai trò và trạng thái giữ tên tiếng Anh trong ngoặc để khớp addendum của brief và doc Tóm tắt nghiệp vụ.

**Vai trò và actor phụ**

- **Người dân (Resident)** — Cư dân tự đăng ký tài khoản, gửi phản ánh, theo dõi phản ánh của mình, bổ sung thông tin khi được yêu cầu. Dùng app mobile.
- **Cán bộ phường (Ward Officer)** — Cán bộ UBND phường điều phối toàn bộ nghiệp vụ: duyệt, tiếp nhận, từ chối, gom và tách nhóm, đặt Mức cuối, giao và thu hồi nhiệm vụ, xét lý do từ chối, xác minh và kiểm tra hiện trường, nghiệm thu, xem bản đồ điểm nóng, dashboard, thống kê. Dùng web.
- **Cán bộ phụ trách** — Cán bộ phường được ghi là người phụ trách một Nhóm phản ánh (FR-18). Nhận thông báo về Nhiệm vụ của Nhóm đó.
- **Cán bộ phòng ban (Task Assignee)** — Cán bộ một phòng ban của phường, nhận nhiệm vụ và xử lý ngoài hiện trường. Dùng app mobile. Không có tình nguyện viên.
- **Admin** — Người làm IT tại UBND phường, chỉ quản trị hệ thống: tài khoản, danh mục, phòng ban. Không truy cập phản ánh, bản đồ điểm nóng, dashboard, thống kê. Dùng web.
- **Tài khoản** — Mỗi tài khoản có đúng một vai trò. `[ASSUMPTION: mỗi tài khoản một vai trò; xem lại nếu CXM-4 cho thấy một người giữ hai vai trò]`
- **AI Module** — Dịch vụ riêng, nằm ngoài ranh giới hệ thống, chạy khi có phản ánh mới: sàng lọc ảnh, gom nhóm, gợi ý mức ưu tiên.
- **Notification Service** — Dịch vụ bên ngoài đẩy thông báo tới điện thoại của Người dân và Cán bộ phòng ban.
- **Map Service** — Dịch vụ bên ngoài cung cấp bản đồ, ghim vị trí và chuyển tọa độ thành địa chỉ.
- **System Timer** — Tác vụ định kỳ trên server: nhắc sắp quá hạn, báo quá hạn, xóa dữ liệu hết hạn.

**Danh mục và tổ chức**

- **Lĩnh vực (Domain)** — Cấp 1 của danh mục, ví dụ Vệ sinh môi trường, Trật tự đô thị, Đường và thoát nước, Chiếu sáng. Một Lĩnh vực có nhiều Loại phản ánh.
- **Loại phản ánh (Category)** — Cấp 2 của danh mục, thuộc đúng một Lĩnh vực.
- **Lĩnh vực thí điểm** — Lĩnh vực Vệ sinh môi trường, là Lĩnh vực duy nhất có Mức gợi ý. Xác định bằng mã cố định trong cấu hình, không bật tắt qua giao diện.
- **Phòng ban** — Phòng ban của UBND phường. `[ASSUMPTION: mỗi Cán bộ phòng ban thuộc đúng một Phòng ban]`
- **Khu vực** — Đơn vị địa bàn dưới phường, gán cho Phản ánh lúc gửi, dùng cho thống kê và cho dữ liệu còn giữ của phản ánh bị từ chối. Cấp chi tiết chưa chốt (§14, câu 6).

**Phản ánh**

- **Phản ánh** — Một lần Người dân gửi: một Loại phản ánh, mô tả, một hoặc nhiều ảnh, một vị trí. Thuộc đúng một Nhóm phản ánh.
- **Người gửi** — Người dân đã gửi một Phản ánh.
- **Nhóm phản ánh** — Tập một hoặc nhiều Phản ánh về cùng một hiện trường. Mọi Phản ánh thuộc đúng một Nhóm; phản ánh chưa gộp là nhóm một phần tử. Trạng thái phản ánh, Mức cuối và Nhiệm vụ gắn với Nhóm; mọi Phản ánh trong Nhóm cùng trạng thái.
- **Nhóm phản ánh đang mở** — Nhóm phản ánh ở Submitted, Received hoặc In Progress.
- **Đề xuất gom** — Liên kết chờ duyệt do AI Module tạo, nối một Phản ánh mới (vẫn ở nhóm một phần tử của nó) với một Nhóm phản ánh đang mở. Phản ánh chỉ vào Nhóm đó khi Cán bộ phường xác nhận.
- **Hàng chờ** — Danh sách các Nhóm phản ánh có ít nhất một Phản ánh ở Submitted, hoặc có Đề xuất gom chờ duyệt (FR-13).
- **Phản ánh đại diện** — Phản ánh được hiển thị đầu tiên cho một Nhóm (brief gọi là "phản ánh rõ nhất").
- **Sàng lọc** — Bước AI Module đánh giá từng ảnh và gắn cờ ảnh có thể không hợp lệ.
- **Ảnh bị gắn cờ** — Ảnh mà Sàng lọc đánh dấu là có thể không hợp lệ, kèm lý do. Chỉ Cán bộ phường quyết định ảnh đó có bị loại không.
- **Gom nhóm** — Bước AI Module tạo Đề xuất gom dựa trên vị trí, Loại phản ánh và ảnh.
- **Mức ưu tiên** — Một trong ba mức Thấp, Trung bình, Cao.
- **Mức gợi ý** — Mức ưu tiên do AI Module đề xuất, chỉ có ở Lĩnh vực thí điểm.
- **Mức cuối** — Mức ưu tiên do Cán bộ phường đặt, lưu riêng với Mức gợi ý, kèm người đặt và thời điểm.
- **Yêu cầu bổ sung** — Yêu cầu Cán bộ phường gửi cho Người gửi để bổ sung chữ hoặc ảnh vào chính Phản ánh của họ.
- **Xác minh hiện trường** — Việc Cán bộ phường kiểm tra hiện trường trước khi giao Nhiệm vụ, ghi kết quả vào Nhóm phản ánh (FR-20).
- **Kiểm tra hiện trường** — Việc Cán bộ phường kiểm tra hiện trường sau khi có Minh chứng, trước khi Nghiệm thu (FR-30).

**Nhiệm vụ**

- **Nhiệm vụ** — Việc Cán bộ phường giao để xử lý một Nhóm phản ánh, có đúng một Người nhận và một Hạn chót. Mỗi Nhóm có tối đa một Nhiệm vụ đang mở tại một thời điểm. `[ASSUMPTION: tối đa một Nhiệm vụ đang mở mỗi Nhóm]`
- **Nhiệm vụ đang mở** — Nhiệm vụ ở Assigned, Accepted, Submitted, Returned, hoặc ở Declined mà Cán bộ phường chưa xét lý do.
- **Nhiệm vụ quá hạn** — Nhiệm vụ ở Assigned, Accepted hoặc Returned đã qua Hạn chót. Nhiệm vụ ở Submitted không bị tính quá hạn khi đang chờ Nghiệm thu.
- **Người nhận** — Người duy nhất thao tác trên Nhiệm vụ: chính Cán bộ phòng ban được giao, hoặc Trưởng nhóm nếu giao cho Nhóm xử lý.
- **Nhóm xử lý** — Tập Cán bộ phòng ban do Cán bộ phường chọn lúc giao Nhiệm vụ, có đúng một Trưởng nhóm. Lập riêng cho từng Nhiệm vụ.
- **Trưởng nhóm** — Thành viên Nhóm xử lý là Người nhận. Thành viên khác chỉ xem và nhận thông báo. Không phải một vai trò riêng trong hệ thống.
- **Hạn chót** — Thời điểm Cán bộ phường đặt khi giao Nhiệm vụ. Thay cho bảng SLA (quyết định 8).
- **Minh chứng** — Ảnh sau xử lý (bắt buộc ít nhất một) và ghi chú do Người nhận nộp.
- **Nghiệm thu** — Quyết định cuối của Cán bộ phường về Minh chứng: duyệt hoặc trả lại làm lại kèm lý do.

### 4.1 Vòng đời

**Trạng thái phản ánh:** Submitted, Received, In Progress, Completed, Rejected. Trạng thái áp dụng cho cả Nhóm phản ánh, trừ Rejected áp dụng cho từng Phản ánh.

| Từ | Sang | Khi nào | Ai | FR |
| --- | --- | --- | --- | --- |
| – | Submitted | Người dân gửi phản ánh | Người dân | FR-6 |
| Submitted | Received | Cán bộ phường tiếp nhận Nhóm phản ánh | Cán bộ phường | FR-16 |
| Submitted | Received hoặc In Progress | Phản ánh được gộp vào một Nhóm đang ở trạng thái đó | Cán bộ phường | FR-10, FR-14 |
| Submitted | Rejected | Cán bộ phường từ chối một Phản ánh, kèm lý do. Trạng thái kết thúc | Cán bộ phường | FR-17 |
| Received | In Progress | Nhiệm vụ đầu tiên của Nhóm được chấp nhận (theo đơn đăng ký) | Người nhận | FR-26 |
| In Progress | Completed | Cán bộ phường duyệt Minh chứng | Cán bộ phường | FR-30 |

`[NOTE FOR PM: một Nhóm đã Received không có đường đóng nào ngoài giao Nhiệm vụ rồi Nghiệm thu, vì Rejected chỉ đi từ Submitted (quyết định 2). Nếu Xác minh hiện trường cho thấy không còn gì để xử lý, cán bộ phải giao một Nhiệm vụ hình thức. Cần hỏi phường trước khi thêm cách đóng khác.]`

**Trạng thái nhiệm vụ:** Assigned, Accepted, Declined, Submitted, Approved, Returned, Cancelled. Để tránh nhầm với phản ánh, PRD luôn viết "phản ánh ở Submitted" hoặc "nhiệm vụ ở Submitted". Addendum của brief có sáu trạng thái; Cancelled do PRD thêm (FR-43). `[ASSUMPTION: thêm trạng thái Cancelled để thu hồi Nhiệm vụ]`

| Từ | Sang | Khi nào | Ai | FR |
| --- | --- | --- | --- | --- |
| – | Assigned | Cán bộ phường giao Nhiệm vụ | Cán bộ phường | FR-23, FR-24, FR-25 |
| Assigned | Accepted | Người nhận chấp nhận | Người nhận | FR-26 |
| Assigned | Declined | Người nhận từ chối kèm lý do. Nhiệm vụ vẫn đang mở cho đến khi được xét | Người nhận | FR-27 |
| Declined | Accepted | Cán bộ phường không chấp nhận lý do; Người nhận phải tiếp tục | Cán bộ phường | FR-28 |
| Declined | (đóng, giữ Declined) | Cán bộ phường chấp nhận lý do. Cán bộ phường giao Nhiệm vụ mới cho người khác | Cán bộ phường | FR-28, FR-25 |
| Accepted hoặc Returned | Submitted | Người nhận nộp Minh chứng | Người nhận | FR-29 |
| Submitted | Approved | Cán bộ phường duyệt. Phản ánh sang Completed | Cán bộ phường | FR-30 |
| Submitted | Returned | Cán bộ phường trả lại kèm lý do. Phản ánh vẫn ở In Progress | Cán bộ phường | FR-30 |
| Assigned, Accepted hoặc Returned | Cancelled | Cán bộ phường thu hồi kèm lý do. Trạng thái kết thúc | Cán bộ phường | FR-43 |

`[ASSUMPTION: "người được giao tiếp tục" (addendum của brief) được hiểu là Nhiệm vụ chuyển từ Declined sang Accepted, không quay về Assigned]`

## 5. Tính năng

### 5.1 Tài khoản và danh mục (nhóm nghiệp vụ 1)

**Mô tả:** Người dân tự đăng ký trên app mobile. Tài khoản cán bộ (Cán bộ phường, Cán bộ phòng ban, Admin) do Admin tạo; cán bộ không tự đăng ký. Admin quản lý danh mục 2 cấp và Phòng ban. Mọi vai trò dùng chung đăng nhập, đổi mật khẩu, hồ sơ cá nhân. Realizes UJ-1, UJ-6.

#### FR-1: Người dân đăng ký tài khoản

Người dân có thể tự đăng ký tài khoản trên app mobile trước khi gửi phản ánh. Realizes UJ-1.

**Consequences (testable):**
- Người chưa đăng nhập không gửi được phản ánh; app chuyển sang màn hình đăng nhập hoặc đăng ký.
- Mỗi số điện thoại chỉ gắn với một tài khoản Người dân. `[ASSUMPTION: số điện thoại là định danh đăng ký, vì Cán bộ phường cần liên hệ Người gửi]` Có xác minh số điện thoại hay không là câu hỏi mở vì gửi SMS có chi phí (§14, câu 8).
- Tài khoản tạo qua đăng ký luôn có vai trò Người dân, không tự nâng lên vai trò khác.

#### FR-2: Đăng nhập, mật khẩu, hồ sơ cá nhân `[CXM-4]`

Mọi vai trò có thể đăng nhập, đăng xuất, đổi mật khẩu và sửa hồ sơ cá nhân của mình. Người dân có thể khôi phục mật khẩu. Realizes UJ-6.

**Consequences (testable):**
- Người dân và Cán bộ phòng ban đăng nhập trên app mobile; Cán bộ phường và Admin đăng nhập trên web. Tài khoản đăng nhập sai nền tảng nhận thông báo lỗi nêu đúng nền tảng cần dùng.
- Tài khoản bị Admin khóa không đăng nhập được, kể cả khi còn phiên cũ.
- Người dân khôi phục mật khẩu qua số điện thoại đã đăng ký; cách gửi mã phụ thuộc §14, câu 8. Cán bộ quên mật khẩu thì Admin đặt lại (FR-3).

#### FR-3: Admin quản lý tài khoản cán bộ `[CXM-4]` `[CXM-2]`

Admin có thể tạo, sửa, khóa, mở khóa và đặt lại mật khẩu cho tài khoản Cán bộ phường, Cán bộ phòng ban và Admin. Realizes UJ-6.

**Consequences (testable):**
- Admin tạo được cả tài khoản Admin khác. `[ASSUMPTION: Admin tạo được tài khoản Admin; doc Tóm tắt nghiệp vụ chỉ nói tài khoản cán bộ do Admin tạo]`
- Khi tạo tài khoản Cán bộ phòng ban, Admin phải chọn Phòng ban.
- Khi Admin khóa một Cán bộ phòng ban đang là Người nhận hoặc thành viên Nhóm xử lý của Nhiệm vụ đang mở, Admin thấy số Nhiệm vụ đó và Cán bộ phụ trách nhận thông báo để thu hồi và giao lại (FR-43, FR-25). `[ASSUMPTION: báo Cán bộ phụ trách khi khóa cán bộ có Nhiệm vụ đang mở]`
- Admin không xóa hẳn tài khoản đã có lịch sử thao tác; chỉ khóa. `[ASSUMPTION: chỉ khóa, không xóa, để giữ lịch sử truy vết]`

#### FR-4: Admin quản lý danh mục 2 cấp `[CXM-4]`

Admin có thể thêm, sửa, ẩn Lĩnh vực và Loại phản ánh. Realizes UJ-6. Quyết định 7.

**Consequences (testable):**
- Mỗi Loại phản ánh thuộc đúng một Lĩnh vực.
- Loại phản ánh bị ẩn không xuất hiện khi Người dân gửi phản ánh mới; phản ánh cũ thuộc loại đó vẫn hiển thị đúng tên loại.
- Lĩnh vực thí điểm không ẩn được và không đổi được mã; Admin chỉ đổi được tên hiển thị. Không có thao tác bật tắt AI trên giao diện Admin (quyết định 6).

#### FR-5: Admin quản lý phòng ban `[CXM-2]`

Admin có thể thêm, sửa, ẩn Phòng ban và xem danh sách cán bộ thuộc mỗi Phòng ban. Realizes UJ-6. Quyết định 9, chờ phường xác nhận.

**Consequences (testable):**
- Chỉ có Phòng ban của phường; không có loại "đơn vị phối hợp" ngoài phường.
- Phòng ban bị ẩn không xuất hiện khi Cán bộ phường chọn người nhận Nhiệm vụ mới.

**Out of Scope:** gán Phòng ban xử lý mặc định cho Loại phản ánh (quyết định 10).

### 5.2 Gửi phản ánh (nhóm nghiệp vụ 2)

**Mô tả:** Người dân chọn Loại phản ánh, viết mô tả, chụp hoặc chọn ảnh, xác nhận vị trí, đồng ý xử lý dữ liệu cá nhân và gửi. Hệ thống xác nhận đã nhận ngay, không chờ AI Module. Realizes UJ-1.

#### FR-6: Gửi phản ánh

Người dân có thể gửi một phản ánh gồm một Loại phản ánh, mô tả và một hoặc nhiều ảnh chụp trực tiếp hoặc chọn từ thư viện. Realizes UJ-1.

**Consequences (testable):**
- Không gửi được khi thiếu Loại phản ánh, thiếu ảnh hoặc thiếu vị trí.
- Số ảnh tối đa mỗi phản ánh là 5. `[ASSUMPTION: tối đa 5 ảnh mỗi phản ánh]`
- Sau khi gửi, phản ánh ở Submitted và xuất hiện trong danh sách phản ánh của Người gửi.
- Phản ánh được lưu và xác nhận cho Người gửi kể cả khi AI Module không phản hồi (FR-12, NFR-1).
- Gửi thất bại vì mất mạng thì phản ánh được giữ làm bản nháp trên điện thoại để gửi lại (NFR-10).

#### FR-7: Xác định vị trí

Người dân có thể xác định vị trí phản ánh bằng GPS của điện thoại, dữ liệu EXIF của ảnh, hoặc ghim trên bản đồ. Realizes UJ-1.

**Consequences (testable):**
- Thứ tự mặc định: GPS khi chụp trực tiếp; EXIF khi chọn ảnh từ thư viện; nếu cả hai không có, app yêu cầu ghim trên bản đồ. `[ASSUMPTION: thứ tự GPS, EXIF, ghim bản đồ]`
- Người dân luôn thấy ghim trên bản đồ và có thể kéo ghim trước khi gửi.
- Hệ thống hiển thị địa chỉ đọc được từ tọa độ (qua Map Service); nếu Map Service lỗi, vẫn gửi được với tọa độ.
- Hệ thống gán Khu vực cho Phản ánh từ tọa độ lúc gửi.
- Vị trí nằm ngoài ranh giới phường Hòa Xuân thì không gửi được, kèm thông báo giải thích. `[ASSUMPTION: chặn vị trí ngoài ranh giới phường]` Nguồn dữ liệu ranh giới còn mở (§14, câu 7).

#### FR-8: Đồng ý xử lý dữ liệu cá nhân khi gửi

Người dân phải đồng ý cho UBND phường xử lý ảnh, vị trí và thông tin liên hệ trước khi gửi phản ánh đầu tiên. Realizes UJ-1. Xem §8.1.

**Consequences (testable):**
- Nội dung đồng ý nêu mục đích xử lý, ai được xem, thời hạn ẩn rồi xóa dữ liệu chi tiết của phản ánh bị từ chối và ảnh bị loại (90 ngày, FR-41), và thời hạn lưu phản ánh khác. `[ASSUMPTION: giữ phản ánh không bị từ chối 24 tháng, làm giá trị tạm để viết được nội dung đồng ý]` Giá trị thật chờ §14, câu 10 và 11.
- Hệ thống lưu thời điểm và phiên bản nội dung mà Người dân đã đồng ý.
- Khi nội dung đồng ý đổi phiên bản, Người dân phải đồng ý lại trước lần gửi tiếp theo. `[ASSUMPTION: đổi phiên bản thì phải đồng ý lại]`

### 5.3 Phân tích tự động (nhóm nghiệp vụ 3)

**Mô tả:** Khi có Phản ánh mới, AI Module sàng lọc từng ảnh, tạo Đề xuất gom cho mọi Lĩnh vực, và đề xuất Mức gợi ý cho Lĩnh vực thí điểm. Mọi kết quả chỉ là gợi ý; Cán bộ phường quyết định. AI Module là dịch vụ riêng (quyết định 14), dùng model pretrained do nhóm tinh chỉnh, chạy trên server của dự án, không gọi AI API bên ngoài. Phần nghiên cứu và cách đánh giá ở §6. Realizes UJ-2.

#### FR-9: Sàng lọc ảnh không hợp lệ

AI Module có thể gắn cờ từng ảnh có thể không hợp lệ, kèm một trong ba lý do theo đơn đăng ký: không phải cảnh thật, không đọc được, hoặc lặp lại. Realizes UJ-2.

**Consequences (testable):**
- Mỗi Ảnh bị gắn cờ có đúng một lý do trong ba lý do trên.
- "Lặp lại" nghĩa là ảnh trùng với một ảnh khác đã có trong WRMS, cùng hoặc khác Phản ánh. `[ASSUMPTION: định nghĩa "lặp lại"]`
- Sàng lọc không bao giờ tự từ chối Phản ánh; Phản ánh có Ảnh bị gắn cờ vẫn vào Hàng chờ ở Submitted.
- Sàng lọc chạy cho mọi Lĩnh vực.

**Notes:** Sàng lọc đứng thứ hai trong thứ tự cắt giảm (§10.3). Nguồn ảnh không hợp lệ để huấn luyện và đánh giá chưa có (§14, câu 9).

#### FR-10: Gom nhóm phản ánh cùng hiện trường `[CXM-1]`

AI Module có thể tạo Đề xuất gom nối một Phản ánh mới với một Nhóm phản ánh đang mở, dựa trên vị trí, Loại phản ánh và ảnh. Realizes UJ-2.

**Consequences (testable):**
- Chỉ đề xuất gom vào Nhóm ở Submitted, Received hoặc In Progress; không gom vào Nhóm đã Completed.
- Trong khi Đề xuất gom chờ duyệt, Phản ánh mới vẫn ở nhóm một phần tử của nó, ở Submitted, và hiện trong Hàng chờ với nhãn "đề xuất gom". `[ASSUMPTION: Đề xuất gom là liên kết chờ duyệt, Phản ánh chưa vào Nhóm cho đến khi được xác nhận]`
- Khi Cán bộ phường xác nhận, Phản ánh vào Nhóm, nhận trạng thái của Nhóm (§4.1), và Người gửi được báo trạng thái đó. Khi Cán bộ phường bác, Phản ánh ở lại nhóm một phần tử.
- Ngưỡng khoảng cách, khoảng thời gian và độ giống ảnh là tham số chọn qua đánh giá ở §6, không cố định trong PRD.
- Đề xuất gom của AI và quyết định của Cán bộ phường lưu riêng, đủ để đo SM-2.

#### FR-11: Gợi ý mức ưu tiên cho Lĩnh vực thí điểm `[CXM-1]`

AI Module có thể nhận diện loại rác trong ảnh của phản ánh thuộc Lĩnh vực thí điểm và suy ra Mức gợi ý Thấp, Trung bình hoặc Cao từ độ đa dạng của rác và việc có rác đặc biệt (nguy hại, y tế, xây dựng, cồng kềnh). Đây là thành phần nghiên cứu (§6). Realizes UJ-2.

**Consequences (testable):**
- Mức gợi ý chỉ có cho phản ánh thuộc Lĩnh vực thí điểm; phản ánh thuộc Lĩnh vực khác không có Mức gợi ý.
- Mỗi Mức gợi ý đi kèm danh sách loại rác phát hiện được, để Cán bộ phường thấy lý do.
- Mức gợi ý của Nhóm phản ánh là mức cao nhất trong các Phản ánh của Nhóm. `[ASSUMPTION: Mức gợi ý của Nhóm lấy mức cao nhất]`
- Chạy lại AI Module chỉ cập nhật Mức gợi ý, không ghi đè Mức cuối đã đặt (quyết định 5).

#### FR-12: Tiếp nhận không phụ thuộc AI

Hệ thống có thể nhận và đưa Phản ánh vào Hàng chờ khi AI Module lỗi, quá thời gian, hoặc bị tắt để bảo trì. Realizes UJ-2.

**Consequences (testable):**
- Phản ánh hiện trong Hàng chờ ngay khi gửi, với nhãn "đang phân tích" cho đến khi có kết quả AI hoặc hết thời hạn ở NFR-2. Hết thời hạn thì nhãn đổi thành "chưa phân tích".
- Phản ánh "chưa phân tích" được phân tích lại khi AI Module hoạt động trở lại, nếu Phản ánh vẫn ở Submitted. `[ASSUMPTION: tự phân tích lại khi AI Module hoạt động trở lại]`
- Mọi thao tác của Cán bộ phường (tiếp nhận, từ chối, đặt Mức cuối, giao Nhiệm vụ) làm được trên Phản ánh "đang phân tích" hoặc "chưa phân tích".

### 5.4 Duyệt và tiếp nhận (nhóm nghiệp vụ 4)

**Mô tả:** Cán bộ phường làm việc với Hàng chờ: xem Phản ánh đại diện, xác nhận hoặc bác Đề xuất gom, tách hoặc gộp nhóm, quyết định Ảnh bị gắn cờ, tiếp nhận hoặc từ chối. Realizes UJ-2.

#### FR-13: Hàng chờ theo Nhóm phản ánh `[CXM-1]`

Cán bộ phường có thể xem Hàng chờ, mỗi Nhóm hiển thị Phản ánh đại diện, số Phản ánh trong Nhóm, Mức cuối hoặc Mức gợi ý (nếu có), số Ảnh bị gắn cờ, và các nhãn "đang phân tích", "chưa phân tích", "đề xuất gom". Realizes UJ-2.

**Consequences (testable):**
- Hàng chờ sắp mặc định theo Mức cuối, nếu chưa có thì theo Mức gợi ý, rồi theo thời gian gửi cũ nhất. Nhóm chưa có mức nào xếp như mức Trung bình. `[ASSUMPTION: thứ tự sắp Hàng chờ]`
- Lọc được theo Lĩnh vực, Loại phản ánh, Mức ưu tiên.
- Phản ánh đại diện mặc định là Phản ánh gửi sớm nhất trong số các Phản ánh không có Ảnh bị gắn cờ; nếu mọi Phản ánh đều có, thì là Phản ánh gửi sớm nhất. Cán bộ phường đổi được Phản ánh đại diện. `[ASSUMPTION: quy tắc chọn Phản ánh đại diện]`
- Từ một Nhóm, Cán bộ phường mở được mọi Phản ánh trong Nhóm và các Nhóm khác đang mở trong bán kính đặt trong cấu hình. `[ASSUMPTION: bán kính mặc định 100 m]`

#### FR-14: Xác nhận gom, tách và gộp nhóm thủ công `[CXM-1]`

Cán bộ phường có thể xác nhận hoặc bác một Đề xuất gom, tách một hoặc nhiều Phản ánh khỏi Nhóm phản ánh, và gộp hai Nhóm phản ánh thành một. Realizes UJ-2.

**Consequences (testable):**
- Phản ánh bị tách ra thành Nhóm mới một phần tử, ở Submitted.
- Gộp hai Nhóm chỉ làm được khi cả hai cùng ở Submitted, hoặc khi một Nhóm ở Submitted được gộp vào Nhóm đã Received hoặc In Progress. Khi đó các Phản ánh được gộp nhận trạng thái của Nhóm đích. `[ASSUMPTION: điều kiện gộp hai Nhóm]`
- Mỗi lần xác nhận, bác, tách hoặc gộp ghi người thao tác và thời điểm (FR-35).

#### FR-15: Quyết định Ảnh bị gắn cờ

Cán bộ phường có thể giữ hoặc loại từng Ảnh bị gắn cờ. Realizes UJ-2.

**Consequences (testable):**
- Ảnh bị loại không hiển thị cho Cán bộ phòng ban và không dùng làm ảnh trước khi Nghiệm thu.
- Ảnh bị loại được xóa theo FR-41.
- Nếu mọi ảnh của một Phản ánh bị loại: khi Nhóm chỉ gồm Phản ánh đó, Cán bộ phường không tiếp nhận được Nhóm và phải từ chối Phản ánh (FR-17); khi Nhóm còn Phản ánh khác có ảnh hợp lệ, Cán bộ phường từ chối Phản ánh đó, hoặc tiếp nhận Nhóm rồi gửi Yêu cầu bổ sung (FR-21).

#### FR-16: Tiếp nhận phản ánh

Cán bộ phường có thể tiếp nhận một Nhóm phản ánh, chuyển mọi Phản ánh trong Nhóm từ Submitted sang Received. Realizes UJ-2.

**Consequences (testable):**
- Mọi Người gửi trong Nhóm nhận thông báo Received (FR-32).
- Cán bộ phường tiếp nhận trở thành Cán bộ phụ trách Nhóm (FR-18).

#### FR-17: Từ chối phản ánh

Cán bộ phường có thể từ chối một Phản ánh ở Submitted, kèm lý do bắt buộc. Realizes UJ-2. Quyết định 2.

**Consequences (testable):**
- Phản ánh chuyển sang Rejected và không đổi trạng thái được nữa.
- Từ chối một Phản ánh trong Nhóm nhiều phần tử sẽ tách Phản ánh đó khỏi Nhóm; các Phản ánh còn lại giữ nguyên.
- Người gửi nhận thông báo kèm lý do (FR-32) và xem được lý do sau khi dữ liệu chi tiết đã bị xóa (FR-41).

#### FR-18: Cán bộ phụ trách Nhóm phản ánh `[CXM-4]`

Hệ thống có thể ghi một Cán bộ phụ trách cho mỗi Nhóm phản ánh đã Received. Realizes UJ-2.

**Consequences (testable):**
- Mọi Cán bộ phường thấy toàn bộ Hàng chờ. `[ASSUMPTION: mọi Cán bộ phường thấy toàn bộ Hàng chờ]`
- Cán bộ phụ trách là người nhận thông báo về Nhiệm vụ của Nhóm (FR-34).
- Cán bộ phường chuyển được quyền phụ trách cho mình hoặc cho Cán bộ phường khác, có ghi lịch sử. `[ASSUMPTION: chuyển được quyền phụ trách]`

**Notes:** `[NOTE FOR PM: khi có nhiều Cán bộ phường, ai chia phản ánh cho từng người vẫn là câu hỏi mở của nhóm. FR-18 chọn cách nhẹ nhất: ai tiếp nhận thì phụ trách. Đây chưa phải quyết định đã chốt. Nếu phường chỉ có một cán bộ điều phối, FR-18 gần như không cần.]`

### 5.5 Xử lý của cán bộ phường (nhóm nghiệp vụ 5)

**Mô tả:** Cán bộ phường đặt Mức cuối, có thể xác minh hiện trường và yêu cầu Người gửi bổ sung thông tin, rồi theo dõi Nhiệm vụ. Realizes UJ-2, UJ-7.

#### FR-19: Đặt Mức cuối

Cán bộ phường có thể đặt hoặc đổi Mức cuối của một Nhóm phản ánh, ở mọi Lĩnh vực, từ khi Nhóm còn ở Submitted. Realizes UJ-2. Quyết định 5, chờ phường xác nhận.

**Consequences (testable):**
- Mức gợi ý và Mức cuối lưu riêng; Mức cuối lưu kèm người đặt và thời điểm.
- Với Lĩnh vực thí điểm, giao diện hiển thị Mức gợi ý và loại rác phát hiện được cạnh ô chọn Mức cuối.
- Nhóm phải có Mức cuối trước khi giao Nhiệm vụ. `[ASSUMPTION: bắt buộc có Mức cuối trước khi giao]`
- Mỗi lần đổi Mức cuối ghi lịch sử (FR-35), để so Mức gợi ý với Mức cuối khi có thí điểm (SM-R1).

#### FR-20: Ghi nhận xác minh hiện trường

Cán bộ phường có thể ghi kết quả Xác minh hiện trường (ghi chú, ảnh) vào một Nhóm phản ánh ở Received.

**Consequences (testable):**
- Kết quả Xác minh hiện trường hiển thị cho Người nhận khi xem Nhiệm vụ (FR-42).
- Xác minh hiện trường không bắt buộc trước khi giao Nhiệm vụ. `[ASSUMPTION: Xác minh hiện trường không bắt buộc]`

#### FR-21: Yêu cầu bổ sung thông tin

Cán bộ phường có thể gửi Yêu cầu bổ sung cho Người gửi của một Phản ánh ở Received hoặc In Progress; Người gửi có thể trả lời bằng chữ và ảnh trong app. Quyết định 12.

**Consequences (testable):**
- Không gửi được Yêu cầu bổ sung cho Phản ánh ở Submitted, Completed hoặc Rejected.
- Thông tin bổ sung gắn vào đúng Phản ánh của Người gửi đó, kể cả khi Phản ánh đã thuộc một Nhóm nhiều phần tử.
- Người dân chỉ bổ sung được khi có Yêu cầu bổ sung đang mở; không có nút bổ sung tự do.
- Cán bộ phụ trách nhận thông báo khi Người gửi trả lời (FR-34).

#### FR-22: Theo dõi tiến độ Nhiệm vụ `[CXM-4]`

Cán bộ phường có thể xem trạng thái, Hạn chót và lịch sử của mọi Nhiệm vụ thuộc các Nhóm mình phụ trách, và đổi Hạn chót của Nhiệm vụ đang mở. Realizes UJ-7. Quyết định 8 và 13, chờ phường xác nhận.

**Consequences (testable):**
- Danh sách Nhiệm vụ lọc được theo trạng thái nhiệm vụ, Nhiệm vụ quá hạn, Nhiệm vụ sắp quá hạn.
- Đổi Hạn chót ghi lịch sử và báo cho Người nhận. `[ASSUMPTION: Cán bộ phường đổi được Hạn chót; brief và addendum không nói]`

### 5.6 Phân công nhiệm vụ (nhóm nghiệp vụ 6)

**Mô tả:** Cán bộ phường giao Nhiệm vụ cho một Cán bộ phòng ban hoặc cho một Nhóm xử lý, mỗi lần đặt một Hạn chót, và thu hồi Nhiệm vụ khi cần. Không có bảng SLA, không có Phòng ban xử lý mặc định. Toàn bộ nhóm nghiệp vụ này giả định Cán bộ phòng ban của phường là người xử lý ngoài hiện trường. Realizes UJ-2, UJ-4, UJ-7. `[CXM-2]`

#### FR-23: Giao Nhiệm vụ cho một Cán bộ phòng ban `[CXM-2]`

Cán bộ phường có thể giao Nhiệm vụ cho một Nhóm phản ánh ở Received hoặc In Progress, chọn một Cán bộ phòng ban làm Người nhận và đặt Hạn chót. Realizes UJ-4, UJ-7. Quyết định 8, chờ phường xác nhận.

**Consequences (testable):**
- Không giao được khi thiếu Hạn chót, hoặc Hạn chót ở quá khứ.
- Không giao được khi Nhóm đã có một Nhiệm vụ đang mở.
- Nhiệm vụ ở Assigned; Người nhận nhận thông báo (FR-33).
- Danh sách chọn Người nhận lọc được theo Phòng ban và hiển thị số Nhiệm vụ đang mở của mỗi người. `[ASSUMPTION: hiển thị số Nhiệm vụ đang mở khi chọn Người nhận]`

#### FR-24: Giao Nhiệm vụ cho Nhóm xử lý `[CXM-2]`

Cán bộ phường có thể giao Nhiệm vụ cho một Nhóm xử lý, chọn các thành viên và đúng một Trưởng nhóm làm Người nhận. Realizes UJ-2. Quyết định 16.

**Consequences (testable):**
- Nhóm xử lý có ít nhất hai Cán bộ phòng ban, có thể thuộc nhiều Phòng ban khác nhau. `[ASSUMPTION: Nhóm xử lý tối thiểu hai người, được khác Phòng ban]`
- Chỉ Trưởng nhóm chấp nhận, từ chối và nộp Minh chứng được; thành viên khác thấy Nhiệm vụ ở chế độ chỉ xem (FR-42).
- Mọi thành viên Nhóm xử lý nhận thông báo của Nhiệm vụ (FR-33).

#### FR-25: Giao lại Nhiệm vụ `[CXM-2]`

Cán bộ phường có thể giao một Nhiệm vụ mới cho Nhóm phản ánh sau khi Nhiệm vụ trước đã đóng ở Declined (lý do được chấp nhận) hoặc Cancelled. Realizes UJ-4, UJ-7.

**Consequences (testable):**
- Nhiệm vụ mới có Người nhận và Hạn chót mới; Nhiệm vụ cũ giữ nguyên trong lịch sử.
- Phản ánh giữ trạng thái hiện tại (Received hoặc In Progress) khi giao lại.

#### FR-43: Thu hồi Nhiệm vụ `[CXM-2]`

Cán bộ phường có thể thu hồi một Nhiệm vụ ở Assigned, Accepted hoặc Returned, kèm lý do bắt buộc. Realizes UJ-7.

**Consequences (testable):**
- Nhiệm vụ chuyển sang Cancelled và không đổi trạng thái được nữa.
- Người nhận và thành viên Nhóm xử lý nhận thông báo kèm lý do (FR-33).
- Phản ánh giữ trạng thái hiện tại; Người gửi không nhận thông báo.
- Không thu hồi được Nhiệm vụ ở Submitted; Cán bộ phường phải Nghiệm thu trước (FR-30).

### 5.7 Nhận hoặc từ chối nhiệm vụ (nhóm nghiệp vụ 7)

**Mô tả:** Cán bộ phòng ban xem nhiệm vụ của mình. Người nhận chấp nhận Nhiệm vụ hoặc từ chối kèm lý do. Cán bộ phường xét lý do. Realizes UJ-3, UJ-4. `[CXM-2]`

#### FR-42: Cán bộ phòng ban xem nhiệm vụ của mình `[CXM-2]`

Cán bộ phòng ban có thể xem danh sách và chi tiết các Nhiệm vụ mà mình là Người nhận hoặc thành viên Nhóm xử lý. Realizes UJ-3.

**Consequences (testable):**
- Danh sách lọc được theo trạng thái nhiệm vụ và Nhiệm vụ quá hạn.
- Chi tiết Nhiệm vụ gồm: ảnh trước (trừ ảnh bị loại), vị trí trên bản đồ, mô tả, Loại phản ánh, Mức cuối, Hạn chót, kết quả Xác minh hiện trường (nếu có), lý do các lần bị trả lại, thành viên Nhóm xử lý.
- Thành viên không phải Trưởng nhóm thấy chi tiết nhưng không có nút thao tác.

#### FR-26: Chấp nhận Nhiệm vụ `[CXM-2]`

Người nhận có thể chấp nhận một Nhiệm vụ ở Assigned. Realizes UJ-3.

**Consequences (testable):**
- Nhiệm vụ chuyển sang Accepted.
- Nếu Nhóm phản ánh đang ở Received, mọi Phản ánh trong Nhóm chuyển sang In Progress và mọi Người gửi nhận thông báo.

#### FR-27: Từ chối Nhiệm vụ kèm lý do `[CXM-2]`

Người nhận có thể từ chối một Nhiệm vụ ở Assigned, kèm lý do bắt buộc. Realizes UJ-4.

**Consequences (testable):**
- Nhiệm vụ chuyển sang Declined và vẫn là Nhiệm vụ đang mở cho đến khi được xét; không từ chối được khi thiếu lý do.
- Cán bộ phụ trách nhận thông báo cần xét lý do (FR-34).
- Không từ chối được Nhiệm vụ đã Accepted. `[ASSUMPTION: chỉ từ chối được ở Assigned]`

#### FR-28: Xét lý do từ chối `[CXM-2]`

Cán bộ phường có thể chấp nhận hoặc không chấp nhận lý do từ chối của một Nhiệm vụ ở Declined. Realizes UJ-4.

**Consequences (testable):**
- Chấp nhận: Nhiệm vụ đóng, giữ Declined; Cán bộ phường được đưa tới bước giao lại (FR-25).
- Không chấp nhận: Nhiệm vụ chuyển sang Accepted với cùng Người nhận và Hạn chót.
- Người nhận nhận thông báo kết quả xét trong cả hai trường hợp (FR-33).

### 5.8 Nghiệm thu (nhóm nghiệp vụ 8)

**Mô tả:** Người nhận nộp Minh chứng có ảnh sau xử lý. Cán bộ phường kiểm tra hiện trường, so ảnh trước và sau, rồi duyệt hoặc trả lại. Nghiệm thu là quyết định cuối; Admin không tham gia (quyết định 1). Realizes UJ-3, UJ-5. `[CXM-3]`

#### FR-29: Nộp Minh chứng `[CXM-2]` `[CXM-3]`

Người nhận có thể nộp Minh chứng cho một Nhiệm vụ ở Accepted hoặc Returned. Realizes UJ-3.

**Consequences (testable):**
- Không nộp được khi không có ít nhất một ảnh sau xử lý.
- Ảnh Minh chứng phải chụp trực tiếp trong app, kèm vị trí GPS và thời điểm chụp. `[ASSUMPTION: ảnh Minh chứng phải chụp trực tiếp, để chống nộp ảnh cũ]`
- Nhiệm vụ chuyển sang Submitted; Cán bộ phụ trách nhận thông báo (FR-34).
- Nộp thất bại vì mất mạng thì Minh chứng được giữ làm bản nháp để nộp lại (NFR-10).

#### FR-30: Kiểm tra hiện trường và Nghiệm thu `[CXM-2]` `[CXM-3]`

Cán bộ phường có thể xem ảnh trước (từ các Phản ánh trong Nhóm) và ảnh sau (từ Minh chứng) cạnh nhau, ghi kết quả Kiểm tra hiện trường, rồi duyệt hoặc trả lại Nhiệm vụ ở Submitted. Realizes UJ-3, UJ-5. Quyết định 1.

**Consequences (testable):**
- Duyệt: Nhiệm vụ chuyển sang Approved; mọi Phản ánh trong Nhóm chuyển sang Completed; mọi Người gửi nhận thông báo kèm ít nhất một ảnh sau xử lý.
- Trả lại: bắt buộc có lý do; Nhiệm vụ chuyển sang Returned; Phản ánh giữ In Progress; Người nhận nhận thông báo kèm lý do.
- Kết quả Kiểm tra hiện trường (ghi chú, ảnh) lưu cùng quyết định Nghiệm thu, nhưng không bắt buộc ghi trước khi duyệt. `[ASSUMPTION: không bắt buộc ghi kết quả Kiểm tra hiện trường]`

### 5.9 Theo dõi và thông báo (nhóm nghiệp vụ 9)

**Mô tả:** Người dân tự tra cứu tiến độ phản ánh của mình. Hệ thống thông báo cho từng vai trò theo sự kiện, và lưu mọi thông báo trong app. Mọi thay đổi trạng thái được ghi lịch sử. Realizes UJ-1, UJ-3, UJ-5.

#### FR-31: Người dân tra cứu tiến độ `[CXM-3]`

Người dân có thể xem danh sách phản ánh mình đã gửi, trạng thái hiện tại, các mốc thời gian đổi trạng thái, lý do từ chối (nếu có) và ảnh sau xử lý khi Completed. Realizes UJ-1.

**Consequences (testable):**
- Người dân chỉ thấy phản ánh của chính mình; không thấy Phản ánh của Người gửi khác trong cùng Nhóm, kể cả ảnh. `[ASSUMPTION: Người dân không thấy Phản ánh của người khác trong cùng Nhóm]`
- Người dân không thấy tên Cán bộ phòng ban, Phòng ban hay nội dung Nhiệm vụ. `[ASSUMPTION: Người dân không thấy thông tin Nhiệm vụ]`

#### FR-32: Thông báo cho Người gửi `[CXM-3]`

Hệ thống có thể gửi thông báo cho Người gửi ở mỗi lần trạng thái phản ánh đổi, kể cả Người gửi của các Phản ánh đã gộp nhóm. Realizes UJ-1, UJ-5.

**Consequences (testable):**
- Có thông báo khi phản ánh sang Received, In Progress, Completed (kèm ảnh sau xử lý), Rejected (kèm lý do), và khi có Yêu cầu bổ sung.
- Mỗi Người gửi trong một Nhóm n phần tử nhận đúng một thông báo cho mỗi lần đổi trạng thái.

#### FR-33: Thông báo cho Cán bộ phòng ban `[CXM-2]`

Hệ thống có thể gửi thông báo cho Người nhận và thành viên Nhóm xử lý theo sự kiện của Nhiệm vụ. Realizes UJ-3, UJ-4. Quyết định 11.

**Consequences (testable):**
- Có thông báo cho bốn sự kiện của quyết định 11: có Nhiệm vụ mới; có kết quả xét lý do từ chối; bị trả lại (kèm lý do); sắp quá hạn (FR-39).
- Có thêm thông báo khi Hạn chót đổi (FR-22) và khi Nhiệm vụ bị thu hồi (FR-43). `[ASSUMPTION: thêm hai sự kiện ngoài quyết định 11]`
- Thông báo mở thẳng tới Nhiệm vụ liên quan trong app.

#### FR-34: Thông báo cho Cán bộ phường `[CXM-4]`

Hệ thống có thể thông báo cho Cán bộ phụ trách khi Minh chứng được nộp, khi Nhiệm vụ bị từ chối, khi Nhiệm vụ quá hạn, và khi Người gửi trả lời Yêu cầu bổ sung. Realizes UJ-4, UJ-5. Quyết định 11, 13.

**Consequences (testable):**
- Thông báo cho Cán bộ phường hiển thị trong web, kèm số chưa đọc. `[ASSUMPTION: cán bộ phường chỉ nhận thông báo trong web, không email hay SMS trong v1]` Nếu Cán bộ phường ít mở web, có thể nâng lên email hoặc web push; hỏi ở buổi làm việc (CXM-4).
- Thông báo về Nhiệm vụ bị từ chối và Nhiệm vụ quá hạn hiển thị cho đến khi được xử lý. `[ASSUMPTION: thông báo cần xử lý không tự ẩn]`

#### FR-44: Danh sách thông báo trong app

Người dân và Cán bộ phòng ban có thể xem lại mọi thông báo đã nhận trong app, đánh dấu đã đọc, và mở phản ánh hoặc nhiệm vụ liên quan. Realizes UJ-1, UJ-3.

**Consequences (testable):**
- Mọi thông báo ở FR-32 và FR-33 có trong danh sách, kể cả khi thông báo đẩy không đến được (NFR-6).
- Danh sách hiển thị số chưa đọc.

#### FR-45: Người dân đánh giá kết quả xử lý

Người gửi có thể đánh giá kết quả xử lý phản ánh của mình từ 1 đến 5 sao khi phản ánh ở Completed. Realizes UJ-1.

**Consequences (testable):**
- Chỉ đánh giá được khi phản ánh ở Completed. Mỗi Người gửi đánh giá một lần cho mỗi phản ánh của mình, kể cả Người gửi các Phản ánh đã gộp nhóm. `[ASSUMPTION: mỗi Người gửi đánh giá một lần, không sửa]`
- Điểm là số nguyên từ 1 đến 5. Người gửi có thể không đánh giá.
- Cán bộ phường xem được điểm ở chi tiết Nhóm phản ánh và điểm trung bình ở thống kê (FR-37). `[ASSUMPTION: điểm hiển thị cho Cán bộ phường ở chi tiết Nhóm và ở FR-37]`
- Điểm thấp không mở lại phản ánh; phản ánh vẫn ở Completed (§9).

#### FR-35: Lịch sử phản ánh và nhiệm vụ

Hệ thống có thể ghi mọi thay đổi trạng thái phản ánh, trạng thái nhiệm vụ, Mức cuối, Hạn chót, quyền phụ trách, Đề xuất gom, tách hoặc gộp nhóm, kèm người thao tác và thời điểm. Cán bộ phường xem được lịch sử đầy đủ của Nhóm phản ánh.

**Consequences (testable):**
- Lịch sử không sửa hay xóa được qua giao diện, kể cả bởi Admin.
- Đủ dữ liệu để tính thời gian từ gửi đến Completed và các số liệu ở FR-38.

### 5.10 Bản đồ điểm nóng, dashboard và thống kê (nhóm nghiệp vụ 10)

**Mô tả:** Chỉ Cán bộ phường dùng; Admin không truy cập (quyết định 3). Bản đồ điểm nóng là thành phần đầu tiên bị cắt nếu trễ tiến độ (§10.3). Giá trị của nhóm nghiệp vụ này phụ thuộc lượng phản ánh thực tế.

#### FR-36: Bản đồ điểm nóng `[CXM-1]`

Cán bộ phường có thể xem bản đồ mật độ phản ánh trong phường, lọc theo Lĩnh vực, Loại phản ánh, trạng thái phản ánh và khoảng thời gian.

**Consequences (testable):**
- Phản ánh Rejected đã bị xóa dữ liệu chi tiết hiển thị theo Khu vực, không theo tọa độ chính xác.
- Nhấn vào một điểm mở được Nhóm phản ánh tương ứng.

#### FR-37: Dashboard và thống kê `[CXM-1]`

Cán bộ phường có thể xem số liệu theo Loại phản ánh, trạng thái phản ánh, Mức ưu tiên, Khu vực, thời gian xử lý, Nhiệm vụ quá hạn và phản ánh bị từ chối, trong một khoảng thời gian chọn được.

**Consequences (testable):**
- Thời gian xử lý tính từ lúc Nhóm sang Received đến lúc sang Completed. `[ASSUMPTION: định nghĩa thời gian xử lý]`
- Mọi con số trên dashboard tính lại được từ lịch sử (FR-35).
- Số liệu phản ánh bị từ chối vẫn đúng sau khi dữ liệu chi tiết đã bị xóa (FR-41).
- Có điểm đánh giá trung bình của Người gửi (FR-45) theo Loại phản ánh và Khu vực.

#### FR-38: Số liệu đo tiêu chí thành công

Hệ thống có thể ghi và xuất số liệu cần cho SM-1 đến SM-4, và xuất lịch sử (FR-35) để tính SM-R4.

**Consequences (testable):**
- Ghi thời điểm Cán bộ phường mở và đóng chi tiết từng Phản ánh trong Nhóm trước khi tiếp nhận hoặc từ chối, để tính thời gian xem thực và số Phản ánh được mở mỗi Nhóm (SM-1).
- Ghi Đề xuất gom của AI và Nhóm cuối cùng sau khi Cán bộ phường xác nhận, bác, tách, gộp (SM-2).
- Ghi thời điểm của lần nộp Minh chứng được duyệt, để so với Hạn chót (SM-3).
- Ghi lần đầu Người gửi mở phản ánh sau khi phản ánh sang Completed (SM-4).
- Số liệu xuất ra dạng bảng CSV để nhóm phân tích ngoài hệ thống. `[ASSUMPTION: xuất CSV]`

### 5.11 Tác vụ tự động theo thời gian (nhóm nghiệp vụ 11)

**Mô tả:** System Timer chạy định kỳ để nhắc hạn, báo quá hạn và xóa dữ liệu hết hạn. Realizes UJ-3, UJ-7.

#### FR-39: Nhắc sắp quá hạn `[CXM-2]`

System Timer có thể nhắc Người nhận và thành viên Nhóm xử lý khi một Nhiệm vụ ở Assigned, Accepted hoặc Returned còn 24 giờ đến Hạn chót. Realizes UJ-3. Quyết định 11.

**Consequences (testable):**
- Mốc nhắc mặc định 24 giờ, đặt trong cấu hình. `[ASSUMPTION: mốc 24 giờ là đề xuất trong quyết định 11, chưa chốt]`
- Nhiệm vụ có Hạn chót cách lúc giao dưới 24 giờ được nhắc ngay khi giao. `[ASSUMPTION: Hạn chót gần thì nhắc ngay]`
- Mỗi Nhiệm vụ chỉ nhận một lần nhắc cho mỗi Hạn chót. Nhiệm vụ ở Submitted, Declined, Approved, Cancelled không được nhắc.

#### FR-40: Báo quá hạn `[CXM-2]`

System Timer có thể đánh dấu Nhiệm vụ quá hạn và báo cho Cán bộ phụ trách. Realizes UJ-7. Quyết định 11.

**Consequences (testable):**
- Nhiệm vụ quá hạn hiển thị nhãn quá hạn trong danh sách của Cán bộ phường (FR-22) và của Cán bộ phòng ban (FR-42).
- Thông báo quá hạn gửi một lần cho mỗi Hạn chót.
- Nhiệm vụ ở Submitted đang chờ Nghiệm thu không bị đánh dấu quá hạn. Nếu bị Returned sau Hạn chót, Nhiệm vụ quá hạn ngay; Cán bộ phường nên đổi Hạn chót khi trả lại.

#### FR-41: Ẩn và xóa dữ liệu hết hạn

Phản ánh Rejected và ảnh bị Cán bộ phường loại (FR-15) bị ẩn ngay khỏi mọi màn hình. Sau 90 ngày, System Timer xóa ảnh, mô tả và tọa độ chính xác của chúng. Quyết định 15, đổi ngày 23/10/2026: mốc xóa hẳn sau 48 giờ đổi thành ẩn 90 ngày rồi xóa.

**Consequences (testable):**
- Trong 90 ngày kể từ lúc Cán bộ phường từ chối phản ánh hoặc loại ảnh, ảnh, mô tả và tọa độ chính xác không hiển thị ở Hàng chờ, bản đồ, thống kê hay app của Người dân.
- Trong 90 ngày đó, Cán bộ phường mở lại được dữ liệu đang ẩn khi cần trả lời khiếu nại, và mỗi lần mở được ghi lịch sử (FR-35). `[ASSUMPTION: chỉ Cán bộ phường mở lại được dữ liệu đang ẩn, có ghi lịch sử]`
- Sau khi xóa, Phản ánh Rejected vẫn giữ Loại phản ánh, lý do từ chối, thời điểm và Khu vực; Người gửi vẫn xem được lý do.
- Ảnh bị gắn cờ mà Cán bộ phường chưa quyết định thì không bị ẩn hay xóa. `[ASSUMPTION: ảnh gắn cờ chưa quyết định không bị ẩn hay xóa]`
- Dữ liệu đã xóa không khôi phục được và không xuất hiện trong bản sao lưu tạo sau thời điểm xóa. `[ASSUMPTION: cách xử lý bản sao lưu cũ chốt ở kiến trúc]`
- Phản ánh Rejected và ảnh bị loại không được dùng làm dữ liệu huấn luyện hay đánh giá, kể cả trong 90 ngày ẩn. Quy tắc này loại luôn một nguồn ảnh không hợp lệ có thể dùng cho Sàng lọc (§14, câu 9).

**Căn cứ:** mốc 90 ngày lấy theo thời hiệu khiếu nại 90 ngày của Luật Khiếu nại 2011, để phường còn dữ liệu nếu Người gửi khiếu nại việc bị từ chối. WRMS không xử lý khiếu nại (§8.3). Việc giữ và xóa dữ liệu tuân theo Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 và Nghị định 356/2025/NĐ-CP (§8.1). `[NOTE FOR PM: cần GVHD hoặc phường xác nhận việc từ chối một phản ánh hiện trường có thuộc diện khiếu nại theo Luật Khiếu nại 2011 không. Nếu không, mốc 90 ngày vẫn dùng được như một lựa chọn thiết kế, nhưng phải bỏ phần căn cứ này.]`

## 6. Thành phần nghiên cứu

Phần này mô tả phần nghiên cứu của đồ án, không phải yêu cầu của phường. Chi tiết so sánh với đơn đăng ký có trong addendum của PRD.

**Câu hỏi nghiên cứu**

- RQ-1: Nhận diện được các loại rác thường và rác đặc biệt (nguy hại, y tế, xây dựng, cồng kềnh) trong ảnh hiện trường chụp tại Hòa Xuân với độ chính xác bao nhiêu, khi model chỉ huấn luyện trên dataset công khai? (FR-11)
- RQ-2: Tiêu chí ưu tiên dựa trên độ đa dạng của rác và việc có rác đặc biệt khớp với nhãn do người gán đến mức nào? (FR-11)
- RQ-3: Gom theo vị trí, Loại phản ánh và ảnh có tốt hơn gom chỉ theo vị trí không? (FR-10)
- RQ-4: Sàng lọc phát hiện ảnh không hợp lệ với độ chính xác bao nhiêu? (FR-9)

**Dữ liệu**

- Huấn luyện: dataset công khai (Kaggle, Hugging Face…). Nghiên cứu nền ghi nhận TACO và TrashNet không giống ảnh đường phố Việt Nam; UrbanDumpSight (ảnh bãi rác đường phố) là ứng viên cần kiểm tra giấy phép.
- Đánh giá: ảnh nhóm tự chụp ở nơi công cộng tại Hòa Xuân, mỗi điểm nhiều góc, không dùng khi huấn luyện.
- Nhãn loại rác và Mức ưu tiên: nhóm viết tiêu chí và tự gán, GVHD duyệt tiêu chí. Cán bộ phường xác nhận lại nếu phường duyệt đề tài.
- Nhãn hiện trường: các ảnh chụp cùng một điểm mang cùng một nhãn hiện trường, làm đáp án cho Gom nhóm.
- Nhãn hợp lệ: nhóm tự dựng thêm ảnh không hợp lệ (ảnh chụp màn hình, ảnh mờ, ảnh lặp) cho tập đánh giá Sàng lọc. `[ASSUMPTION: nhóm tự dựng ảnh không hợp lệ cho tập đánh giá]` Nguồn ảnh không hợp lệ cho huấn luyện vẫn mở (§14, câu 9).

**Quy tắc đánh giá**

- Tiêu chí ưu tiên và nhãn của tập đánh giá chốt trước khi chạy model trên tập đánh giá, để tránh chỉnh tiêu chí cho khớp kết quả model (SM-C4).
- Hạn chế: quy tắc suy ra Mức gợi ý và nhãn của tập đánh giá đều do nhóm viết. Vì vậy RQ-2 và SM-R1 chủ yếu đo độ chính xác nhận diện rác sau khi qua quy tắc, chưa đo được tiêu chí có giống cách phường xếp ưu tiên không. Để giảm vòng tự đo, một người ngoài nhóm (GVHD hoặc sinh viên khác) gán nhãn độc lập một phần tập đánh giá theo cùng tiêu chí, và nhóm báo mức đồng thuận giữa những người gán. `[ASSUMPTION: có người ngoài nhóm gán nhãn độc lập]`
- Thước đo: SM-R1 dùng weighted kappa và recall của mức Cao; SM-R2 dùng precision và recall theo cặp phản ánh; SM-R3 dùng precision và recall của cờ. `[ASSUMPTION: thước đo cụ thể cho SM-R1 đến SM-R3, chờ GVHD duyệt]`
- Báo cáo độ chính xác đo được, kể cả khi thấp. `[NOTE FOR PM: AI chỉ gợi ý nên hiện không có ngưỡng tối thiểu để đưa Mức gợi ý vào hệ thống. Nên đặt cùng GVHD một ngưỡng (ví dụ recall của mức Cao); dưới ngưỡng đó thì ẩn Mức gợi ý trong thí điểm để không làm sai lệch quyết định của cán bộ.]`
- Ngưỡng của model chỉnh theo góp ý của Cán bộ phường nếu có thí điểm.

**Sản phẩm đầu ra của nghiên cứu**

1. AI Module gồm Sàng lọc, Gom nhóm, nhận diện rác, kèm kết quả đánh giá.
2. Bộ ảnh đánh giá tự chụp tại Hòa Xuân, có nhãn hiện trường, hợp lệ, loại rác và Mức ưu tiên. Có công bố bộ ảnh hay không là câu hỏi mở (§14, câu 19) vì ảnh có thể chứa dữ liệu cá nhân.
3. Tiêu chí ưu tiên và ngưỡng Gom nhóm đã đánh giá.
4. Báo cáo đánh giá và báo cáo đồ án.

**Còn mở:** cỡ tập đánh giá; nguồn ảnh không hợp lệ cho huấn luyện (§14, câu 9); cách xử lý mặt người và biển số trong ảnh nhóm tự chụp (§8.1).

## 7. Yêu cầu phi chức năng xuyên suốt

- **NFR-1 Phản hồi khi gửi.** Sau khi tải ảnh xong, app xác nhận đã nhận phản ánh trong 5 giây ở 95% lần gửi, không chờ AI Module. `[ASSUMPTION: 5 giây ở 95% lần gửi]`
- **NFR-2 Thời gian phân tích.** AI Module trả kết quả cho 95% Phản ánh trong 2 phút khi đang hoạt động. Quá 10 phút thì Phản ánh mang nhãn "chưa phân tích" (FR-12). `[ASSUMPTION: 2 phút ở 95% phản ánh, hết hạn sau 10 phút]`
- **NFR-3 Quy mô.** Hệ thống chạy ổn với tối đa 50 phản ánh mỗi ngày và 20 tài khoản cán bộ dùng đồng thời. Đây là mức dự phòng; ước lượng của brief chỉ khoảng 9 phản ánh mỗi tháng. `[ASSUMPTION: 50 phản ánh mỗi ngày, 20 cán bộ đồng thời]` `[CXM-1]` `[CXM-4]`
- **NFR-4 Phân quyền.** `[CXM-4]` Mỗi API và màn hình kiểm tra vai trò. Admin không đọc được nội dung phản ánh, ảnh, bản đồ điểm nóng, dashboard, thống kê. Người dân chỉ đọc được phản ánh của mình. Cán bộ phòng ban chỉ đọc được Nhóm phản ánh của Nhiệm vụ mình là Người nhận hoặc thành viên Nhóm xử lý. `[ASSUMPTION: Cán bộ phòng ban không xem Hàng chờ chung]`
- **NFR-5 Bảo mật.** Mọi kết nối dùng HTTPS. Mật khẩu lưu dạng băm. Ảnh chỉ tải được qua đường dẫn có kiểm tra quyền, không có đường dẫn công khai. Phiên web hết sau 8 giờ không hoạt động; tài khoản bị khóa đăng nhập 15 phút sau 5 lần nhập sai liên tiếp. `[ASSUMPTION: phiên web 8 giờ, khóa 15 phút sau 5 lần sai]`
- **NFR-6 Thông báo dự phòng.** Thông báo đẩy không đến được thì vẫn có trong danh sách thông báo trong app (FR-44) hoặc trên web (FR-34).
- **NFR-7 Ngôn ngữ và nền tảng.** Giao diện tiếng Việt. App mobile theo cỡ chữ hệ thống của điện thoại. Web chạy trên Chrome và Edge bản mới, màn hình rộng từ 1366 px. `[ASSUMPTION: cỡ chữ hệ thống; Chrome và Edge; màn hình từ 1366 px]` App hỗ trợ Android, iOS hay cả hai còn mở (§14, câu 8).
- **NFR-8 AI chạy nội bộ.** Không gửi ảnh, vị trí hay mô tả ra AI API bên ngoài. Map Service và Notification Service chỉ nhận tọa độ và nội dung thông báo cần cho chức năng của chúng.
- **NFR-9 Ghi log.** Lỗi và thời gian xử lý của AI Module được ghi lại, đủ để tính NFR-2 và hỗ trợ đánh giá ở §6.
- **NFR-10 Mạng yếu.** App nén mỗi ảnh về tối đa 2 MB trước khi tải. Gửi phản ánh hoặc nộp Minh chứng thất bại thì giữ bản nháp trên điện thoại và cho thử lại. `[ASSUMPTION: nén ảnh về tối đa 2 MB]`
- **NFR-11 Sao lưu.** Dữ liệu được sao lưu hằng ngày, giữ 14 ngày; nhóm chạy thử khôi phục một lần trước thí điểm. `[ASSUMPTION: sao lưu hằng ngày, giữ 14 ngày]`

## 8. Ràng buộc

### 8.1 Dữ liệu cá nhân

Ảnh và vị trí của người dân là dữ liệu cá nhân theo Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 và Nghị định 356/2025/NĐ-CP, hiệu lực từ 01/01/2026.

- Đồng ý khi gửi phản ánh (FR-8).
- Ẩn ảnh, mô tả, tọa độ chính xác của phản ánh bị từ chối và ảnh bị loại trong 90 ngày, rồi xóa (FR-41); không giữ làm dataset. Người dân được báo thời hạn này khi đồng ý (FR-8).
- Admin không truy cập nội dung phản ánh (NFR-4). `[CXM-4]` Nếu sinh viên trong nhóm giữ vai trò Admin, quy tắc này là thứ duy nhất ngăn nhóm đọc dữ liệu cá nhân của người dân; nhóm không được cấp cho mình vai trò Cán bộ phường trên dữ liệu thật.
- `[NOTE FOR PM: brief ghi "cân nhắc làm mờ mặt và biển số". PRD chưa đưa thành FR. Nếu làm, đây là thêm một thành phần AI vào khối lượng vốn đã lớn. Cần quyết định trước khi chốt kiến trúc.]`
- Chưa có quy tắc cho: thời hạn lưu phản ánh không bị từ chối (FR-8 đang dùng giá trị tạm 24 tháng); Người dân rút lại đồng ý hoặc xóa tài khoản thì phản ánh của họ xử lý thế nào; ảnh phản ánh được chấp nhận có được dùng để huấn luyện không. Xem §14, câu 10, 11.
- Ảnh nhóm tự chụp cho tập đánh giá cũng chịu luật này.

### 8.2 AI

- AI chỉ gợi ý; con người quyết định cuối ở cả ba thành phần (FR-9, FR-10, FR-11).
- AI lỗi thì phản ánh vẫn được tiếp nhận (FR-12).
- Model pretrained do nhóm tinh chỉnh, chạy trên server của dự án, không dùng AI API bên ngoài (NFR-8).

### 8.3 Phạm vi pháp lý

WRMS không xử lý khiếu nại, tố cáo (có luật và quy trình riêng) và không nhận hồ sơ thủ tục hành chính. Phản ánh hiện trường chỉ khớp lỏng với Nghị định 20/2008/NĐ-CP về phản ánh, kiến nghị; nhóm không dựa vào nghị định này để định nghĩa quy trình.

## 9. Ngoài mục tiêu

- WRMS không thay Góp ý Đà Nẵng, 1022 hay Zalo, và không nhận phản ánh từ các kênh đó. Cán bộ phường vẫn theo dõi các kênh thành phố song song.
- WRMS không chuyển phản ánh lên cấp thành phố và không làm việc với đơn vị phối hợp ngoài phường. `[CXM-2]`
- Không xử lý khiếu nại, tố cáo, hồ sơ thủ tục hành chính.
- Không có tình nguyện viên, không có tính năng cộng đồng (điểm, xếp hạng, phần thưởng).
- Không hiển thị công khai phản ánh, không có hỏi đáp chính sách (quyết định 10).
- Không có bảng SLA, Phòng ban xử lý mặc định, workflow template, minh chứng theo Loại phản ánh (quyết định 8, 10).
- Không có bật tắt AI; AI không tự quyết định (quyết định 5, 6).
- Không gọi AI API bên ngoài.
- `[NON-GOAL for MVP]` Người dân sửa hoặc rút lại phản ánh đã gửi.
- `[NON-GOAL for MVP]` Người dân phản hồi khi phản ánh báo Completed mà hiện trường chưa sạch. `[NOTE FOR PM: đây là một phần của chân "khép kín vòng" trong luận điểm, và hội đồng có thể hỏi. Thêm thì cần cách mở lại phản ánh đã Completed, tức là thêm một chuyển trạng thái mới. FR-45 cho Người gửi chấm điểm, nhưng không mở lại phản ánh.]`

## 10. Phạm vi MVP

### 10.1 Trong phạm vi (01/01/2027 – 30/04/2027)

- Phản ánh hiện trường gửi qua app WRMS tại phường Hòa Xuân.
- App mobile cho Người dân và Cán bộ phòng ban; web cho Cán bộ phường và Admin. `[ASSUMPTION: một app mobile chung, hiển thị theo vai trò]`
- Cả 11 nhóm nghiệp vụ ở §5 (FR-1 đến FR-45).
- Sàng lọc và Gom nhóm cho mọi Lĩnh vực; Mức gợi ý chỉ cho Lĩnh vực thí điểm.
- Đánh giá nghiên cứu và bốn sản phẩm đầu ra ở §6.

### 10.2 Ngoài phạm vi MVP

- Mọi mục ở §9.
- Làm mờ mặt và biển số: chưa quyết định (§8.1).
- Mức gợi ý cho Lĩnh vực ngoài Lĩnh vực thí điểm: để sau khi có kết quả thí điểm.

### 10.3 Thứ tự cắt giảm khi trễ tiến độ

Các FR chia thành ba tầng:

- **Lõi luận điểm (không cắt):** gửi phản ánh, tài khoản và danh mục (FR-1 đến FR-8); Hàng chờ và quyết định (FR-12, FR-13, FR-14, FR-16, FR-17, FR-19); giao, giao lại, thu hồi (FR-23, FR-25, FR-43); nhận và từ chối nhiệm vụ (FR-26, FR-27, FR-28, FR-42); Nghiệm thu (FR-29, FR-30); thông báo và lịch sử (FR-31 đến FR-35, FR-44); nhắc hạn, báo quá hạn, xóa dữ liệu (FR-39, FR-40, FR-41); số liệu đo SM (FR-38).
- **Nghiên cứu (không cắt, theo brief):** Gom nhóm (FR-10) và Mức gợi ý (FR-11).
- **Phần thêm (cắt theo thứ tự):**
  1. Bản đồ điểm nóng (FR-36). Theo brief.
  2. AI Sàng lọc (FR-9). Theo brief. Cắt kéo theo: bỏ FR-15, phần Ảnh bị gắn cờ ở FR-13, phần xóa ảnh bị loại ở FR-41, RQ-4 và SM-R3; Cán bộ phường tự xem mọi ảnh.
  3. Dashboard và thống kê (FR-37); giữ FR-38 để vẫn đo được SM. `[ASSUMPTION: giữ FR-37 khi cắt FR-36, và các bước từ 3 trở đi là đề xuất của PRD]`
  4. Nhóm xử lý (FR-24): chỉ giao cho một Cán bộ phòng ban.
  5. Đánh giá sao của Người dân (FR-45).
  5. Ghi nhận Xác minh hiện trường (FR-20) và chuyển quyền phụ trách (FR-18).
  6. Yêu cầu bổ sung (FR-21) và đổi Hạn chót (phần đổi ở FR-22).

`[NOTE FOR PM: hai bước đầu theo brief giữ phần nghiên cứu và cắt phần có ích trực tiếp cho phường. Nếu buổi làm việc với phường cho thấy lượng phản ánh thấp (CXM-1), nên xem lại thứ tự này. Các bước 3 đến 6 do PRD đề xuất; nhóm chốt.]`

## 11. Các bên và phê duyệt

| Bên | Phê duyệt gì | Khi nào |
| --- | --- | --- |
| UBND phường Hòa Xuân | Đồng ý thí điểm; trả lời bốn câu ở §2; xác nhận 16 quyết định nghiệp vụ | Trước 01/01/2027 |
| GVHD | Sáu thay đổi so với đơn đăng ký (dưới đây); tiêu chí ưu tiên; thước đo nghiên cứu; hướng mặc định ở §2.1 | Trước khi chốt PRD cho kiến trúc |
| Hội đồng bảo vệ | Đánh giá đồ án | Sau 30/04/2027 |

Sáu thay đổi so với đơn đăng ký cần báo GVHD:

1. Bỏ tình nguyện viên; Cán bộ phòng ban chỉ là cán bộ phòng ban của phường.
2. Admin chỉ quản trị hệ thống. Cán bộ phường điều phối toàn bộ, nghiệm thu cuối, và xem bản đồ điểm nóng, dashboard, thống kê (đơn ghi các việc này cho Admin).
3. Phản ánh có thêm trạng thái Rejected (5 trạng thái thay vì 4).
4. Người kiểm chứng kết quả AI là Cán bộ phường (bảng khai báo AI trong đơn ghi Admin).
5. Phản ánh bị từ chối bị ẩn 90 ngày rồi xóa dữ liệu chi tiết, thay cho "giữ dạng ẩn danh".
6. Kế hoạch dữ liệu, baseline và thử nghiệm mới (addendum của PRD).

Trạng thái nhiệm vụ Cancelled (FR-43), nếu nhóm giữ, là một thay đổi nữa, nhưng so với addendum của brief chứ không so với đơn đăng ký.

**Vận hành sau 04/2027.** `[CXM-4]` Chưa có kế hoạch: chưa rõ server đặt ở đâu, ai trả chi phí, ai bảo trì phần mềm và model. Hiện chỉ có một thành viên nhóm nhận lời hỗ trợ khi phường liên hệ. Theo brief, nơi đặt server và người chịu chi phí chốt khi phường duyệt. Kế hoạch vận hành là điều kiện để đạt mục tiêu "phường thật sự dùng" ở §1.

## 12. Tiêu chí thành công

Điều kiện đầu tiên: UBND phường Hòa Xuân đồng ý thí điểm. Nếu phường không đồng ý, chỉ đo được SM-R1 đến SM-R3. Mức mục tiêu của các chỉ số cần thí điểm đặt sau buổi làm việc với phường, khi có số liệu về quy trình hiện tại.

**Chính (cần thí điểm)**

- **SM-1: Công sức rà soát mỗi Nhóm phản ánh.** Trung vị thời gian xem thực và số Phản ánh Cán bộ phường mở cho mỗi Nhóm trước khi tiếp nhận hoặc từ chối. Mục tiêu: chưa đặt. Validates FR-10, FR-13, FR-14. `[CXM-1]`
- **SM-2: Độ đúng của Gom nhóm trong thí điểm.** Precision và recall theo cặp phản ánh: cặp AI đề xuất gom chung so với cặp cùng Nhóm sau khi Cán bộ phường xác nhận, bác, tách, gộp. Mục tiêu: chưa đặt. Validates FR-10, FR-14. `[CXM-1]`
- **SM-3: Tỷ lệ Nhiệm vụ đúng hạn.** Tỷ lệ Nhiệm vụ Approved mà lần nộp Minh chứng được duyệt nằm trước Hạn chót. Mục tiêu: chưa đặt. Validates FR-23, FR-39, FR-40. `[CXM-2]`
- **SM-4: Tỷ lệ Người gửi biết kết quả.** Tỷ lệ Phản ánh Completed mà Người gửi mở xem trong app trong vòng 7 ngày. Mục tiêu: chưa đặt. Validates FR-31, FR-32. `[CXM-3]` `[ASSUMPTION: mốc 7 ngày]`
- **SM-5: Số lần Người dân phải hỏi lại tiến độ.** Đo bằng khảo sát ngắn Người gửi cuối thí điểm và hỏi Cán bộ phường số lần bị hỏi qua kênh khác, ngoài hệ thống. Mục tiêu: chưa đặt. Validates FR-31, FR-32. `[CXM-3]` `[ASSUMPTION: đo SM-5 bằng khảo sát]`
- **SM-R4: Thời gian xử lý.** Thời gian từ gửi đến Completed và thời gian xử lý (FR-37), so với quy trình hiện tại nếu phường có số liệu. Validates FR-35, FR-38. `[CXM-1]`

`[NOTE FOR PM: brief đo kết quả "không đôn đốc bằng miệng" bằng tỷ lệ nhiệm vụ có hạn chót và tỷ lệ nhiệm vụ quá hạn được cảnh báo trước, và đo "khép kín nghiệm thu" bằng tỷ lệ phản ánh hoàn thành có ảnh trước và sau. Theo thiết kế, cả ba gần như luôn 100%: FR-23 bắt buộc Hạn chót, FR-39 nhắc mọi Nhiệm vụ, FR-29 bắt buộc ảnh sau. Chúng chỉ còn là phép kiểm hệ thống chạy đúng. PRD thay bằng SM-3 và SM-4 đo kết quả. Nhóm cần đồng ý vì đây là đổi so với brief.]`

**Nghiên cứu (đo trên tập đánh giá, không cần thí điểm)**

- **SM-R1: Độ khớp Mức gợi ý.** So với nhãn của nhóm (và của người gán nhãn độc lập); so với Mức cuối của Cán bộ phường nếu có thí điểm. Validates FR-11, FR-19.
- **SM-R2: Độ chính xác Gom nhóm.** So gom theo vị trí, Loại phản ánh và ảnh với baseline gom chỉ theo vị trí. Validates FR-10.
- **SM-R3: Độ chính xác Sàng lọc.** Validates FR-9.

Thước đo cụ thể cho SM-R1 đến SM-R3 ở §6.

**Chỉ số đối trọng (không tối ưu)**

- **SM-C1: Tỷ lệ phản ánh bị từ chối.** Có thể giảm SM-1 bằng cách từ chối nhanh. Theo dõi cùng SM-1.
- **SM-C2: Độ dài Hạn chót trung bình.** Có thể tăng SM-3 bằng cách đặt Hạn chót dài. Theo dõi cùng SM-3.
- **SM-C3: Tỷ lệ Nhiệm vụ bị trả lại.** Có thể tăng SM-3 và rút ngắn SM-R4 bằng cách duyệt dễ. Theo dõi cùng SM-3, SM-R4.
- **SM-C4: Tỷ lệ bỏ sót mức Cao.** Độ khớp chung có thể cao trong khi model bỏ sót phản ánh mức Cao. Báo cáo cùng SM-R1, và chốt nhãn trước khi chạy model (§6).

## 13. Rủi ro

Bảy rủi ro trong brief vẫn giữ nguyên. Bảng dưới tóm tắt hệ quả và ghi chỗ PRD xử lý từng rủi ro.

| Rủi ro (brief) | Hệ quả | Chỗ xử lý trong PRD |
| --- | --- | --- |
| Chưa làm việc với UBND phường; phường chưa duyệt | Vấn đề phía phường chỉ là giả thuyết; không có thí điểm thật | §2, §2.1, §11; mục tiêu SM chưa đặt |
| Chưa có kế hoạch vận hành sau 04/2027 | Không ai chịu trách nhiệm server, chi phí, bảo trì; hỗ trợ dựa vào một thành viên nhóm | §11; §14, câu 12 |
| Ít phản ánh đi qua WRMS | Gom nhóm, thống kê ít giá trị; cán bộ phải theo dõi hai nơi | CXM-1; NFR-3; ghi chú ở §10.3 |
| Dữ liệu công khai khác ảnh đường phố Việt Nam | Model kém trên ảnh thật | §6 (đánh giá trên ảnh tự chụp, báo độ chính xác thật) |
| Ảnh có mặt người, biển số xe | Vi phạm Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 | FR-8, FR-41, §8.1 |
| Lệch so với đơn đăng ký | Hội đồng hỏi vì sao làm khác đề tài đã đăng ký | §3.2, §11 (sáu thay đổi) |
| Khối lượng lớn: 2 app, 3 thành phần AI, 5 người, 4 tháng | Trễ hạn hoặc làm nông | §10.3 (ba tầng, sáu bước cắt) |

## 14. Câu hỏi mở

| # | Câu hỏi | Ai chốt | Trước khi nào | Chặn |
| --- | --- | --- | --- | --- |
| 1 | CXM-1: lượng phản ánh mỗi tháng, kênh, tỷ lệ trùng | UBND phường | 01/01/2027 | FR-10, FR-11, FR-36, FR-37, NFR-3, mục tiêu SM |
| 2 | CXM-2: ai xử lý ngoài hiện trường cho từng Lĩnh vực | UBND phường | 01/01/2027 | §5.6 đến §5.8, danh mục Lĩnh vực |
| 3 | CXM-3: hiện nay ai báo lại kết quả, cho ai, bằng cách nào | UBND phường | 01/01/2027 | SM-4, SM-5 |
| 4 | CXM-4: ai dùng WRMS hằng ngày, phòng ban nào, bao nhiêu người; có người làm IT không | UBND phường | 01/01/2027 | FR-3, FR-18, mô hình tài khoản ở §4 |
| 5 | Khi có nhiều Cán bộ phường, ai chia phản ánh cho từng người | UBND phường, nhóm | Trước kiến trúc | FR-18 |
| 6 | Khu vực là gì: tổ dân phố, ba địa bàn cũ (Hòa Xuân, Hòa Châu, Hòa Phước), hay ô lưới bản đồ | Nhóm, hỏi phường | Trước kiến trúc (Khu vực gán lúc gửi) | FR-7, FR-36, FR-37, FR-41 |
| 7 | Nguồn dữ liệu ranh giới phường Hòa Xuân sau sáp nhập theo Nghị quyết 1659/NQ-UBTVQH15 | Nhóm | Trước kiến trúc | FR-7 |
| 8 | Có xác minh số điện thoại và khôi phục mật khẩu qua SMS không (có chi phí, ai trả); app hỗ trợ Android, iOS hay cả hai | Nhóm, GVHD; phường nếu phường trả phí | Trước kiến trúc | FR-1, FR-2, NFR-7 |
| 9 | Ảnh không hợp lệ cho huấn luyện Sàng lọc lấy từ đâu, khi FR-41 không cho dùng ảnh bị loại và phản ánh bị từ chối | Nhóm, GVHD | Trước khi huấn luyện | FR-9, RQ-4, SM-R3 |
| 10 | Thời hạn lưu phản ánh không bị từ chối; ảnh phản ánh được chấp nhận có dùng cho huấn luyện hay đánh giá không | UBND phường | Trước khi viết nội dung đồng ý | FR-8 |
| 11 | Người dân rút lại đồng ý hoặc xóa tài khoản thì phản ánh đang xử lý và đã xong xử lý thế nào | UBND phường, nhóm | Trước thí điểm | FR-8, §8.1 |
| 12 | Sau 04/2027: server đặt ở đâu, ai trả chi phí, ai bảo trì phần mềm và model | UBND phường, nhóm | Khi phường duyệt | §11 |
| 13 | Có làm mờ mặt người và biển số không | Nhóm, GVHD | Trước kiến trúc | §8.1 |
| 14 | Báo GVHD sáu thay đổi so với đơn đăng ký và xin xác nhận | GVHD | Trước khi chốt PRD cho kiến trúc | §11 |
| 15 | Hướng mặc định khi phường chưa trả lời hoặc không duyệt; mốc cuối được đổi phạm vi | Nhóm, GVHD | 01/01/2027 | §2.1 |
| 16 | Cách đóng một Nhóm đã Received mà không cần xử lý | UBND phường | Trước kiến trúc | §4.1, FR-16 |
| 17 | Ngưỡng tối thiểu cho Mức gợi ý | Nhóm, GVHD | Trước thí điểm | FR-11, §6 |
| 18 | Thứ tự cắt giảm từ bước 3 trở đi | Nhóm | Trước sprint đầu | §10.3 |
| 19 | Có công bố bộ ảnh đánh giá không | Nhóm, GVHD | Trước báo cáo đồ án | §6, §8.1 |
| 20 | Giữ trạng thái nhiệm vụ Cancelled; thay chỉ số của brief bằng SM-3, SM-4; Người dân phản hồi sau Completed | Nhóm, xác nhận với phường | Trước kiến trúc | FR-43, §12, §9 |
| 21 | Chọn sẵn hướng thu hẹp Lĩnh vực nếu CXM-2 khác giả định | Nhóm | Trước buổi làm việc với phường | §2 |
| 22 | Việc từ chối phản ánh hiện trường có thuộc diện khiếu nại theo Luật Khiếu nại 2011 không (căn cứ cho mốc 90 ngày) | GVHD, UBND phường | Trước khi viết nội dung đồng ý | FR-41, FR-8, §8.1 |

## 15. Chỉ mục giả định

Mọi thẻ `[ASSUMPTION]` trong PRD, chia theo người cần xác nhận. Nên đưa các mục cần phường xác nhận vào danh sách hỏi trong buổi làm việc.

**Cần UBND phường xác nhận**

- §3.3 — UJ-1 đến UJ-7 là hành trình giả định.
- §4.1 — thêm trạng thái nhiệm vụ Cancelled.
- §4.1 — "người được giao tiếp tục" nghĩa là Declined chuyển sang Accepted.
- FR-1 — số điện thoại là định danh đăng ký.
- FR-7 — chặn vị trí ngoài ranh giới phường.
- FR-8 — giữ phản ánh không bị từ chối 24 tháng (giá trị tạm).
- FR-18 — mọi Cán bộ phường thấy toàn bộ Hàng chờ.
- FR-18 — chuyển được quyền phụ trách.
- FR-19 — bắt buộc có Mức cuối trước khi giao.
- FR-20 — Xác minh hiện trường không bắt buộc.
- FR-22 — Cán bộ phường đổi được Hạn chót.
- FR-29 — ảnh Minh chứng phải chụp trực tiếp.
- FR-30 — không bắt buộc ghi kết quả Kiểm tra hiện trường.
- FR-31 — Người dân không thấy thông tin Nhiệm vụ.
- FR-34 — cán bộ phường chỉ nhận thông báo trong web.
- FR-39 — mốc nhắc 24 giờ.
- FR-41 — chỉ Cán bộ phường mở lại được dữ liệu đang ẩn, có ghi lịch sử.
- SM-5 — đo bằng khảo sát.

**Cần GVHD xác nhận**

- §2.1 — nhóm và GVHD chấp nhận hướng mặc định.
- §6 — có người ngoài nhóm gán nhãn độc lập.
- §6 — thước đo cụ thể cho SM-R1 đến SM-R3.
- §6 — nhóm tự dựng ảnh không hợp lệ cho tập đánh giá.

**Nhóm tự chốt**

- §4 — mỗi tài khoản một vai trò.
- §4 — mỗi Cán bộ phòng ban thuộc đúng một Phòng ban.
- §4 — tối đa một Nhiệm vụ đang mở mỗi Nhóm.
- FR-3 — Admin tạo được tài khoản Admin.
- FR-3 — báo Cán bộ phụ trách khi khóa cán bộ có Nhiệm vụ đang mở.
- FR-3 — chỉ khóa, không xóa tài khoản có lịch sử.
- FR-6 — tối đa 5 ảnh mỗi phản ánh.
- FR-7 — thứ tự GPS, EXIF, ghim bản đồ.
- FR-8 — đổi phiên bản nội dung đồng ý thì phải đồng ý lại.
- FR-9 — định nghĩa "lặp lại".
- FR-10 — Đề xuất gom là liên kết chờ duyệt.
- FR-11 — Mức gợi ý của Nhóm lấy mức cao nhất.
- FR-12 — tự phân tích lại khi AI Module hoạt động trở lại.
- FR-13 — thứ tự sắp Hàng chờ.
- FR-13 — quy tắc chọn Phản ánh đại diện.
- FR-13 — bán kính mặc định 100 m.
- FR-14 — điều kiện gộp hai Nhóm.
- FR-23 — hiển thị số Nhiệm vụ đang mở khi chọn Người nhận.
- FR-24 — Nhóm xử lý tối thiểu hai người, được khác Phòng ban.
- FR-27 — chỉ từ chối được ở Assigned.
- FR-31 — Người dân không thấy Phản ánh của người khác trong cùng Nhóm.
- FR-33 — thêm hai sự kiện ngoài quyết định 11.
- FR-34 — thông báo cần xử lý không tự ẩn.
- FR-37 — định nghĩa thời gian xử lý.
- FR-38 — xuất CSV.
- FR-39 — Hạn chót gần thì nhắc ngay.
- FR-41 — ảnh gắn cờ chưa quyết định không bị ẩn hay xóa.
- FR-45 — mỗi Người gửi đánh giá một lần, không sửa.
- FR-45 — điểm hiển thị cho Cán bộ phường ở chi tiết Nhóm và ở FR-37.
- NFR-1 — 5 giây ở 95% lần gửi.
- NFR-2 — 2 phút ở 95% phản ánh, hết hạn sau 10 phút.
- NFR-3 — 50 phản ánh mỗi ngày, 20 cán bộ đồng thời.
- NFR-4 — Cán bộ phòng ban không xem Hàng chờ chung.
- NFR-5 — phiên web 8 giờ, khóa 15 phút sau 5 lần sai.
- NFR-7 — cỡ chữ hệ thống; Chrome và Edge; màn hình từ 1366 px.
- NFR-10 — nén ảnh về tối đa 2 MB.
- NFR-11 — sao lưu hằng ngày, giữ 14 ngày.
- §10.1 — một app mobile chung.
- §10.3 — giữ FR-37 khi cắt FR-36; các bước cắt từ 3 trở đi.
- SM-4 — mốc 7 ngày.

**Giao cho kiến trúc**

- FR-41 — cách xử lý bản sao lưu cũ.
