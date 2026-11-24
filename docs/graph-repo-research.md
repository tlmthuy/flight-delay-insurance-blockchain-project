# Repo nghiên cứu Graph Analytics cho flight delay

**Cập nhật:** 13/11/2026  
**Mục tiêu:** tìm repo có phân tích đồ thị thực sự liên quan đến delay prediction/propagation, rồi đánh giá cách dùng cho đề tài bảo hiểm của ANTs. Thông tin repo/metric dưới đây là của tác giả, không phải kết quả nhóm ANTs.

## Kết luận nhanh

Graph Analytics **có liên quan** nếu nhóm dùng mạng sân bay để mô hình hóa việc trễ ở một sân bay có thể ảnh hưởng chuyến bay/sân bay kế tiếp, rồi kiểm tra nó có giúp ước lượng xác suất sự kiện bảo hiểm hay không. Nó ít có ý nghĩa hơn nếu chỉ tính PageRank/centrality và vẽ network mà không nối với rủi ro policy.

Không tìm thấy một repo duy nhất ghép đủ **flight-delay insurance + Smart Contract + airport graph**. Có các repo riêng cho graph delay prediction/propagation. Hướng hợp lý là lấy một graph method làm phần Data/Research, đổi target thành điều khoản bảo hiểm của nhóm, rồi ghép đầu ra xác suất vào luồng quote/contract qua backend/oracle theo thiết kế của ANTs.

## Xếp hạng theo mức phù hợp với ANTs

| Ưu tiên | Repo / nghiên cứu | Graph được dùng thế nào | Mức khớp | Khả năng tái lập và hạn chế |
|---:|---|---|---|---|
| **1 — Method nên khảo sát/kế thừa** | [yajun668/FlightDelayPrediction](https://github.com/yajun668/FlightDelayPrediction), bài *Flight Delay Dynamics…*, Decision Support Systems (2025), DOI [10.1016/j.dss.2025.114494](https://doi.org/10.1016/j.dss.2025.114494) | Tạo mạng sân bay có hướng và phụ thuộc thời gian; tính Airport-Network-Spilled Propagation (ANSP) score từ ảnh hưởng delay lan qua các kết nối sân bay. Score được thêm vào các model dự đoán delay khởi hành. | **Khớp câu hỏi nghiên cứu nhất:** graph feature có bổ sung thông tin rủi ro chuyến bay ngoài feature thường không? Bài báo báo cáo cải thiện AUC tối đa 5.49% và ANSP là feature quan trọng nhất trong SHAP trên thí nghiệm của họ. | Repo có MIT; data từ BTS + FAA + IEM, tải riêng trên [Mendeley Data](https://data.mendeley.com/datasets/j3zfnxk56h/2), CC BY 4.0. Paper dùng 423,029 chuyến, 30 sân bay Large Hub, 1/6–31/7/2023; dự đoán **departure delay** ở các mốc 2/3/6 giờ. Khác Kaggle 2015 và target arrival/cancel của ANTs. Repo nhỏ nhưng README ít hướng dẫn chạy/dependency, nên cần smoke-test trước khi quyết định tái lập nguyên repo. |
| **2 — Ý tưởng nhẹ để tham khảo trên cùng vùng dữ liệu Mỹ** | [sudikshas/flight-delay-prediction-pyspark](https://github.com/sudikshas/flight-delay-prediction-pyspark) | Tạo airport PageRank feature từ graph dùng lịch sử 2015–2018; kết hợp rolling congestion features vào classifier. | Cùng vùng dữ liệu BTS, có train theo thời gian, graph feature được đưa vào dự đoán delay. Gợi ý một cách ablation graph so với tabular. | Task là **13 lớp departure-delay**, data 2015–2021 + NOAA, khoảng 15M dòng raw; dùng Databricks/PySpark và test 2019. README báo weighted F1 RF khoảng 0.82 nhưng đó là metric upstream, không chuyển thành kết quả ANTs. Repo public nhưng danh sách file hiện không thấy LICENSE và dữ liệu ghép không kèm trong repo; chỉ tham khảo ý tưởng cho tới khi xác minh quyền dùng code/data và khả năng chạy local. |
| **3 — Repo GNN airport propagation, tham khảo kiến trúc** | [gonzalonao/flight-delay-propagation](https://github.com/gonzalonao/flight-delay-propagation) | 70 airport nodes, route edges; hourly graph snapshots với traffic/delay/weather; so sánh DenseNN/LSTM/GCN/GAT và spatio-temporal Transformer để dự đoán arrival delay trung bình theo sân bay, 1–8 giờ. | Graph được dùng trực tiếp để mô hình hóa propagation; có baseline ladder và temporal test. Hợp nếu cần minh họa phương pháp GNN. | MIT, có lockfile/test và hướng dẫn tải dataset Kaggle 2018–2022; nhưng không cùng dataset 2015, prediction unit là airport-hour chứ không phải xác suất bồi thường cho từng flight, triển khai kèm Azure/Fabric và mô hình nặng. Tác giả báo MAE 10.02, RMSE 18.26 phút cho model lớn; không phải benchmark so sánh trực tiếp với ANTs. |
| **4 — Ví dụ ngắn về GraphFrames/airport metrics** | [dennyglee/databricks — On-Time Flight Performance with GraphFrames](https://github.com/dennyglee/databricks/blob/master/notebooks/Users/denny%40databricks.com/flights/On-Time%20Flight%20Performance.py) | Dựng airport/flight graph, tìm flight-chain motifs qua sân bay trung chuyển, PageRank và top transfer airports. Dùng BTS Q1/2014 và OpenFlights. | Có thể học cách trình bày graph analytics cụ thể và motif/transfer; dễ nối câu chuyện “delay lan qua các chuyến kết nối”. | Notebook cũ từ 2016, dựa GraphFrames/Databricks API cũ; đây là minh họa analytics chứ không phải pipeline model/insurance có thể dùng nguyên xi. Hợp để học định nghĩa graph hơn là clone. |
| **5 — ST-GNN học thuật nhưng data khó lấy** | [ConstantinosAr/Air-traffic-delays-prediction-model](https://github.com/ConstantinosAr/Air-traffic-delays-prediction-model), [junzis/atdelay](https://github.com/junzis/atdelay) | Dự đoán trễ nhiều airport theo thời gian bằng ST-GNN/DST-GAT, bên cạnh RF cấp chuyến và LSTM cấp sân bay. | Rất gần nếu mục tiêu là nghiên cứu delay propagation bằng GNN. | Cả hai dựa EUROCONTROL; TU Delft capstone nói dữ liệu không công khai vì lý do pháp lý, còn atdelay yêu cầu xin license. TU Delft repo cũng yêu cầu TensorFlow/Spektral đời cũ. Không ưu tiên nếu nhóm chưa có quyền data/môi trường chạy. |

## Repo số 1 liên quan bảo hiểm của ANTs ở điểm nào?

Bài ANSP dự báo **delay khởi hành** chứ không dự báo trực tiếp “policy có được bồi thường hay không”. Nhưng ý tưởng network spillover có thể làm feature rủi ro trước chuyến bay:

1. Lập graph có hướng giữa các sân bay/tuyến bay từ dữ liệu lịch sử.
2. Tính điểm network delay risk tại mốc báo giá, chỉ dựa trên các chuyến/kết quả đã có tới thời điểm đó.
3. Gắn điểm rủi ro sân bay đi/đến (hoặc route) vào dòng chuyến bay cần báo giá.
4. Dự đoán nhãn do ANTs định nghĩa, ví dụ `cancelled OR arrival_delay >= policy_threshold`.
5. So sánh trên cùng temporal split: baseline tabular → baseline + graph feature → nếu đủ thời gian, dynamic propagation score.
6. Đổi xác suất được hiệu chuẩn thành quote theo công thức nhóm công bố; Smart Contract chỉ nhận quote/điều khoản đã kiểm tra, không tự tính model.

Do bài ANSP tập trung departure-delay prediction, bước chuyển sang arrival-delay insurance là **đề xuất cần thử nghiệm**, không phải đã được chứng minh bởi bài báo. Nếu không cải thiện Brier/calibration hoặc hiệu quả tài chính của pool, phải báo cáo graph không tạo cải thiện trong setup của nhóm thay vì cố khẳng định graph có ích.

## Kế hoạch tái lập phù hợp 1 tháng

**Không nên clone cả platform GNN đầu tiên.** Dùng Kaggle Flight Delays 2015 làm nguồn chính như đăng ký; mượn method ANSP/airport graph làm phương pháp và tự tạo target theo policy.

1. **Bản tối thiểu (khuyến nghị):** dựng directed airport-route graph từ các chuyến 2015; tạo historical route/airport delay rate và một số graph feature tính chỉ trên train/history. Dùng baseline LR/XGBoost, so sánh thêm graph feature.
2. **Bản nghiên cứu tốt hơn nếu kịp:** tái lập simplified ANSP score (delay propagation có decay theo thời gian) trên các airport/flight liên quan; chạy ablation và temporal test. Chỉ dùng feature có sẵn tại thời điểm mua.
3. **Bản mở rộng:** tải Mendeley dataset v2 và chạy repo/paper ANSP nguyên trạng để kiểm tra benchmark độc lập. Đây là dataset 2023 khác proposal; dùng như supplementary replication hoặc chỉ chuyển thành data chính nếu thầy đồng ý.
4. **Không ưu tiên:** clone ST-GNN lớn, ghép thêm nhiều nguồn weather, dựng Azure/production serving hay train Spark 15M rows; các bước này không cần để chứng minh network feature có ích cho premium.

### Đánh giá cần báo

- So sánh cùng split và cùng label: Brier score, reliability/calibration, PR-AUC/recall và phí thu/payout/loss ratio.
- Với model graph, ghi node, edge có hướng, weight, window/decay, cutoff thời điểm, dữ liệu tạo graph và cách tránh temporal leakage.
- Mọi metric nêu từ paper/repo phải ghi là **kết quả upstream**; ANTs phải chạy lại trên dữ liệu/split của nhóm trước khi báo cáo kết quả.

## Nguồn gốc và giới hạn đã kiểm tra

- Bài ANSP và code availability: [publisher article / abstract](https://www.sciencedirect.com/science/article/pii/S0167923625000958); [GitHub repo](https://github.com/yajun668/FlightDelayPrediction); [file graph features](https://github.com/yajun668/FlightDelayPrediction/blob/main/network_feature.py); [Mendeley dataset v2](https://data.mendeley.com/datasets/j3zfnxk56h/2).
- Sudiksha README/code: [GitHub repo](https://github.com/sudikshas/flight-delay-prediction-pyspark).
- Gonzalo README/code: [GitHub repo](https://github.com/gonzalonao/flight-delay-propagation).
- Databricks GraphFrames notebook: [GitHub source](https://github.com/dennyglee/databricks/blob/master/notebooks/Users/denny%40databricks.com/flights/On-Time%20Flight%20Performance.py); notebook ghi nguồn BTS/OpenFlights và giai đoạn BTS 1/1–31/3/2014.
- TU Delft ST-GNN: [GitHub repo](https://github.com/ConstantinosAr/Air-traffic-delays-prediction-model); atdelay: [GitHub repo](https://github.com/junzis/atdelay).

**Giới hạn khảo sát:** trang repo/README/paper được đọc để sàng lọc mức phù hợp; chưa clone hay chạy repo trong lượt khảo sát này. Cần xác minh commit, dependency, license của từng thành phần và chạy smoke test trước khi gọi là tái lập được.

## Kiểm định khả năng ghép Graph với pipeline Prashant trên Kaggle 2015

### Kết luận cho quyết định hiện tại

Không repo nào cho phép cam kết **tái lập 100%, không gặp trục trặc** khi ghép nguyên trạng với Prashant và dataset Kaggle 2015. Chưa có repo nào chạy trên đúng môi trường, dữ liệu và điều khoản bảo hiểm của ANTs; một số repo còn dùng target, giai đoạn dữ liệu hoặc đơn vị dự đoán khác. Metric upstream không dự báo được metric sau khi đổi target, cutoff thời gian và split.

Nếu tiêu chí chính là **khả năng tái lập trong môi trường của nhóm**, lựa chọn ít rủi ro nhất là giữ pipeline tabular của Prashant làm baseline rồi tự bổ sung một lượng nhỏ graph feature theo ý tưởng PageRank của Sudiksha, tính graph chỉ trên tập lịch sử/train. Đây là **tái triển khai phương pháp**, không phải clone/chạy nguyên repo Spark. Chỉ giữ graph nếu ablation trên temporal holdout cải thiện hoặc đem lại phân tích hữu ích; không hứa trước rằng metric sẽ tăng.

| Repo graph | Ghép với Prashant + Kaggle 2015 | Rủi ro tái lập | Nhận định |
|---|---|---|---|
| **Sudiksha — PySpark/PageRank** | **Cao nhất trong ba nếu chỉ mượn PageRank/airport graph.** Cùng hệ sinh thái chuyến bay Mỹ và có ý tưởng airport-level feature; map score sân bay đi/đến vào dòng flight của Prashant tương đối đơn giản. | Repo gốc dùng Spark/Databricks, 2015–2021 + NOAA, 13 lớp departure delay; khác target và data của nhóm, dữ liệu ghép không có sẵn, license chưa thấy. | Không clone nguyên pipeline. Viết phiên bản nhỏ với NetworkX/pandas trên dữ liệu 2015; graph train-only; so sánh Prashant tabular với tabular+PageRank. Dễ chạy hơn GNN nhưng PageRank tĩnh có thể không tăng dự đoán delay. |
| **Gonzalo — GCN/GAT/spatio-temporal** | Thấp. Đầu vào là airport-hour graph snapshots và output là delay trung bình theo sân bay/horizon; Prashant là phân loại từng chuyến. | Dữ liệu 2018–2022, nhiều bước tạo snapshot/weather, framework deep learning và target khác. Cần thiết kế lại model/nhãn/feature chứ không chỉ thêm cột graph. | Không chọn để tích hợp nếu ưu tiên an toàn tái lập. Hợp làm hướng riêng nếu chuyển câu hỏi nghiên cứu sang airport-level propagation và được chấp nhận đổi dữ liệu. |
| **ANSP — yajun668/FlightDelayPrediction** | Tương đồng nghiên cứu cao: graph propagation dùng để dự đoán delay. Tuy nhiên không phải feature plug-in đã tương thích với Kaggle 2015/Prashant. | Dataset 2023 khác. Khi đọc code, `empirical_validation.py` dường như đưa các trường hậu chuyến bay vào `x` qua `reg_data.iloc[:,1:]` rồi dùng random KFold; cần sửa leakage và đánh giá theo thời gian. Trong `delay_score.py`, trọng số edge được lấy từ min của toàn bộ filtered window thay vì riêng các chuyến A→B, có thể làm sai trọng số. `main.py` dùng đặc trưng mạng theo tháng đầy đủ nên nếu cắt ngẫu nhiên trong tháng có nguy cơ nhìn trước dữ liệu. Chưa chạy repo để xác nhận các vấn đề này bằng thực thi. | Chỉ kế thừa khái niệm sau khi audit và viết lại theo cutoff nghiêm ngặt; không dùng metric upstream làm kỳ vọng. Rủi ro sửa/đối chiếu cao hơn PageRank đơn giản. |

### Thiết kế thử nghiệm có khả năng chạy lại cao nhất

1. Cố định một commit của Prashant; trước hết tái chạy baseline trên Kaggle 2015 và lưu đúng preprocessing, phiên bản package, seed, label và split. Nếu baseline không chạy sạch thì sửa riêng pipeline trước khi thêm graph.
2. Chốt nhãn theo policy (arrival delay/hủy) và một thời điểm báo giá. Loại khỏi feature mọi trường chỉ biết sau chuyến bay. Với đề cương hiện tại, đặc biệt kiểm tra không dùng `DEPARTURE_DELAY`, `ARRIVAL_DELAY`, `CANCELLED`, `CANCELLATION_REASON`, actual times hoặc delay causes làm đầu vào báo giá.
3. Chia theo thời gian, ví dụ các tháng đầu năm cho train, một giai đoạn kế tiếp cho validation, các tháng cuối năm cho test. Chỉ xây graph và tính PageRank từ train/history có trước cutoff; không dựng graph từ toàn bộ 2015 rồi mới chia.
4. Dùng node là sân bay và edge có hướng Origin→Destination; tạo một số feature gọn như PageRank của origin/destination, weighted degree và tỷ lệ biến cố lịch sử đã smoothing. Fit smoothing chỉ từ train. Quy định fallback cho sân bay/tuyến chưa thấy.
5. Chạy hai nhánh trên đúng các dòng và cùng split: (A) feature tabular của Prashant, (B) feature tabular + graph. Đo Brier score/calibration và PR-AUC/recall; thêm loss ratio/payout simulation nếu nhãn và điều khoản policy đã chốt. Ghi rõ graph có ích hay không; không tối ưu test set.
6. Lưu script sinh feature, cấu hình, mapping airport ID, số dòng rơi/mất mapping, seed và output metrics. Kiểm tra schema và join cardinality để tránh nhân đôi dòng chuyến bay.

### Điều kiện trước khi gọi là tái lập

- Dataset thực tế đã tải, checksum/phiên bản và schema được ghi nhận; hiện tại repo project chưa có bằng chứng dataset đã được tải.
- Baseline Prashant chạy được độc lập trên máy nhóm, không chỉ dựa vào README/metric upstream.
- Graph feature được sinh xác định từ dữ liệu trước prediction cutoff, không rò rỉ test/future data.
- Một lần chạy sạch từ đầu tạo đúng số lượng hàng, không có duplicate join, và sinh metric đã lưu được.
- Có ablation trên cùng temporal test; kết quả có thể thấp hơn, ngang hoặc cao hơn baseline. Kết quả thấp không đồng nghĩa code không tái lập được — có thể graph không đóng góp cho nhãn/feature đã chọn.

**Đánh giá cuối:** ưu tiên phương án **Prashant + graph PageRank tối giản tự triển khai theo ý tưởng Sudiksha**. Mức tin cậy hiện tại: *tương đối cao về khả năng triển khai kỹ thuật*, nhưng *chưa kiểm chứng bằng chạy thực tế* và *không đảm bảo cải thiện metric*. Không thể cam kết 100% không trục trặc trước khi có dataset, môi trường cố định và chạy thử end-to-end. Nếu yêu cầu graph phải mô hình hóa lan truyền trễ rõ hơn PageRank, có thể thiết kế feature propagation lịch sử đơn giản; nhưng nên làm sau khi baseline + ablation PageRank chạy ổn.
