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
| §5.3 | 3. Phân tích tự động | FR-9 đến FR-12, FR-50 | D |
| §5.4 | 4. Duyệt và tiếp nhận | FR-13 đến FR-18 | Leader |
| §5.5 | 5. Xử lý của cán bộ phường | FR-19 đến FR-22 | Leader |
| §5.6 | 6. Phân công nhiệm vụ | FR-23 đến FR-25, FR-43 | C |
| §5.7 | 7. Nhận hoặc từ chối nhiệm vụ | FR-26 đến FR-28, FR-42 | C |
| §5.8 | 8. Nghiệm thu | FR-29, FR-30 | Leader |
| §5.9 | 9. Theo dõi và thông báo | FR-31 đến FR-35, FR-44, FR-45 | A |
| §5.10 | 10. Bản đồ và thống kê | FR-36 đến FR-38 | D |
| §5.11 | 11. Tác vụ tự động theo thời gian | FR-39 đến FR-41 | C |
| §5.12 | 12. Phối hợp cơ quan ngoài phường | FR-46 đến FR-49, FR-51 đến FR-55 | B (đề xuất) |

Leader sở hữu ba nhóm (4, 5, 8). B còn một nhóm sau khi bỏ nhóm Quản lý tình nguyện viên ngày 23/10; addendum của brief ghi có thể cần chia lại việc. Nhóm 12 thêm ngày 23/10/2026; đề xuất giao B vì B đang ít việc nhất, nhóm chốt (§14 của PRD, câu 27). Nhóm 12 đụng vào nhóm 2 (FR-6, FR-8, của A), nhóm 3 (FR-50, của D), nhóm 4 (FR-13, FR-14, FR-15, FR-16, FR-17, của Leader), nhóm 6 và 7 (khóa giao việc, On Hold, của C), nhóm 8 (FR-30, của Leader), nhóm 9 (thông báo, của A), nhóm 10 (FR-37, FR-38, của D) và nhóm 11 (nhắc mốc, của C); cần thống nhất giao diện giữa các nhóm này trước sprint đầu.

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

## Mẫu biểu cho nhóm nghiệp vụ 12

Bốn mẫu dưới đây là bản thiết kế để UX và nhóm 12 dựng bản in tự điền (FR-48, FR-54, FR-55). Thể thức theo Nghị định 30/2020/NĐ-CP; câu chữ cuối cùng do văn thư hoặc cán bộ pháp chế của phường chốt (§14 của PRD, câu 25). Trường có dấu `*` là bắt buộc trong WRMS; trường `[tự điền]` do hệ thống lấy từ Nhóm phản ánh. Không mẫu nào chứa họ tên hay số điện thoại của Người gửi (FR-8).

### PC-01. Phiếu chuyển phản ánh

Dùng cho FR-48 (ngoài thẩm quyền) và bước 3 của Hồ sơ nguy hại (FR-54).

```text
ỦY BAN NHÂN DÂN                        CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
PHƯỜNG HÒA XUÂN                                Độc lập - Tự do - Hạnh phúc
Số: ......./PC-UBND                     Hòa Xuân, ngày ... tháng ... năm ...*

                         PHIẾU CHUYỂN PHẢN ÁNH
                    (Mã nhóm phản ánh WRMS: [tự điền])

Kính gửi: [Cơ quan nhận, từ Danh bạ]*

Ngày [thời điểm gửi sớm nhất, tự điền], Ủy ban nhân dân phường Hòa Xuân nhận
được [số Phản ánh, tự điền] phản ánh của người dân qua Hệ thống WRMS về việc:
[Loại phản ánh, tự điền] tại [địa chỉ, tự điền] (tọa độ [tự điền]).

Nội dung phản ánh: [mô tả của Phản ánh đại diện, tự điền]

[Biến thể A, FR-48, gửi Cơ quan có thẩm quyền]
Xét thấy nội dung trên thuộc thẩm quyền giải quyết của [Cơ quan nhận] vì
[lý do phân loại]*, Ủy ban nhân dân phường Hòa Xuân chuyển phản ánh đến
[Cơ quan nhận] để xem xét, giải quyết theo thẩm quyền.

[Biến thể B, bước 3 của Hồ sơ nguy hại]
Qua xác minh (Biên bản số ......./BB-XM kèm theo), hiện trường có dấu hiệu
chất thải nguy hại. Ủy ban nhân dân phường Hòa Xuân [nội dung đề nghị]*:
- gửi cơ quan quản lý: báo cáo để chỉ đạo, phối hợp xử lý theo quy định;
- gửi Đơn vị có chức năng: đề nghị thu gom, vận chuyển, xử lý theo giấy phép
  môi trường số [tự điền từ Danh bạ].

Đề nghị [Cơ quan nhận] thông báo kết quả cho Ủy ban nhân dân phường Hòa Xuân
qua [kênh liên hệ của Cán bộ phụ trách] để phường thông tin cho người dân.

Kèm theo: [k] ảnh hiện trường [tự điền, tối đa 3]; [BB-01 số ..., nếu luồng nguy hại].

Nơi nhận:                                   TM. ỦY BAN NHÂN DÂN
- Như trên;                                 [CHỨC VỤ NGƯỜI KÝ]
- Lưu: VT, hồ sơ WRMS [mã nhóm].            (Ký, ghi rõ họ tên, đóng dấu)
```

Trường ghi trong WRMS sau khi phát hành, không in: kênh chuyển*, định danh việc chuyển theo kênh* (FR-48), ngày chuyển*, bản chụp văn bản đã ký. Số `PC-UBND` chỉ có khi kênh là văn bản; với Góp ý Đà Nẵng, đường dây nóng, email thì định danh theo kênh thay cho số văn bản, và bản in chỉ dùng làm nội dung cần báo.

### BB-01. Biên bản xác minh hiện trường có dấu hiệu chất thải nguy hại

Dùng cho bước 2 của Hồ sơ nguy hại (FR-54). Đây là biên bản ghi nhận hiện trường, không phải biên bản vi phạm hành chính.

```text
ỦY BAN NHÂN DÂN                        CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
PHƯỜNG HÒA XUÂN                                Độc lập - Tự do - Hạnh phúc
Số: ......./BB-XM

                    BIÊN BẢN XÁC MINH HIỆN TRƯỜNG
               CÓ DẤU HIỆU CHẤT THẢI NGUY HẠI, CHẤT THẢI Y TẾ
                    (Mã nhóm phản ánh WRMS: [tự điền])

Hôm nay, lúc ... giờ ... ngày ... tháng ... năm ...*, tại [địa chỉ, tự điền]
(tọa độ [tự điền]; mốc nhận diện: ..........)*

I. THÀNH PHẦN
1. Đại diện UBND phường: Ông/Bà .........., chức vụ ..........*
2. Người chứng kiến: Ông/Bà .........., [tổ trưởng tổ dân phố / công an phường / ...]*
3. Đại diện cơ quan, đơn vị khác (nếu có): ..........

II. NỘI DUNG XÁC MINH
1. Nguồn phát hiện*: [ ] Người dân qua WRMS  [ ] AI Module  [ ] Cán bộ phòng ban
   [ ] Cán bộ phường. Thời điểm gắn Cờ nguy hại: [tự điền]
2. Loại chất thải nghi là nguy hại* (chọn ít nhất một):
   [ ] Chất thải y tế lây nhiễm (kim tiêm, bơm tiêm, bông băng, ...)
   [ ] Pin, ắc quy    [ ] Hóa chất, bao bì chứa hóa chất
   [ ] Bóng đèn huỳnh quang    [ ] Dầu thải    [ ] Khác: ..........
3. Số lượng, khối lượng ước tính và quy cách (túi, can, thùng, ...)*: ..........
4. Tình trạng*: [ ] Nguyên vẹn  [ ] Rò rỉ, tràn đổ  [ ] Vỡ  [ ] Có mùi lạ
   [ ] Có dấu hiệu cháy. Lẫn với chất thải thông thường: [ ] Có  [ ] Không
5. Phạm vi ảnh hưởng*: diện tích ước tính ...... m2; gần khu dân cư / trường học /
   nguồn nước / miệng cống (ghi khoảng cách): ..........
6. Biện pháp đã thực hiện*: khoanh vùng lúc ...... giờ, phạm vi ......,
   người thực hiện ..........; biển cảnh báo: [ ] Có  [ ] Không.
   Không cán bộ nào tiếp xúc, thu gom, di chuyển chất thải: [ ] Xác nhận*
7. Dấu hiệu nhận biết nguồn thải (nhãn mác, tên cơ sở trên bao bì, ...), nếu có:
   .......... (chỉ ghi nhận, không kết luận vi phạm)
8. Đề xuất*: báo cáo [cơ quan quản lý môi trường]; đề nghị Đơn vị có chức năng
   thu gom, vận chuyển, xử lý.

III. ẢNH KÈM THEO*
Danh sách ảnh X1, X2, X3 (mã ảnh, thời điểm, tọa độ) [tự điền từ WRMS]

Biên bản kết thúc lúc ... giờ ... cùng ngày, gồm ... trang, đã đọc lại cho
những người có mặt cùng nghe và thống nhất ký tên.

NGƯỜI CHỨNG KIẾN          NGƯỜI LẬP BIÊN BẢN          ĐẠI DIỆN UBND PHƯỜNG
(Ký, ghi rõ họ tên)       (Ký, ghi rõ họ tên)         (Ký, ghi rõ họ tên)
```

### BB-02. Biên bản bàn giao hiện trường cho Đơn vị có chức năng

Dùng cho bước 4 của Hồ sơ nguy hại (FR-54).

```text
ỦY BAN NHÂN DÂN                        CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
PHƯỜNG HÒA XUÂN                                Độc lập - Tự do - Hạnh phúc
Số: ......./BB-BG

                    BIÊN BẢN BÀN GIAO HIỆN TRƯỜNG
                       CÓ CHẤT THẢI NGUY HẠI
                    (Mã nhóm phản ánh WRMS: [tự điền])

Căn cứ Biên bản xác minh hiện trường số ......./BB-XM ngày ......*
và Phiếu chuyển [số văn bản hoặc định danh theo kênh, tự điền] ngày ......*;
Hôm nay, lúc ... giờ ... ngày ... tháng ... năm ...*, tại [địa chỉ, tự điền]

I. BÊN GIAO: ỦY BAN NHÂN DÂN PHƯỜNG HÒA XUÂN
   Đại diện: Ông/Bà .........., chức vụ ..........*

II. BÊN NHẬN: [Đơn vị có chức năng, từ Danh bạ]*
   Địa chỉ: [tự điền]
   Giấy phép môi trường số ...... do ...... cấp, thời hạn đến ......* [tự điền, chặn nếu hết hạn]
   Đại diện: Ông/Bà .........., chức vụ .........., điện thoại ..........*
   Phương tiện thu gom, vận chuyển (biển số, nếu có): ..........

III. NỘI DUNG BÀN GIAO
1. Hiện trạng lúc bàn giao so với BB-01*: [ ] Không thay đổi  [ ] Có thay đổi: ..........
2. Loại và khối lượng ước tính chất thải bàn giao*: ..........
3. Khu vực khoanh vùng và biển cảnh báo được bàn giao cho bên nhận quản lý
   trong thời gian thu gom: [ ] Có  [ ] Không
4. Kể từ thời điểm ký biên bản này, bên nhận thực hiện thu gom, vận chuyển,
   xử lý chất thải theo giấy phép môi trường và quy định pháp luật; thông báo
   cho UBND phường khi hoàn tất và cung cấp số chứng từ chất thải nguy hại (nếu có).

IV. ẢNH KÈM THEO*
Ảnh B1 (mã ảnh, thời điểm, tọa độ) [tự điền từ WRMS]

Biên bản lập thành 02 bản, mỗi bên giữ 01 bản.

ĐẠI DIỆN BÊN NHẬN                              ĐẠI DIỆN BÊN GIAO
(Ký, ghi rõ họ tên, đóng dấu nếu có)           (Ký, ghi rõ họ tên)
```

### Bộ ảnh nghiệm thu cho Hồ sơ nguy hại

Mọi ảnh lưu thời điểm và vị trí chụp (FR-54). Người chụp không bước vào vùng khoanh và tránh chụp rõ mặt người. Ảnh X1 là góc chuẩn; giao diện bước 5 hiện X1 làm mẫu để chụp N1 cùng vị trí đứng và cùng góc.

| Mã | Bước | Nội dung ảnh | Tối thiểu | Yêu cầu |
| --- | --- | --- | --- | --- |
| A1 | 1. Cảnh báo hiện trường | Dây khoanh vùng hoặc biển cảnh báo | 1 | Thấy được biển và phạm vi khoanh |
| X1 | 2. Xác minh | Toàn cảnh | 1 | Đứng ngoài vùng khoanh, thấy một mốc cố định (cột điện, biển số nhà) |
| X2 | 2. Xác minh | Cận cảnh chất thải | 1 | Dùng zoom; thấy được nhãn hoặc hình dạng chất thải |
| X3 | 2. Xác minh | Mốc vị trí | 1 | Biển tên đường, số nhà hoặc công trình gần nhất |
| B1 | 4. Bàn giao | Lúc bàn giao | 1 | Thấy người hoặc phương tiện của Đơn vị có chức năng tại hiện trường |
| N1 | 5. Nghiệm thu | Toàn cảnh sau thu gom | 1 | Cùng vị trí đứng và góc với X1; chụp sau thời điểm bàn giao |
| N2 | 5. Nghiệm thu | Cận cảnh vị trí chất thải cũ | 1 | Cùng vị trí với X2 |
| N3 | 5. Nghiệm thu | Hiện trường đã gỡ khoanh vùng | 1 | Không còn dây, biển cảnh báo (hoặc ghi lý do nếu cần giữ) |

Ảnh gửi cho Người gửi khi Completed (FR-32): N1 và N2. Ảnh A1, X2, B1 không hiển thị cho Người dân.
