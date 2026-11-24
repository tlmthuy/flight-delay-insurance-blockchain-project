# Điều khoản bảo hiểm chuyến bay V1 — ANTs

**IS355 · ANTs Q4H648 · 21/11/2026**  
**Mục đích** · Bộ quy tắc dùng chung để triển khai và nghiệm thu bản demo trên local EVM bằng ETH thử nghiệm.

Hành khách xem trước phí, hạn mua và quyền lợi của một chuyến bay cụ thể. Sau khi mua, hành khách có thể theo dõi kết quả, biết vì sao policy được chi trả hoặc kết thúc và rút tiền nếu có khoản được ghi có. Bản demo đạt yêu cầu khi cùng một điều khoản cho ra kết quả khớp nhau ở dữ liệu, Smart Contract và DApp trong mọi trường hợp ở bảng nghiệm thu.

## 1. Điều khoản hành khách nhìn thấy

| Điều khoản | Quy tắc V1 |
| --- | --- |
| Chuyến được bảo hiểm | Một chuyến theo lịch, xác định bằng mã hãng khai thác, số hiệu, sân bay đi, sân bay đến, ngày khởi hành theo giờ địa phương tại sân bay đi và thời điểm khởi hành dự kiến quy đổi sang UTC. Các thành phần đã chuẩn hóa tạo thành `flightId`; mọi báo giá, policy và kết quả dùng cùng định danh. |
| Hạn mua | Phải mua **sớm hơn 24 giờ** trước giờ khởi hành dự kiến. Giao dịch được xác nhận đúng mốc 24 giờ bị từ chối. Chuyến đã có kết quả cuối cùng bị khóa mua ngay, kể cả khi chưa đến hạn mua. |
| Thời hạn báo giá | Hiệu lực tối đa **15 phút từ khi phát hành** và kết thúc chậm nhất tại hạn mua. Giao dịch phải được xác nhận trước cả hai mốc. Hết hạn thì lấy báo giá mới. |
| Quyền lợi | Nhận **0,01 ETH thử nghiệm** nếu chuyến bị hủy hoặc đến sân bay đích theo lịch **trễ từ 120 phút trở lên**. Mức trễ tính so với giờ đến dự kiến. Trễ đúng 120 phút đủ điều kiện. Mỗi policy nhận tối đa một khoản. |
| Chuyển hướng | Chuyến có kết quả cuối cùng là chuyển hướng và không bị hủy kết thúc với **0 ETH**. Nếu nguồn xác nhận chuyến bị hủy, áp dụng quyền lợi hủy một lần. |
| Thiếu kết quả | Policy hiển thị **Chờ kết quả chuyến bay** và quỹ giữ đủ tiền bồi thường. Nếu luồng tự động chưa cập nhật sau chuyến bay, khách có thể gửi yêu cầu xác minh kèm giấy tờ qua kênh hỗ trợ. |
| Giới hạn mua | **Một policy cho mỗi ví trên mỗi chuyến**, tính cả policy đã kết thúc. Nhiều ví có thể mua cùng chuyến nếu quỹ còn đủ dự trữ. Quy tắc được áp dụng theo địa chỉ ví. |

**Lý do chọn bộ quy tắc này.** Trễ đến phản ánh việc hành khách tới đích muộn. Mốc 120 phút tạo một ranh giới dễ kiểm thử. Hạn mua 24 giờ giảm khả năng mua khi sự cố đã gần xảy ra. Payout cố định cho phép dùng một xác suất và một mức dự trữ trên mỗi policy. Giữ policy trong lúc xác minh giúp bảo toàn quyền lợi khi nguồn dữ liệu hoặc oracle chậm. Các con số là lựa chọn thiết kế cho đồ án. Nhóm sẽ báo độ phổ biến của biến cố và tác động lên quỹ sau khi chạy dữ liệu 2015.

## 2. Báo giá, mua và dự trữ quỹ

1. **Báo giá.** Dịch vụ Python ước lượng xác suất phát sinh bồi thường `p` từ thông tin có tại lúc phát hành báo giá. Phí V1 là `premiumWei = max(1, ceil(p × payoutWei))`, với `p` thuộc `[0, 1]` và `payoutWei = 10^16`. Dịch vụ dùng phép tính thập phân và làm tròn lên đến wei. V1 dùng phí thuần, phụ phí bằng 0. Ví dụ `p = 5%` cho phí **0,0005 ETH** trước gas.
2. **Khóa điều khoản.** Dịch vụ ký báo giá cho đúng người mua và chuyến. Dữ liệu được ký gồm chain ID, địa chỉ contract, ví mua, `flightId` và thông tin lịch bay đã chuẩn hóa, premium, payout, ngưỡng trễ, mốc mua, thời điểm phát hành/hết hạn, nonce và phiên bản policy/mô hình. Contract kiểm tra người ký, ví mua, thời hạn, nonce, giá trị gửi đúng bằng phí và các hằng số nghiệp vụ V1. Policy giữ điều khoản tại thời điểm mua.
3. **Giữ vốn.** Mỗi policy mới cần dự trữ đủ **0,01 ETH**, kể cả trong thời gian chờ kết quả. Contract chỉ nhận mua nếu số dư sau khi nhận phí đủ cho toàn bộ policy đang hiệu lực và các khoản đã ghi có nhưng chưa rút, kể cả policy mới. Nếu thiếu vốn, giao dịch mua bị hủy.
4. **Giới hạn quỹ.** Admin cấp vốn bằng ETH thử nghiệm và chỉ rút phần dư sau khi trừ trách nhiệm đang giữ và khoản đã ghi có. V1 kiểm soát sức chứa bằng dự trữ toàn quỹ. Mô phỏng tài chính cần có tình huống nhiều ví mua và nhiều chuyến đủ điều kiện chi trả gần nhau.

## 3. Kết quả oracle và cách nhận tiền

- **Đăng ký chuyến và ghi kết quả.** Admin đăng ký các chuyến demo trên contract trước khi mở bán, dùng cùng danh mục chuyến với dịch vụ báo giá và DApp. Contract khóa giờ khởi hành dùng để tính hạn mua. Chỉ mock oracle được cấp quyền mới ghi kết quả cho chuyến đã đăng ký. Một chuyến chỉ có một kết quả cuối cùng hợp lệ dùng chung cho mọi policy. Contract từ chối kết quả lặp hoặc mâu thuẫn với kết quả đã ghi.
- **Thế nào là kết quả hợp lệ.** `Arrived` cần độ trễ đến theo phút với dấu, cho phép số âm nếu đến sớm. `Cancelled` và `Diverted` không cần độ trễ đến. `Arrived` và `Diverted` chỉ được ghi từ giờ khởi hành dự kiến trở đi. Hủy đã xác nhận có thể ghi sớm hơn và khóa bán ngay. Trạng thái tạm hoặc bản ghi đến bị thiếu số phút trễ chưa phải kết quả cuối cùng.
- **Yêu cầu xác minh thủ công theo cách AirCare.** Khi luồng tự động chưa xác nhận được kết quả, khách có thể gửi mã policy, xác nhận trễ hoặc hủy của hãng bay và giấy tờ hành trình qua kênh hỗ trợ. Người vận hành đối chiếu giấy tờ với chuyến ghi trong policy. Nếu đủ bằng chứng, người vận hành dùng oracle hiện có để ghi kết quả và contract xét theo điều khoản lúc mua. Nếu giấy tờ chưa đủ, policy tiếp tục chờ và vốn dự trữ vẫn được giữ. Nếu kết quả tự động đã được ghi trong lúc chờ xử lý yêu cầu, contract dùng kết quả đã ghi và chỉ xử lý policy một lần. [Điều khoản AirCare, mục Loss Provisions](https://docs.bhtp.com/bhtp-descriptions-of-coverage/AirCare%204%20062015/FL.pdf)
- **Phạm vi demo.** Mô phỏng việc khách gửi yêu cầu bằng một bộ giấy tờ giả lập bên ngoài DApp. Người vận hành ghi kết quả qua mock oracle. DApp chỉ hiển thị mã policy và hướng dẫn liên hệ hỗ trợ khi chưa có kết quả. Smart Contract chỉ nhận kết quả chuyến bay đã xác minh. Giấy tờ hành trình được xử lý ngoài chuỗi.
- **Xử lý policy.** Bất kỳ địa chỉ nào cũng có thể gọi xử lý từng policy khi đã có kết quả hợp lệ, kể cả kết quả đến muộn. Contract quy định số tiền và ví nhận. Việc xử lý chỉ thực hiện được một lần. Khi còn chờ kết quả, policy giữ trạng thái `Active`.
- **Nhận tiền.** Contract ghi có tiền bồi thường cho ví đã mua. Chỉ ví đó được rút, kể cả khi địa chỉ khác gọi xử lý policy. Tiền còn được giữ nếu giao dịch rút thất bại.

| Từ `Active` | Trạng thái tiếp theo | Xử lý tiền |
| --- | --- | --- |
| Hủy hoặc đến trễ đủ ngưỡng | `Claimable` | Chuyển khoản dự trữ thành khoản phải trả **0,01 ETH**. Rút thành công chuyển sang `Paid`. |
| Đến trễ dưới ngưỡng hoặc chuyển hướng hợp lệ | `Closed` | Giải phóng dự trữ. Khách không có khoản để rút. |
| Chưa có kết quả hợp lệ | `Active` | Giữ đủ dự trữ trong lúc chờ dữ liệu tự động hoặc xác minh theo yêu cầu của khách. |

## 4. Quy tắc chung cho dữ liệu và DApp

| Phần | Cách áp dụng |
| --- | --- |
| **Nhãn ML** | `1` cho hủy hoặc chuyến đến với `ARRIVAL_DELAY ≥ 120`. `0` cho chuyến đến có số phút hợp lệ dưới 120 hoặc chuyển hướng đã xác nhận mà không hủy. Nếu bản ghi đánh dấu cả hủy và chuyển hướng, ưu tiên hủy. Chuyến đến thiếu số phút trễ và bản ghi không xác định được kết quả được tách ra, thống kê số lượng và loại khỏi tập huấn luyện/đánh giá nhị phân. |
| **Mô phỏng quỹ** | Ghi phí thu, bồi thường và vốn còn bị giữ ở các policy đang chờ. Có thể mô phỏng oracle gửi muộn hoặc thiếu kết quả bằng kịch bản có kiểm soát. Ghi rõ cách tạo dữ liệu mô phỏng và các trường hợp thiếu trong dữ liệu gốc. |
| **Màn hình mua** | Hiện đúng chuyến, giờ địa phương ở sân bay đi, hạn mua, thời hạn báo giá, phí, payout và điều kiện hủy, trễ, chuyển hướng. Khi người dùng ký, trạng thái chỉ chuyển sang đã mua sau receipt thành công. |
| **Màn hình policy** | Hiện chờ kết quả chuyến bay, đủ điều kiện rút bồi thường, đã nhận bồi thường hoặc kết thúc không chi trả. Khi còn chờ, hiện mã policy và hướng dẫn liên hệ hỗ trợ. Kết quả giao dịch và số tiền hiển thị theo dữ liệu đọc từ chain. |

## 5. Bảng nghiệm thu trước demo

| Tình huống | Kết quả kỳ vọng |
| --- | --- |
| Mua trước hạn một giây, báo giá còn hiệu lực, gửi đúng phí và quỹ đủ | Tạo policy `Active`, khóa điều khoản và dự trữ 0,01 ETH. |
| Mua đúng hạn, báo giá hết hạn, gửi sai phí, sai ví hoặc dùng lại nonce | Giao dịch bị từ chối. Số dư quỹ, trạng thái policy và dự trữ không đổi. |
| Cùng ví mua lần hai cho cùng `flightId` | Giao dịch bị từ chối. Ví khác vẫn có thể mua nếu đủ điều kiện. |
| Hủy đã được ghi nhận trước hạn mua | Policy đã mua đủ điều kiện chi trả. Yêu cầu mua mới bị từ chối. |
| Đến sớm hoặc trễ 119 phút | Nhãn `0`. Policy `Closed`, giải phóng dự trữ. |
| Đến trễ đúng 120 phút hoặc trễ 121 phút | Nhãn `1`. Policy `Claimable` với 0,01 ETH. |
| Hủy hoặc chuyển hướng có kết quả cuối cùng | Hủy có nhãn `1` và chi trả 0,01 ETH. Chuyển hướng không hủy có nhãn `0` và kết thúc không chi trả. |
| Luồng tự động chưa có dữ liệu hoặc khách gửi giấy tờ chưa đủ | Policy tiếp tục `Active`, giữ đủ dự trữ. DApp hiển thị chờ kết quả và hướng dẫn liên hệ hỗ trợ. |
| Khách gửi xác nhận của hãng bay về chuyến trễ 125 phút. Người vận hành xác minh và gửi kết quả qua oracle | Policy `Claimable` với 0,01 ETH. Ví mua vẫn rút được theo điều khoản ban đầu. |
| Oracle gửi kết quả hợp lệ đến muộn, chuyến đến trễ 30 phút | Policy `Closed`, giải phóng dự trữ. |
| Sai quyền oracle, ghi trùng, xử lý hoặc rút lần hai | Giao dịch không hợp lệ bị từ chối, không thay đổi khoản khách đã được ghi có. |
| Quỹ thiếu dự trữ hoặc admin rút vượt phần dư | Giao dịch bị từ chối. Tiền đang dự trữ và tiền khách chưa rút vẫn được giữ. |

**Tiêu chí bàn giao.** Nguyên tạo nhãn và báo giá từ bộ quy tắc trên. Thùy chạy bảng nghiệm thu trên local chain và lưu kết quả thực tế. Quốc Anh đối chiếu phí, thời hạn, lý do kết thúc và số tiền rút trên DApp với receipt và trạng thái contract. Bản demo trình bày ba trường hợp **không đủ điều kiện, đủ điều kiện theo dữ liệu tự động và khách được bồi thường sau khi gửi yêu cầu xác minh**.
