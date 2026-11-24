# Định hướng đồ án IS355 — ANTs

**Nhóm ANTs · Q4H648 · DeFi & Banking · Mức 4 — Research**  
**Đề tài đăng ký** · Blockchain-Based Parametric Flight Delay Insurance Supported by Historical Aviation Data Analysis  
**Trạng thái** · Bản trao đổi nội bộ ngày 21/11/2026. Các giá trị ghi «đề xuất» cần nhóm thống nhất trước khi dùng chung cho code, dữ liệu và demo.

## 1. Nhóm đang làm sản phẩm gì?

Hành khách chọn một chuyến bay, xem phí bảo hiểm và mức bồi thường, rồi mua bằng ví trước hạn. Một dịch vụ Python dùng dữ liệu chuyến bay lịch sử để ước lượng xác suất phát sinh bồi thường và tạo báo giá. Khi chuyến bay có kết quả cuối cùng, oracle gửi kết quả vào Smart Contract. Contract áp dụng điều khoản đã khóa lúc mua, ghi có khoản bồi thường nếu đủ điều kiện và cho hành khách rút tiền.

Blockchain ghi nhận giao dịch mua, kết quả oracle đã gửi, trạng thái policy và khoản tiền quỹ phải dành cho khách. Dịch vụ báo giá chịu trách nhiệm về mức phí, oracle chịu trách nhiệm về kết quả chuyến bay. Trong demo, oracle dùng kết quả mô phỏng, còn giao dịch mua và nhận tiền chạy trên local EVM với ETH thử nghiệm.

| Nội dung | Trạng thái hiện tại |
| --- | --- |
| Bài toán và dữ liệu | Đã chốt ở cấp nhóm. Giữ bảo hiểm trễ hoặc hủy chuyến bay và **Kaggle Flight Delays 2015** làm dữ liệu thực nghiệm chính. BTS mới hơn là lựa chọn kiểm tra bổ sung nếu được thống nhất. |
| Smart Contract | Đã chọn **FlySure** làm nền tham khảo theo hướng Solidity + Hardhat. Ghim commit, giữ thông tin license, chạy test upstream rồi điều chỉnh cho policy ANTs. Overdoo và Etherisc dùng để tham khảo kiến trúc và related work. [Repo FlySure](https://github.com/y4hyya/FlySure) |
| Stack và môi trường | Local EVM là mục tiêu demo. Cần xác nhận với giảng viên về khuyến nghị Vyper + Ape + Anvil và yêu cầu testnet trước khi khóa stack. |
| Repo dự đoán | Dùng [`Prashant-4527/flight-delay-prediction`](https://github.com/Prashant-4527/flight-delay-prediction) làm điểm xuất phát cho pipeline ML trên Kaggle 2015. Đây là repo nhóm đã trao đổi theo hướng làm theo và xếp ưu tiên số một. Cần ghim commit, chạy thử và đổi nhãn theo policy ANTs. |
| Graph Analytics | Đề xuất bỏ graph features khỏi luồng định phí chính. Đồ thị sân bay–tuyến bay và các chỉ số mạng có thể là phần phân tích riêng. Cần xác nhận với giảng viên phạm vi tối thiểu để đáp ứng Mức 4. |
| Thực nghiệm | Đã chốt hướng đánh giá hiệu quả tài nguyên và dấu chân vận hành của Blockchain/DApp, gồm benchmark FlySure B0/B1 và đánh giá điện năng/CO₂e khi có phương pháp phù hợp. Nhánh định phí đánh giá Brier score, mức chi trả so với phí thu và khả năng thanh toán của quỹ. |
| Tiến độ kiểm chứng | Workspace này có tài liệu và prototype Python mô phỏng nghiệp vụ. Tiến độ contract, DApp, pipeline và số đo cần được đối chiếu với nhánh nhóm đang làm trước khi xác nhận mốc. |

## 2. Điều khoản đề xuất để cả nhóm dùng chung

Các giá trị dưới đây cho phép cả ba thành viên thảo luận trên cùng một kịch bản. Sau khi thống nhất, Nguyên dùng đúng định nghĩa này để tạo nhãn và báo giá, Thùy dùng để viết contract và test, Quốc Anh dùng để hiển thị điều khoản trên DApp.

| Quyết định | Phương án đề xuất cho demo |
| --- | --- |
| Định danh chuyến bay | Dùng hãng, số hiệu, sân bay đi/đến và ngày khởi hành theo lịch tại sân bay đi. Lưu thêm giờ khởi hành dự kiến dưới dạng Unix timestamp UTC và đưa vào khóa định danh để phân biệt các lịch cùng ngày. Thống nhất quy tắc chuẩn hóa trước khi sinh `flightId`. |
| Trễ đủ điều kiện | Trễ **giờ đến từ 120 phút trở lên**. Trễ 119 phút kết thúc không bồi thường. Trễ đúng 120 phút đủ điều kiện. |
| Hủy chuyến | Kết quả hủy đã xác nhận đủ điều kiện nhận cùng mức bồi thường. Nếu trường hợp hủy đồng thời có thông tin trễ hoặc chuyển hướng, ưu tiên hủy và ghi nhận một lần. |
| Chuyển hướng và thiếu kết quả | Chuyến chuyển hướng có kết quả cuối cùng, không bị hủy, được đề xuất nằm ngoài phạm vi bồi thường. Chuyến chưa có kết quả hoặc thiếu số phút trễ cần thiết tiếp tục chờ tới hạn xử lý. Phương án để nhóm biểu quyết là hoàn phí nếu sau **72 giờ kể từ giờ khởi hành dự kiến** vẫn chưa có kết quả hợp lệ. |
| Hạn mua | Mua khi thời gian giao dịch **nhỏ hơn** giờ khởi hành dự kiến trừ 24 giờ, báo giá còn hiệu lực và chuyến chưa có kết quả cuối cùng. Mua đúng mốc 24 giờ bị từ chối theo phương án này. |
| Phí và bồi thường | Payout cố định minh họa **0,01 ETH thử nghiệm**. Phí thuần bằng `p × payout`, với `p` là xác suất chi trả ước lượng trước lúc mua. Chốt phí tối thiểu trước khi chạy mô phỏng tài chính. Dùng wei trên contract và quy định làm tròn phí lên đến wei. |
| Giới hạn và vốn | Đề xuất một policy trên mỗi ví cho mỗi `flightId`. Một chuyến vẫn có thể có nhiều policy thuộc các ví khác nhau. Quỹ phải đủ vốn dự trữ trước khi nhận policy mới. Hạn mức tổng chi trả theo chuyến là quyết định cần chốt nếu nhóm đưa vào contract. |

**Điểm cần thống nhất nếu chọn timeout hoàn phí.** Kết quả chỉ được ghi nhận khi thời gian giao dịch còn trước hạn. Khi tới hạn, policy được hoàn phí nếu chuyến chưa có kết quả hợp lệ. Nếu oracle đã gửi kết quả hợp lệ trước hạn, policy tiếp tục giải quyết theo kết quả đó kể cả khi giao dịch giải quyết đến sau hạn. Cặp quy tắc này cần cùng một cách so sánh timestamp trong contract và test.

## 3. Kiến trúc và dữ liệu bàn giao giữa các nhánh

| Thành phần | Trách nhiệm và đầu ra cần thống nhất |
| --- | --- |
| Pipeline dữ liệu và mô hình | Làm sạch dữ liệu 2015, tạo nhãn, huấn luyện mô hình bảng và sinh xác suất. Bàn giao phiên bản dataset/model, bảng metric và một bộ chuyến mẫu có báo giá để DApp chạy được. |
| Dịch vụ báo giá | Nhận chuyến bay và địa chỉ ví. Trả `flightId`, ngày bay, giờ khởi hành UTC, `premiumWei`, `payoutWei`, ngưỡng trễ, hạn mua, `quoteExpiry`, `nonce`, phiên bản báo giá/mô hình và chữ ký. Đề xuất trao đổi số tiền wei qua JSON dưới dạng chuỗi số nguyên. |
| DApp và ví | Hiển thị phí, số tiền bồi thường, hạn mua và điều khoản. Gửi giao dịch mua qua ví, đọc receipt/event và trạng thái policy. Màn hình policy hiển thị bước phù hợp như chờ kết quả, đủ điều kiện rút, đã nhận hoặc kết thúc. Dashboard hiển thị chỉ số ML và giao dịch demo. |
| Smart Contract | Xác minh báo giá, khóa điều khoản, nhận phí, dự trữ vốn và phát event. Nhận kết quả chuyến bay từ oracle được cấp quyền, giải quyết từng policy và quản lý quyền rút tiền. Bàn giao ABI, địa chỉ deploy, chain ID, event và các lỗi dự kiến để DApp xử lý. |
| Mock oracle | Gửi đúng `flightId`, trạng thái cuối cùng và số phút trễ đến nếu áp dụng. Bàn giao bộ tình huống đúng giờ, trễ sát ngưỡng, trễ đủ ngưỡng và hủy. Cùng một kết quả được dùng cho mọi policy thuộc chuyến đó. |

**Báo giá ký ngoài chuỗi là thiết kế đề xuất.** Thống nhất schema và quy tắc ký giữa Python, Solidity và frontend trước khi tách nhánh triển khai. Chữ ký cần ràng buộc chain ID, địa chỉ contract, ví mua, dữ liệu định danh chuyến, premium, payout, ngưỡng, hạn mua, hạn báo giá, nonce và phiên bản. Contract kiểm tra signer có quyền và chỉ chấp nhận nonce một lần. Tách quyền signer báo giá, oracle và quản lý quỹ trong thiết kế.

**Luồng tiền đề xuất.** Mua thành công chuyển policy sang `Active` và giữ dự trữ theo mức payout đã khóa. Khi đủ điều kiện, contract chuyển khoản dự trữ sang khoản phải trả và policy sang `Claimable`. Khách rút thành công thì policy sang `Paid`. Kết quả không đủ điều kiện đưa policy sang `Closed` và giải phóng dự trữ. Nếu chọn hoàn phí, ghi có khoản hoàn phí theo nhánh riêng. Với mọi giao dịch, số dư quỹ phải đủ trang trải cả policy còn hiệu lực lẫn các khoản đã ghi có nhưng chưa rút. Nếu số tiền hoàn phí có thể vượt payout, phải dự trữ theo nghĩa vụ tối đa của policy.

**Điểm nối cần khóa đầu tiên.** Một fixture chuyến bay và báo giá mẫu, các test vector dùng chung để đối chiếu `flightId` và chữ ký, ABI mua/đọc/giải quyết/rút, cách đọc event và mã lỗi. Có thể dùng báo giá mẫu để nối luồng Web3 trong lúc Nguyên hoàn thiện mô hình. Khi thay bằng báo giá từ model, dùng cùng schema và kiểm tra lại toàn tuyến.

## 4. Data, ML, Graph và cách chứng minh kết quả

1. **Tạo dữ liệu và nhãn.** Kiểm kê schema và nguồn, ghi phiên bản dữ liệu, chuẩn hóa mã sân bay, ngày giờ và các mã sân bay dạng số. Nếu nhóm duyệt điều khoản đề xuất, nhãn `1` là hủy hoặc trễ đến ≥120 phút, nhãn `0` là kết quả hợp lệ không được bồi thường. Chuyến thiếu kết quả hoặc thiếu số phút trễ cần thiết được đánh dấu chưa xác định và thống kê riêng. Trường hợp hoàn phí được theo dõi trong mô phỏng tài chính.
2. **Chia và lọc đặc trưng.** Phương án mở đầu là tháng 1–8 train, tháng 9 validation, tháng 10–12 test. Kiểm tra độ phủ và phiên bản ánh xạ sân bay trước khi khóa split. Chỉ dùng thông tin đã biết trước lúc mua như hãng, tuyến và giờ bay theo lịch. Kết quả thực tế và nguyên nhân trễ chỉ phục vụ tạo nhãn hoặc phân tích sau chuyến bay. Fit bước tiền xử lý trên train, dùng validation để chọn mô hình hoặc hiệu chuẩn, rồi đánh giá trên test.
3. **Tái sử dụng pipeline Prashant.** Repo gốc dự đoán **trễ đến hơn 15 phút** trên chuyến hoàn tất và có Logistic Regression, Random Forest, XGBoost. ANTs ghim commit và chạy thử pipeline, sau đó tạo nhãn theo policy của mình, rà soát leakage và chạy lại theo temporal split. So sánh **M0** (tỷ lệ biến cố lịch sử, có thể thêm smoothing theo hãng/tuyến) với **M1** (Logistic Regression). Có thể thêm XGBoost hiệu chuẩn nếu còn thời gian. Dùng chung nhãn, split và hàng test. Kết quả báo cáo lấy từ run của ANTs.
4. **Graph Analytics là phương án riêng cho Mức 4.** Nếu giảng viên chấp nhận mức phân tích mô tả, dùng data 2015 để dựng đồ thị có hướng sân bay đi → sân bay đến, trọng số là số chuyến. Bàn giao bảng hoặc hình về các sân bay và tuyến quan trọng bằng weighted degree hoặc PageRank. Luồng báo giá dùng M0/M1 và chạy độc lập với phần này. Đưa đặc trưng graph vào model và so sánh có/không graph là mở rộng tùy kết quả trao đổi với giảng viên.
5. **Đánh giá xác suất và quỹ.** Báo Brier score, biểu đồ hiệu chuẩn và PR-AUC nếu phù hợp. Mô phỏng lại dòng tiền theo thứ tự thời gian, công bố vốn đầu kỳ, quy tắc mua giả định, số policy, premium, payout và hoàn phí. Ghi riêng số dư thấp nhất, số lần quỹ từ chối nhận thêm policy và tỷ lệ tiền bồi thường trên phí thu với mẫu số đã nêu. Dữ liệu 2015 phục vụ nghiên cứu hồi cứu.

## 5. Kiểm thử Blockchain và đo hiệu năng

| Nhóm kiểm tra | Kịch bản và bằng chứng cần lưu |
| --- | --- |
| Mua policy | Thành công khi phí, chữ ký, hạn mua và quỹ hợp lệ. Kiểm tra sai phí, mua đúng hoặc sau cutoff, báo giá hết hạn, sai ví, nonce đã dùng và quỹ thiếu. Lưu input, expected, actual. |
| Xử lý chuyến bay | Demo chạy được ba nhánh đúng giờ, trễ đủ ngưỡng và hủy. Test thêm 119/120/121 phút theo ngưỡng đề xuất, nhiều ví cùng chuyến, oracle không có quyền và kết quả cuối trùng hoặc mâu thuẫn. Nếu chọn hoàn phí, test trước, đúng và sau hạn. |
| Tiền và trạng thái | Payout đúng ví, đúng khoản, một lần. Kiểm tra dự trữ và khoản phải trả sau từng chuyển trạng thái. Thử từ chối giao dịch rút làm xâm phạm tiền đã cam kết. Lưu receipt, số dư và event để đối chiếu với DApp. |
| Bảo mật | Viết ít nhất ba mục theo cấu trúc rủi ro → tình huống → giảm thiểu. Ưu tiên oracle gửi sai/trễ hoặc lộ khóa, sai quyền quản trị, replay báo giá và reentrancy khi rút. Nêu cơ chế nào đã được kiểm thử và giả định nào còn nằm ở bên vận hành oracle. |
| Gas và độ trễ | **B0** tắt, **B1** bật compiler optimizer trên cùng commit, compiler version, môi trường, trạng thái đầu và kịch bản. Lưu `gasUsed` khi deploy và khi mua, gửi kết quả, giải quyết, rút. Ghi cách đo thời gian gửi–nhận receipt trên local và tách khỏi thời gian chờ dữ liệu oracle. |

### Đánh giá tài nguyên và CO₂e của Blockchain/DApp

Đây là hướng đã chốt cùng FlySure. Phạm vi là tài nguyên và điện năng phát sinh khi chạy workload bảo hiểm trên môi trường thử nghiệm. So sánh B0/B1 với cùng source code, test, trạng thái ban đầu và bộ giao dịch. Báo gas theo từng giao dịch, tổng gas theo kịch bản, số transaction, số lần ghi storage nếu đo được, độ trễ và CPU/bộ nhớ nếu thu được. Nếu chỉ số bằng nhau, báo đúng kết quả. B2 là một thay đổi tối ưu code có test tương đương và chỉ thực hiện nếu còn thời gian.

| Repo hoặc nguồn phương pháp | Cách dùng trong đồ án |
| --- | --- |
| **FlySure** | Chạy cùng một bộ giao dịch với B0 và B1 để thu gas và độ trễ. Đây là workload đầu vào cho phép đo điện năng local. [Repo FlySure](https://github.com/y4hyya/FlySure) |
| **`hyperledger-labs/blockchain-carbon-accounting`** | Repo carbon đã nhắc trong buổi khảo sát. Dùng tham khảo cách hệ thống ghi nhận và tính toán phát thải. Phạm vi repo là ứng dụng carbon accounting trên Blockchain. [Repo Hyperledger Carbon Accounting](https://github.com/hyperledger-labs/blockchain-carbon-accounting) |
| **`mlco2/codecarbon`** | Công cụ đề xuất để thử trên máy benchmark của nhóm. Dùng chế độ `machine` để theo dõi điện năng của CPU, RAM và GPU trong lúc local node và bộ phát giao dịch cùng chạy. Ghi rõ phiên bản công cụ và phương pháp mà máy hỗ trợ. Đầu ra CO₂e từ công cụ là ước tính. [Repo CodeCarbon](https://github.com/mlco2/codecarbon) · [Phương pháp CodeCarbon](https://docs.codecarbon.io/3.3/explanation/methodology/) |
| **Cambridge và CCRI** | Nguồn phương pháp đã nhắc trong buổi khảo sát để mô tả điện năng và CO₂e ở cấp mạng Ethereum. Kết quả của ANTs có phạm vi là máy benchmark và workload local. [Cambridge Ethereum Methodology](https://ccaf.io/cbnsi/ethereum/methodology) · [Ethereum Energy Consumption](https://ethereum.org/energy-consumption/) |

**Nếu đo được điện năng**, dùng cùng máy, phạm vi đo và workload lặp lại cho hai cấu hình. Ghi số policy, số lần chạy, thời gian, thiết bị hoặc công cụ đo và điện năng nền trong khoảng thời gian tương ứng. Ước tính điện năng tăng thêm bằng điện năng khi chạy trừ điện năng nền. Báo điện năng theo kịch bản hoặc mỗi policy, rồi tính `CO₂e (kg) = điện năng (kWh) × hệ số phát thải điện (kg CO₂e/kWh)`. Ghi rõ nguồn, vùng và năm của hệ số.

**Nếu chỉ có mô hình điện năng**, ghi CO₂e là ước tính, kèm đầu vào và giả định. Nếu thiếu cả số đo lẫn mô hình đủ căn cứ, trình bày gas, độ trễ và tài nguyên đã đo, rồi ghi giới hạn của phần CO₂e. Kết quả local mô tả máy và workload thử nghiệm. Gas được báo bằng gas units, còn CO₂e cần dữ liệu hoặc ước tính điện năng riêng.

## 6. Phân công và điều kiện bàn giao

| Thành viên | Phần phụ trách | Đầu ra để teammate nhận và kiểm tra |
| --- | --- | --- |
| **Quốc Anh** | Web3 và DApp, đầu mối video demo | Giao diện kết nối ví, mua, xem trạng thái và rút tiền. Dashboard đọc kết quả mẫu từ Nguyên. Kịch bản demo và hướng dẫn chạy từ ví đến receipt. Đối chiếu ABI/event với Thùy. |
| **Nguyên** | Data/ML/Graph/định phí, đầu mối source code và README | Pipeline chạy lại được theo hướng Prashant, bộ chuyến và báo giá mẫu, bảng metric M0/M1, kết quả mô phỏng quỹ và đầu ra graph theo phạm vi đã xác nhận. Đối chiếu nhãn và công thức với điều khoản nhóm thống nhất. |
| **Thùy** | Smart Contract/oracle/test, đầu mối PDF và slide | Commit tham chiếu FlySure, contract và script local, ABI/event, test input–expected–actual, benchmark B0/B1, rủi ro bảo mật và ghi nhận phương pháp hoặc giới hạn đo CO₂e. Đối chiếu báo giá của Nguyên và kiểm tra gọi contract cùng Quốc Anh. |

Mỗi người viết phần báo cáo và cung cấp bằng chứng cho module mình. Đầu mối tổng hợp và kiểm tra tính nhất quán giữa **source code, README, báo cáo PDF, slide và video demo 5–10 phút**. Phần nghiên cứu liên quan cần tối thiểu ba bài bình duyệt theo góp ý của giảng viên. Nhóm xác minh metadata và DOI trước khi trích dẫn, đồng thời ghi rõ phần kế thừa FlySure và phần ANTs tự điều chỉnh, tích hợp hoặc đo lại.

| Giai đoạn | Điều kiện để đánh dấu đạt |
| --- | --- |
| **Tích hợp đầu** | Luồng local chạy từ báo giá đến mua, oracle gửi kết quả và nhận payout. DApp đọc được ít nhất một kết quả model. |
| **Khóa tính năng** | Cố định interface và phiên bản dùng để đo. Có kết quả test, bảng model, mô phỏng quỹ và số liệu gas/độ trễ. Ghi phạm vi Graph Analytics và khả năng đo điện năng/CO₂e để hoàn thiện báo cáo. |
| **Diễn tập** | Một thành viên khác chạy từ checkout sạch theo README. Cả nhóm chạy ba kịch bản demo và kiểm tra PDF, slide, video dựa trên cùng kết quả. |
| **Đóng gói nội bộ** | Chốt phiên bản source và đủ năm giao phẩm. Đối chiếu hạn, kênh nộp và lịch bảo vệ theo thông báo giảng viên. |

Đối chiếu nhánh làm việc và lưu bằng chứng cho từng giai đoạn đã đạt.

## 7. Checklist cho buổi thống nhất

- [ ] **Điều khoản và nhãn.** Chốt loại trễ, ngưỡng, hạn mua, payout, phí tối thiểu, chuyển hướng, timeout và giới hạn policy. Dùng ít nhất ba ví dụ đúng giờ, trễ đúng ngưỡng và hủy để đối chiếu nhãn với kết quả contract.
- [ ] **Stack và code tham khảo.** Chốt commit FlySure, cách xác nhận khuyến nghị Vyper + Ape + Anvil, môi trường local và yêu cầu testnet nếu có.
- [ ] **Tích hợp.** Chốt fixture, cách sinh `flightId`, schema báo giá, quy tắc ký, ABI/event và thứ tự giao các đầu ra giữa ba thành viên.
- [ ] **Phạm vi thực nghiệm.** Ghim commit Prashant, chốt temporal split và bộ so sánh M0/M1. Xác nhận với giảng viên liệu phân tích đồ thị sân bay riêng có đủ cho Mức 4. Thống nhất workload B0/B1, thử CodeCarbon hoặc thiết bị đo trên máy benchmark, rồi chốt phạm vi công bố CO₂e dựa trên dữ liệu thu được.
- [ ] **Phân công.** Đối chiếu code nhóm đang làm với checklist giao phẩm, ghi người phụ trách và bằng chứng còn thiếu. Xác nhận track chấm với giảng viên. Ghi quyết định sau buổi họp vào nhật ký dự án.
