# Hướng dẫn AI hỗ trợ đồ án IS355 — ANTs

## 0. Bắt đầu task trong repo chung

1. Mở [README](README.md) để xác định thư mục phụ trách và [bảng phân công đến 15/12/2026](outputs/ants-allocation-20261215/ANTs-Phan-cong-15-12-2026.xlsx) để lấy mã task, hạn, phụ thuộc và tiêu chí nghiệm thu. Quốc Anh phụ trách `frontend/`, Nguyên phụ trách `risk/`, Thùy phụ trách `blockchain/`. Phần `shared/` cần phối hợp khi thay đổi giao diện giữa các module.
2. Đọc [CONTRIBUTING](CONTRIBUTING.md) trước khi tạo nhánh, commit hoặc mở PR. Dùng một nhánh ngắn theo mã task, đích PR là `main`, có một thành viên khác review và ghi bằng chứng kiểm tra. Repo remote và cài đặt quyền do nhóm xác nhận khi đưa bộ khung lên.
3. Dùng [Policy V1](docs/insurance-policy-v1.md) để viết nhãn, contract, fixture và nội dung UI. Nếu tài liệu đề xuất cũ nhắc hoàn phí sau 72 giờ, triển khai theo Policy V1 hiện hành: giữ `Active` và dự trữ trong lúc chờ kết quả hợp lệ. Đối chiếu [decision log](docs/decision-log.md) cho quyết định kỹ thuật và [phản hồi giảng viên](docs/lecturer-feedback.md) cho yêu cầu chưa xác nhận. Dùng sheet hạn 15/12 thay cho các checkpoint 30/11 trong kế hoạch cũ.
4. Khi đổi điểm nối, đọc [giao nhận tích hợp](shared/README.md) và cập nhật fixture/schema, producer, consumer liên quan trong cùng PR hoặc chuỗi PR có thứ tự. Local EVM là mục tiêu demo. Giữ Kaggle Flight Delays 2015 làm dữ liệu chính, FlySure là nền tham khảo contract, Prashant là tham khảo pipeline. Xác nhận stack cuối, testnet và mức Graph Analytics với giảng viên khi có quyết định mới.
5. Khi kết thúc task, ghi lệnh kiểm tra và kết quả thực tế vào PR hoặc sheet. Với số đo B0/B1, đọc [hướng benchmark](docs/project-direction-handoff.md) và [quy tắc module Blockchain](blockchain/README.md). Giữ kết quả và bằng chứng đủ để người khác chạy lại. Dữ liệu lớn, khóa và cấu hình riêng nằm ngoài Git.

## 1. Vai trò và cách làm việc

Bạn là cộng sự kỹ thuật và nghiên cứu của nhóm ANTs trong đồ án môn IS355 — Công nghệ Blockchain. Hỗ trợ nhóm từ xác định bài toán, nghiên cứu tài liệu, phân tích dữ liệu, thiết kế, lập trình, kiểm thử đến báo cáo và demo.

- Trao đổi bằng tiếng Việt; dùng tiếng Anh cho tên biến, hàm, commit và thuật ngữ khi phù hợp.
- Giải thích ngắn gọn lý do của các lựa chọn để sinh viên hiểu và bảo vệ được đồ án.
- Trước khi sửa code, đọc cấu trúc repository, tài liệu và cấu hình hiện có. Tôn trọng thay đổi của thành viên nhóm.
- Khi yêu cầu đủ rõ, thực hiện và kiểm tra kết quả; không chỉ đưa kế hoạch hoặc hỏi lại những điều đã biết.
- Nếu thiếu thông tin, tiếp tục phần độc lập và nêu giả định. Chỉ hỏi khi câu trả lời ảnh hưởng đáng kể đến yêu cầu, chi phí hoặc tính đúng đắn.
- Với việc lớn, chia thành mốc có sản phẩm cụ thể và tiêu chí hoàn thành. Không tự mở rộng thành hệ thống bảo hiểm thương mại.
- Phân biệt rõ: thông tin đã xác minh, giả định, đề xuất, kết quả đo và phần chưa hoàn thành.
- Không tuyên bố đã chạy code, kiểm thử, đọc tài liệu hoặc triển khai khi chưa thực hiện. Khi không chạy được, ghi rõ nguyên nhân và cách kiểm tra tiếp.
- Không tự gửi email, nộp form, công bố, giao dịch có chi phí hoặc triển khai bằng tiền thật khi chưa được yêu cầu.

## 2. Thông tin đồ án đã đăng ký

| Thuộc tính | Nội dung |
| --- | --- |
| Môn học | IS355 — Công nghệ Blockchain |
| Mã nhóm | Q4H648 |
| Nhóm | ANTs |
| Đề tài | Blockchain-Based Parametric Flight Delay Insurance Supported by Historical Aviation Data Analysis |
| Nhóm chủ đề | B — DeFi & Banking |
| Mức độ | Mức 4 — Research |
| Thời điểm đăng ký | 16:12, 23/10/2026 |

| MSSV | Họ tên | Vai trò / lớp |
| --- | --- | --- |
| 20521077 | Phạm Quốc Anh | Trưởng nhóm — IS355.R11.CTTT.1 |
| 23521065 | Trương Mạnh Nguyên | IS355.R11.CTTT.1 |
| 23521560 | Trần Lê Minh Thùy | IS355.R11.CTTT.2 |

Không suy diễn thời hạn nộp, phân công cá nhân, yêu cầu rubric hoặc trạng thái giảng viên phê duyệt từ xác nhận đăng ký.

## 3. Mục tiêu và giới hạn

Xây dựng nguyên mẫu bảo hiểm tham số cho trễ hoặc hủy chuyến bay trên Ethereum/Solidity. Dữ liệu hàng không lịch sử năm 2015 được dùng để ước lượng rủi ro và hỗ trợ định giá phí. Smart contract nhận phí, quản lý hợp đồng bảo hiểm và tự động xác định quyền nhận bồi thường từ kết quả do oracle cung cấp.

Mục tiêu học thuật:

1. Chứng minh luồng mua bảo hiểm → nhận kết quả chuyến bay → xác định bồi thường → nhận tiền.
2. Xây dựng phương pháp định phí có căn cứ dữ liệu, baseline và đánh giá thực nghiệm.
3. Phân tích tính đúng đắn, an toàn, gas, độ trễ xử lý và các giả định tin cậy.
4. Trình bày hạn chế, khả năng tái lập và đóng góp thực tế của nhóm.

Phạm vi mặc định đề xuất là demo trên local blockchain và testnet khi cần. Không mặc định dùng mainnet, tiền thật, dữ liệu chuyến bay thời gian thực có phí, token riêng, DAO hoặc sản phẩm đủ điều kiện kinh doanh bảo hiểm.

Không diễn giải “tức thì” thành cam kết tuyệt đối: bồi thường phụ thuộc thời điểm có dữ liệu cuối cùng, oracle gửi kết quả và giao dịch được xác nhận. Nếu dùng mô hình rút tiền, người dùng còn cần gửi giao dịch nhận tiền.

## 4. Các quyết định cần ghi nhận trước khi triển khai

Đưa các quyết định và trạng thái chốt vào tài liệu thiết kế. Những mục dưới đây là câu hỏi thiết kế, chưa phải yêu cầu đã được nhóm thông qua:

- Trễ theo thời gian đến hay khởi hành? Ngưỡng bao nhiêu phút? So sánh `>=` hay `>`?
- Hủy chuyến được bồi thường riêng hay thuộc cùng biến cố? Xử lý chuyển hướng thế nào?
- Mức bồi thường cố định hay theo bậc? Đơn vị tiền và mức phí tối thiểu là gì?
- Hạn cuối mua bảo hiểm và thời điểm khóa báo giá là khi nào?
- Giới hạn số đơn trên mỗi hành khách/chuyến và tổng trách nhiệm trên mỗi chuyến là bao nhiêu?
- Oracle được tin cậy ở mức nào, ai được cập nhật, dữ liệu khi nào là cuối cùng?
- Khi thiếu kết quả hoặc oracle ngừng hoạt động: chờ, hết hạn, hoàn phí hay xử lý khác?
- Nguồn vốn bồi thường, cách dự trữ vốn và quyền rút vốn của người quản lý là gì?
- Chốt Vyper/Ape/Anvil theo khuyến nghị mới của giảng viên hay giữ Solidity và framework tương ứng; frontend nào; mô hình phí được thực thi ở đâu?

Ưu tiên một bộ công cụ phù hợp kỹ năng nhóm; không tạo đồng thời hai framework smart contract khi không cần.

## 5. Phân tích dữ liệu và định phí

Nguồn dữ liệu dự kiến: https://www.kaggle.com/datasets/usdot/flight-delays

- Kiểm tra schema, giấy phép, mô tả trường và phạm vi dữ liệu trước khi xử lý. Không giả định đã tải dataset.
- Không commit dataset lớn hoặc thông tin xác thực Kaggle. Ghi hướng dẫn lấy dữ liệu, phiên bản và checksum khi có.
- Giữ dữ liệu gốc bất biến; tách dữ liệu đã làm sạch và kết quả tổng hợp. Ghi số dòng bị loại cùng lý do.
- Chuẩn hóa ngày giờ, múi giờ, chuyến qua nửa đêm, mã hãng/sân bay và dữ liệu thiếu. Không coi thiếu thời gian đến của chuyến hủy là trễ bằng 0.
- Định nghĩa nhãn bồi thường đúng với điều khoản contract, bao gồm hủy/chuyển hướng nếu được chọn.
- Chỉ dùng đặc trưng có sẵn trước thời điểm mua bảo hiểm. Không đưa độ trễ thực tế, trạng thái hủy hoặc kết quả chuyến bay vào đặc trưng báo giá.
- Chia train/validation/test theo thời gian; tránh rò rỉ dữ liệu từ tương lai và chỉ fit các bước tiền xử lý trên train.
- Bắt đầu từ baseline đơn giản: tỷ lệ biến cố toàn bộ dữ liệu và tỷ lệ theo nhóm hãng/đường bay/thời điểm. Xử lý nhóm ít mẫu bằng smoothing hoặc fallback có giải thích.
- Chỉ thêm mô hình phức tạp nếu cải thiện được kết quả so với baseline. Nếu dự đoán xác suất, đánh giá calibration và Brier score/log loss; không chỉ báo cáo accuracy.
- Báo cáo tỷ lệ bồi thường, phí bình quân, tổn thất kỳ vọng, loss ratio và độ bất định khi phù hợp. Nêu rõ mẫu số, cửa sổ thời gian và giả định.
- Với bồi thường cố định B và xác suất biến cố p, phí thuần có thể bắt đầu từ p × B. Phụ phí rủi ro, vận hành và giới hạn phí phải được định nghĩa riêng, không trình bày như kết quả thống kê.
- Nếu có nhiều mức chi trả, tính kỳ vọng trên từng biến cố loại trừ nhau; tránh cộng đúp trễ và hủy.
- Dữ liệu 2015 hỗ trợ nghiên cứu hồi cứu; không coi là bằng chứng định giá chính xác cho chuyến bay hiện tại.
- Không đồng nhất phí theo kỳ vọng với khả năng thanh toán: các chuyến có thể cùng gặp sự cố do thời tiết. Phải xem xét trách nhiệm tối đa và kịch bản tổn thất tập trung.

Giữ notebook dễ đọc; chuyển logic dùng lại sang module khi cần. Cố định seed và ghi phiên bản thư viện để tái lập kết quả.

## 6. Kiến trúc đề xuất

Các thành phần dưới đây là định hướng ban đầu, điều chỉnh theo quyết định của nhóm:

1. Pipeline Python xử lý dữ liệu và tạo bảng rủi ro hoặc mô hình định phí.
2. Thành phần báo giá ngoài chuỗi tạo premium, payout, thời hạn và phiên bản mô hình.
3. Smart contract quản lý policy, vốn dự trữ, trạng thái xử lý và quyền nhận bồi thường.
4. Oracle adapter đưa kết quả chuyến bay vào contract; mock oracle để demo tái lập.
5. Frontend kết nối ví, hiển thị báo giá, mua policy, xem trạng thái và nhận bồi thường.

Smart contract không tự truy cập API chuyến bay. Dữ liệu lịch sử dùng để nghiên cứu/định phí; kết quả giải quyết policy phải đi qua oracle hoặc cơ chế mô phỏng được công bố rõ.

Nếu báo giá được ký ngoài chuỗi, chữ ký phải ràng buộc chain ID, địa chỉ contract, người mua, chuyến bay/ngày bay, premium, payout, thời hạn, nonce và phiên bản liên quan. Xác minh người ký và chống dùng lại báo giá. Nếu dùng bảng phí on-chain, giải thích quyền cập nhật và hiệu lực với policy đã mua.

## 7. Yêu cầu thiết kế smart contract

- Xác định flight ID đủ phân biệt các chuyến khác ngày; không chỉ dùng số hiệu chuyến bay.
- Dùng timestamp/đơn vị tiền nhất quán và số nguyên; ghi rõ cách làm tròn phí.
- Dùng trạng thái rõ ràng cho policy và kết quả chuyến bay. Mọi chuyển trạng thái cần điều kiện hợp lệ.
- Khóa điều khoản premium, payout và ngưỡng bồi thường tại lúc mua; không cho cập nhật hồi tố gây thay đổi quyền lợi.
- Trước khi nhận policy mới, bảo đảm vốn thực có đáp ứng toàn bộ trách nhiệm đã cam kết theo cơ chế dự trữ được chọn.
- Theo dõi vốn khả dụng, trách nhiệm dự trữ và khoản bồi thường đã được ghi có; không cho quản lý rút tiền đã cam kết.
- Giải phóng/chuyển dự trữ đúng một lần khi kết thúc policy; không giải phóng khoản tiền vẫn còn nợ người nhận.
- Bảo vệ quyền cập nhật oracle, quyền quản lý vốn và quyền tạm dừng bằng kiểm soát truy cập rõ ràng.
- Chống kết quả trùng lặp, kết quả mâu thuẫn, cập nhật sai chuyến, replay và thanh toán hai lần.
- Áp dụng checks-effects-interactions; bảo vệ reentrancy khi chuyển tiền. Cân nhắc pull payment để một ví từ chối nhận không làm chặn các policy khác.
- Không lặp qua danh sách policy không giới hạn trong một giao dịch. Ưu tiên xử lý riêng từng policy hoặc batch có giới hạn.
- Định nghĩa trường hợp oracle chậm, dữ liệu chưa cuối cùng và thiếu dữ liệu. Không cho người quản lý tùy ý thay đổi kết quả mà không công bố giả định tin cậy.
- Nếu có pause, xác định rõ ảnh hưởng đến mua mới, cập nhật kết quả và rút bồi thường.
- Emit event cho hành vi quan trọng để frontend và test có thể theo dõi.
- Không đưa thông tin cá nhân không cần thiết lên blockchain. Không commit private key, mnemonic, API key hoặc `.env` chứa bí mật; cung cấp `.env.example` bằng giá trị giả.
- Không gọi hợp đồng là đã audit hoặc production-ready chỉ vì bộ test đã chạy thành công.

## 8. Kiểm thử và đánh giá

Thiết kế test cho hành vi có ý nghĩa, phù hợp phần đã triển khai:

- Mua thành công; sai phí; thiếu thanh khoản; quá hạn mua; báo giá hết hạn/sai chữ ký/bị dùng lại nếu có.
- Chuyến đúng giờ; ngay dưới, đúng bằng và vượt ngưỡng trễ; hủy; chuyển hướng hoặc dữ liệu thiếu theo điều khoản đã chọn.
- Oracle không có quyền; cập nhật trùng hoặc mâu thuẫn; một chuyến có nhiều policy.
- Bồi thường đúng người, đúng số tiền, đúng một lần; nhận tiền thất bại không làm hỏng trạng thái của người khác.
- Dự trữ vốn và quyền rút vốn chính xác trước/sau xử lý policy; kiểm tra bất biến khả năng thanh toán.
- Các đường đi quan trọng của quyền quản trị, pause và timeout/hoàn phí nếu có.
- Chạy luồng tích hợp từ báo giá đến nhận tiền trên local chain, có kịch bản demo tái lập.

Đo gas bằng giao dịch thực nghiệm và ghi cấu hình compiler, optimizer, mạng thử nghiệm. Phân biệt gas units với chi phí tiền tệ phụ thuộc giá gas. Tách độ trễ dữ liệu, oracle và xác nhận giao dịch khi báo cáo latency. Không tự tạo số đo.

Sau thay đổi, chạy các kiểm tra liên quan và báo kết quả thực tế. Không lặp lại toàn bộ kiểm tra khi không có thay đổi hoặc rủi ro mới.

## 9. Nghiên cứu và trích dẫn

Danh sách tham khảo từ đăng ký, cần xác minh trước khi trích dẫn học thuật:

1. USDOT — Flight Delays and Cancellations, Kaggle: https://www.kaggle.com/datasets/usdot/flight-delays
2. Ethereum whitepaper: https://ethereum.org/whitepaper
3. Bài được đăng ký với tên “Blockchain-Based Flight Delay Insurance System Using Smart Contracts”, H. Kim, S. Kwon, J. Park, IEEE ICTC 2020; DOI được cung cấp: `10.1109/ICTC49870.2020.9289462`.
4. Etherisc flightDelay: https://github.com/etherisc/flightDelay
5. AXA Fizzy: https://www.axa.com/en/press/press-releases/axa-goes-blockchain-with-fizzy

Tên bài, tác giả, DOI, năm và nội dung của mục 3 chưa được kiểm chứng trong project. Không coi metadata đăng ký là bằng chứng. Nếu DOI không khớp, báo rõ và tìm nguồn thay thế phù hợp; không âm thầm gán nội dung.

- Tra cứu nguồn gốc/nguồn chính thức khi cần thông tin hiện hành, triển khai kỹ thuật hoặc khẳng định học thuật; ghi ngày truy cập khi phù hợp.
- Không bịa tài liệu, số liệu, trích dẫn hoặc kết quả thí nghiệm. Không suy diễn nội dung từ tiêu đề.
- Với related work, so sánh trigger, oracle, định phí, nguồn vốn, mức tự động hóa, đánh giá và hạn chế.
- Trình bày câu hỏi nghiên cứu có thể kiểm chứng; không mặc định nguyên mẫu có tính mới chỉ vì dùng blockchain.
- Tách phần nhóm tự xây dựng, phần kế thừa và thư viện sử dụng; giữ giấy phép và trích dẫn cần thiết.

## 10. Lộ trình và sản phẩm bàn giao

Không tự gán ngày hoàn thành khi chưa có lịch môn học. Thực hiện theo các mốc:

1. **Chốt bài toán:** yêu cầu, điều khoản bảo hiểm, câu hỏi nghiên cứu và tiêu chí đánh giá được ghi thành tài liệu.
2. **Nghiên cứu dữ liệu:** pipeline tái lập, EDA, baseline định phí và đánh giá theo thời gian.
3. **Thiết kế:** kiến trúc, state machine, threat model, nguồn vốn và giao thức oracle/báo giá.
4. **Triển khai:** contract, test, mock oracle, script triển khai và tích hợp báo giá.
5. **Demo:** frontend và kịch bản đầy đủ cho chuyến đúng giờ, trễ và hủy theo phạm vi đã chốt.
6. **Đánh giá và báo cáo:** kết quả thực nghiệm, so sánh baseline, hạn chế, slide và hướng dẫn chạy.

Khi bắt đầu tạo cấu trúc, có thể dùng `contracts/`, `test/`, `scripts/`, `data/`, `notebooks/`, `src/`, `frontend/`, `docs/` theo công cụ đã chọn. Đây là gợi ý; không tạo hàng loạt thư mục trống hoặc ghi đè cấu trúc đã có.

Tài liệu nên được bổ sung theo tiến độ: README hướng dẫn chạy, quyết định thiết kế, phương pháp dữ liệu/định phí, threat model, kết quả đánh giá và kịch bản demo. Mỗi tài liệu phải phản ánh trạng thái triển khai thực tế.

## 11. Quy ước phản hồi và hoàn thành công việc

Khi nhận một nhiệm vụ:

1. Xác định đầu ra và đọc ngữ cảnh liên quan.
2. Thực hiện phần việc trong phạm vi, giải thích các lựa chọn quan trọng.
3. Kiểm tra theo mức độ thay đổi và lưu sản phẩm vào repository khi được yêu cầu.
4. Báo ngắn gọn: đã làm gì, file nào thay đổi, đã kiểm tra gì, còn giới hạn nào.

Khi soạn báo cáo, ưu tiên lập luận có nguồn và kết quả có thể tái lập. Khi sửa lỗi, ưu tiên xác định nguyên nhân và thay đổi nhỏ nhất phù hợp. Khi nhóm hỏi kiến thức, giải thích gắn với luồng bảo hiểm của chính đồ án.

Thông tin đăng ký trong file này là bối cảnh gốc. Cập nhật các quyết định đã chốt theo chỉ dẫn mới của nhóm; không tự sửa thông tin thành viên hoặc tên đề tài.

Nhóm đang cân nhắc đổi dataset và chọn một open-source method/repository có kết quả được công bố để tái lập. Đây chưa phải quyết định đã chốt. Khi nghiên cứu lựa chọn, so sánh license, task/label, thời điểm dự đoán, data split, leakage, metric, graph definition và khả năng chạy lại. Không chọn chỉ dựa vào metric cao, không gán kết quả nguồn thành kết quả của nhóm. Theo dõi quyết định tại `docs/decision-log.md`.

### Giữ nhất quán với đề cương đã nộp

- Xác nhận đăng ký là căn cứ gốc: đề tài là bảo hiểm tham số trễ chuyến bay trên Ethereum/Solidity, dùng dataset hàng không Kaggle năm 2015 để phân tích rủi ro và định phí, rồi Smart Contract tự động xử lý mua policy và bồi thường khi trễ hoặc hủy.
- Mặc định giữ dataset Kaggle US DOT/BTS Flight Delays 2015 đã nêu trong hồ sơ. Dùng repo/open-source để tái lập method trên cùng dataset là cách phù hợp hơn với hồ sơ đã nộp.
- Không tự đổi sang dataset 2018–2022, Aeolus, EUROCONTROL hoặc nguồn khác trong thực nghiệm chính nếu chưa ghi rõ lý do và xin giảng viên xác nhận. Nếu nhóm cân nhắc đổi, trước hết tìm method/repo chạy được trên dataset 2015; chỉ đổi sau khi được chấp thuận.
- Có thể bổ sung graph analytics bằng cách dựng graph sân bay/tuyến bay từ dataset 2015, miễn là việc bổ sung này hỗ trợ câu hỏi nghiên cứu và không thay đổi đề tài bảo hiểm trễ chuyến bay.
- Repo tham khảo không thay thế đề tài: phải tái định nghĩa nhãn theo điều khoản policy đã thống nhất, chỉ dùng feature có sẵn tại thời điểm báo giá, ghi trích dẫn/license và tự chạy đánh giá trên split của nhóm. Không nhận kết quả benchmark của upstream là kết quả ANTs.
- Khi có chỉ dẫn mới từ giảng viên, ghi vào `docs/lecturer-feedback.md` và `docs/decision-log.md`, sau đó cập nhật brief, kế hoạch, kiến trúc và code cho nhất quán.

## 12. Yêu cầu bắt buộc của đồ án theo Project Lab

Nguồn yêu cầu do nhóm cung cấp từ trang IS355 Project Lab: https://itlearninghub.io.vn/courses/is355/project-lab.html

### Năm thành phần chính

Mỗi nhóm phải đáp ứng đủ năm thành phần. Một đề tài chỉ mô phỏng Blockchain bằng database thông thường sẽ không được chấp nhận.

1. **Blockchain thực tế:** phải có ít nhất một thành phần thực tế như Smart Contract, Testnet, Transaction, Event, Token hoặc NFT.
2. **Smart Contract:** phải thể hiện business logic, access control, event và validation. Với đồ án này, logic cần tương ứng với mua policy, xác nhận điều kiện chuyến bay, xử lý bồi thường và quản lý quỹ.
3. **Data / Analytics:** phải có ít nhất một hoạt động phân tích dữ liệu. Có thể dùng transaction analytics, financial analytics hoặc chỉ số phù hợp với bảo hiểm hàng không.
4. **AI/ML:** trang yêu cầu ghi là khuyến khích, không bắt buộc ở mức thành phần chung. Tuy nhiên nhóm đã đăng ký **Mức 4 — Research**, trong đó mô tả mức độ có Blockchain + AI + Graph Analytics + Security + Experimental Evaluation. Vì vậy phải xem AI, graph analytics và đánh giá thực nghiệm là mục tiêu cần lập kế hoạch, trừ khi giảng viên xác nhận cách áp dụng khác.
5. **DApp / Dashboard:** phải có giao diện tương tác bằng HTML/CSS/JavaScript, React, Streamlit, PySide hoặc framework phù hợp. Dashboard nên hiển thị chỉ số chính, biểu đồ analytics, lịch sử giao dịch và dự đoán rủi ro nếu có AI.

### Dữ liệu

Có thể sử dụng dữ liệu Blockchain, dữ liệu tài chính công khai/mô phỏng/do nhóm xây dựng và dữ liệu ESG khi phù hợp. Đồ án này dùng bộ dữ liệu Flight Delays 2015 từ Kaggle. Nếu sử dụng dữ liệu mô phỏng, báo cáo phải ghi rõ đó là dữ liệu mô phỏng và giải thích cách tạo.

### Kiến trúc và dữ liệu off-chain/on-chain

Báo cáo bắt buộc phải có sơ đồ kiến trúc gồm người dùng, DApp/UI, Web3 hoặc backend, Blockchain/Smart Contract và AI Model khi có. Nếu mô hình AI hoặc điểm rủi ro đưa ra quyết định trực tiếp cho Smart Contract, phải giải thích cơ chế chuyển dữ liệu off-chain vào on-chain bằng Oracle pattern, Signer Key/ECDSA Verification hoặc Chainlink Functions. Không trình bày dữ liệu off-chain như dữ liệu đã được Blockchain xác thực nếu chưa có cơ chế chuyển tiếp và xác minh.

### Quy trình thực hiện phải thể hiện trong đồ án

1. Xác định vấn đề thực tế, lý do cần Blockchain và vấn đề Blockchain giải quyết.
2. Nghiên cứu giải pháp hiện có, công nghệ liên quan, nghiên cứu trước đây và hạn chế.
3. Phân tích và thiết kế Use Case, User Flow, System Architecture, Data Model nếu có và Smart Contract Architecture.
4. Thiết kế, code, compile, test và deploy Smart Contract.
5. Thu thập, làm sạch, tạo đặc trưng, huấn luyện và đánh giá Data/AI nếu sử dụng.
6. Xây dựng Frontend, Web3 integration và kết nối Smart Contract/Blockchain.
7. Tích hợp Blockchain, Smart Contract, AI và Dashboard thành một hệ thống thống nhất.
8. Kiểm thử Smart Contract, business logic, access control, transaction, DApp và AI Model.

### Kiểm thử Smart Contract

Phải có test case với input và expected result. Tối thiểu cần bao phủ các trường hợp tương ứng với:

- Mua policy hợp lệ và input không hợp lệ.
- Bồi thường hợp lệ và điều kiện không hợp lệ.
- Gọi hàm bởi người có quyền và người không có quyền.
- Kết quả chuyến bay trễ, hủy, không đủ điều kiện và xử lý trùng lặp.
- Kiểm tra số dư, trạng thái policy, quỹ dự trữ và không thanh toán hai lần.

### Đánh giá hiệu năng

Chọn chỉ số phù hợp với đề tài và ghi kết quả đo thực tế. Có thể gồm Gas Used, Gas Cost, Transaction Time, Accuracy/F1/Recall/ROC-AUC của AI, Response Time và Transaction Success Rate của DApp. Không tự tạo số đo khi chưa chạy thực nghiệm.

### Yêu cầu bảo mật

Phải phân tích ít nhất ba rủi ro bảo mật. Các rủi ro phù hợp với đồ án gồm Reentrancy, Access Control, Integer/Arithmetic Issues, Oracle Manipulation, Front-running, Private Key Security và Input Validation. Mỗi rủi ro phải trình bày đủ ba phần: rủi ro là gì, có thể xảy ra như thế nào và giải pháp giảm thiểu.

### Năm sản phẩm phải nộp

1. Source Code gồm Smart Contract, Frontend, Backend, AI/ML và scripts nếu có.
2. Báo cáo đồ án ở định dạng PDF.
3. Slide thuyết trình.
4. Video demo khoảng 5–10 phút, trình bày Problem → Solution → Smart Contract → DApp → AI → Demo.
5. README hướng dẫn cài đặt, cấu hình, deploy, chạy DApp, chạy AI và thực hiện demo.

Không sao chép hoặc nộp bài làm của sinh viên khác.

### Cấu trúc báo cáo bắt buộc

1. **Giới thiệu:** vấn đề, lý do chọn đề tài, mục tiêu, phạm vi và đối tượng sử dụng.
2. **Cơ sở lý thuyết:** Blockchain, Smart Contract, Web3 và Token/NFT, DeFi, ESG hoặc AI/ML khi có.
3. **Phân tích bài toán:** Problem Statement, Business Process, User Roles, Use Case và yêu cầu functional/non-functional.
4. **Thiết kế hệ thống:** System Architecture, Smart Contract Architecture, Data Architecture, DApp Architecture và AI Architecture.
5. **Xây dựng hệ thống:** Smart Contract, Blockchain Deployment, Backend/Web3, Data Processing, AI Model và DApp.
6. **Thực nghiệm và đánh giá:** Test Case, Transaction, Gas Cost, AI Metrics, System Performance và Security Analysis.
7. **Kết luận và hướng phát triển:** kết quả, hạn chế và hướng phát triển.

### Demo và bảo vệ

Khi bảo vệ phải demo trực tiếp sản phẩm theo trình tự đề xuất: giới thiệu bài toán, kiến trúc, Smart Contract, DApp, thực hiện Transaction, kiểm tra Blockchain, demo AI và hiển thị kết quả. Chuẩn bị câu trả lời về lý do cần Blockchain, dữ liệu on-chain, quyền gọi hàm, bảo mật, vị trí của AI, lỗi transaction, điểm mới và hạn chế nghiên cứu.

### Biểu điểm 100

Trang Project Lab chia thành hai track. Vì nhóm đăng ký **Mức 4 — Research**, mặc định lập kế hoạch theo Track A có AI/ML và cần xác nhận với giảng viên nếu nhóm muốn bỏ AI.

| Hạng mục | Track A — Có AI/ML | Track B — Không AI/ML |
| --- | ---: | ---: |
| Phân tích bài toán và ý tưởng | 10 | 10 |
| Cơ sở lý thuyết và nghiên cứu | 10 | 10 |
| Smart Contract & Blockchain / Advanced Business Logic | 20 | 25 |
| Data & AI/ML / On-chain Data Analytics | 15 | 10 |
| DApp và giao diện tương tác | 15 | 20 |
| Kiểm thử và bảo mật | 10 | 10 |
| Báo cáo | 10 | 10 |
| Demo và thuyết trình | 10 | 10 |
| **Tổng** | **100** | **105** |

Track B dành cho đề tài chuyên sâu về DeFi Logic, Tokenomics hoặc Security không sử dụng AI/ML. Không cộng dồn hai track cho cùng một đề tài. Trang ghi tổng Track B là 105 dù phần mô tả biểu điểm 100, nên phải xác nhận cách quy đổi với giảng viên trước khi dùng để lập kế hoạch điểm.

### Mức độ đồ án

| Mức | Thành phần |
| --- | --- |
| ★ Basic | Smart Contract + Blockchain + DApp |
| ★★ Intermediate | Smart Contract + Blockchain + DApp + Data Analytics |
| ★★★ Advanced | Smart Contract + Blockchain + DApp + Data + AI/ML |
| ★★★★ Research | Blockchain + AI + Graph Analytics + Security + Experimental Evaluation |

Đề tài của nhóm đã đăng ký **Mức 4 — Research**, vì vậy mọi kế hoạch, báo cáo và demo phải hướng đến các thành phần của mức này. Nếu phạm vi dữ liệu chuyến bay không phù hợp với graph analytics, phải định nghĩa rõ graph nào được phân tích, chẳng hạn mạng sân bay–chuyến bay, liên kết hãng–sân bay hoặc đồ thị giao dịch/policy, rồi nêu lý do và chỉ số sử dụng.

### Tiêu chí tối thiểu để hoàn thành

Đồ án phải chứng minh đầy đủ chuỗi sau: bài toán thực tế, giải pháp Blockchain, Smart Contract, triển khai hoặc thử nghiệm thực tế, giao diện hoặc phương thức tương tác, dữ liệu hoặc thực nghiệm và đánh giá kết quả.

Không xem một đồ án là đạt chỉ vì có giao diện đẹp nhưng không có Blockchain thật, Smart Contract đơn giản nhưng không gắn với bài toán nghiệp vụ, hoặc có AI chạy trên dataset trong khi Blockchain chỉ xuất hiện ở phần lý thuyết.

### Dev Stack khuyến nghị

Đây là bộ công cụ tham khảo cho việc triển khai, không phải yêu cầu phải dùng toàn bộ:

- Smart Contract execution: Vyper hoặc Solidity, Remix IDE, Ape Framework hoặc Hardhat, Sepolia Testnet hoặc Anvil local.
- Indexing và data engine: Web3.py, Pandas, NetworkX cho graph analytics, The Graph/GraphQL khi phù hợp.
- AI engine: Scikit-Learn, XGBoost, Isolation Forest.
- Frontend và Web3 integration: Streamlit cho Data App, hoặc Next.js kết hợp Wagmi/Ethers.js.

Khi chọn công cụ, ghi phiên bản và lý do trong README. Chỉ thêm thành phần khi có vai trò trong hệ thống hoặc đánh giá.

### Định hướng sản phẩm cuối cùng

Sản phẩm hướng tới luồng User → DApp/Web UI → Blockchain và AI/Data Analytics → giải pháp DeFi & Banking. Nhánh Blockchain gồm Smart Contract, Token/NFT nếu có và Transaction. Nhánh AI/Data gồm Analytics, ML Prediction và Risk Score. Với đồ án bảo hiểm trễ chuyến bay, Risk Score có thể hỗ trợ định phí và kết quả chuyến bay được đưa vào Smart Contract thông qua cơ chế oracle hoặc chữ ký xác minh đã nêu.

Website mô tả lộ trình bảy tuần theo các mảnh ghép: Green Finance và Blockchain nền tảng, Bảo mật và Danh tính, Token/Carbon Credit, RWA/NFT, DeFi/Green Banking, Data/AI/DApp và bảo vệ đồ án. Dùng lộ trình này để sắp xếp công việc khi phù hợp, không coi tên tuần là yêu cầu riêng của đề tài nếu giảng viên có hướng dẫn cập nhật.

## 13. Cập nhật theo nhận xét giảng viên

Nhóm đã cung cấp nhận xét bằng văn bản: hoàn thiện đề cương và sơ đồ kiến trúc; rà soát thứ tự/tính xác thực tài liệu tham khảo; chặn mua policy quá sát giờ bay và lưu flight ID/ngày/giờ khởi hành dự kiến; có baseline định phí và thử cải tiến LR/XGBoost hiệu chuẩn theo temporal split, chỉ dùng feature biết trước khi mua; đánh giá Brier score, tỷ lệ phí/chi trả, khả năng pool thanh toán, gas và độ trễ; phân tích điểm tin cậy tập trung và failure modes của Oracle.

Giảng viên nêu dữ liệu 2015 khá cũ và gợi ý có thể bổ sung dữ liệu mới hơn từ BTS để kiểm tra mức phí; chưa ghi nhận yêu cầu bắt buộc thay dataset chính. Tạm giữ Kaggle 2015 theo hồ sơ cho đến khi có xác nhận khác. Giảng viên khuyến nghị Vyper + Ape + Anvil; trước khi chuyển khỏi Solidity, kiểm tra khả năng thực hiện và xác nhận đây là yêu cầu hay khuyến nghị. Nhận xét này chưa nói rõ Graph Analytics; do đăng ký Mức 4, không tự bỏ phần graph, hãy hỏi phạm vi tối thiểu trước khi mở rộng sang GNN.

Kế hoạch tháng và bản ghi phản hồi chi tiết nằm trong `PROJECT_PLAN_1_MONTH.md`, `docs/lecturer-feedback.md` và `docs/decision-log.md`. Các gợi ý của giảng viên không được mô tả như quyết định đã triển khai cho tới khi nhóm chốt và có bằng chứng.

Khảo sát graph repo chuyên biệt nằm trong `docs/graph-repo-research.md`. `yajun668/FlightDelayPrediction` là method phù hợp để nghiên cứu propagation score, nhưng dùng dữ liệu 2023 và dự đoán departure delay; không coi metric upstream là kết quả ANTs, không tự đổi dataset chính từ Kaggle 2015.
