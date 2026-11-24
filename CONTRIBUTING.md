# Cách làm việc trên repo ANTs

## Clone và nhận task

Nhóm dùng một remote chung và một nhánh tích hợp `main`. Dùng remote riêng tư của nhóm cho bộ khung hiện tại vì `AGENTS.md` có thông tin thành viên. Nếu nhóm đã có lịch sử code, đưa bộ khung vào repo đó qua một PR, giữ lịch sử và nhánh của các bạn.

Sau khi được cấp quyền, dùng URL remote của nhóm. Thay `URL_REPO_NHOM` trước khi chạy.

```powershell
git clone URL_REPO_NHOM ants-is355
cd ants-is355
git switch main
git pull --ff-only origin main
git switch -c feat/qa02-quote-screen
```

Lấy mã, hạn và điều kiện nghiệm thu từ [sheet ngày 15/12](outputs/ants-allocation-20261215/ANTs-Phan-cong-15-12-2026.xlsx). Một nhánh cho một task hoặc một nhóm task phụ thuộc chặt được ghi rõ trong PR. Dùng `feat/`, `fix/`, `docs/` hoặc `chore/`, ví dụ `feat/ng03-policy-label`, `feat/th05-purchase-reserve`, `chore/th08-optimizer-benchmark`.

## Commit và mở PR

1. Kiểm tra `git status`, đọc `AGENTS.md` và README của module. Khi sửa schema, ABI, event hoặc fixture, báo người đang dùng đầu ra trước khi đổi.
2. Chạy kiểm tra liên quan, xem `git diff` và chỉ stage các file của task. Commit tiếng Anh, có mã task. Push nhánh của mình.

   ```powershell
   git status --short
   git diff
   git add frontend/README.md
   git diff --cached
   git commit -m "docs(QA02): document quote screen requirements"
   git push -u origin feat/qa02-quote-screen
   ```

3. Mở PR vào `main`, dùng [mẫu PR](.github/pull_request_template.md) và yêu cầu review từ một người khác. Khi PR đổi dữ liệu bàn giao, yêu cầu reviewer là người sử dụng đầu ra ở module kế bên. Dán link PR hoặc bằng chứng vào sheet.
4. Khi cần đồng bộ, lưu công việc trên nhánh task, chạy `git fetch origin` và `git merge origin/main`. Giải quyết xung đột với người phụ trách đoạn bị ảnh hưởng, rồi chạy lại kiểm tra liên quan.
5. Merge sau khi đã xử lý review và kiểm tra đạt. Nhóm dùng squash merge nếu remote hỗ trợ. Mỗi người push nhánh task của mình. `main` nhận thay đổi qua PR và tránh force push trên nhánh dùng chung.

## Người review và nghiệm thu

| PR của | Reviewer mặc định | Kiểm tra trước khi merge |
| --- | --- | --- |
| Quốc Anh | Thùy cho Web3, Nguyên cho dashboard/báo giá | Ví đúng mạng, receipt và event khớp chain, lỗi giao dịch hiện đúng. |
| Nguyên | Quốc Anh cho giao nhận quote, Thùy cho nhãn và điều khoản | Lệnh tái lập, temporal split, metric từ lần chạy của nhóm, vector quote đọc được. |
| Thùy | Quốc Anh cho ABI/event, Nguyên cho quote/nhãn | Compile, test policy/oracle/quỹ, chạy local và gửi ABI nếu interface đổi. |

Các PR thay đổi Policy V1 hoặc giao diện dùng chung nêu tác động tới cả ba module và thống nhất thứ tự merge. Đánh dấu **Xong** khi có đầu ra đạt tiêu chí trong sheet và bằng chứng có thể mở hoặc chạy lại.

## Thiết lập remote và bàn giao

- Người quản lý remote mời ba thành viên, đặt `main` làm mặc định và bật yêu cầu PR + một review nếu gói GitHub hỗ trợ. Mẫu PR có hiệu lực khi có trên nhánh mặc định. [GitHub branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) · [GitHub PR template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
- Commit source, lockfile của công cụ đã chọn, fixture nhỏ, cấu hình mẫu và bản tổng hợp kết quả đủ tái lập. Giữ dataset gốc, file sinh lại được, cache, log thô và khóa riêng ở local hoặc nơi lưu nội bộ phù hợp. Ghi nguồn, license và commit của code tham khảo nếu tái sử dụng.
- Nguyên xác nhận commit hoặc tag của bản nộp và README. Thùy đối chiếu số liệu trong PDF/slide. Quốc Anh đối chiếu video và kiểm đủ năm giao phẩm ngày 15/12.
