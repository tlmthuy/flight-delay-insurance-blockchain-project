# Phân công — Đồ án IS355 nhóm ANTs

**Căn cứ:** Project Lab mục 11 (5 sản phẩm phải nộp), mục 12 (cấu trúc báo cáo), mục 13 (demo), mục 15 (rubric), cùng hướng hiện tại: bảo hiểm tham số chuyến bay, dữ liệu Kaggle 2015, ML báo giá, graph airport feature, smart contract và oracle mock.

Phân công đầu mối quản lý và checklist giao nội dung nằm trong [checklist giao phẩm](deliverable-checklist.md). Đầu mối quản lý giao phẩm khác với người phụ trách module: đầu mối lên sườn, kiểm tra và đóng gói; các thành viên vẫn điền phần chuyên môn theo vai trò.

## 1. Các sản phẩm phải nộp

Project Lab yêu cầu mỗi **nhóm** nộp 5 thành phần:

| # | Sản phẩm | Nội dung phải có | Chủ sở hữu chính |
|---|---|---|
| 1 | **Source Code** | Smart Contract, Frontend, Backend, AI/ML, scripts phù hợp phạm vi | Nguyên quản lý repo/ghép bản; mỗi người nộp module mình phụ trách |
| 2 | **Báo cáo PDF** | 7 chương theo Project Lab; kiến trúc, dữ liệu/mô hình, contract, test, bảo mật và đánh giá | Thùy quản lý sườn/ghép bản; cả ba điền phần chuyên môn |
| 3 | **Slide** | Problem → Solution → architecture → contract → data/AI/graph → evaluation → limitations | Thùy quản lý deck; cả ba gửi nội dung/hình và trình bày phần mình |
| 4 | **Video demo 5–10 phút** | Problem → Solution → Smart Contract → DApp → AI → Demo | Quốc Anh quản lý storyboard/quay/ghép; cả ba quay phần module mình |
| 5 | **README** | Cài đặt, cấu hình, deploy, chạy DApp, chạy AI/data, kịch bản demo | Nguyên quản lý README; cả ba gửi hướng dẫn module của mình |

Ngoài 5 sản phẩm, nhóm phải có bản demo trực tiếp, test contract, đánh giá hiệu năng phù hợp và phân tích ít nhất 3 rủi ro bảo mật. Các phần này cần được phản ánh trong source, report, slide, video và README.

## 2. Phân công theo thành viên và đầu ra

Tên thành viên theo hồ sơ đề tài:

- **A — Phạm Quốc Anh (20521077), trưởng nhóm**
- **B — Trương Mạnh Nguyên (23521065)**
- **C — Trần Lê Minh Thùy (23521560)**

| Thành viên | Vai trò chính | Công việc | Đầu ra phải bàn giao | Kiểm tra chéo |
|---|---|---|---|---|
| **A — Phạm Quốc Anh** | Web3 integration, wallet và giao dịch DApp | Tích hợp giao diện với ví/Web3 và contract ABI/address; xử lý connect network/account, mua policy, hiển thị transaction hash/status/event; kết nối quote output từ B với contract do C xây; xử lý lỗi transaction và chuẩn bị phần Web3 demo. Viết phần Web3 integration, DApp interaction và transaction flow trong báo cáo. | Module Web3/frontend integration; transaction/status UI; test tích hợp hoặc checklist; 1 phần báo cáo/slide; README mục cấu hình ví/network và chạy DApp. | C xác nhận ABI, function, event và revert behavior; B xác nhận quote/output hiển thị đúng. |
| **B — Trương Mạnh Nguyên** | Data, ML, Graph và đánh giá định phí | Tạo inventory và pipeline Kaggle 2015; ánh xạ airport ID; tạo label đúng policy; audit leakage; baseline xác suất; Logistic Regression; graph sân bay directed với PageRank/weighted degree; temporal split; ablation không graph/có graph; Brier/PR-AUC/calibration/recall; premium-payout-loss ratio replay; viết phần dữ liệu, ML/Graph, thực nghiệm và giới hạn. | Scripts/notebook tái lập; data inventory/data quality report; bảng model comparison; graph definition/plot; financial replay CSV/plot; 1 phần báo cáo/slide; README mục lấy data và chạy pipeline. | A rà nhãn/policy và công thức payout; C chạy lại hướng dẫn và kiểm tra dashboard nhận output đúng. |
| **C — Trần Lê Minh Thùy** | Smart Contract, policy/oracle và kiểm thử Blockchain | Chốt policy fields cùng nhóm; hoàn thiện lifecycle mua policy → kết quả oracle → eligibility → payout; hạn mua; chống trả trùng; access control; reserve/pool; event; triển khai local/testnet theo stack đã chọn; đo gas/transaction time; chuẩn bị test case và kịch bản contract demo. Viết phần smart contract, blockchain, threat/risk và test trong báo cáo. | Contract source + deploy/test scripts; bảng test input/expected/actual; bảng gas/transaction time đã đo; 1 phần báo cáo/slide; README mục deploy và test. | B review quyền hạn/luồng nghiệp vụ; A kiểm tra contract gọi được qua Web3, function/event và transaction status hiển thị. |

### Nguyên tắc để công việc không dồn vào một người

- A, B, C đều phải viết tối thiểu một phần nội dung báo cáo và tự thuyết trình phần đó; người tổng hợp tài liệu không phải người duy nhất viết báo cáo.
- Mỗi module phải có hướng dẫn chạy và test/evidence ngắn. Người phụ trách không chỉ giao file mà còn bàn giao cách chạy.
- Mỗi đầu ra có một người chịu trách nhiệm cuối cùng và một người review chéo; người review ghi lỗi/đã kiểm tra trong checklist hoặc issue.
- Mỗi người giữ lịch sử đóng góp qua commit riêng/PR, notebook hoặc tài liệu có tên tác giả; không dùng commit để “đếm điểm”, chỉ để minh bạch tiến độ và hỗ trợ giải trình đóng góp.
- Chốt phạm vi trước khi triển khai. Sau khi khóa tính năng, ưu tiên sửa lỗi và kiểm tra giao phẩm.

## 3. Trình tự triển khai và kiểm tra

| A — Web3 integration | B — Data/ML/Graph | C — Smart Contract/Blockchain | Mốc nhóm phải kiểm tra |
|---|---|---|---|
| Chốt UI/API flow và ví/network cùng nhóm | Xác nhận data source/schema/label và temporal split | Chốt fields, states, quyền oracle, hạn mua; ghi decision log | **Scope freeze:** threshold, cancellation/diversion, payout, stack, demo path |
| UI shell và contract interface stub | Load data, schema, duplicate/missingness, airport mapping | Skeleton contract + test harness | Ba module có thể chạy độc lập; chia sẻ ABI/schema/interface |
| Connect wallet/network, đọc trạng thái cơ bản | Label + feature allow/deny lists; data quality table | Policy creation/purchase, hạn mua, access control | Khóa ABI contract ↔ Web3; không đổi field tùy tiện |
| Quote page với mock JSON; transaction states | Temporal split + baseline prevalence/by carrier/route | Funding/reserve và event | Demo dữ liệu → quote mock và tạo policy trên local |
| Tích hợp mua policy từ UI và đọc receipt | Logistic Regression, Brier/PR-AUC/calibration | Oracle result, eligibility, payout/claim | **Vertical slice đầu:** quote → buy → mock outcome → payout tối thiểu |
| Policy status, transaction history, xử lý lỗi cơ bản | Graph route/PageRank/degree từ train only | Test case hợp lệ/không hợp lệ; sửa critical bugs | Mọi module có output; không module nào chặn tích hợp |
| Dashboard hiển thị model/graph metrics | Ablation M1 vs M1+graph trên cùng split | Chống duplicate payout, unauthorized oracle, thiếu quỹ | Kết luận sơ bộ graph có/không giúp; không tuning trên test |
| Hiển thị quote/outcome/financial charts | Insurance replay: premium, payout, loss ratio, solvency | Đo gas và thời gian transaction | **Feature freeze**; chỉ sửa lỗi/hoàn thiện đo lường |
| Kiểm tra end-to-end và lỗi transaction | Ghi limitations/metric definitions/repro steps | Review quyền quản lý, pause/oracle risk | Demo chạy liên tục được; mọi con số trace về output |
| Chốt sơ đồ và draft report/README Web3 | Đóng băng kết quả và artifacts | Hoàn thành bảng security risk tối thiểu 3 mục | **Code/data freeze**; bắt đầu soát nhất quán tài liệu |
| Viết Web3/DApp integration và transaction flow | Viết chương data/ML/graph/experiments | Viết chương contract, testing, security | Mỗi người nộp phần mình đã review |
| Review UI và transaction flow trong demo | Review metric, hình/table, claims | Review contract demo/test evidence | Soát 7 chương, citation, figure/table numbering |
| Diễn tập ví và transaction | Diễn tập AI/graph/data result | Diễn tập contract/oracle/payout | Một lần chạy sạch theo README; lưu transaction/evidence |
| Bàn giao Web3/DApp README section | Chốt output data/metrics và reproducibility | Bàn giao contract/tests; cả nhóm final audit | **Final audit:** đủ 5 sản phẩm + demo/test/security/metrics |

## 4. Phân công phần báo cáo, slide và video

Nội dung được chia theo module; người ráp tài liệu không thay thế trách nhiệm viết và kiểm tra nội dung của từng người:

| Phần | Người viết chính | Người phản biện | Nội dung tối thiểu |
|---|---|---|---|
| Chương 1: Giới thiệu | A | C | Bài toán, đối tượng, mục tiêu, phạm vi, lý do blockchain |
| Chương 2: Cơ sở lý thuyết/related work | C | B | Parametric insurance, oracle, smart contract, nguồn đã kiểm chứng |
| Chương 3: Phân tích bài toán | C | A | Policy, roles, business process, use cases, requirements |
| Chương 4: Thiết kế hệ thống | A điều phối; A/B/C viết phần module | C | Architecture, Web3, data/AI, graph, contract/oracle flow |
| Chương 5: Xây dựng | A: Web3/DApp integration; B: data/ML/graph; C: contract/oracle | Review chéo | Code thật, cấu hình, giao diện, tích hợp |
| Chương 6: Thực nghiệm & đánh giá | A: Web3/system; B: ML/finance; C: contract/security | A tổng hợp | Test, gas/latency, model metrics, pool replay, hạn chế |
| Chương 7: Kết luận | A ráp từ kết luận của B/C | Cả nhóm | Đạt/chưa đạt, hạn chế và hướng phát triển |
| Slide/video | Mỗi người làm slide + nói phần module của mình; A ráp/biên tập | Cả nhóm diễn tập | Demo trực tiếp và số liệu khớp báo cáo |

## 5. Tỷ trọng công sức nội bộ (để cân việc, không phải điểm môn)

Gợi ý để cả ba dành công sức tương đối ngang nhau:

| Thành viên | Ước lượng effort | Lý do cân bằng |
|---|---:|---|
| A | ~1/3 tổng effort | Web3 integration và DApp transaction flow; cùng ráp báo cáo/slide/video, phối hợp demo. |
| B | ~1/3 tổng effort | Data/ML/graph và đánh giá là một pipeline có nhiều bước, cần tái lập và giải thích. |
| C | ~1/3 tổng effort | Smart Contract/oracle/security/test và nội dung nghiệp vụ; A/B review chéo và cùng làm tài liệu. |

Không dùng phần trăm nội bộ này để suy ra điểm. Đây chỉ là cách theo dõi khối lượng nhóm; nếu một module gặp blocker, nhóm phân công hỗ trợ lại theo công việc còn tồn.

## 6. Trang Project Lab nói gì về điểm cá nhân?

Trang hiện ghi rõ **mỗi nhóm nộp** năm sản phẩm và chia rubric theo các hạng mục đồ án/track. Track A (có AI/ML) liệt kê 8 hạng mục: phân tích bài toán 10, lý thuyết/nghiên cứu 10, contract/blockchain 20, data & AI/ML 15, DApp 15, kiểm thử/bảo mật 10, báo cáo 10, demo/thuyết trình 10 — tổng 100. Trang cũng ghi nhóm được chấm theo track đã đăng ký, không cộng dồn hai track.

Trong nội dung trang đã kiểm tra, **không thấy quy định** rằng điểm được chia đều cho từng thành viên, cũng không thấy công thức ai làm nhiều thì tự động được nhiều điểm hơn, log commit được quy đổi thành điểm, hay phần bảo vệ được chấm cá nhân. Vì vậy không nên khẳng định điểm cá nhân sẽ bằng nhau hoặc khác nhau chỉ dựa trên website. Rubric được công bố là rubric cho đồ án/nhóm; cách quy đổi sang điểm cá nhân cần giảng viên xác nhận.

Điều trang có nêu ở cấp sản phẩm là 5 giao phẩm nhóm phải nộp; ở phần bảo vệ yêu cầu demo trực tiếp và có các câu hỏi có thể hỏi về Blockchain, contract, AI, hệ thống, research. Đây **không đồng nghĩa** đã có quy định chấm cá nhân theo mức đóng góp.

### Câu nên hỏi giảng viên ngay

> “Thưa thầy, rubric Project Lab hiện chấm theo các hạng mục của đồ án và ghi mỗi nhóm nộp 5 sản phẩm. Điểm cuối cùng được áp dụng chung cho cả nhóm hay có phần điểm cá nhân qua vấn đáp/đánh giá đóng góp? Nếu có, nhóm nên lưu bằng chứng phân công/commit/demo theo cách nào để thầy xem xét công bằng?”

## 7. Checklist giao phẩm cuối cùng

- [ ] Source code có contract, frontend, backend/quote, data/ML/graph scripts cần thiết.
- [ ] PDF có đủ 7 chương, sơ đồ kiến trúc, data inventory, policy, test, security và evaluation.
- [ ] Slide thống nhất với báo cáo và có phân công người trình bày.
- [ ] Video 5–10 phút thể hiện Problem → Solution → Contract → DApp → AI → Demo.
- [ ] README giúp một thành viên khác cài/chạy data, model, chain, DApp và demo.
- [ ] Demo trực tiếp chạy; test cases lưu input/expected/actual; security có tối thiểu 3 rủi ro.
- [ ] Mọi metric, gas và latency là số đo thực; mỗi người hiểu được module mình bảo vệ.
- [ ] Ghi lại người phụ trách, reviewer, commit/artifact và trạng thái từng đầu ra; không coi lịch sử Git là công thức điểm.

## Nguồn

- [IS355 Project Lab — mục 11 Sản phẩm phải nộp](https://itlearninghub.io.vn/courses/is355/project-lab.html#san-pham-nop)
- [IS355 Project Lab — mục 12 Cấu trúc báo cáo](https://itlearninghub.io.vn/courses/is355/project-lab.html#cau-truc-bao-cao)
- [IS355 Project Lab — mục 13 Demo](https://itlearninghub.io.vn/courses/is355/project-lab.html#demo)
- [IS355 Project Lab — mục 15 Tiêu chí đánh giá](https://itlearninghub.io.vn/courses/is355/project-lab.html#tieu-chi)
