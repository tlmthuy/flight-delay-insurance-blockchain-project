# Đề xuất đồ án để trao đổi với giảng viên

**ANTs · Q4H648 · IS355 · Mức đăng ký 4 — Research**

**Blockchain-Based Parametric Flight Delay Insurance Supported by Historical Aviation Data Analysis**

## Bài toán và mục tiêu

Nhóm đề xuất nguyên mẫu bảo hiểm tham số cho chuyến bay trễ hoặc hủy. Khách mua một policy trước chuyến bay. Điều khoản xác định trước mức phí, ngưỡng trễ và tiền bồi thường. Khi oracle cung cấp kết quả cuối cùng, Smart Contract xác định quyền nhận tiền theo điều khoản đã khóa.

Blockchain được dùng để công khai điều khoản thực thi, ghi nhận giao dịch và quản lý tiền đã cam kết. Tính đúng của kết quả chuyến bay vẫn phụ thuộc nguồn oracle. Nhóm sẽ phân tích giả định tin cậy và quyền quản trị này trong báo cáo.

## Phạm vi đề xuất cho một tháng

| Thành phần | Dự kiến thực hiện |
| --- | --- |
| Smart Contract | Luồng mua policy, nhận kết quả, giải quyết policy, rút bồi thường và cấp vốn quỹ. Hồ sơ ghi Ethereum/Solidity; giảng viên khuyến nghị Vyper/Ape/Anvil, stack cuối cùng đang chờ smoke-test/xác nhận |
| Blockchain | Mục tiêu local chain, lưu transaction receipt và event. Xác nhận yêu cầu testnet với giảng viên |
| Oracle | Tài khoản được cấp quyền gửi kết quả mô phỏng để demo tái lập |
| Dữ liệu | Phân tích lịch sử Flight Delays 2015 theo nguồn đã đăng ký |
| AI | So sánh baseline xác suất biến cố với một mô hình dự đoán, đánh giá theo thời gian |
| Định phí | Phí thuần dựa trên xác suất biến cố nhân mức bồi thường, phụ phí được công bố riêng |
| Graph Analytics | Đăng ký Mức 4 có nêu graph; nhận xét mới của giảng viên chưa nói rõ mức cần làm. Phạm vi graph đang chờ xác nhận |
| DApp | Xem báo giá, mua policy bằng ví, xem trạng thái, nhận tiền và xem analytics |
| Đánh giá | Test nghiệp vụ, kiểm tra vốn, gas, thời gian xử lý, metric AI và ít nhất ba rủi ro bảo mật |

## Hướng triển khai đã chốt ở cấp nhóm

Nhóm giữ bài toán bảo hiểm tham số trễ hoặc hủy chuyến bay và bổ sung đánh giá hiệu quả tài nguyên của Smart Contract. FlySure được dùng làm codebase tham khảo chính vì có sẵn flight-insurance policy, oracle, payout, Hardhat test và gas reporting. Nhóm sẽ fork một commit cụ thể, chạy lại test gốc, rồi điều chỉnh tối thiểu theo điều khoản ANTs. Overdoo và Etherisc được dùng làm nguồn tham khảo kiến trúc/related work, không phải codebase chính.

Premium và mô hình rủi ro chạy ngoài chuỗi bằng Python trên dữ liệu Flight Delays 2015. DApp hiển thị báo giá và gọi Smart Contract. Contract lưu policy, kiểm tra cutoff, nhận kết quả từ mock oracle, giải quyết trạng thái và cho người dùng rút payout.

Thí nghiệm resource efficiency dùng cùng source code FlySure với hai cấu hình compiler. B0 tắt optimizer và B1 bật optimizer. Cùng workload và test được chạy cho cả hai cấu hình để đo gas deployment, gas runtime, số transaction, storage writes và latency. Nếu có thời gian, nhóm thêm một thay đổi code tối ưu có kiểm chứng thành B2. CO₂e chỉ được báo cáo khi có phương pháp đo điện năng hoặc mô hình hóa minh bạch, không suy ra trực tiếp từ gas.

## Điều khoản để xin góp ý

Các con số trong đề xuất ban đầu — trễ đến **120 phút trở lên**, mua trước giờ khởi hành **24 giờ**, payout minh họa **0,01 ETH thử nghiệm** — chỉ là giá trị để thảo luận, chưa phải điều khoản đã chốt. Chuyến chuyển hướng và thiếu dữ liệu cần quy tắc riêng trước khi triển khai. Thầy yêu cầu chặn mua muộn nhưng ngưỡng thời gian cụ thể còn cần xác nhận.

## Câu hỏi nghiên cứu dự kiến

1. Mô hình xác suất có cải thiện Brier score và calibration so với tỷ lệ biến cố lịch sử không?
2. Đặc trưng đồ thị tính từ dữ liệu quá khứ có cải thiện dự đoán so với bộ đặc trưng ban đầu không?
3. Smart Contract có bảo toàn tiền cam kết và ngăn thanh toán trùng trong các kịch bản kiểm thử không? Gas và thời gian xử lý đo được là bao nhiêu?

Đặc trưng chỉ sử dụng thông tin có trước thời điểm mua bảo hiểm. Phân tích dữ liệu 2015 là thực nghiệm hồi cứu. Chưa có kết quả huấn luyện, số đo hiệu năng hoặc deployment tại thời điểm soạn bản này.

## Nội dung còn cần xác nhận

- Graph analytics tối thiểu nào phù hợp với Mức 4?
- Oracle mô phỏng và local blockchain được chấp nhận đến mức nào? Có bắt buộc testnet không?
- Vyper/Ape/Anvil là yêu cầu bắt buộc hay khuyến nghị; nhóm có thể giữ Solidity không?
- Kaggle 2015 giữ làm dữ liệu chính và BTS mới làm kiểm tra phụ có đúng ý thầy không?
- Track chấm, hạn nộp, lịch bảo vệ, kênh nộp và quy cách bàn giao là gì?

## Ghi chú phạm vi tham khảo

Repo Prashant chỉ là baseline ML cho dự đoán nhị phân trễ đến >15 phút. Repo này không chứa airport graph. Nếu thực hiện Graph Analytics theo Mức 4, nhóm xây graph sân bay/tuyến bay riêng từ dataset đã chọn hoặc dùng nguồn graph khác đã kiểm tra, sau đó so sánh nó với baseline ML. DApp là giao diện kết nối ví và gọi contract, không chỉ là trang biểu đồ.
