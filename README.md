# Buổi 2 — Python, PySerial và dữ liệu từ thiết bị đo

Repository này chứa các ví dụ Python dùng trong buổi thực hành về cổng COM/serial, lệnh SCPI, ghi dữ liệu CSV và hàng đợi lỗi.

> **Phạm vi:** Repository chỉ gồm mã Python; không chứa mã nguồn Arduino hoặc firmware. Arduino/mô hình thực hành tại lớp đã được chuẩn bị sẵn, không cần nạp firmware. Một số phản hồi SCPI của mô hình thực hành có thể khác thiết bị Keithley Model 2000 thật.

## Lấy mã nguồn

Trên trang GitHub, chọn **Code → Download ZIP**, tải và giải nén. Trong VS Code, chọn **File → Open Folder…** và mở thư mục `Buoi2_Python_PySerial_GitHub` vừa giải nén.

Nếu không mở được repository, hãy báo giảng viên để kiểm tra link hoặc quyền truy cập.

## Các tệp trong repository

| Tệp | Mục đích |
|---|---|
| `code/01_list_ports.py` | Liệt kê các cổng COM khả dụng. |
| `code/02_serial_client.py` | Gửi lệnh SCPI tương tác và đọc phản hồi. |
| `code/03_test_commands.py` | Kiểm tra một chuỗi lệnh cấu hình, truy vấn và đo. Có lệnh `*RST` đưa thiết bị về trạng thái mặc định. |
| `code/04_log_csv.py` | Đo lặp và lưu các phản hồi hợp lệ vào CSV. |
| `code/06_settings_and_measurement.py` | Minh họa cấu hình và truy vấn phép đo. |
| `code/07_timed_logger.py` | Ghi các mẫu hợp lệ theo thời gian; bỏ qua timeout. |
| `code/08_error_queue_lab.py` | Khảo sát hàng đợi lỗi SCPI bằng các lệnh thực hành. |
| `requirements.txt` | Các thư viện Python cần thiết. |

Đánh số tệp theo trình tự mô-đun của học liệu; mô-đun GUI/PyQt6 không thuộc phạm vi repository này. Tệp `ve_do_thi.py` được sinh viên tạo trong phần thực hành Matplotlib nên không có sẵn ở đây.

## Cài thư viện của repository

Hãy hoàn thành hướng dẫn cài đặt Python/VS Code đã được gửi riêng và chọn đúng môi trường `.venv` trong VS Code. Tại Terminal ở thư mục gốc repository, chạy:

```powershell
python -m pip install -r requirements.txt
```

Các thư viện được cài là `pyserial` và `matplotlib`.

## Chạy ví dụ đầu tiên

Có thể chạy chương trình liệt kê cổng COM mà không gửi lệnh đo:

```powershell
python .\code\01_list_ports.py
```

Nếu máy chưa kết nối thiết bị USB-serial hoặc chưa có driver, danh sách cổng có thể trống; điều đó không nhất thiết là lỗi cài đặt Python.

## Chạy các ví dụ giao tiếp serial

Các chương trình còn lại mở cổng COM và gửi lệnh SCPI. Chỉ chạy theo hướng dẫn của giảng viên, với đúng thiết bị và cổng đã xác minh. Mặc định `COM4` chỉ là ví dụ; cần thay bằng cổng thực tế trong tệp `.py` hoặc truyền tham số `--port` cho `02_serial_client.py`.

Cấu hình thực hành trong buổi học:

- Baud rate: **9600**
- Data bits: **8**
- Parity: **None**
- Stop bits: **1** — **8N1**
- Flow control: **NONE**
- Terminator: **CR** (`\r`)

Chỉ một ứng dụng nên mở một cổng COM tại một thời điểm. Ngắt kết nối trong Hercules trước khi chạy chương trình Python.

## Lưu ý về thiết bị và lệnh SCPI

- Ví dụ được dùng để học theo trình tự giao tiếp trong lớp; mô hình Arduino đã chuẩn bị sẵn không mô phỏng toàn bộ hành vi của Keithley Model 2000.
- Lệnh `*RST` trong `03_test_commands.py` đưa thiết bị về trạng thái mặc định. Chỉ chạy theo hướng dẫn của giảng viên.
- Không mặc định thang `SENS:VOLT:DC:RANG 5` là không hợp lệ: 5 V có thể là thang đo hợp lệ trên Keithley Model 2000. Đối chiếu manual của đúng thiết bị trước khi kết luận một lệnh gây lỗi.
- Khi dùng Keithley thật, cần cáp hoặc bộ chuyển đổi RS-232 phù hợp. Không nối trực tiếp cổng DB9 RS-232 với chân RX/TX mức TTL của Arduino Uno.
- Các giá trị minh họa trong code hoặc slide không mặc nhiên là số đo thực nghiệm.
- Không nạp hoặc chỉnh sửa firmware Arduino trong phạm vi buổi học.

## Lỗi thường gặp

- **Không thấy cổng COM:** kiểm tra cáp dữ liệu, driver và **Device Manager → Ports (COM & LPT)**.
- **Cổng đang bận:** ngắt kết nối trong Hercules và đóng ứng dụng khác đang dùng cổng.
- **Không import được thư viện:** kiểm tra VS Code có chọn đúng `.venv`, sau đó chạy lại lệnh cài `requirements.txt`.
- **Không nhận phản hồi:** kiểm tra đúng COM, thông số serial, terminator CR và loại lệnh; làm theo hướng dẫn của giảng viên.
