# Flight Delay Insurance — A Blockchain Project

Nhóm **ANTs Q4H648** · IS355 · Mức 4 Research. Tên đề tài đăng ký là **Blockchain-Based Parametric Flight Delay Insurance Supported by Historical Aviation Data Analysis**.

## Bắt đầu tại đây

1. Đọc [AGENTS.md](AGENTS.md) để nắm context, quy tắc nghiệp vụ, yêu cầu Project Lab và tiêu chí đánh giá.
2. Mở [bảng phân công đến 15/12/2026](outputs/ants-allocation-20261215/ANTs-Phan-cong-15-12-2026.xlsx) và lấy mã task từ tab của mình.
3. Xem [Git flow](CONTRIBUTING.md), [Policy V1](docs/insurance-policy-v1.md) và [giao nhận tích hợp](shared/README.md) trước khi sửa code.
4. Kiểm tra [nhật ký quyết định](docs/decision-log.md) trước khi đổi dataset, nhãn, graph, stack hoặc kiến trúc. [Kế hoạch một tháng](PROJECT_PLAN_1_MONTH.md) lưu định hướng ban đầu. Deadline hiện hành là **15/12/2026**.

## Cấu trúc

```text
.
├── AGENTS.md          # Context chung, quy tắc nghiệp vụ và yêu cầu môn
├── CONTRIBUTING.md    # Clone, nhánh task, PR, review và release
├── .github/           # Mẫu pull request
├── blockchain/       # Thùy · contract, deploy, mock oracle, test, benchmark
├── risk/              # Nguyên · dữ liệu, ML, graph, định phí và ký quote
├── frontend/          # Quốc Anh · DApp, ví, dashboard, tích hợp
├── shared/            # Schema và fixture dùng chung khi được chốt
├── docs/              # Policy V1, kiến trúc, quyết định, nghiên cứu
├── outputs/           # Bảng phân công hiện hành
└── scripts/           # Prototype nghiệp vụ Python hiện có
```

## Trạng thái hiện tại

Workspace hiện có bộ khung module, tài liệu và prototype nghiệp vụ. Tiến độ Smart Contract, DApp, pipeline model/graph và benchmark được xác nhận bằng nhánh hoặc PR và bằng chứng kiểm tra trong bảng phân công.

## Chạy prototype nghiệp vụ

```powershell
python scripts/business_flow_demo.py
```

Prototype chỉ minh họa luồng quy tắc tại local process; nó không deploy contract, không kết nối ví/oracle và không chứng minh số đo blockchain.

## Nguyên tắc dữ liệu và kết quả

- Dataset Flight Delays 2015 là nguồn chính đã ghi trong đăng ký, trừ khi giảng viên chấp thuận thay đổi.
- Không commit secrets hoặc dữ liệu lớn nếu chưa kiểm tra điều khoản sử dụng.
- Mọi metric, gas, latency và kết quả model trong báo cáo phải được nhóm tự chạy và ghi lại môi trường/split.
