# Nhật ký quyết định và hướng nghiên cứu — ANTs Q4H648

Tài liệu này ghi các thông tin đã đăng ký, yêu cầu môn, đề xuất làm việc và suy nghĩ mới của nhóm. Mục có nhãn **đang cân nhắc** chưa phải quyết định nhóm đã chốt. Cập nhật trạng thái sau khi hỏi đủ thành viên hoặc giảng viên.

## Đã đăng ký

- Môn IS355 — Công nghệ Blockchain.
- Nhóm ANTs, mã Q4H648.
- Đề tài: **Blockchain-Based Parametric Flight Delay Insurance Supported by Historical Aviation Data Analysis**.
- Chủ đề B — DeFi & Banking.
- Mức 4 — Research.
- Dataset được ghi trong xác nhận đăng ký: Kaggle Flight Delays 2015.

## Yêu cầu môn đã nhận từ nội dung Project Lab

- Có bài toán thực tế, thành phần Blockchain thật, Smart Contract có nghiệp vụ, dữ liệu/thực nghiệm, đánh giá và giao diện/phương thức tương tác.
- Mức 4 mô tả Blockchain + AI + Graph Analytics + Security + Experimental Evaluation.
- Nộp Source Code, báo cáo PDF, slide, video demo khoảng 5–10 phút và README.
- Báo cáo gồm 7 chương; phải có sơ đồ kiến trúc, test case và phân tích ít nhất 3 rủi ro bảo mật.
- AI/ML được ghi là khuyến khích trong phần thành phần chung, nhưng AI và graph analytics xuất hiện trong mô tả Mức 4. Cần xác nhận yêu cầu áp dụng cho nhóm.
- Bảng biểu điểm Track B trên nội dung nhóm gửi cộng thành 105 dù trang gọi biểu điểm 100. Cần hỏi cách tính. Chưa biết nhóm chính thức được phân track nào.

## Hướng kỹ thuật đang cân nhắc

## Quyết định mới — hướng triển khai Smart Contract và đánh giá tài nguyên

Trạng thái: **đã chốt ở cấp nhóm, cần xác nhận với giảng viên nếu thay stack hoặc thay phạm vi chấm**.

- Giữ bài toán gốc: bảo hiểm tham số trễ hoặc hủy chuyến bay trên Ethereum/EVM, định phí từ dữ liệu Flight Delays 2015.
- Dùng repo `y4hyya/FlySure` làm codebase tham khảo chính cho flight-insurance DApp vì repo có Solidity, Hardhat, oracle, policy, payout, test và gas reporting. License của repo là MIT. Nhóm không coi code này là đã audit hoặc production-ready.
- Không dùng Overdoo làm codebase chính. Overdoo được giữ làm nguồn tham khảo kiến trúc và related work. Các giới hạn của Overdoo không được nhận là đã sửa trong sản phẩm ANTs.
- Nhóm sẽ fork một commit cụ thể của FlySure, chạy test gốc trước, sau đó điều chỉnh tối thiểu cho policy ANTs: flight ID/ngày bay/giờ khởi hành, cutoff mua, threshold, premium, payout, mock oracle và kiểm tra double claim.
- Premium và mô hình rủi ro chạy off-chain bằng Python. Smart Contract chỉ xác minh điều khoản, nhận tiền, lưu policy, nhận kết quả oracle và xử lý payout.
- Thí nghiệm gas có hai cấu hình trên cùng source code FlySure. B0 tắt Solidity compiler optimizer. B1 bật optimizer với cấu hình được ghi trong môi trường. Hai cấu hình dùng cùng workload, test, compiler version và network. Nếu đủ thời gian, B2 chỉ thêm một thay đổi code tối ưu có lý do và kiểm thử tương đương.
- Chỉ gọi một phiên bản là tối ưu khi gas report hoặc benchmark thực tế cho thấy cải thiện và toàn bộ test nghiệp vụ/bảo mật vẫn đạt. Không lấy tuyên bố `gas-optimized` trong README upstream làm kết quả của nhóm.
- Đánh giá CO₂ tập trung vào dấu chân vận hành của Blockchain/DApp. Gas, transaction count, storage writes, latency, CPU/memory là số đo chính. CO₂e chỉ báo cáo là đo trực tiếp khi có dữ liệu điện năng phù hợp, hoặc là kết quả mô hình hóa khi dùng hệ số phát thải và giả định được ghi rõ.
- Không tuyên bố gas giảm đồng nghĩa CO₂ giảm theo cùng tỷ lệ. Không dùng Anvil để đại diện cho tổng phát thải Ethereum Mainnet.
- Kaggle Flight Delays 2015 vẫn là dữ liệu thực nghiệm chính. Kaggle Ethereum Blockchain chỉ là nguồn bổ sung tùy chọn cho phân tích hành vi/hệ sinh thái và phải kiểm tra schema, quyền truy cập, license/điều khoản trước khi dùng.
- Không đổi đề tài thành carbon credit, CO₂ hàng không, NFT hoặc một DApp thương mại khác.

### Ý định mới của nhóm

Nhóm từng cân nhắc **đổi dataset** và chọn một **open-source project/method có metric công bố cao** để tái lập hoặc điều chỉnh cho đồ án. Mục tiêu là tận dụng code và dữ liệu phù hợp. Ở thời điểm khảo sát này, dataset, repo, model, nhãn, metric và phạm vi graph còn chờ chốt.

**Kiểm tra nhất quán với hồ sơ:** xác nhận đăng ký nêu cụ thể dataset Kaggle năm 2015 và dùng dữ liệu đó để định phí bảo hiểm. Vì vậy mặc định ưu tiên repo/method có thể chạy trên dataset 2015. Đổi dataset sẽ làm lệch chi tiết hồ sơ, cần hỏi giảng viên trước khi thay đổi thực nghiệm chính.

### Nguyên tắc chọn nguồn và benchmark

Khi tìm repo/dataset, lập bảng đối chiếu các mục sau trước khi chọn:

1. License của code, điều kiện sử dụng dữ liệu và yêu cầu attribution.
2. Task, unit of prediction, target label/threshold và prediction time.
3. Dataset/version, thời kỳ, quốc gia/vùng bay, số dòng và các trường sẵn có.
4. Cách chia train/validation/test, có temporal split hay không, có leakage hay không.
5. Metric nào được báo cáo, cách tính, baseline so sánh và kết quả có tái lập được không.
6. Graph definition: node, edge, weight, graph snapshot, node/edge feature và cách tránh dùng tương lai.
7. Môi trường chạy, dependency, phần cứng, thời gian huấn luyện và khả năng tái lập.
8. Mức độ khớp với policy insurance: dự đoán rủi ro trước chuyến bay, hủy/trễ theo ngưỡng hợp đồng, và đầu ra có dùng để đề xuất phí được không.

Metric cao từ repo khác không đảm bảo sẽ lặp lại trên dataset/label khác. Không trích metric gốc như kết quả của nhóm. Chạy lại baseline và model trên test set riêng, cùng cách chia dữ liệu, rồi báo metric thực tế.

### Thứ tự ưu tiên hiện tại

Theo khả năng tái lập và mức khớp với đề tài, hiện ưu tiên:

1. `Prashant-4527/flight-delay-prediction` với US DOT/BTS 2015. Cùng data, MIT, có pipeline LR/RF/XGBoost. Phải đổi nhãn, bỏ feature leakage và chạy lại.
2. Pipeline baseline Logistic Regression tự viết trên dataset 2015, tham khảo tutorial Data UAB. Dễ chạy để đối chiếu và ít phụ thuộc.
3. Repo PySpark/AWS dùng data 2015. Khớp data nhưng phải kiểm tra code, license và gỡ dịch vụ AWS.
4. `gonzalonao/flight-delay-propagation` với data 2018–2022. MIT, graph model nhiều baseline, nhưng nặng và khác task.
5. `junzis/atdelay` với EUROCONTROL. Method graph gần nhưng data cần xin license, nên khó đảm bảo tái lập.

Shortlist bổ sung: `sudikshas/flight-delay-prediction-pyspark` báo weighted F1 ~0.82, có airport PageRank và temporal holdout, nhưng data/task/computing khác (OTPW + weather 2015–2021, Spark, 13-class departure delay). Dùng tham khảo method; chưa nâng lên repo chính đến khi xác minh data access và khả năng chạy local. Repo `aneessaheba/realtime-flight-delay-predictor-bigdata` báo metric cao hơn nhưng dùng actual DEP_DELAY/TAXI_OUT làm feature, không hợp dự đoán rủi ro trước chuyến bay.

Với graph dataset/code, ưu tiên tự tạo graph từ Flights 2015; tiếp theo dùng OpenFlights để học topology metrics; sau đó xem Aeolus; rồi repo Gonzalo; cuối cùng atdelay do rào cản data. Bảng chi tiết, nguồn và lý do nằm trong `docs/risk-methods-review.md`.

## Những gì đã khảo sát ban đầu

- **Prashant-4527/flight-delay-prediction:** cùng US DOT/BTS 2015, có Logistic Regression, Random Forest, XGBoost, Streamlit và MIT. Bài toán gốc là arrival delay >15 phút, loại cancellation/diversion. Hợp dataset nhưng cần sửa nhãn theo policy và rà soát feature leakage.
- **junzis/atdelay:** có Random Forest cấp chuyến, LSTM cấp sân bay, DST-GAT cấp mạng. README chỉ ra nguồn EUROCONTROL cần xin license, nên cần xác minh quyền truy cập data trước khi chọn.
- **gonzalonao/flight-delay-propagation:** MIT, có baseline bảng, LSTM, GCN, GAT và mô hình không-thời gian, nhưng dùng dữ liệu 2018–2022 và task dự đoán trễ trung bình airport theo giờ.
- **OpenFlights network analysis:** có mẫu code centrality/topology airport, nhưng graph topology OpenFlights không chứa kết quả trễ của dataset 2015.
- Đã có các nghiên cứu học thuật dùng airport graph cho delay propagation/forecasting. Xem `docs/risk-methods-review.md` để lấy nguồn và giới hạn.

## Quyết định tạm thời về graph

Nếu tiếp tục với dataset Flight Delays 2015, hướng gọn là dựng graph sân bay trực tiếp từ flights.csv. Sân bay là node, Origin → Destination là directed edge, weight là số chuyến hoặc thống kê lịch sử. So sánh model tabular với model cộng graph features trên cùng temporal split. Nếu đổi dataset, cần dựng lại graph definition theo schema mới và ghi rõ lý do graph phù hợp với câu hỏi nghiên cứu.

Graph analytics không nhất thiết buộc phải là GNN. Cần hỏi giảng viên liệu graph feature/centrality và thí nghiệm ablation có đáp ứng mức 4, hay cần mô hình graph neural network.

**Làm rõ về Prashant:** repo này không có mạng sân bay/Graph Analytics. Chỉ dùng nó làm baseline tabular cho dự đoán trễ đến. Graph là nhánh nghiên cứu riêng, nhóm có thể dựng airport-route graph trực tiếp từ cùng dataset 2015 rồi so sánh mô hình có và không có graph features, hoặc tìm repo graph riêng nếu được yêu cầu. Không mô tả rằng nhóm kế thừa graph từ Prashant.

## Ghi chú giải thích rubric và DApp

**DApp** là ứng dụng phi tập trung có giao diện người dùng kết nối ví và gọi Smart Contract. Dashboard biểu đồ thuần túy chưa đủ để chứng minh luồng DApp nếu không tương tác với contract.

Phạm vi DApp tối thiểu đề xuất gồm: nhập/chọn chuyến bay, xem báo giá và điều khoản, kết nối ví, mua policy bằng giao dịch, xem trạng thái cùng transaction hash, mô phỏng/gửi kết quả oracle, và nhận payout hoặc thông báo policy không đủ điều kiện. Dashboard analytics có thể nằm trong cùng ứng dụng.

### Phân tích bài toán — 10 điểm

- Mô tả vấn đề hành khách gặp khi chuyến bay trễ/hủy và quy trình xử lý thủ công.
- Xác định actor, ví dụ hành khách, Admin/nhà cung cấp vốn và Oracle.
- Định nghĩa policy cụ thể: chọn trễ đến hay trễ khởi hành, ngưỡng, quy tắc hủy/chuyển hướng, phí, payout, thời hạn mua và xử lý thiếu dữ liệu.
- Vẽ quy trình từ xem phí, mua policy, nhận kết quả chuyến bay đến quyết định bồi thường.
- Giải thích Blockchain phù hợp ở điểm nào: điều khoản thực thi công khai, trạng thái/giao dịch có thể kiểm tra, payout theo rule. So sánh ngắn với backend tập trung và thừa nhận Oracle vẫn là nguồn tin cậy ngoài chuỗi.
- Ghi mục tiêu, phạm vi, giả định và yêu cầu chức năng/phi chức năng.

### Lý thuyết và nghiên cứu — 10 điểm

- Trình bày khái niệm liên quan đủ để giải thích thiết kế: Blockchain, Smart Contract, DApp/Web3, parametric insurance, Oracle và mô hình dự đoán rủi ro.
- So sánh ít nhất các hướng tham khảo phù hợp: repo Prashant là baseline ML trễ đến; Etherisc/AXA Fizzy là tham khảo hệ thống/ý tưởng bảo hiểm bay; nguồn graph airport-delay riêng nếu nhóm triển khai graph.
- Với mỗi nguồn, ghi bài toán, dữ liệu, phương pháp, điểm mạnh, giới hạn và phần nhóm học hỏi.
- Phân biệt rõ phần tái lập (code/method), phần nhóm điều chỉnh (nhãn/policy/data split), và phần nhóm tự xây (contract, oracle flow, graph experiment, integration).
- Không tuyên bố novelty hoặc thành tích của upstream là của nhóm. Trích license, paper/repo và kết quả tái chạy của ANTs.

Đầu ra nên có bảng so sánh related work và sơ đồ Use Case/User Flow trong báo cáo. Rubric có 10 điểm cho mỗi phần; dùng đây làm checklist đầy đủ, không phải cam kết điểm số.

## Các lựa chọn cần chốt

- [ ] Giữ Flight Delays 2015 hay đổi dataset.
- [ ] Nếu đổi, xác nhận được license, nguồn, schema và khả năng tải dữ liệu.
- [ ] Chọn repo/method sau khi đối chiếu task, metric và khả năng chạy lại.
- [ ] Chốt định nghĩa target phù hợp điều khoản bảo hiểm.
- [ ] Chốt prediction time và chỉ dùng đặc trưng đã biết tại thời điểm đó.
- [ ] Chốt graph definition và mức graph method cần triển khai.
- [ ] Chốt track chấm, hạn nộp, lịch bảo vệ và yêu cầu testnet với giảng viên.
- [ ] Chốt phạm vi Smart Contract/DApp theo khả năng triển khai và kiểm thử của nhóm.

## Kế hoạch thực hiện tiếp theo

Kế hoạch cũ tìm 3–5 cặp repo/dataset đã được thay bằng kế hoạch cập nhật sau khi nhận nhận xét giảng viên. Theo thứ tự ưu tiên và cổng quyết định mới tại `PROJECT_PLAN.md`: hoàn thiện đề cương/tài liệu, chốt điều khoản và stack, giữ dataset 2015 trừ khi có xác nhận khác, chạy baseline trước khi mở rộng graph.

## Buổi hỏi giảng viên

Danh sách câu hỏi theo nhận xét mới nằm trong `lecturer-meeting.md`; trạng thái trả lời lưu ở `lecturer-feedback.md`.

## Ghi chú về prototype hiện có

`scripts/business_flow_demo.py` là mô phỏng nghiệp vụ trong bộ nhớ, không phải Blockchain, chưa có mô hình dự đoán, graph hoặc dữ liệu thật. Dùng nó để hiểu policy lifecycle; không trình bày như sản phẩm Blockchain đã xây xong.

## Nhận xét giảng viên mới nhận được

Nhóm đã cung cấp nhận xét bằng văn bản trên đề cương/đăng ký; ngày nhận chưa rõ. Ghi nhận các định hướng sau, không đánh đồng đề xuất với quyết định đã triển khai:

- Smart Contract cần chặn mua muộn (sau giờ khởi hành hoặc trong khoảng X giờ trước chuyến bay) và lưu flight ID, ngày bay, giờ khởi hành dự kiến.
- Định phí cần baseline theo tỷ lệ trễ thực nghiệm; phần cải tiến có thể là LR/XGBoost hiệu chuẩn với feature chỉ có trước chuyến bay, temporal split và Brier score.
- Đánh giá gồm phí thu/chi trả, khả năng thanh toán pool khi replay, gas và latency.
- Oracle Python đơn là điểm tin cậy tập trung; phân tích sai/trễ dữ liệu và lộ khóa, cân nhắc multi-oracle ký, cửa sổ khiếu nại và giới hạn payout mỗi chuyến.
- Dataset 2015 bị lưu ý là cũ; giảng viên gợi ý **có thể dùng thêm** BTS mới để kiểm tra mức phí. Tạm giữ Kaggle 2015 làm dữ liệu chính theo đăng ký; chưa có chỉ dẫn bắt buộc thay thế. Cần hỏi lại ý giảng viên.
- Giảng viên khuyên Vyper + Ape + Anvil; cần smoke-test và hỏi liệu đây là bắt buộc hay khuyến nghị trước khi chuyển stack.
- Cần hoàn thiện đề cương, sơ đồ kiến trúc, bibliography và tối thiểu 3 bài bình duyệt. DOI/nội dung Kim et al. phải được xác minh hoặc thay.
- Nhận xét mới chưa nói rõ Graph Analytics. Vì nhóm đăng ký Mức 4, không tự bỏ graph; hỏi giảng viên phạm vi tối thiểu, tránh tự mở rộng thành GNN trước khi có câu trả lời.

Khảo sát mới tìm được repo/paper sát hướng graph-delay propagation hơn PageRank topology thuần: `yajun668/FlightDelayPrediction` (bài Decision Support Systems 2025, Airport-Network-Spilled Propagation score). Code MIT và dataset BTS/FAA/IEM riêng trên Mendeley CC BY 4.0; thí nghiệm upstream dùng 2023, dự đoán departure delay và khác dataset/label bảo hiểm của nhóm. Đây là method tham khảo/ứng viên tái lập, chưa phải quyết định đổi dataset hoặc clone repo. Chi tiết và các lựa chọn khác ở `docs/graph-repo-research.md`.

Kế hoạch hành động đã cập nhật trong `PROJECT_PLAN.md`; toàn bộ nhận xét và trạng thái câu hỏi nằm trong `docs/lecturer-feedback.md`.
