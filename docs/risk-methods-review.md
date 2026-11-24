# Khảo sát method dự đoán rủi ro trễ chuyến

Khảo sát chi tiết và cập nhật hơn về các repo dùng Graph Analytics trực tiếp cho delay propagation nằm trong [`graph-repo-research.md`](graph-repo-research.md). File này giữ phần tổng hợp model/repo ban đầu; ưu tiên dùng báo cáo graph chuyên biệt khi chốt graph method.

## Mục tiêu

Tìm phương pháp có căn cứ nghiên cứu và code công khai để nhóm có baseline tái lập trong thời gian đồ án. “Clone” ở đây nên hiểu là fork/checkout mã nguồn có giấy phép phù hợp, chạy lại có trích dẫn và ghi thay đổi. Không bê nguyên kết quả bài báo sang dataset hay tuyên bố kết quả của người khác là kết quả của nhóm.

## Phương pháp phù hợp

| Phương pháp | Vai trò | Điểm mạnh | Hạn chế với nhóm |
| --- | --- | --- | --- |
| Logistic Regression | Baseline phân loại xác suất chuyến đạt điều kiện bồi thường | Dễ giải thích, chạy nhanh, cho xác suất cơ sở | Quan hệ phi tuyến hạn chế |
| Random Forest | Baseline phi tuyến cho dữ liệu dạng bảng | Bắt tương tác, không đòi scaling mạnh | Cần kiểm soát lệch lớp và hiệu chuẩn xác suất |
| Gradient Boosting | Ứng viên mô hình tốt cho dữ liệu bảng | Nghiên cứu so sánh trên mạng sân bay Mỹ báo cáo GBM tốt nhất trong các LR, RF, GBM và mạng feed-forward | Cần tái lập trên feature hợp lệ và split thời gian của nhóm |
| GNN không gian-thời gian | Phân tích lan truyền trễ giữa sân bay theo mạng và chuỗi thời gian | Gắn Graph Analytics trực tiếp với hiện tượng lan truyền trễ | Khác bài toán dự đoán xác suất cho từng chuyến bay; dữ liệu, cách tạo graph và dependency nặng hơn |

Một nghiên cứu trên dữ liệu chuyến bay và thời tiết BTS/NOAA mô hình hóa dự đoán arrival delay như bài toán phân loại và so sánh logistic regression, random forest, gradient boosting, feed-forward neural network. Nghiên cứu báo cáo GBM tốt nhất trong tập so sánh, đồng thời nhấn mạnh mất cân bằng nhãn và đánh giá nhiều metric. Đây là lý do chọn GBM làm ứng viên, không phải cam kết nó sẽ tốt nhất trên dataset nhóm.

Một bài báo GCN theo time-evolving airport graphs mô tả dự đoán ở mức mạng nhiều sân bay với các snapshot đồ thị không gian-thời gian. Đây là hướng graph phù hợp nếu nhóm muốn nghiên cứu propagation, nhưng cần phân biệt với risk score của policy ở cấp chuyến bay.

## Repo có thể tái sử dụng

### Khuyến nghị chính: Prashant-4527 / flight-delay-prediction

Đây là điểm khởi đầu hợp nhất với dataset nhóm: README ghi rõ US DOT/BTS 2015, MIT, pipeline so sánh Logistic Regression, Random Forest và XGBoost, notebook EDA/feature engineering/evaluation/SHAP, cùng giao diện Streamlit và API. Có thể fork hoặc clone để tham khảo và tái lập pipeline.

Không dùng nguyên model hay metric của repo làm kết quả của ANTs. Repo gốc dự đoán arrival delay `>15` phút và loại cancelled/diverted flights. Đề tài nhóm cần định nghĩa nhãn riêng theo policy, ví dụ cancelled hoặc arrival delay `>=120` phút, và phải quyết định diversion. Đọc từng feature để giữ lại chỉ thông tin có trước giờ báo giá. Thêm feature graph sân bay và chạy ablation có/không graph trên cùng temporal split. Bản MIT được nêu trong README; khi fork giữ LICENSE và attribution.

### Junzis / atdelay

Repo khai báo mã cho ba mức: Random Forest dự đoán arrival delay từng chuyến, LSTM cho sân bay đơn, và DST-GAT cho network nhiều sân bay. README nói pipeline dùng dữ liệu EUROCONTROL cần xin license, nên có khả năng không chạy trực tiếp trên US DOT Kaggle dataset. Cần tự kiểm tra file LICENSE và data requirements trước khi copy hay fork. Phù hợp tham khảo kiến trúc graph và cách xử lý nhiều mức dự đoán, có nguy cơ tốn thời gian chuyển dữ liệu.

### gonzalonao / flight-delay-propagation

Repo MIT license, gồm DenseNN, LSTM, BasicGCN, MultiHorizonGAT và spatio-temporal Transformer. Repo mô tả pipeline BTS cộng thời tiết, graph 70 sân bay và dataset 2018–2022. Đây là repo có license và các baseline rõ, nhưng data period và mục tiêu dự đoán theo giờ/sân bay khác dataset đăng ký 2015 và payout theo từng policy. Không nên clone toàn bộ pipeline với deadline một tháng; có thể lấy cấu trúc so sánh baseline/graph hoặc fork riêng nếu nhóm chủ động đổi dataset và trích dẫn.

## Khuyến nghị thực nghiệm trong một tháng

1. Định nghĩa nhãn trực tiếp theo hợp đồng bảo hiểm: `1` nếu chuyến bay bị hủy hoặc arrival delay đạt ngưỡng nhóm chốt, `0` nếu không.
2. Chỉ dùng biến biết được lúc báo giá: hãng, sân bay đi/đến, ngày, thứ, tháng, giờ dự kiến và đặc trưng graph tính từ dữ liệu lịch sử. Không dùng actual departure/arrival time, arrival delay, cancellation cause hoặc biến chỉ xuất hiện sau chuyến bay để dự đoán trước chuyến bay.
3. Chia dữ liệu theo thời gian, ví dụ train các tháng đầu năm, validation các tháng kế tiếp, test các tháng cuối năm. Fit preprocessing chỉ trên train.
4. Chạy theo cùng split: baseline tỷ lệ gộp/smoothing theo tuyến hoặc hãng, Logistic Regression, Gradient Boosting, và Gradient Boosting + graph features.
5. Báo cáo PR-AUC, recall, precision, F1 và Brier score/calibration. Vì đây là giá rủi ro dùng để định phí, xác suất được hiệu chuẩn quan trọng. Chọn threshold vận hành riêng, không chỉ tối ưu accuracy.
6. Dùng graph analytics theo hai mức khả thi: thống kê degree/weighted degree của sân bay và so sánh mô hình có/không có các đặc trưng đó. GNN chỉ thêm nếu graph snapshot và tích hợp code chạy ổn sau baseline.
7. Định phí tham khảo theo `premium = predicted_probability × payout + disclosed_loading`, có giới hạn min/max nếu cần. Loading là giả định thiết kế, phải báo riêng và không trình bày là kết quả học máy.

## Lưu ý nhãn và leakage

Ngưỡng 120 phút trong đề xuất hợp đồng không giống định nghĩa delay 15 phút thường dùng trong các bài dự đoán vận hành. Nhóm phải tự tạo nhãn đúng với policy và báo cáo prevalence của nhãn mới. Nếu dùng dữ liệu năm 2015, một thí nghiệm test theo các tháng cuối năm vẫn chỉ đánh giá hồi cứu trong cùng năm, chưa chứng minh khái quát sang các năm hiện nay.

Không trộn actual departure delay vào một mô hình báo phí trước chuyến bay. Một số nghiên cứu arrival delay có thể dùng thông tin gần giờ bay hoặc weather forecast. Phải ghi rõ prediction time và tập thông tin có sẵn tại mốc đó.

## Bước kiểm tra trước khi clone repo

- Đọc LICENSE và giữ copyright/notice theo yêu cầu.
- Xác nhận repo có code, checkpoint, dataset và hướng dẫn tái lập nào.
- Kiểm tra Python/framework và phiên bản phụ thuộc trên máy nhóm.
- Tạo fork hoặc thư mục upstream riêng, lưu commit/tag làm mốc.
- Chạy một thí nghiệm mẫu trước khi tích hợp vào DApp.
- Ghi citation, đường dẫn nguồn, commit, thay đổi của nhóm và kết quả chạy lại.

## Nguồn đã khảo sát

- K. K. et al., “Study of Delay Prediction in the US Airport Network,” *Aerospace*, 2023. DOI 10.3390/aerospace10040342. https://www.mdpi.com/2226-4310/10/4/342
- IEEE, “A Deep Learning Approach for Flight Delay Prediction Through Time-Evolving Graphs,” DOI 10.1109/TITS.2021.3103502. https://ieeexplore.ieee.org/document/9512525/
- Prashant-4527/flight-delay-prediction, US DOT/BTS 2015, Logistic Regression/Random Forest/XGBoost, Streamlit, MIT. https://github.com/Prashant-4527/flight-delay-prediction
- Data UAB, Logistic Regression tutorial dùng cùng dataset 2015, nhưng nhãn 30 phút và cách chia/evaluation cần được cải thiện cho nhóm. https://datauab.github.io/flight-delays/
- junzis/atdelay, mô tả Random Forest, LSTM và DST-GAT. https://github.com/junzis/atdelay
- gonzalonao/flight-delay-propagation, MIT license và pipeline graph spatio-temporal cho dữ liệu BTS 2018–2022. https://github.com/gonzalonao/flight-delay-propagation
- Kaggle, Flight Delays 2015 đã đăng ký. https://www.kaggle.com/datasets/usdot/flight-delays

Tên bài và repo là đầu mối để nghiên cứu. Trước khi đưa số liệu hoặc nhận định cụ thể vào báo cáo, kiểm tra bản gốc, tác giả, data split, license, code và khả năng tái lập.

## Graph sân bay: nghiên cứu, code và data

Có nghiên cứu graph sân bay cho cả phân tích cấu trúc và dự đoán lan truyền trễ. Một bài Physica A phân tích dữ liệu Trung Quốc và Mỹ trong hai tháng năm 2018, xây mạng lan truyền từ quan hệ giữa chuỗi trễ sân bay rồi dùng k-core và cấu trúc đa lớp. Bài IEEE về time-evolving airport graphs dùng GCN không gian-thời gian để dự đoán delay trên nhiều sân bay. Hai bài là căn cứ phương pháp; chưa xác nhận được bộ dữ liệu và code đầy đủ có thể tái lập từ các trang đã xem.

Repo `junzis/atdelay` cung cấp Random Forest cấp chuyến, LSTM cấp sân bay và DST-GAT cấp mạng, nhưng README cho biết data chính là EUROCONTROL R&D cần xin license. Repo `dlleonardo/openflights-airport-network-analysis` là mẫu gọn cho topology graph và centrality, dựa trên OpenFlights, không phải dữ liệu delay chuyến năm 2015. Repo `gonzalonao/flight-delay-propagation` có GCN/GAT/Transformer với license MIT và dataset Kaggle 2018–2022. Repo `Flnny/Delay-data` dựng flight-chain và flight-network graph từ Aeolus, một dataset khác và nặng hơn.

### Đề xuất cho ANTs

Giữ nguyên Flight Delays 2015 cho bài toán chính và dựng directed weighted graph từ chính dữ liệu đó. Sân bay là node, tuyến Origin → Destination là edge, edge weight là số chuyến hoặc thống kê trễ lịch sử. Từ graph, tạo đặc trưng lịch sử như weighted degree, degree, centrality và tỷ lệ trễ/hủy sân bay/tuyến. Tính các đặc trưng chỉ từ dữ liệu trước ngày chuyến bay cần báo giá, tạo graph riêng trong từng time split để tránh rò rỉ dữ liệu tương lai.

Sau đó so sánh cùng một mô hình bảng trên cùng temporal split: baseline và XGBoost không có graph features, rồi baseline và XGBoost có graph features. Nhãn phải theo điều khoản policy của nhóm. Đây là cách kiểm chứng graph có giúp dự đoán rủi ro của chuyến bay được bảo hiểm hay không, thay vì chỉ vẽ network hoặc báo cáo centrality rời rạc.

Nguồn: Physica A, https://doi.org/10.1016/j.physa.2023.128526 ; IEEE time-evolving graph, https://ieeexplore.ieee.org/document/9512525/ ; OpenFlights graph, https://github.com/dlleonardo/openflights-airport-network-analysis ; atdelay, https://github.com/junzis/atdelay ; Gonzalo repo, https://github.com/gonzalonao/flight-delay-propagation ; Aeolus code/data, https://github.com/Flnny/Delay-data

## Xếp hạng ưu tiên theo khả năng tái lập

Thứ tự này là đánh giá hiện tại cho nhóm ANTs với khoảng một tháng, chưa có xác nhận từ giảng viên. “Dễ tái lập” được ưu tiên hơn con số metric cao trong README, vì các bài toán và cách chia test có thể khác.

Hồ sơ đăng ký của nhóm nêu đích danh dataset Kaggle năm 2015. Vì vậy các repo dùng dataset khác chỉ là tham khảo phụ cho đến khi giảng viên chấp thuận đổi nguồn dữ liệu.

### A. Repo/model dự đoán trên dữ liệu gần với đề tài

| Ưu tiên | Repo/data | Đánh giá cho ANTs | Việc phải điều chỉnh |
| ---: | --- | --- | --- |
| **1** | [Prashant-4527/flight-delay-prediction](https://github.com/Prashant-4527/flight-delay-prediction) + [US DOT/BTS 2015 Kaggle](https://www.kaggle.com/datasets/usdot/flight-delays) | Khớp chính dataset đã đăng ký; README nêu MIT, Logistic Regression/RF/XGBoost, notebooks, pinned requirements, API/dashboard. Tốt nhất làm điểm xuất phát để nhóm tái lập benchmark. | Repo gốc dự đoán trễ >15 phút và bỏ hủy/chuyển hướng. Đổi target theo policy; kiểm tra feature tại thời điểm báo giá; dùng temporal split; chạy lại metric của chính nhóm. Không mang nguyên metric repo vào báo cáo. |
| **2** | Tự dựng pipeline nhỏ trên cùng [US DOT/BTS 2015 Kaggle](https://www.kaggle.com/datasets/usdot/flight-delays), tham khảo Logistic Regression tutorial của [Data UAB](https://datauab.github.io/flight-delays/) | Dữ liệu đã có trong proposal, ít phụ thuộc dịch vụ ngoài; mô hình logistic đơn giản dễ chạy để có baseline kiểm chứng. | Tutorial gốc dùng target >30 phút, notebook/tutorial có giới hạn về split/evaluation và không phải pipeline production. Dùng như tham khảo method, viết lại split theo thời gian và target của policy. |
| **3** | [sudikshas/flight-delay-prediction-pyspark](https://github.com/sudikshas/flight-delay-prediction-pyspark) + 2015–2021 OTPW (flight + NOAA weather) | README báo weighted F1 khoảng 0.82 cho Random Forest, PageRank airport feature và temporal holdout năm 2019. Hữu ích nhất để mượn ý tưởng graph feature/congestion. | 15M hàng thô, Spark/Databricks, data ghép thời tiết và 13 lớp departure delay. Khác insurance target. Data không được đóng gói trong repo theo khảo sát, cần xác minh đường lấy/join trước khi chọn làm nguồn chính. Ưu tiên tham khảo method, không mang metric sang đồ án. |
| **4** | [nishantsingh-ds/Mining-Big-Data-Flight-Delay-Classification](https://github.com/nishantsingh-ds/Mining-Big-Data-Flight-Delay-Classification) + Kaggle 2015 | Cùng dataset và logistic regression, nhưng quy trình đặt trong AWS/Spark/S3/Athena. | Bỏ phần AWS, chạy local và xác minh notebook thực sự tải được data. README/license/reproducibility cần kiểm tra kỹ trước khi dùng. |
| **5** | [gonzalonao/flight-delay-propagation](https://github.com/gonzalonao/flight-delay-propagation) + Kaggle 2018–2022 | Repo MIT, có nhiều bậc baseline đến GNN, lockfile và tests. Tốt làm tham khảo graph prediction nếu nhóm đổi dataset có chủ đích. | Dataset khác giai đoạn, task dự đoán airport-hour nhiều horizon thay vì probability cho policy; phụ thuộc PyTorch/GNN và tài nguyên lớn hơn. Chỉ chọn nếu giảng viên chấp nhận đổi data/task và môi trường nhóm chạy được. |
| **6** | [junzis/atdelay](https://github.com/junzis/atdelay) + EUROCONTROL R&D data | Có DST-GAT gần với network delay research. | Data chính cần xin license; đây là rào cản tái lập lớn trong deadline hiện tại. Không ưu tiên nếu nhóm chưa có quyền truy cập sẵn. |

Repo `aneessaheba/realtime-flight-delay-predictor-bigdata` nêu AUC-ROC khoảng 0.968 và delayed-class F1 khoảng 0.806 trên dữ liệu 2023, nhưng top features bao gồm DEP_DELAY và TAXI_OUT. Đây là thông tin phát sinh sau thời điểm mua bảo hiểm, nên kết quả đó không hợp lệ để định giá trước chuyến bay. Không chọn chỉ vì metric cao.

### B. Repo/dataset cho graph analysis

| Ưu tiên | Nguồn | Dùng cho việc gì | Đánh giá |
| ---: | --- | --- | --- |
| **1** | Flight Delays 2015 gốc đã đăng ký | Dựng directed route graph và tạo graph features từ dữ liệu lịch sử | Khớp bài toán, tránh ghép nguồn khác. Cần tự làm code graph, kiểm soát temporal leakage. |
| **2** | [dlleonardo/openflights-airport-network-analysis](https://github.com/dlleonardo/openflights-airport-network-analysis) + dữ liệu [OpenFlights trên Skewed.de](https://networks.skewed.de/net/openflights) | Học/tái lập degree, betweenness, PageRank, assortativity, network efficiency | Dễ hiểu, nhưng graph là route topology, không chứa delay lịch sử của chính dataset 2015. Dùng minh họa hoặc tham khảo code, không dùng thay dữ liệu label. |
| **3** | [Aeolus data/code](https://github.com/Flnny/Delay-data) | Tái lập flight-chain/network graph experiments | Có cấu trúc graph phong phú hơn, nhưng phải chuyển sang dataset khác và kiểm tra dung lượng, license, yêu cầu tính toán. |
| **4** | [gonzalonao/flight-delay-propagation](https://github.com/gonzalonao/flight-delay-propagation) | Tái lập graph neural network spatio-temporal prediction | Source MIT và dataset Kaggle 2018–2022, nhưng nặng và khác task. Hợp khi mục tiêu chính là GNN propagation, không phải đường ngắn nhất cho bảo hiểm policy. |
| **5** | [junzis/atdelay](https://github.com/junzis/atdelay) | Đọc implementation DST-GAT | Phụ thuộc EUROCONTROL R&D cần xin license, nên chưa phải lựa chọn data dễ tái lập. |

`Sudikshas` là nguồn tham khảo thêm cho cách đưa PageRank/rolling congestion vào mô hình delay, nhưng pipeline Spark, dữ liệu thời tiết ghép sẵn và task 13 lớp khiến nó không đứng đầu theo độ dễ tái lập.

### Đề xuất thực hiện theo thứ tự

1. Tải và xác nhận schema/nguồn của Flight Delays 2015. Chọn một temporal split cố định.
2. Chạy baseline đơn giản và pipeline repo ưu tiên 1. Ghi lại commit, môi trường và metric thực chạy.
3. Dựng directed graph theo route từ phần train, tạo historical route/airport features không dùng thông tin tương lai.
4. Chạy ablation cùng model và cùng split, có/không graph features.
5. Chỉ sau khi các bước trên hoạt động mới cân nhắc clone GNN nặng hoặc đổi sang dataset/repo khác.

Nếu yêu cầu mức Research khiến GNN cụ thể bắt buộc, hỏi giảng viên trước bước 5. Metric cao trong README không thay thế được khả năng tái lập, target khớp và đánh giá test độc lập.
