# Ghi nhận phản hồi giảng viên

## Nhận xét trên bản đăng ký/đề cương

Nhóm cung cấp nhận xét bằng văn bản; ngày nhận chưa được ghi rõ. Đây là nhận xét tham khảo cho đề tài Mức 4, không phải toàn bộ rubric đã xác nhận.

### Điểm đạt được

- Bài toán rõ, gần thực tế; Blockchain có vai trò qua smart contract tự chi trả theo điều kiện trễ đạt ngưỡng hoặc hủy.
- Có liên kết phân tích dữ liệu với định phí theo rủi ro hãng/tuyến, thay cho mức phí cố định.
- Dự kiến đánh giá gas/độ trễ lẫn phí thu/chi và khả năng thanh toán pool bằng replay dữ liệu.
- Đã nhận diện một số vấn đề missing data trong chuyến hủy và delay-cause.

### Việc giảng viên yêu cầu lưu ý

- **Cao — đề cương:** thay placeholder `[Project title]`, bỏ hướng dẫn mẫu ở mục 2.1, 3.3, 4.1 và thêm sơ đồ kiến trúc.
- **Cao — tài liệu:** sửa thứ tự trích dẫn; xác minh DOI/nội dung bài Kim et al. Nếu không tìm thấy thì thay nguồn. Trích dẫn không có thật có thể ảnh hưởng nghiêm trọng điểm phần 1.
- **Cao — stack:** giảng viên khuyên Vyper + Ape + Anvil theo công cụ môn học; Ganache đã ngừng phát triển. Nhóm cần smoke-test và chốt stack; chưa ghi nhận việc đổi stack đã được thực hiện.
- **Cao — adverse selection:** chặn mua sau giờ khởi hành dự kiến hoặc trong X giờ trước; lưu flight ID, ngày bay và giờ khởi hành dự kiến trong policy.
- **Trung bình — model:** baseline là tỷ lệ trễ thực nghiệm; cải tiến bằng LR/XGBoost hiệu chuẩn, chỉ dùng feature có trước chuyến bay, temporal split (ví dụ tháng 1–9 train, 10–12 test), đo Brier score và tỷ lệ chi trả/phí pool. Không dùng `DEPARTURE_DELAY` hoặc nguyên nhân trễ làm feature báo giá.
- **Trung bình — oracle:** Python script đơn là điểm tin cậy tập trung; phân tích ghi sai/trễ, lộ khóa. Cân nhắc nhiều oracle ký, cửa sổ khiếu nại và giới hạn chi trả mỗi chuyến.
- **Trung bình — dữ liệu:** 2015 khá cũ; có thể bổ sung dữ liệu BTS mới hơn để kiểm tra mức phí. `flights.csv` khoảng 5,8 triệu dòng; tháng 10/2015 mã sân bay có thể ở dạng số cần ánh xạ.
- **Thấp — phạm vi:** nhóm 3 người nên giữ phạm vi gọn.
- **Báo cáo tuần 3:** tối thiểu 3 bài bình duyệt về blockchain parametric insurance, oracle và flight-delay prediction; Etherisc/AXA là ứng dụng tham khảo. Cần bảng input/output (flight ID, ngày, mức bảo hiểm → policy ID, phí, payout, trạng thái).

### Trạng thái và việc cần hỏi tiếp

| Nội dung | Trạng thái | Việc tiếp theo |
| --- | --- | --- |
| Nhận xét về đề cương | Đã nhận bằng văn bản; ngày chưa ghi | Áp dụng checklist trong `PROJECT_PLAN_1_MONTH.md` |
| Mức Research / Track chấm | Mức 4 vẫn là mức đăng ký; track chưa xác nhận | Hỏi track áp dụng và cách tính Track B hiển thị 105 |
| AI/ML | Góp ý baseline + LR/XGBoost calibration | Chạy temporal split, feature có trước chuyến bay |
| Graph Analytics | Nhận xét vừa nhận không nói rõ | Hỏi yêu cầu tối thiểu cho Mức 4; chưa tự bỏ hoặc mở rộng sang GNN |
| Stack | Khuyến nghị Vyper/Ape/Anvil | Smoke-test; hỏi có bắt buộc chuyển từ Solidity hay không |
| Dataset | Dữ liệu 2015 cũ; có thể thêm BTS mới để kiểm tra | Hỏi giữ 2015 làm data chính và BTS làm validation phụ có phù hợp không |
| Oracle | Rủi ro tập trung được nêu | Thiết kế mock/local và phân tích failure; hỏi có cần testnet/multi-oracle thật không |
| Điều khoản/hạn mua | Chặn mua muộn; ngưỡng X chưa chốt | Hỏi giờ cutoff/timezone; ghi điều khoản trong decision log |
| Hạn nộp/kênh nộp, ngày bảo vệ | Chưa có trong nhận xét đã gửi | Xác nhận với giảng viên |
