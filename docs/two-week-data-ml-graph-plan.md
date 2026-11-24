# Khung Data, ML và Graph trong 2 tuần

**Dự án:** ANTs — Blockchain-Based Parametric Flight Delay Insurance  
**Mục tiêu:** tạo một nhánh Data/ML/Graph nhỏ, kiểm chứng được, tích hợp được vào DApp và đủ bằng chứng cho báo cáo/demo trong 14 ngày.  
**Trạng thái:** kế hoạch thực thi; các điều khoản policy và metric bên dưới cần được nhóm chốt ngày 1.

Phân công chi tiết theo 3 thành viên và 5 giao phẩm được ghi riêng tại [`docs/two-week-team-allocation.md`](two-week-team-allocation.md).

## 1. Phạm vi chốt để kịp bàn giao

### Câu hỏi thực nghiệm

> Với thông tin có trước giờ khởi hành, mô hình có ước lượng được xác suất chuyến bay chạm điều kiện bảo hiểm không; graph feature sân bay có cải thiện xác suất đó so với baseline tabular không?

### Bài toán ML

- **Đơn vị dự đoán:** một chuyến bay (`flight_id + flight_date`), tại thời điểm mua/báo giá.
- **Label:** `eligible = 1` nếu chuyến bị hủy hoặc thời gian đến trễ đạt ngưỡng policy `T`; `eligible = 0` nếu chuyến hoàn tất và trễ dưới `T`.
- **`T`:** nhóm phải chốt cùng điều khoản contract trong ngày đầu. Nếu chưa có chỉ dẫn, hỏi giảng viên/người hướng dẫn ngay; ví dụ 120 phút chỉ là đề xuất minh họa, không phải ngưỡng đã được duyệt.
- **Chuyến diverted:** chốt rõ trong ngày đầu. Phương án gọn: loại khỏi thí nghiệm chính, báo riêng số lượng và làm một phân tích nhạy cảm nếu còn thời gian.
- Dataset không có “ground truth được bảo hiểm”. Nhóm tạo nhãn nghiên cứu bằng cách áp điều khoản policy lên kết quả chuyến bay thật; ghi rõ đây là nhãn dẫn xuất.
- **Phân biệt hai chức năng:** ML ước lượng rủi ro để tạo quote trước chuyến bay; oracle cung cấp kết quả thực tế sau chuyến bay để contract quyết định eligibility/payout. Không dùng dự đoán ML làm bằng chứng chuyến đã trễ.

### Đầu ra tối thiểu cần hoàn thành

1. Data inventory + script làm sạch/label/mapping, có log số dòng.
2. Baseline tỷ lệ biến cố và một model xác suất Logistic Regression; thêm XGBoost chỉ khi baseline, contract và tích hợp đã ổn.
3. Graph sân bay có hướng và hai feature dễ giải thích (PageRank, weighted degree hoặc degree); ablation model không graph / có graph.
4. Temporal evaluation, Brier score, PR-AUC, recall/precision và calibration plot; không hứa graph sẽ tăng điểm.
5. File kết quả gọn (JSON/CSV) để dashboard hiển thị xác suất, quote và biểu đồ.
6. Mô tả luồng off-chain → quote → contract và oracle → kết quả thật → payout; test/demo dùng mock oracle trên local chain.

**Không đưa vào phạm vi 2 tuần:** GNN/GCN/GAT, Spark, weather join, đổi dataset chính, dự báo thời gian thực, oracle production hoặc model chạy trực tiếp trên chain.

## 2. Quy trình xử lý dữ liệu

### Nguồn và kiểm kê

- Nguồn chính: Kaggle US DOT/BTS Flight Delays 2015 đã nêu trong đề cương.
- Dùng `flights.csv` làm bảng chính; `airlines.csv` và `airports.csv` để giải mã hãng/sân bay nếu cần.
- Không commit file dữ liệu lớn hoặc thông tin đăng nhập Kaggle. README phải nêu link, cách tải, phiên bản, checksum nếu nhóm tạo được.
- Tạo `data/README.md` ghi file cần có, schema, nguồn/license được kiểm tra, kích thước và quy trình chạy.

### Pipeline bắt buộc

1. **Load & schema check:** cột bắt buộc có mặt, kiểu dữ liệu, khoảng ngày, số dòng và duplicate.
2. **Chuẩn hóa định danh:** tạo `flight_id` ổn định từ ngày + carrier + flight number + origin + destination + scheduled departure; ánh xạ mã airport, kiểm tra riêng tháng 10/2015 vì định dạng ID được ghi nhận có thể khác.
3. **Tạo label:** label theo policy đã chốt; cancelled là nhánh riêng vì arrival time có thể thiếu; diverted xử lý theo quyết định; không chuyển missing arrival delay thành 0.
4. **Feature báo giá:** chỉ các trường biết trước chuyến bay: carrier, origin, destination, scheduled departure/arrival time, day of week, month, route và graph structural features. Chỉ giữ distance nếu đã có tại thời điểm quote và được xác minh.
5. **Loại khỏi X:** `DEPARTURE_DELAY`, `ARRIVAL_DELAY`, `CANCELLED`, `CANCELLATION_REASON`, `AIR_SYSTEM_DELAY`, `SECURITY_DELAY`, `AIRLINE_DELAY`, `LATE_AIRCRAFT_DELAY`, `WEATHER_DELAY`, actual times và mọi trường phát sinh sau chuyến bay. Một số trường trong danh sách dùng để tạo label/kiểm tra, không bao giờ làm input dự đoán.
6. **Data quality report:** missingness từng cột, số dòng hủy/diverted, duplicate, mã không map được, label prevalence, dòng loại và lý do.
7. **Split theo thời gian:** đề xuất train Jan–Aug, validation Sep, test Oct–Dec/hoặc giữ test cuối năm tùy số mẫu. Chốt đúng một split trước khi xem kết quả test; mọi preprocessing chỉ fit trên train.

### Bảng data inventory đưa vào báo cáo

| Nhóm trường | Ví dụ | Dùng làm gì | Có trước giờ bay? |
|---|---|---|---|
| ID | flight date, carrier, flight number, origin, destination | Khóa chuyến và nối bảng | Có |
| Lịch dự kiến | CRS departure/arrival time, day/month | Quote và feature thời gian | Có |
| Kết quả bay | actual departure/arrival, delay, cancellation/diversion | Tạo label/đối soát oracle demo | Không; chỉ làm label/evaluation |
| Delay causes | weather/airline/late aircraft/security | Phân tích hậu nghiệm nếu cần | Không; không đưa vào model |
| Graph-derived | origin/destination PageRank, degree, historical route rate | Ablation graph | Tính từ train/history trước cutoff |

## 3. Baseline, model và graph experiment

### Thứ tự triển khai

**M0 — baseline actuarial:** xác suất label toàn bộ train; kế tiếp smoothing theo hãng; nếu có đủ mẫu, thêm origin-destination. Báo prevalence, Brier và expected payout. Route ít mẫu fallback về hãng/toàn cục. Không dùng metric baseline trên test để chọn nhóm.

**M1 — tabular ML:** Logistic Regression trước vì nhanh, xác suất dễ kiểm tra; one-hot các cột categorical, impute/scale chỉ khi cần. Nếu pipeline chạy ổn và còn thời gian, chạy XGBoost/HistGradientBoosting làm candidate thứ hai. Hiệu chuẩn bằng validation, không fit calibrator trên test.

**M2 — graph ablation:** tạo directed graph `origin → destination` từ phần train. Tạo PageRank của sân bay origin/destination và weighted degree (số chuyến/kết nối lịch sử). Nối hai giá trị vào feature row. Ưu tiên topology features, không dùng actual delay test/future để tạo graph. Nếu thêm historical delay rate, phải tính time-forward và smoothing; nếu chưa làm đúng, bỏ khỏi bản chính.

So sánh M0, M1 và M2 trên **cùng test rows, cùng label, cùng split**. Graph chỉ được gọi là đóng góp nếu kết quả thực nghiệm chứng minh; kết quả ngang/thấp vẫn báo trung thực và giải thích hạn chế graph tĩnh.

### Chỉ số

- **Brier score (primary probability metric):** xác suất thấp hơn tốt hơn; dùng cho quote/premium.
- **PR-AUC:** hữu ích khi label hiếm; so với prevalence baseline.
- **Recall/precision/F1:** ở threshold đã chọn từ validation; không tối ưu threshold bằng test.
- **Calibration/reliability plot:** nhóm ước lượng 10% thì tần suất thực nghiệm có gần 10% không.
- **Insurance simulation:** premium thu, payout giả định, loss ratio, tổng trách nhiệm/đỉnh tổn thất theo ngày hoặc airport. Đây là mô phỏng trên dữ liệu lịch sử với điều khoản và vốn giả định được công khai.
- Ghi số mẫu test, prevalence, seed, split, phiên bản thư viện, feature list và confusion matrix; không dùng accuracy đơn lẻ làm bằng chứng model tốt.

### Tạo báo giá

`pure_premium = p_calibrated × payout_amount`

Nếu dùng loading/minimum/maximum premium thì ghi thành quy tắc thiết kế riêng, không gộp vào kết quả thống kê. Quote tối thiểu phải chứa `flight_id`, ngày bay, ngưỡng, payout, premium, `quote_expiry`, `model_version` và `nonce`/chữ ký nếu contract xác minh quote ký. Contract chốt điều khoản tại thời điểm mua; không nhận xác suất ML như kết quả chuyến bay cuối cùng.

## 4. Định nghĩa graph và giới hạn diễn giải

- **Node:** sân bay.
- **Directed edge:** tuyến khai thác `ORIGIN → DESTINATION`.
- **Weight:** số chuyến scheduled/observed trong phần train. Chốt một cách và ghi rõ; không trộn số chuyến với tỷ lệ delay.
- **Features bản tối thiểu:** PageRank(origin), PageRank(destination), weighted out-degree(origin), weighted in-degree(destination). NetworkX đủ dùng; không cần graph database.
- **Ablation:** M1 không graph so với M2 có graph trên cùng temporal holdout.
- **Giới hạn:** graph tuyến mô tả cấu trúc kết nối, không tự chứng minh trễ lan truyền. Muốn kết luận propagation cần feature động theo thời gian/chuỗi chuyến và thí nghiệm riêng; không tuyên bố PageRank chứng minh delay contagion.
- Xử lý airport chưa thấy trong graph bằng giá trị fallback đã định nghĩa (ví dụ 0 hoặc giá trị trung vị train) và báo tỷ lệ fallback.
- Tạo graph chỉ từ train. Với dữ liệu dùng để huấn luyện và feature tĩnh tạo từ toàn train, ghi rõ đây là offline retrospective experiment; test cuối năm hoàn toàn không tham gia tạo graph.

## 5. Tích hợp với Blockchain/DApp

```text
Kaggle 2015 → clean/label → M0/M1/M2 evaluation
                                ↓
                    quote API / risk dashboard
                                ↓ (premium, payout, terms)
User wallet → DApp → policy contract ← mock oracle ← flight outcome
                         ↓                         ↓
                    policy/event             eligible/payout
```

- Data/ML chạy off-chain. DApp hiển thị xác suất, premium, điều khoản và phiên bản model.
- Sau mua, policy lưu ID chuyến/ngày bay, thời điểm khởi hành dự kiến, premium, payout, threshold, hạn mua và trạng thái.
- Mock oracle gửi outcome thật đã được nhóm chọn từ record test; contract kiểm tra quyền, điều kiện, trạng thái và chống chi trả trùng.
- Dashboard có tab: (1) data summary/label balance, (2) model comparison/calibration, (3) airport network, (4) quote/policy/transaction/payout.
- Không ghi dataset, feature lớn hoặc thông tin cá nhân lên chain; lưu hash/URI/version nếu thật sự cần chứng minh phiên bản.

## 6. Lịch 14 ngày và cổng hoàn thành

| Ngày | Công việc chính | Sản phẩm kiểm tra được |
|---:|---|---|
| **1** | Chốt policy threshold, cancellation/diversion, split, scope graph; kiểm tra dataset có thể tải và đọc | `docs/decision-log.md` cập nhật; data sample/schema chạy được |
| **2** | Data inventory, ID, mapping airport, missingness/duplicate | `data/README.md`, `reports/data_quality.md` |
| **3** | Label và feature pipeline; leakage allow/deny list | Script chạy từ raw → clean table; label counts |
| **4** | Temporal split, baseline toàn cục/hãng/tuyến; sanity check | Bảng M0 + split manifest |
| **5** | Logistic Regression pipeline, Brier/PR-AUC/calibration | M1 metric JSON/CSV và plot |
| **6** | Chốt metric/model; nếu ổn thử XGBoost, nếu lỗi quay về LR | Model đã chọn theo validation và config cố định |
| **7** | Graph route, PageRank/degree; airport ID join validation | Graph table/plot, số node/edge, fallback counts |
| **8** | M2 graph ablation cùng split; phân tích lỗi | Bảng M0/M1/M2 và kết luận có/không cải thiện |
| **9** | Insurance replay: premium, payout, loss ratio, pool stress | CSV/plot tài chính với giả định công khai |
| **10** | Nối quote/ML output với DApp; contract flow và mock oracle | Luồng end-to-end local hoạt động |
| **11** | Viết Data/ML/Graph/AI, kiến trúc, limitation và related-work | Các chương báo cáo draft + sơ đồ |
| **12** | Hoàn thiện báo cáo, bảng test, security, kết quả | PDF draft; số liệu nhất quán với output |
| **13** | Slide và quay video demo 5–10 phút; chạy lại từ README | Slide + video; evidence tx/metrics |
| **14** | Tổng duyệt, sửa lỗi, bàn giao source/report/slides/video/README | Release folder; checklist hoàn tất |

### Chia việc cho 3 thành viên (đề xuất)

- **Bạn A — Data/ML lead:** inventory, preprocessing, label, M0/M1, metrics, model artifact.
- **Bạn B — Graph + evaluation:** graph construction/feature, ablation, dashboard charts, kiểm tra leakage và kết quả tài chính.
- **Bạn C — Contract/DApp + integration:** quote interface, policy flow, mock oracle, local demo, gas/latency.
- Cả ba cùng chốt điều khoản ngày 1, rà soát báo cáo ngày 11–14. Mỗi đầu ra có một người chịu trách nhiệm nhưng ít nhất một thành viên khác chạy lại.

Nếu nhóm đã có code/contract chia khác thì giữ phân công đang chạy; bảng trên là phương án mặc định, không phải phân công chính thức.

## 7. Cổng giảm phạm vi khi trễ

1. Nếu ngày 3 data pipeline chưa xong: bỏ XGBoost và weather; dùng một file/schema nhỏ được giải thích để hoàn thiện baseline, ưu tiên sửa pipeline chính.
2. Nếu ngày 6 model chưa ổn: giữ Logistic Regression; không dành thời gian tuning hyperparameter.
3. Nếu ngày 8 graph không chạy hoặc metric xấu: giữ graph network visualization + feature ablation đã chạy được; báo kết quả trung thực. Không chuyển sang GNN.
4. Nếu dashboard trễ: dùng Streamlit/CSV metric + giao diện quote/policy đơn giản; giữ demo contract chạy end-to-end.
5. Không cắt test contract, label/leakage audit, README, PDF, slide hoặc video vì đây là sản phẩm bàn giao/bằng chứng bắt buộc trong project brief.

## 8. Checklist giao phẩm Data/AI/Graph

- [ ] Data inventory: nguồn, giai đoạn, schema, license/source notes, missingness, mapping, loại dòng.
- [ ] Label definition khớp điều khoản policy; prevalence và xử lý cancellation/diversion.
- [ ] Feature allowlist chỉ gồm thông tin có trước quote; leakage denylist được kiểm tra.
- [ ] Temporal split cố định; preprocessing fit trên train; test không dùng chọn model/threshold.
- [ ] M0 baseline, M1 tabular model, M2 graph ablation; Brier + PR-AUC + calibration + threshold metrics.
- [ ] Graph node/edge/weight, cutoff, feature, fallback, số node/edge được ghi lại.
- [ ] Premium/payout/loss ratio/solvency replay có giả định và mẫu số rõ.
- [ ] Output model/quote phiên bản hóa; ML off-chain, outcome oracle tách riêng.
- [ ] Dashboard/DApp hiển thị ít nhất quote và các bằng chứng analytics; local demo tái lập.
- [ ] Báo cáo ghi giới hạn: dữ liệu 2015, retrospective split, graph topology không chứng minh propagation, oracle mock và metric thực tế.

## 9. Lưu ý về tính trung thực và tiêu chí thành công

“Hoàn thành” không đồng nghĩa graph bắt buộc phải tăng metric. Thành công là pipeline chạy lại được, split và label hợp lệ, kết quả không rò rỉ, ablation được thực hiện công bằng, và kết luận đúng theo bằng chứng. Không ghi bất kỳ metric nào trước khi script chạy trên dữ liệu nhóm.
