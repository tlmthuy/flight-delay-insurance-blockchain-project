# Giao nhận tích hợp giữa ba module

Dùng thư mục này cho schema và fixture đã thống nhất. Xem [phân công nhóm](../docs/team-allocation.md) để biết đầu ra của từng module. [Policy V1](../docs/insurance-policy-v1.md) là căn cứ cho điều khoản và kết quả kỳ vọng.

| Đầu ra | Người giao | Người dùng |
| --- | --- | --- |
| Bộ chuyến demo, quy tắc chuẩn hóa `flightId`, ngày bay, giờ khởi hành UTC và kết quả mẫu | Nguyên chuẩn bị, Thùy và Quốc Anh xác nhận | Pipeline, contract và DApp |
| Quote có premium/payout bằng wei, hạn mua, hạn quote, ví mua, nonce, phiên bản và chữ ký | Nguyên phối hợp Thùy thống nhất dữ liệu ký | Contract xác minh, DApp hiển thị và gửi giao dịch |
| ABI, event, lỗi dự kiến, chain ID và địa chỉ deploy local | Thùy | Quốc Anh tích hợp ví, Nguyên đối chiếu domain chữ ký |
| Bảng metric và kết quả graph | Nguyên | Quốc Anh hiển thị dashboard, Thùy đưa vào báo cáo/slide |

Khi đổi định dạng, ghi ví dụ đầu vào và đầu ra, cập nhật producer và consumer, rồi chạy lại ca tích hợp liên quan. Truyền wei dưới dạng chuỗi số nguyên trong JSON. Dùng mốc UTC cho dữ liệu trao đổi và giờ địa phương tại sân bay cho phần hiển thị cần thiết. Giữ khóa ký và cấu hình riêng ở máy của người vận hành.
