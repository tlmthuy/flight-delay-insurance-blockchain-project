# Kế hoạch triển khai đồ án IS355 của nhóm ANTs

Xem [kế hoạch Data, ML và Graph](docs/data-ml-graph-plan.md) và [checklist giao phẩm](docs/deliverable-checklist.md).

## Mục tiêu

Hoàn thiện nguyên mẫu có thể demo và đánh giá được cho đề tài **Blockchain-Based Parametric Flight Delay Insurance Supported by Historical Aviation Data Analysis**. Hướng thực hiện cập nhật theo nhận xét giảng viên: bảo hiểm tham số có điều khoản rõ, định phí từ dữ liệu với baseline và mô hình cải tiến, Smart Contract xử lý policy/quỹ/chi trả, phân tích rủi ro Oracle và đánh giá cả kỹ thuật lẫn tài chính.

Đề tài vẫn đăng ký **Mức 4 — Research**. Kế hoạch này không tự hạ mức. Graph Analytics chưa được nêu trong nhận xét giảng viên vừa nhận; cần xác nhận riêng yêu cầu tối thiểu cho Mức 4 trước khi dành nhiều thời gian cho graph/GNN.

## Hướng kỹ thuật đã ghi nhận

### Được giảng viên góp ý

- Bài toán và vai trò Blockchain phù hợp: Smart Contract tự động chi trả theo điều kiện trễ đạt ngưỡng hoặc chuyến bị hủy.
- Nối phân tích dữ liệu với định phí theo rủi ro thực nghiệm của hãng/tuyến; cần baseline và một cải tiến có căn cứ.
- Đánh giá gồm gas, độ trễ, phí thu/tiền chi và khả năng thanh toán của pool khi phát lại dữ liệu.
- Chặn mua sau giờ khởi hành dự kiến (hoặc trong khoảng X giờ trước chuyến bay); policy lưu flight ID, ngày bay và giờ khởi hành dự kiến.
- Không dùng `DEPARTURE_DELAY` hoặc nguyên nhân trễ làm feature báo giá vì chúng chỉ biết sau khi chuyến bay diễn ra.
- Phân tích điểm tin cậy tập trung của một Python oracle; cân nhắc nhiều oracle ký, thời gian khiếu nại và giới hạn chi trả mỗi chuyến.
- Dữ liệu 2015 có hạn chế về độ mới; có thể bổ sung dữ liệu BTS mới để kiểm tra tính ổn định của mức phí.
- Đề cương cần hoàn chỉnh, có hình kiến trúc và trích dẫn đã kiểm chứng.

### Quyết định/đề xuất tạm thời

- **Dataset chính:** giữ Kaggle US DOT Flight Delays 2015 theo hồ sơ đăng ký. Góp ý “có thể dùng thêm dữ liệu mới hơn từ BTS” được hiểu là kiểm tra bổ sung, chưa phải yêu cầu thay dataset chính. Nếu lấy BTS mới, dùng một giai đoạn làm temporal validation/robustness check; ghi rõ khác biệt schema và không gộp tùy tiện với 2015.
- **Nhãn:** định nghĩa theo policy đã chốt, ví dụ `cancelled OR arrival_delay >= threshold`. Dataset không có nhãn “được bảo hiểm”; nhóm tạo nhãn từ kết quả thực tế và điều khoản của mình.
- **Mô hình:** baseline tỷ lệ biến cố theo hãng (và tuyến nếu đủ mẫu), sau đó Logistic Regression hoặc XGBoost có hiệu chuẩn xác suất. Chia theo thời gian; ưu tiên Brier score/calibration cùng metric phân loại phù hợp.
- **Policy:** lưu flight ID, ngày bay, giờ khởi hành dự kiến, hạn mua, premium, payout và trạng thái. Khóa quyền lợi lúc mua; chống mua quá hạn và claim hai lần.
- **Oracle:** demo local/mock được dùng nếu công bố rõ là mô phỏng; đánh giá tin cậy, dữ liệu sai/trễ, lộ khóa. Multi-oracle hoặc thời gian khiếu nại là phương án giảm thiểu, chỉ triển khai nếu còn thời gian.
- **Stack:** thầy khuyến nghị Vyper + Ape + Anvil, trong khi kế hoạch cũ ghi Hardhat/Ganache. Kiểm tra khả năng triển khai và chọn một stack duy nhất; ưu tiên stack môn học nếu khả thi. Không dùng Ganache trong kế hoạch mới.
- **Graph:** chưa tự coi là bỏ yêu cầu Mức 4. Hỏi giảng viên graph analytics tối thiểu cần có. Nếu cần, dùng graph sân bay/tuyến bay từ data 2015 với centrality hoặc graph features; chưa làm GNN trước baseline và contract.

Khảo sát repo graph mới nhất và xếp hạng khả năng dùng được lưu tại [`docs/graph-repo-research.md`](docs/graph-repo-research.md). Repo ANSP 2025 là method match để thử; dataset/target khác nên không được coi là đã tái lập trên Kaggle 2015.

## Điều khoản bảo hiểm cần khóa trước khi triển khai

Ghi quyết định vào `docs/decision-log.md` trước khi triển khai:

1. Trigger là trễ đến hay trễ khởi hành; ngưỡng dùng `>=` hay `>`; hủy chuyến có trigger riêng không?
2. Payout cố định hay theo bậc; đơn vị tiền và cách làm tròn?
3. Hạn mua cụ thể: trước giờ khởi hành bao lâu; giờ địa phương hay UTC?
4. Flight ID gồm trường nào để phân biệt chuyến cùng số hiệu ở các ngày?
5. Trách nhiệm tối đa mỗi chuyến và vốn phải dự trữ ra sao?
6. Kết quả nào là cuối cùng; có thời gian khiếu nại/đính chính không?

Phạm vi gọn đề xuất: một policy cho một chuyến, trigger trễ đến hoặc hủy, payout cố định, mock oracle có quyền giới hạn, local chain. Con số cụ thể cần được nhóm thống nhất, không coi ví dụ là quy định đã duyệt.

## Kiến trúc sản phẩm cần hoàn thành

`User → DApp → Web3/Wallet → Smart Contract`  
`Historical data → cleaning/EDA → baseline + model → quote/risk output`  
`Flight outcome source/mock oracle → Smart Contract → eligibility/payout`

- **DApp:** chọn chuyến bay; xem điều khoản/báo giá; kết nối ví; mua policy; xem policy ID, trạng thái và transaction hash; xem kết quả và payout/lý do không đủ điều kiện.
- **Data inventory:** nguồn, phiên bản/thời kỳ, license, schema, missingness, quy tắc làm sạch, mapping mã sân bay, label, temporal split. Kiểm tra mã sân bay dạng số ở tháng 10/2015.
- **Data/ML:** baseline, mô hình cải tiến, metric thực chạy và kiểm tra leakage. Model/quote chạy off-chain; contract không tự chạy ML.
- **Graph (nếu được yêu cầu):** định nghĩa node/edge/weight, cửa sổ thời gian, metric và tránh feature tương lai; làm phân tích nhỏ, không để chặn luồng bảo hiểm.
- **Smart Contract:** policy lifecycle, mua, funding, oracle result, eligibility/payout, access control, events, chống trả trùng và kiểm soát solvency.
- **Oracle:** adapter/mock có quyền; lưu nguồn và thời gian cập nhật. Nêu rõ mock không phải oracle production.
- **Evaluation:** model metrics, phí thu/payout, loss ratio, pool solvency khi replay, gas, latency và transaction success rate.

## Giai đoạn triển khai và tiêu chí hoàn thành

### Giai đoạn 1 — Đề cương, policy, dữ liệu và stack

**Đầu ra:** đề cương sạch, quyết định nghiệp vụ, data inventory bản đầu, kiến trúc và stack được chọn.

- Sửa `[Project title]`, xóa hướng dẫn mẫu ở 2.1, 3.3, 4.1; thêm sơ đồ kiến trúc.
- Rà soát danh mục và số thứ tự trích dẫn. Xác minh DOI/nội dung Kim et al.; nếu không kiểm chứng được thì thay nguồn.
- Tìm ít nhất 3 bài bình duyệt về blockchain parametric insurance, oracle và flight-delay prediction. Etherisc/AXA là ví dụ ứng dụng, không thay paper bình duyệt.
- Chốt trigger, ngưỡng, payout, hạn mua, tiền tệ, flight ID và trách nhiệm tối đa.
- Kiểm kê Kaggle 2015: schema, nguồn/license, missing values, mapping sân bay, nhãn và temporal split.
- Chạy smoke test Vyper/Ape/Anvil; nếu không khả thi trong thời gian, ghi lý do và thống nhất stack thay thế.
- Hỏi giảng viên: có cần thay dataset chính không; BTS mới chỉ là kiểm tra bổ sung có đúng không; graph tối thiểu cho Mức 4; stack Vyper/Ape/Anvil bắt buộc hay khuyến nghị.

**Điều kiện hoàn thành giai đoạn 1:** thống nhất điều khoản, đề cương hết placeholder, stack/phạm vi được ghi trong decision log.

### Giai đoạn 2 — Baseline, model và Smart Contract

**Đầu ra:** pipeline baseline/model tái lập; contract local và test nghiệp vụ chính.

- Tạo baseline xác suất trễ/hủy theo hãng; thử theo tuyến nếu mẫu đủ, có smoothing/fallback cho nhóm ít chuyến.
- Huấn luyện Logistic Regression trước; chỉ thử XGBoost khi pipeline ổn. Chỉ dùng feature biết trước giờ mua (hãng, sân bay, lịch bay, tháng/giờ/ngày); loại delay thực tế và nguyên nhân trễ.
- Chia theo thời gian (ví dụ tháng 1–9 train, 10–12 test nếu phù hợp); lưu pipeline, seed, dependency và kết quả.
- Báo Brier score/calibration và metric phân loại phù hợp; không chọn theo accuracy đơn lẻ.
- Viết contract policy, funding, oracle role, result và payout; khóa premium/payout/threshold khi mua; chặn mua quá hạn.
- Test mua hợp lệ/không hợp lệ, hạn mua, trễ dưới/đúng/vượt ngưỡng, hủy, unauthorized oracle, claim trùng và thiếu quỹ.

**Điều kiện hoàn thành giai đoạn 2:** có kết quả model thực chạy; test contract cốt lõi pass; phân biệt rõ dữ liệu báo giá và dữ liệu quyết định bồi thường.

### Giai đoạn 3 — Oracle, DApp, tích hợp và pool

**Đầu ra:** demo end-to-end trên local chain và dashboard có kết quả.

- Làm mock oracle/Python adapter gửi kết quả vào contract; lưu timestamp và transaction hash.
- Thử oracle gửi sai, trễ, trùng hoặc sai quyền; ghi biện pháp và giới hạn. Nếu không triển khai multi-oracle thật, chỉ trình bày như phương án thiết kế.
- Xây DApp tối thiểu: quote/terms, kết nối ví, mua policy, xem trạng thái, kết quả, claim hoặc lý do từ chối.
- Replay dữ liệu qua pool: tổng premium, payout, loss ratio, số dư và tổn thất tập trung theo ngày/hãng/sân bay.
- Đo gas, transaction time và response latency thực tế; ghi cấu hình và tách thời gian oracle khỏi xác nhận chain.
- Nếu graph được yêu cầu: dựng directed airport-route graph từ 2015, tính degree/PageRank/betweenness hoặc graph features. Chỉ so sánh model có/không graph nếu còn thời gian.
- Nếu BTS mới được duyệt và lấy thuận tiện: kiểm tra phụ một giai đoạn, so sánh tỷ lệ biến cố/mức phí; ghi khác biệt dữ liệu, không gộp tùy tiện.

**Điều kiện hoàn thành giai đoạn 3:** chạy được quote → mua → oracle → quyết định → payout; pool replay và số đo có thể tái lập.

### Giai đoạn 4 — Bảo mật, báo cáo, demo và bàn giao

**Đầu ra:** source, báo cáo, slide, video và README khớp sản phẩm thật.

- Hoàn thiện test matrix có input/expected/actual cho contract, oracle và DApp.
- Phân tích ít nhất 3 rủi ro: oracle manipulation/availability/key compromise, access control, reentrancy/double payout/solvency hoặc input validation. Mỗi rủi ro có kịch bản và giảm thiểu.
- Chạy đánh giá cuối: Brier/calibration và metric model; premium vs payout/loss ratio/solvency; gas, latency, transaction success. Chỉ ghi số đo thật.
- Hoàn thiện 7 chương báo cáo, related-work table, sơ đồ kiến trúc/sequence, data inventory, policy table, test table và limitations.
- Làm slide và video demo 5–10 phút; demo quote → buy → kiểm tra transaction → oracle result → eligibility → payout/pool.
- README hướng dẫn cài, lấy dữ liệu, chạy preprocessing/model, local chain, deploy, DApp và demo.
- Tổng duyệt từ môi trường sạch; không commit credentials hoặc dataset lớn trái điều kiện sử dụng.

**Cổng cuối:** thành viên khác có thể làm theo README để chạy lại demo; báo cáo chỉ khẳng định điều code và kết quả chứng minh.

## Câu hỏi còn mở cho giảng viên

1. Với Mức 4, Graph Analytics tối thiểu là centrality/graph features hay cần GNN? Nhận xét vừa nhận chưa nói rõ graph.
2. Giữ Kaggle 2015 làm data chính và dùng BTS mới làm kiểm tra phụ có đúng ý thầy không?
3. Vyper + Ape + Anvil bắt buộc hay khuyến nghị? Nếu nhóm đã bắt đầu Solidity, có được giữ không?
4. Mock oracle local có đủ cho demo hay cần multi-oracle/testnet thật?
5. Hạn mua nên theo mốc nào; có yêu cầu X giờ trước chuyến bay không?
6. Track chấm và tổng Track B hiển thị 105 được xác nhận thế nào?

## Checklist sản phẩm hệ thống

- [ ] DApp tương tác được với ví và contract.
- [ ] Data inventory và pipeline tái lập, xử lý/mapping được ghi rõ.
- [ ] Baseline và model cải tiến có temporal evaluation, không leakage.
- [ ] Contract có policy state, hạn mua, oracle permissions, funding và payout đúng một lần.
- [ ] Oracle/mock tích hợp, nêu trust assumptions và failure scenarios.
- [ ] Graph Analytics theo phạm vi giảng viên xác nhận.
- [ ] Pool replay có phí thu/chi, loss ratio và solvency.
- [ ] Test cases và tối thiểu 3 phân tích rủi ro bảo mật.
- [ ] Số đo gas/latency thực chạy và cấu hình đo.
- [ ] README, PDF, slide, video demo và source code.

## Nguyên tắc thực hiện

- Ưu tiên các luồng end-to-end có thể chứng minh.
- Không chọn repo chỉ vì metric cao; kiểm tra task, label, split, leakage, license và khả năng chạy.
- Repo Prashant chỉ là baseline/tham khảo tabular cho arrival delay; không có graph sân bay hoặc insurance/contract.
- Không dùng kết quả upstream làm kết quả ANTs, không tự tạo số đo.
- Graph/GNN và BTS mới là phần có cổng quyết định; không để chúng chặn contract, dữ liệu chính và demo cốt lõi.
- Ghi phản hồi và quyết định trong `docs/lecturer-feedback.md` và `docs/decision-log.md`.
