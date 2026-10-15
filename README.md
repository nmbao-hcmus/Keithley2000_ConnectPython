# HƯỚNG DẪN THỰC HÀNH: GIAO TIẾP THIẾT BỊ ĐO KEITHLEY 2000 BẰNG PYTHON

Repository này chứa mã nguồn Python dùng trong buổi thực hành về **cổng COM/Serial, lệnh điều khiển SCPI, ghi dữ liệu CSV và hàng đợi lỗi SCPI**.

## 1. Tải và mở mã nguồn trong VS Code

1. Trên trang GitHub, nhấn **Code → Download ZIP**.
2. Tải và giải nén tệp ZIP. Nếu repository tên `Keithley2000_ConnectPython` và nhánh chính là `main`, thư mục giải nén thường có tên `Keithley2000_ConnectPython-main`.
3. Mở **Visual Studio Code**.
4. Chọn **File → Open Folder…** và mở toàn bộ thư mục project vừa giải nén.

> **Lưu ý:** Chọn **Open Folder** tại thư mục gốc của project, không mở riêng lẻ từng tệp `.py`. Như vậy Terminal và các đường dẫn tương đối sẽ trỏ đúng thư mục.

## 2. Cấu trúc và mục đích các tệp

| Tệp | Nội dung / mục đích |
|---|---|
| `code/01_list_ports.py` | Quét và liệt kê các cổng COM mà máy tính nhận diện. |
| `code/02_serial_client.py` | Mở kết nối serial, gửi lệnh SCPI và đọc phản hồi. |
| `code/03_test_commands.py` | Thử một chuỗi lệnh cấu hình, truy vấn và đọc kết quả đo. |
| `code/04_log_csv.py` | Đo lặp và lưu các phản hồi hợp lệ vào tệp CSV. |
| `code/06_settings_and_measurement.py` | Minh họa cấu hình và truy vấn phép đo. |
| `code/07_timed_logger.py` | Lấy mẫu theo khoảng thời gian và lưu các mẫu hợp lệ. |
| `code/08_error_queue_lab.py` | Đọc và khảo sát hàng đợi lỗi SCPI bằng các lệnh thực hành. |
| `requirements.txt` | Danh sách thư viện Python cần cài: `pyserial`, `matplotlib`. |
| `README.md` | Hướng dẫn lấy mã nguồn, chuẩn bị thư viện và chạy ví dụ. |
| `.gitignore` | Loại trừ môi trường ảo, cache và các tệp dữ liệu CSV khỏi Git. |

Tệp `ve_do_thi.py` được sinh viên tạo trong phần thực hành Matplotlib; nếu chưa có sẵn, hãy tạo theo hướng dẫn tại lớp. 

## 3. Chuẩn bị môi trường trước khi chạy code

1. Hoàn thành cài đặt **Python 3** và **VS Code** theo thông báo hướng dẫn cài đặt đã gửi riêng.
2. Mở Terminal trong VS Code bằng **Terminal → New Terminal** hoặc `Ctrl + ~`.
3. Nếu đã tạo môi trường `.venv` theo hướng dẫn cài đặt, hãy chọn đúng interpreter `.venv` trong VS Code. Tại thư mục gốc của repository, cài các thư viện cần thiết:

```powershell
python -m pip install -r requirements.txt
```

## 4. Ba cách chạy chương trình Python trong VS Code

### Cách 1 — Nút Run

1. Trong **Explorer**, mở thư mục `code/` và chọn tệp muốn chạy.
2. Nhấn biểu tượng **Run Python File** (nút Play) ở góc trên bên phải.
3. Kết quả sẽ xuất hiện trong **Terminal**.

### Cách 2 — Menu chuột phải

Nhấp chuột phải trong cửa sổ code và chọn **Run Python File in Terminal**.

### Cách 3 — Chạy từ Terminal

Tại thư mục gốc của project, chạy:

```powershell
python .\code\01_list_ports.py
```

Thay tên tệp nếu muốn chạy ví dụ khác. Các lệnh kết nối thiết bị chỉ được chạy khi đã chọn đúng COM và được giảng viên hướng dẫn.

## 5. Chạy thử và lưu ý trong buổi thực hành

- **Có thể chạy thử tại nhà:** chỉ chạy `code/01_list_ports.py` để quan sát danh sách cổng COM.
- Nếu máy chưa cắm USB-to-Serial hoặc chưa có driver, danh sách có thể trống. Điều này không nhất thiết là lỗi Python.
- Các tệp từ `02` đến `08` mở cổng serial và gửi lệnh SCPI. Chỉ chạy khi có thiết bị/cổng serial tương thích và theo hướng dẫn của giảng viên. Một số bài thực hành dùng mô hình đã được chuẩn bị sẵn; mô hình này không mô phỏng toàn bộ Keithley 2000.
- `03_test_commands.py` và `06_settings_and_measurement.py` có lệnh `*RST`, đưa thiết bị về trạng thái mặc định. **Không chạy lệnh này trên thiết bị thật nếu chưa được giảng viên cho phép.**
- `08_error_queue_lab.py` cố ý gửi một số lệnh không hợp lệ để khảo sát error queue. Chỉ chạy trong bài thực hành có giám sát.


## 6. Thông số serial dùng trong ví dụ (8N1)

- **Baud rate:** 9600
- **Data bits:** 8
- **Parity:** None
- **Stop bits:** 1
- **Flow control:** NONE
- **Terminator:** CR (`\r`)

Tên cổng như `COM4` trong code chỉ là ví dụ; cổng thực tế tùy từng máy. Mỗi cổng COM chỉ nên được mở bởi một phần mềm tại một thời điểm. Hãy **Disconnect** trong Hercules trước khi chạy Python.


## 7. Xử lý lỗi thường gặp

- **Không mở được link GitHub:** báo giảng viên để kiểm tra link hoặc quyền truy cập.
- **Không tìm thấy cổng COM:** kiểm tra cáp dữ liệu, driver, rồi mở **Device Manager → Ports (COM & LPT)**.
- **Cổng COM đang bận / Access Denied:** ngắt kết nối Hercules và đóng ứng dụng khác đang sử dụng cổng.
- **Không nhận được phản hồi:** kiểm tra đúng cổng, baud rate 9600, cấu hình 8N1, terminator `\r`, và thực hiện các bước kiểm tra theo hướng dẫn của giảng viên.
- **`ModuleNotFoundError`:** chọn đúng interpreter `.venv`, mở Terminal tại thư mục gốc và chạy lại `python -m pip install -r requirements.txt`.
