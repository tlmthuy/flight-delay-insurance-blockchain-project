# Nội dung checkpoint cho bảng sản phẩm nộp

**Cách dùng:** các tên trong cột “Phân công” là **đầu mối quản lý giao phẩm**: giữ cấu trúc, nhắc hạn, chia phần cho thành viên, nhận phần đã điền, kiểm tra tính nhất quán và đóng gói. Đầu mối không phải người duy nhất làm toàn bộ sản phẩm.

**Đầu mối theo bảng nhóm gửi:**

- **Source Code — Nguyên:** Trương Mạnh Nguyên (quản lý repo/integration; các module do người phụ trách module nộp).
- **README — Nguyên:** nhận hướng dẫn chạy từ cả ba, chuẩn hóa và kiểm tra lại.
- **Báo cáo PDF — Thùy:** Trần Lê Minh Thùy (tạo sườn, chia chương; cả ba điền phần chuyên môn).
- **Slide — Thùy:** nhận nội dung/ảnh/kết quả từ cả ba, ráp deck và giữ thống nhất với báo cáo.
- **Video demo — Quốc Anh:** Phạm Quốc Anh (storyboard, lịch quay, ráp video; mỗi thành viên quay phần module mình).

**Người điền nội dung chuyên môn theo phân công module hiện tại:** Quốc Anh — Web3 integration; Nguyên — Data/ML/Graph; Thùy — Smart Contract/oracle/test. Tại mỗi checkpoint, đầu mối giao phẩm cập nhật checkbox khi đã nhận đủ phần, review xong và lưu bản tương ứng.

## Bảng mốc 3 ngày

Ngày bắt đầu lấy theo bảng nhóm: **16/11/2026**. Các checkpoint cách 3 ngày là 16, 19, 22, 25, 28/11; **30/11 là mốc chốt bàn giao** (2 ngày sau checkpoint gần nhất để còn buffer sửa lỗi).

| Sản phẩm / đầu mối | 16/11 — Sườn & giao việc | 19/11 — Bản khung chạy được | 22/11 — Bản tích hợp đầu | 25/11 — Đủ nội dung & feature freeze | 28/11 — Review/diễn tập | 30/11 — Đóng gói cuối |
|---|---|---|---|---|---|---|
| **Source Code — Nguyên** | Tạo/kiểm tra repo structure, branch và issue; chốt interface/ABI, định dạng quote, output model và người phụ trách từng module. Thùy: contract skeleton; Quốc Anh: Web3/DApp shell; Nguyên: data pipeline skeleton. | Thùy nộp policy purchase + access-control skeleton/test; Quốc Anh nộp connect wallet/network và đọc contract stub; Nguyên nộp schema, label draft, baseline chạy được trên sample. Có hướng dẫn chạy từng module. | Chạy được luồng local quote → mua policy → oracle mock → eligibility/payout; dashboard hiển thị ít nhất một kết quả model và một graph view/metric. Lưu log lỗi và phân công fix. | **Feature freeze.** Merge code, test happy path + reject paths; model/graph ablation có output; ít nhất 3 risk/security mitigations được thể hiện trong thiết kế/test. Không thêm tính năng mới. | Thành viên không viết module đó chạy thử theo README; sửa bug, kiểm tra config/ABI/address, xóa key/dữ liệu bí mật; lưu evidence test và transaction. | Tag/release source cuối; kiểm tra file/folder cần nộp; kèm scripts, `.env.example` không chứa secret, artifacts metric nhỏ, link/ghi chú lấy dataset. Chạy lại demo lần cuối. |
| **README — Nguyên** | Tạo mục lục: overview, prerequisites, install, data, model, graph, contract, DApp, demo, limitations; giao mỗi người viết mục chạy module mình. | Thùy điền lệnh compile/test/deploy; Quốc Anh điền ví/network/DApp; Nguyên điền data path, preprocess/train/evaluate, graph; đánh dấu phần nào chưa xác nhận. | Có hướng dẫn end-to-end bản nháp; ghi chính xác môi trường, dependencies, dataset cần tải và cách cấu hình địa chỉ contract. | Tất cả lệnh đã chốt; không còn placeholder quan trọng; ghi rõ oracle mock, model off-chain, kết quả chưa production. | Người khác làm theo từ checkout sạch; ghi lại lỗi và sửa README/code cho khớp. | README cuối khớp source release, chỉ dẫn cài/chạy/demo theo đúng thứ tự, có troubleshooting ngắn và expected output. |
| **Báo cáo PDF — Thùy** | Tạo template 7 chương, format, danh sách hình/bảng/tài liệu tham khảo; giao: Quốc Anh chương Web3/DApp/transaction; Nguyên data/ML/graph/evaluation; Thùy problem/policy, contract/security/test; mỗi người nhận một reviewer. | Có Ch.1–3 draft; Ch.4 architecture sơ bộ; bảng điều khoản policy, use case, data inventory ban đầu; trích dẫn nguồn đã xác minh, bỏ placeholder của mẫu. | Ch.4–5 có kiến trúc và implementation thật; Ch.6 có test/model/graph results sơ bộ được ghi là preliminary; các bảng/figure có chú thích và nguồn. | Đủ 7 chương; thay toàn bộ số liệu tạm bằng output đã chạy; có test table, security ≥3 rủi ro (risk→scenario→mitigation), gas/latency thực đo, pool replay/limitations. | Soát logic, citation/DOI, tên/thuật ngữ, mục lục, đánh số hình/bảng; reviewer của từng chương xác nhận đúng code và output. | Xuất PDF cuối, mở kiểm tra trang bìa/mục lục/hình/bảng/link; thống nhất nội dung với source, slide và video; lưu file bàn giao. |
| **Slide — Thùy** | Tạo sườn 8–12 slide theo flow: problem, related work, architecture, data/AI/graph, contract, evaluation/security, demo, limitations; giao mỗi người phần của mình. | Có nội dung placeholder có người chịu trách nhiệm; Quốc Anh gửi Web3 flow/screenshot; Nguyên gửi data/graph hình draft; Thùy gửi policy/state machine/contract outline. | Deck đầy đủ lần 1; thay placeholder bằng sơ đồ/ảnh thật; kết quả ML/Graph ghi rõ preliminary nếu chưa freeze. | Slide khớp kết quả cuối, không dùng số chưa đo; có demo flow, 3 security risks, hạn chế và phân chia người nói. | Diễn tập bấm giờ, kiểm tra chữ/hình và chuyển người nói; sửa phần khó hiểu hoặc quá dài. | Xuất PPTX/PDF nếu cần; kiểm tra font/media; lưu bản cuối cùng dùng bảo vệ. |
| **Video demo 5–10 phút — Quốc Anh** | Viết storyboard và chia lời: mở đầu/problem; kiến trúc; Web3/transaction; model/graph; contract/oracle/payout; kết quả/hạn chế. Đặt lịch quay từng người. | Quay thử màn hình từng module; kiểm tra mic, ví/local chain, dataset artifacts; tạo shot list và phương án dự phòng nếu transaction demo lỗi. | Có footage draft của quote→buy→oracle→payout; mỗi người thuyết minh module mình; chèn kết quả ML/graph từ run thật. | Quay đủ toàn bộ nội dung; xác nhận thời lượng khoảng 5–10 phút; quay lại đoạn sai; không đọc số liệu chưa freeze. | Ráp bản gần cuối, kiểm tra âm thanh/độ nét/chữ; cả nhóm xem và ghi timestamp lỗi. | Render video cuối; mở xem file sau render, kiểm tra âm thanh/thời lượng; lưu đúng tên/định dạng nơi nhóm sẽ nộp. |

## Gói nội dung thành viên phải nộp cho đầu mối

| Người điền | Gửi cho đầu mối giao phẩm | Mỗi gói bàn giao cần có |
|---|---|---|
| **Thùy — Smart Contract** | Source Code/README: Nguyên; Báo cáo/Slide: Thùy; Video: Quốc Anh | Contract + tests/deploy steps; ABI/address/network info; event/transaction evidence; contract fields/state diagram; test cases expected/actual; gas/latency thực đo; 3 rủi ro và mitigations. |
| **Nguyên — Data/ML/Graph** | Source Code/README: Nguyên; Báo cáo/Slide: Thùy; Video: Quốc Anh | Preprocess/model/graph scripts; data inventory; label/split/feature allowlist; metrics và plots đã chạy; graph definition/cutoff; premium-payout replay; limitations/reproduction steps. |
| **Quốc Anh — Web3** | Source Code/README: Nguyên; Báo cáo/Slide: Thùy; Video: Quốc Anh | UI/Web3 source; wallet/network/ABI config steps; transaction states/error handling; screenshots hoặc tx evidence; architecture/dataflow; Web3 run instructions. |

## Quy tắc cập nhật checkbox

Đánh dấu một mốc hoàn thành khi đủ cả ba điều kiện: **(1)** thành viên gửi phần của mình, **(2)** đầu mối tích hợp vào đúng giao phẩm và review, **(3)** artifact/bản nháp được lưu trong repo hoặc thư mục nhóm. Nếu mới có code rời hoặc placeholder thì để chưa hoàn thành.

Không có file spreadsheet gốc trong repository hiện tại; tài liệu này là nội dung copy vào các cột ngày của bảng nhóm. Nếu ngày nộp thực tế khác 30/11, giữ thứ tự checkpoint và dời cột cuối theo hạn của giảng viên.
