# Blockchain và mock oracle

Thùy phụ trách module này. Đọc [Policy V1](../docs/insurance-policy-v1.md) và [giao nhận tích hợp](../shared/README.md) trước khi sửa rule hoặc ABI. Mục tiêu là local EVM. [FlySure](https://github.com/y4hyya/FlySure) là nền tham khảo theo quyết định nhóm. Ghi commit, license, kết quả test gốc và phần ANTs thay đổi khi đưa code vào repo.

Khi triển khai, đặt source vào `contracts/`, test vào `test/`, deploy và mock oracle vào `scripts/`, cấu hình chạy và tổng hợp số đo vào `benchmarks/` trong module này. Bàn giao lệnh compile/test/deploy, chain ID, ABI cần cho frontend, địa chỉ deploy local và fixture oracle.

Benchmark B0 tắt và B1 bật compiler optimizer. Giữ cùng source, compiler, môi trường, trạng thái đầu và workload. Lưu receipt gas theo thao tác và ghi cấu hình để chạy lại. Khi thu đủ dữ liệu điện năng, ghi phương pháp đo hoặc ước tính CO₂e, baseline máy và hệ số phát thải theo [hướng đánh giá](../docs/project-direction-handoff.md). Giữ log lớn ở `benchmarks/raw/`.
