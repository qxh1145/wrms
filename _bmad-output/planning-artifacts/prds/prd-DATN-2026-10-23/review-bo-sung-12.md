---
title: "Review: bổ sung nhóm nghiệp vụ 12 (FR-46 đến FR-55)"
created: 2026-10-23
reviewer: critic (độc lập)
inputs: prd.md, prd.bak-truoc-bo-sung-12.md, addendum.md (Mẫu biểu cho nhóm nghiệp vụ 12)
---

# Review bổ sung nhóm nghiệp vụ 12

**VERDICT: REVISE.** Hướng thiết kế dùng được. Bảng trạng thái của Cờ nguy hại và Hồ sơ nguy hại còn ba lỗ hổng mức high: gắn Cờ tay không dừng Nhiệm vụ đang chạy; Cờ Đã xử lý không cho báo lại; Hồ sơ kẹt sau bước 3. Ngoài ra có hai ca giao thoa với gom nhóm và từ chối chưa xử lý. Luồng A (Transferred) chặt hơn, chủ yếu lỗi tham chiếu và Phiếu chuyển gắn nhiều Nhóm.

Phạm vi: diff giữa `prd.bak-truoc-bo-sung-12.md` và `prd.md`, các FR cũ đã sửa, và phần Mẫu biểu ở cuối addendum. Không xét văn phong. Không đề xuất tính năng mới; mỗi đề xuất chỉ chốt hoặc sửa quy tắc đã có.

Dự đoán trước khi đọc: (1) trạng thái kết thúc hoặc ngõ cụt trong luồng mới; (2) giao thoa giữa Cờ, On Hold và các trạng thái nhiệm vụ Submitted, Declined; (3) giao thoa với gom và tách nhóm; (4) tham chiếu chéo lệch sau khi chèn FR; (5) căn cứ pháp lý nói quá. Cả năm đều có phát hiện.

## High

### H1. Cờ do Cán bộ phường gắn tay bỏ qua Chờ xác nhận, nên Nhiệm vụ đang chạy không bị dừng
- **Mức:** high
- **Vị trí:** §4.1 bảng Cờ, dòng `– hoặc Đã gỡ → Đã xác nhận`; §4.1 bảng nhiệm vụ, dòng `… → On Hold`; FR-51 gạch 1 và gạch 4; FR-52; FR-53; FR-43; FR-30.
- **Mô tả:** FR-51 nói Cán bộ phường gắn tay thì `Cờ sang Đã xác nhận ngay`, và bảng Cờ cũng đi thẳng `– → Đã xác nhận`. Nhưng chỉ khi `Gắn Cờ Chờ xác nhận` thì Nhiệm vụ mới chuyển On Hold (FR-51 gạch 4). Khi xác nhận, FR-52 cũng chỉ hủy `Nhiệm vụ On Hold`. Bảng nhiệm vụ lại ghi nguồn của On Hold là `Cờ nguy hại Chờ xác nhận (AI, Người nhận báo, hoặc Cán bộ phường gắn)`, trái với FR-51. Nếu làm theo FR-51 và FR-52 thì có hai hậu quả:
  - Nhiệm vụ ở Assigned, Accepted hoặc Returned vẫn chạy. Người nhận không nhận thông báo dừng, vì FR-33 chỉ báo khi chuyển On Hold, nên cán bộ tiếp tục dọn chất thải nguy hại.
  - Nhiệm vụ ở Submitted không thu hồi được (FR-43) và không bị On Hold. FR-53 chỉ chặn duyệt Nhiệm vụ On Hold, nên Cán bộ phường vẫn duyệt được. Khi đó FR-30 đưa Nhóm sang Completed trong lúc Cờ Đã xác nhận và Hồ sơ nguy hại đang mở; bước 3 và bước 5 mất nghĩa. Đây là tình huống dễ gặp nhất: Cán bộ phường thấy kim tiêm trong ảnh Minh chứng rồi gắn Cờ tay.
- **Đề xuất:** Ghi rõ gắn tay nghĩa là tạo Cờ Chờ xác nhận rồi xác nhận ngay trong cùng một thao tác, để Nhiệm vụ đi qua On Hold rồi sang Cancelled. Sửa dòng bảng Cờ và FR-51 cho khớp. Cách khác: thêm vào FR-52 và bảng nhiệm vụ quy tắc "Cờ sang Đã xác nhận thì mọi Nhiệm vụ đang mở, trừ Declined chưa xét, chuyển Cancelled, kể cả Submitted".

### H2. Cờ Đã xử lý là trạng thái kết thúc, nên không báo lại được chất thải nguy hại trên cùng Nhóm
- **Mức:** high
- **Vị trí:** §4.1 bảng Cờ (`Đã xác nhận → Đã xử lý … Trạng thái kết thúc`; `một Nhóm có tối đa một Cờ`); FR-51 gạch 5; FR-42 gạch 4; FR-55 kết luận "còn chất thải thông thường"; UJ-9 edge case 1; FR-50 gạch cuối.
- **Mô tả:** Với kết luận "còn chất thải thông thường", Cờ sang Đã xử lý và Nhóm giao lại được Nhiệm vụ nội bộ, đúng như UJ-9 edge case 1. Giả sử anh Tuấn quay lại dọn phần xà bần và gặp thêm một túi kim tiêm:
  - FR-42 vẫn cho bấm "Báo chất thải nguy hại".
  - Bảng Cờ chỉ có chuyển `– hoặc Đã gỡ → Chờ xác nhận`.
  - FR-51 chỉ cho nguồn mới "ghi thêm" khi Cờ đang Chờ xác nhận hoặc Đã xác nhận.
  - Không tạo được Cờ thứ hai, vì mỗi Nhóm có "tối đa một Cờ".

  Kết quả là nút báo không có tác dụng (không On Hold, không Cảnh báo đỏ), hoặc lập trình viên tự tạo Cờ thứ hai, trái định nghĩa. Cán bộ phường gắn tay cũng bị chặn như vậy. Riêng FR-50 gạch cuối (`Nhóm đích nhận Cờ Chờ xác nhận nếu Nhóm đích chưa có Cờ Chờ xác nhận hoặc Đã xác nhận`) lại ngầm cho phép Đã xử lý → Chờ xác nhận, trái với bảng.
- **Đề xuất:** Thêm chuyển `Đã xử lý → Chờ xác nhận` (AI Module, Người nhận) và `Đã xử lý → Đã xác nhận` (Cán bộ phường), kèm mở Hồ sơ nguy hại mới. Hoặc đổi quy tắc thành "tối đa một Cờ chưa kết thúc mỗi Nhóm". Bỏ chữ "Trạng thái kết thúc" ở dòng Đã xử lý.

### H3. Hồ sơ nguy hại kẹt vĩnh viễn sau bước 3
- **Mức:** high
- **Vị trí:** FR-52 (`Sau bước 3 không gỡ được Cờ`); §4.1 bảng bước của Hồ sơ nguy hại; FR-53 gạch 4; FR-54 bước 4 và nhắc mốc; FR-49.
- **Mô tả:** Sau bước 3, đường ra duy nhất là bước 4 (BB-02 có chữ ký của Đơn vị có chức năng, giấy phép còn hạn) rồi bước 5. PRD chưa có đường ra cho bốn tình huống thực tế:
  - Đơn vị có chức năng kết luận không phải chất thải nguy hại và không nhận.
  - Chất thải biến mất trước khi bàn giao, do người khác dọn hoặc chủ nguồn thải tự thu hồi.
  - Sở Nông nghiệp và Môi trường tự bố trí thu gom, phường không ký BB-02.
  - Không đơn vị nào đến.

  Khi đó Hồ sơ dừng ở bước 3 mãi: Nhóm ở In Progress mãi, khóa giao việc không mở (FR-53 chỉ mở khi Đã gỡ hoặc Đã xử lý), và System Timer nhắc mỗi 24 giờ không có điểm dừng (FR-54). Thêm nữa, Phản hồi của cơ quan (FR-49) chỉ ghi được cho Nhóm Transferred, nên văn bản trả lời của Sở cho Phiếu chuyển ở bước 3 không có chỗ ghi.
- **Đề xuất:** Cho bước 5 hoàn tất mà không cần bước 4 khi có lý do, ảnh hiện trường và (nếu có) văn bản của cơ quan, với kết luận "không còn chất thải nguy hại tại hiện trường". Hoặc cho gỡ Cờ sau bước 3 kèm văn bản đó. Mở rộng FR-49 để ghi được Phản hồi của cơ quan cho Phiếu chuyển của Hồ sơ nguy hại, nhưng không đổi trạng thái Nhóm.

## Medium

### M1. Từ chối Phản ánh hoặc loại ảnh khi Cờ còn Chờ xác nhận làm Cảnh báo đỏ không tắt được và lộ dữ liệu đã ẩn
- **Mức:** medium
- **Vị trí:** FR-17, FR-15, FR-41, FR-51 gạch 2, FR-52.
- **Mô tả:** FR-17 không cấm từ chối Phản ánh khi Nhóm có Cờ Chờ xác nhận, ví dụ khi ảnh vừa bị Sàng lọc gắn cờ "không phải cảnh thật" vừa mang nhãn "y tế". Sau khi từ chối, Phản ánh `bị ẩn ngay khỏi mọi màn hình` (FR-41). Nhưng Cảnh báo đỏ vẫn hiện `địa chỉ … nhãn và ảnh có nhãn` trên mọi trang, và `chỉ tắt khi Cờ được xác nhận hoặc gỡ`. Hai cách tắt đều vướng:
  - Xác nhận: FR-52 phải tiếp nhận Nhóm ở Submitted trước, mà Phản ánh Rejected thì không tiếp nhận được.
  - Gỡ: cần `ít nhất một ảnh xác minh`, tức phải ra hiện trường để tắt cảnh báo cho một phản ánh đã từ chối.

  Khi ảnh mang nhãn bị loại ở FR-15 cũng gặp đúng vấn đề này.
- **Đề xuất:** Chọn một trong hai:
  - Chặn từ chối Phản ánh và chặn loại ảnh mang nhãn khi Nhóm có Cờ Chờ xác nhận; phải xác nhận hoặc gỡ Cờ trước.
  - Quy định: từ chối Phản ánh duy nhất mang nhãn thì Cờ tự sang Đã gỡ, lấy lý do từ chối làm lý do gỡ.

  Ghi thêm rằng Cảnh báo đỏ không hiển thị ảnh đã ẩn theo FR-41.

### M2. Cờ trên Phản ánh đang có Đề xuất gom không dừng Nhiệm vụ của Nhóm đích, và xác nhận Cờ làm việc gom không thực hiện được nữa
- **Mức:** medium
- **Vị trí:** FR-10, FR-14, FR-50, FR-51, FR-52; §4.1 dòng `Submitted → Received hoặc In Progress` (gom).
- **Mô tả:** Giả sử một Phản ánh mới mang nhãn "y tế" và có Đề xuất gom vào Nhóm X đang In Progress, Người nhận của X đang ở hiện trường. Cờ gắn vào nhóm một phần tử của Phản ánh mới, không gắn vào X, nên Nhiệm vụ của X không bị On Hold. Nếu Cán bộ phường xử lý Cảnh báo đỏ trước bằng cách xác nhận Cờ, nhóm một phần tử sang Received (FR-52). Từ lúc đó không gộp được nữa: FR-14 chỉ gộp Nhóm ở Submitted, còn FR-10 và bảng §4.1 giả định Phản ánh được gom đang ở Submitted. Cuối cùng có hai Nhóm cho cùng một hiện trường: một Nhóm chạy Hồ sơ nguy hại, Nhóm kia vẫn có cán bộ đang dọn.
- **Đề xuất:** Quy định: khi Nhóm có Cờ Chờ xác nhận còn Đề xuất gom chờ duyệt, Cảnh báo đỏ nêu Nhóm đích và Nhiệm vụ đang mở của Nhóm đó. Cán bộ phường phải xác nhận hoặc bác Đề xuất gom trước khi xác nhận Cờ.

### M3. Quy tắc gộp Cờ ở FR-50 dùng sai đối tượng và không khớp bảng Cờ
- **Mức:** medium
- **Vị trí:** FR-50 gạch cuối; §4.1 bảng Cờ.
- **Mô tả:** Câu `Khi Phản ánh có Cờ được gộp` sai đối tượng, vì §4.1 gắn Cờ với Nhóm, không với Phản ánh. Câu này cũng không nói Cờ của nhóm nguồn phải ở trạng thái nào thì mới chuyển sang. Theo câu chữ hiện tại, nếu nhóm nguồn có Cờ Đã gỡ (Cán bộ phường đã ra hiện trường gỡ), Nhóm đích vẫn nhận Cờ Chờ xác nhận mới; Cảnh báo đỏ và On Hold bật lại không có lý do. Câu này cũng không nói Cờ của nhóm nguồn ra sao sau khi gộp. Bảng Cờ không có dòng "→ Chờ xác nhận do gộp nhóm" (người thao tác: Cán bộ phường, FR-10, FR-14).
- **Đề xuất:** Viết lại thành: "Khi một Nhóm có Cờ Chờ xác nhận được gộp vào Nhóm khác (FR-10, FR-14), Nhóm đích nhận Cờ Chờ xác nhận nếu Nhóm đích chưa có Cờ hoặc Cờ ở Đã gỡ. Cờ Đã gỡ của nhóm nguồn không chuyển." Thêm dòng tương ứng vào bảng Cờ. Trường hợp Nhóm đích có Cờ Đã xử lý xử lý theo H2.

### M4. Thành viên Nhóm xử lý có nút "Báo chất thải nguy hại", trái với định nghĩa Người nhận và Trưởng nhóm
- **Mức:** medium
- **Vị trí:** §4 (`Người nhận — Người duy nhất thao tác trên Nhiệm vụ`; `Trưởng nhóm — … Thành viên khác chỉ xem và nhận thông báo`); FR-42 gạch 3 và gạch 4; FR-51 gạch 1; bảng Cờ cột "Ai"; FR-37.
- **Mô tả:** FR-42 gạch 3 ghi `Thành viên không phải Trưởng nhóm … không có nút thao tác`, nhưng gạch 4 ngay sau đó lại cho `mọi thành viên Nhóm xử lý có nút "Báo chất thải nguy hại"`. Cột "Ai" của bảng Cờ chỉ ghi "Người nhận". FR-37 thống kê nguồn theo "AI, Người nhận, Cán bộ phường", nên báo cáo của thành viên không biết xếp vào nguồn nào.
- **Đề xuất:** Thêm vào định nghĩa Trưởng nhóm và FR-42 gạch 3 một ngoại lệ ghi rõ cho nút này. Bảng Cờ ghi "Người nhận hoặc thành viên Nhóm xử lý". Ghi rõ FR-37 tính báo cáo của thành viên vào nguồn nào.

### M5. Phiếu chuyển gắn nhiều Nhóm, nhưng Phản hồi của cơ quan ghi theo từng Nhóm
- **Mức:** medium
- **Vị trí:** §4 Phiếu chuyển (`một hoặc nhiều Nhóm phản ánh`); FR-48 gạch 5 và 6; FR-49; UJ-8.
- **Mô tả:** FR-49 ghi Phản hồi `vào một Nhóm Transferred`. UJ-8 lại cho anh Minh ghi một lần mà `cả hai người gửi được báo`, nghĩa là ghi theo Phiếu. Khi cơ quan trả lại, PRD không nói mọi Nhóm gắn vào Phiếu đều về Received hay chỉ Nhóm được ghi. FR-48 gợi ý gắn Nhóm mới vào `các Phiếu chuyển 30 ngày gần nhất` mà không loại Phiếu đã bị trả lại. Việc gắn thêm Nhóm cũng trái với `Phiếu chuyển không sửa được sau khi lưu`.
- **Đề xuất:** Chốt Phản hồi gắn với Phiếu chuyển và áp cho mọi Nhóm của Phiếu, hoặc chốt theo Nhóm, nhưng phải viết rõ. Loại Phiếu đã có phản hồi "trả lại" khỏi danh sách gợi ý. Ghi việc gắn thêm Nhóm là ngoại lệ của quy tắc không sửa, có ghi lịch sử (FR-35).

### M6. Tách Phản ánh khỏi Nhóm Transferred tạo một lối ra không có trong bảng
- **Mức:** medium
- **Vị trí:** FR-14 gạch 1; §4.1 dòng `Transferred → Received … Đường ra duy nhất của Transferred`.
- **Mô tả:** FR-14 cho tách Phản ánh khỏi Nhóm ở bất kỳ trạng thái nào, và `Phản ánh bị tách ra thành Nhóm mới một phần tử, ở Submitted`. Áp vào Nhóm Transferred, việc này tạo chuyển Transferred → Submitted, trái với câu "đường ra duy nhất". Người gửi đã được báo phản ánh chuyển cơ quan khác, nay lại thấy phản ánh mới gửi. Lỗi cùng loại đã có từ trước với Completed, nhưng bản sửa này khẳng định thêm một điều mà FR-14 phá vỡ.
- **Đề xuất:** Thêm điều kiện vào FR-14: chỉ tách được khỏi Nhóm đang mở. Nếu muốn tách khỏi Nhóm Transferred thì ghi chuyển đó vào bảng.

### M7. Mẫu PC-01 không dùng được nguyên trạng cho bước 3 của Hồ sơ nguy hại; BB-02 đòi số Phiếu chuyển không phải lúc nào cũng có
- **Mức:** medium
- **Vị trí:** Addendum PC-01 (`[lý do phân loại]*`, `thuộc thẩm quyền giải quyết của [Cơ quan nhận]`, `Số: ......./PC-UBND*`); Addendum BB-02 (`Phiếu chuyển số ......./PC-UBND ngày ......*`); FR-48 gạch 1 và 2; FR-54 bước 3; FR-47; FR-52.
- **Mô tả:** Mẫu PC-01 có ba chỗ không khớp:
  - PC-01 dùng chung cho bước 3, nhưng trường bắt buộc "lý do phân loại" không có nguồn dữ liệu: FR-47 cấm phân loại Nhóm nguy hại, và FR-52 hủy phân loại khi xác nhận Cờ.
  - Câu "thuộc thẩm quyền giải quyết của [Cơ quan nhận]" sai khi người nhận là Đơn vị có chức năng, vốn là doanh nghiệp được cấp phép, không có thẩm quyền giải quyết phản ánh.
  - Số `PC-UBND` mang dấu `*` ("bắt buộc trong WRMS"), nhưng FR-48 cho kênh đường dây nóng, email hay Góp ý Đà Nẵng không có số văn bản. Vì vậy BB-02 không điền được trường bắt buộc "Phiếu chuyển số" khi bước 3 đi qua các kênh đó.
- **Đề xuất:** Ghi rõ cho bước 3: trường lý do lấy từ nội dung BB-01 hoặc từ một ô nhập riêng. Thêm biến thể câu cho Đơn vị có chức năng ("đề nghị thu gom, vận chuyển, xử lý"). Đổi số `PC-UBND` và trường "Phiếu chuyển số" trong BB-02 thành "số văn bản hoặc định danh việc chuyển theo kênh (FR-48)".

### M8. "Cơ quan quản lý môi trường" ở bước 3 không có trong §4 và không kiểm được
- **Mức:** medium
- **Vị trí:** §4.1 bảng bước, bước 3; FR-54 bước 3; FR-46 gạch 1 (loại cơ quan).
- **Mô tả:** Điều kiện hoàn tất bước 3 là Phiếu chuyển `tới cơ quan quản lý môi trường hoặc Đơn vị có chức năng`. Danh bạ chỉ có ba loại: cơ quan quản lý nhà nước, đơn vị dịch vụ công ích, Đơn vị có chức năng. Không có thuộc tính nào cho biết cơ quan đó quản lý môi trường. Hệ thống chỉ kiểm được vế "Đơn vị có chức năng", còn vế kia thì kiểm thử không viết được.
- **Đề xuất:** Hoặc thêm vào Danh bạ một dấu "nhận báo cáo chất thải nguy hại" và đưa thuật ngữ vào §4, hoặc đổi điều kiện thành "tới một cơ quan trong Danh bạ" và để Cán bộ phường tự chịu trách nhiệm chọn.

### M9. §8.3 nói quá khoản 4 Điều 83 Luật Bảo vệ môi trường 2020
- **Mức:** medium
- **Vị trí:** §4 "Đơn vị có chức năng" (`được phép thu gom và vận chuyển chất thải nguy hại (khoản 4 Điều 83…)`); §8.3 gạch 2; FR-53 gạch 1, câu lý do trên nút giao.
- **Mô tả:** Theo các bản phân tích luật tra được, khoản 4 Điều 83 quy định đối tượng được *vận chuyển* chất thải nguy hại: chủ nguồn thải có phương tiện đạt yêu cầu, hoặc cơ sở có giấy phép môi trường với chức năng xử lý chất thải nguy hại phù hợp. Khoản này không nói về *thu gom*. Vì vậy câu "chỉ Đơn vị có chức năng được thu gom, vận chuyển" và lập luận "cán bộ không thuộc hai đối tượng này, nên WRMS khóa việc giao họ đi dọn" đi xa hơn văn bản. Việc dọn tại chỗ không đồng nghĩa với vận chuyển. Hội đồng có thể chỉ ra điểm này.
- **Đề xuất:** Viết lại: "khoản 4 Điều 83 chỉ cho phép hai đối tượng vận chuyển chất thải nguy hại; WRMS khóa giao việc vì cán bộ không có phương tiện, trang bị phù hợp, và để không vận chuyển trái khoản 4". Bỏ chữ "thu gom" ở chỗ dẫn khoản 4, hoặc tìm căn cứ riêng cho thu gom. Vẫn phải đối chiếu văn bản gốc như NOTE ở §8.3 đã nêu.

### M10. "Ảnh xác minh" khi gỡ Cờ chưa rõ nghĩa, ảnh hưởng trực tiếp tới khóa giao việc
- **Mức:** medium
- **Vị trí:** FR-52 gạch 3; §4.1 bảng Cờ, dòng `Chờ xác nhận → Đã gỡ`; FR-50 gạch 3 (ưu tiên recall); UJ-9 edge case 2.
- **Mô tả:** Có hai cách hiểu. (a) Phải là ảnh mới chụp tại hiện trường, có thời điểm và vị trí. (b) Ảnh bất kỳ, kể cả ảnh của chính phản ánh. FR-50 chỉnh ngưỡng nghiêng về recall, nên AI sẽ báo nhầm nhiều. Theo cách (a), mỗi lần AI báo nhầm thì Nhóm bị khóa giao việc cho tới khi có người ra hiện trường, trong khi Cán bộ phường làm việc trên web (§14 câu 28). Theo cách (b), Cán bộ phường gỡ được ngay tại bàn. Hai lập trình viên sẽ làm khác nhau.
- **Đề xuất:** Chốt một cách. Nếu chọn (a), ghi rõ ảnh phải có thời điểm và vị trí như FR-54. Nếu chọn (b), ghi rõ cho phép ảnh có sẵn trong Phản ánh.

## Low

- **L1 (low) — FR-28 và FR-53 lệch điều kiện mở khóa.** FR-28 khóa "không chấp nhận" `cho đến khi Cờ bị gỡ`. FR-53 mở khóa khi Cờ `Đã gỡ hoặc Đã xử lý`. Hệ quả: Nhiệm vụ Declined chưa xét không bị hủy khi xác nhận Cờ, nên nằm suốt Hồ sơ nguy hại. Sau kết luận "còn chất thải thông thường", nó vẫn là Nhiệm vụ đang mở và chặn việc giao mới (FR-23). *Đề xuất:* sửa FR-28 thành "cho đến khi Cờ sang Đã gỡ hoặc Đã xử lý". Ghi thêm vào FR-55 rằng phải xét xong Nhiệm vụ Declined trước khi giao.
- **L2 (low) — Tham chiếu sai ở FR-40.** Gạch cuối ghi `không thể có Hạn chót ở quá khứ (FR-53)`, nhưng quy tắc đặt Hạn chót mới nằm ở FR-52 gạch 3. *Đề xuất:* đổi thành FR-52.
- **L3 (low) — Số tầng ở §10.3 không khớp.** Câu dẫn ghi `Các FR chia thành ba tầng:` nhưng bên dưới liệt kê bốn tầng, và §13 ghi "bốn tầng". Tầng "Nghiên cứu (… theo brief)" giờ còn gồm FR-50, vốn không có trong brief. *Đề xuất:* sửa thành "bốn tầng"; ghi FR-50 là thêm sau brief.
- **L4 (low) — §14 câu 21 mồ côi.** Câu hỏi "Chọn sẵn hướng thu hẹp Lĩnh vực nếu CXM-2 khác giả định" trỏ tới §2, nhưng hàng CXM-2 mới đã bỏ cả hướng thu hẹp lẫn NOTE tương ứng. *Đề xuất:* xóa câu 21 hoặc viết lại theo hai nhánh mới của CXM-2.
- **L5 (low) — FR-37 không đo được cho Nhóm từng Transferred.** `Thời gian xử lý tính từ lúc Nhóm sang Received` mâu thuẫn với `Nhóm Transferred không tính vào thời gian xử lý` khi Nhóm đi Received → Transferred → Received → Completed: có hai mốc Received, và không rõ Nhóm đó có được tính không. *Đề xuất:* chốt dùng mốc Received cuối cùng, và chỉ loại Nhóm đang ở Transferred.
- **L6 (low, có từ trước nhưng chạm vào FR-28 vừa sửa) — Thiếu chuyển trạng thái phản ánh.** FR-28 "không chấp nhận" đưa Nhiệm vụ từ Declined sang Accepted, nhưng không đưa Nhóm từ Received sang In Progress. Vì vậy khi FR-30 duyệt, Nhóm đi Received → Completed, mà bảng không có chuyển này. Ngoài ra dòng `Received → In Progress: Nhiệm vụ đầu tiên…` không đúng với Nhóm trở về từ Transferred. *Đề xuất:* đổi thành "khi một Nhiệm vụ sang Accepted (FR-26, FR-28) mà Nhóm đang ở Received".
- **L7 (low) — Bảng bước Hồ sơ nguy hại ghi sai trạng thái mặc định.** Bước 1 ghi `Không đổi (Received)`, nhưng Nhóm có thể đã In Progress khi Cờ đến từ Người nhận, như UJ-9 edge case 1. *Đề xuất:* ghi "Không đổi".
- **L8 (low) — Một số Consequence ảnh của Hồ sơ nguy hại không kiểm được.** FR-55 ghi `Thời điểm chụp phải sau thời điểm bàn giao`, và FR-54 ghi `lưu thời điểm và vị trí chụp`. Khi Cán bộ phường tải ảnh qua web, ảnh có thể mất EXIF. FR-54 chỉ xử lý trường hợp thiếu vị trí, chưa xử lý thiếu thời điểm. Yêu cầu "cùng góc" không kiểm bằng máy được. *Đề xuất:* nêu cách xử lý khi thiếu thời điểm (cảnh báo như vị trí, hoặc chặn). Đổi "cùng góc" thành "giao diện hiện ảnh X1 làm mẫu".
- **L9 (low) — Nhắc mốc ở FR-54 chưa rõ phạm vi.** Không rõ `nhắc lại mỗi 24 giờ` áp cho bước 1, bước 4 hay cả hai, và khi nào thì dừng. *Đề xuất:* ghi rõ.
- **L10 (low) — "Cán bộ phường đang hoạt động" có hai nghĩa.** FR-51 và FR-34 dùng cụm này. Nó có thể là tài khoản chưa bị khóa, hoặc người đang mở phiên. Nếu hiểu là đang mở phiên, cán bộ đăng nhập sau sẽ không thấy cảnh báo. *Đề xuất:* chốt là "mọi tài khoản Cán bộ phường không bị khóa", và dải đỏ hiện theo trạng thái Cờ, không theo sự kiện.
- **L11 (low) — UJ-8 dùng kênh không có trong FR-48.** UJ-8 ghi `kênh "Điện thoại"`, còn FR-48 gọi kênh này là "Đường dây nóng". *Đề xuất:* thống nhất một tên.
- **L12 (low) — Định nghĩa System Timer chưa cập nhật.** §4 System Timer và mô tả §5.11 chưa nhắc hai tác vụ mới: báo Nhóm chờ chuyển quá mốc (FR-47) và nhắc mốc Hồ sơ nguy hại (FR-54). *Đề xuất:* bổ sung.
- **L13 (low) — Truy vết chưa hai chiều.** UJ-8 và UJ-9 trỏ tới FR-31, FR-32, FR-33, nhưng tiêu đề các FR này chưa ghi "Realizes UJ-8, UJ-9". UJ-9 edge case 1 dùng FR-42 (nút báo) và FR-23 (giao lại) nhưng dòng Realizes không liệt kê. FR-6 nhắc UJ-9 trong Consequence nhưng tiêu đề chỉ ghi UJ-1. *Đề xuất:* bổ sung.
- **L14 (low) — FR-21 chưa tính tới Transferred.** Danh sách "không gửi được Yêu cầu bổ sung" thiếu Transferred, và PRD chưa nói Yêu cầu bổ sung đang mở xử lý thế nào khi Nhóm sang Transferred. *Đề xuất:* thêm Transferred vào danh sách; Yêu cầu bổ sung đang mở tự đóng khi Nhóm sang Transferred.
- **L15 (low) — Người gửi có thể không nhận lời khuyên an toàn.** Người gửi có Phản ánh được gom vào Nhóm có Cờ Đã xác nhận không nhận thông báo an toàn, vì FR-32 chỉ báo lúc Cờ đổi trạng thái. Người gửi đã được cảnh báo cũng không được báo khi Cờ Đã xác nhận bị gỡ. *Đề xuất:* thêm vào FR-32 hai trường hợp này, hoặc ghi rõ đây là chủ ý.
- **L16 (low) — Addendum thiếu nhóm phụ thuộc.** Danh sách các nhóm mà nhóm 12 "đụng vào" mới có nhóm 3, 6, 7, 9. Còn thiếu nhóm 2 (FR-6, FR-8, chủ là A), nhóm 4 (FR-13 ghim đầu Hàng chờ, FR-16 tự tiếp nhận, chủ là Leader), nhóm 8 (FR-30, chủ là Leader), nhóm 10 (FR-37, FR-38, chủ là D). *Đề xuất:* bổ sung để chốt giao diện trước sprint đầu.
- **L17 (low) — Mẫu số 04 của Thông tư 05/2021.** Khoản 2 Điều 20 Thông tư 05/2021/TT-TTCP quy định việc chuyển đơn "theo Mẫu số 04" kèm Thông tư. PRD dẫn Điều 20 làm căn cứ, nhưng PC-01 tự dựng theo thể thức Nghị định 30/2020 và không nhắc Mẫu số 04. Mẫu chuyển đơn thường nêu người gửi đơn, nên có thể vướng quy tắc không chuyển họ tên Người gửi ở FR-8 (chưa đối chiếu nguyên văn mẫu). *Đề xuất:* thêm vào NOTE ở §8.3 và §14 câu 24 việc đối chiếu PC-01 với Mẫu số 04.
- **L18 (low) — Bước cắt 7 ở §10.3 đụng FR-52.** Bước 7 cắt "đổi Hạn chót (phần đổi ở FR-22)", nhưng FR-52 thuộc tầng không cắt lại cần đặt Hạn chót mới khi gỡ Cờ. *Đề xuất:* ghi rõ FR-52 tự làm việc đặt Hạn chót mới, không phụ thuộc FR-22.
- **L19 (low) — "Hạn chót ngừng tính" có hai cách hiểu.** Có thể là chỉ không nhắc và không tính quá hạn, hoặc là dời Hạn chót theo thời gian tạm dừng. Quy tắc "Hạn chót đã qua thì đặt mới" ngầm chọn cách đầu. *Đề xuất:* viết thẳng "Hạn chót không tự dời".

## Đã kiểm, không thấy lỗi

- Điều kiện chặn của Transferred (`không có Nhiệm vụ đang mở và không là Nhóm nguy hại`) khớp với FR-47, FR-48 gạch cuối và FR-52 (hủy phân loại khi xác nhận Cờ).
- Nhiệm vụ Declined chưa xét không sang On Hold: §4.1, FR-28 và FR-53 nói giống nhau, trừ điều kiện mở khóa ở L1.
- On Hold đã được đưa nhất quán vào định nghĩa Nhiệm vụ đang mở, Nhiệm vụ quá hạn, FR-39, FR-40, FR-42, FR-43 và FR-33.
- Khi AI Module lỗi (FR-12), Cờ vẫn có hai nguồn thay thế: Cán bộ phường gắn tay và Người nhận báo.
- Các tham chiếu §14 câu 23 đến 28 trỏ đúng câu. §15 có đủ 81 thẻ ASSUMPTION. Hàng CXM-2 ở §2 khớp với các FR mang nhãn `[CXM-2]`.
- Pháp lý: tên Sở sau hợp nhất năm 2025 và chính quyền hai cấp từ 01/07/2025 đúng. Khoản 2 Điều 20 Thông tư 05/2021/TT-TTCP đúng là quy định chuyển đơn và thông báo cho người gửi. Khoản 4 Điều 83 đúng là nêu hai đối tượng; chỉ phần "thu gom" là nói quá (M9).

## Câu hỏi mở (không chấm điểm)

- Nhóm nguy hại có tính vào SM-3 không, khi Nhiệm vụ bị hủy vì Cờ? Và có tính vào thời gian xử lý ở FR-37 không?
- NFR-4: sau khi Nhiệm vụ bị hủy vì Cờ, Cán bộ phòng ban có còn xem được Nhóm đó không?
- Bản nháp Minh chứng nộp lại sau khi mạng có lại (NFR-10), nhưng Nhiệm vụ đã sang On Hold trong lúc mất mạng: app báo gì cho Người nhận?

Nguồn pháp lý đã tra (bài phân tích, chưa phải Công báo): luatminhkhue.vn và hethongphapluat.com cho Điều 83 Luật Bảo vệ môi trường 2020; caselaw.vn cho Điều 20 Thông tư 05/2021/TT-TTCP.
