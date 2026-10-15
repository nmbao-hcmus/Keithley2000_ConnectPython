"""Chạy một chuỗi kiểm tra cài đặt, đo và hàng đợi lỗi."""
import time
import serial

PORT = "COM4"       # Ví dụ; đổi thành cổng thực tế trên máy
BAUDRATE = 9600


def send(connection, command):
    print(f"\n> {command}")
    connection.write((command + "\r").encode("ascii"))
    connection.flush()
    if "?" in command:
        answer = connection.read_until(b"\r").decode("ascii", errors="replace").strip()
        print("<", answer if answer else "(không có phản hồi)")
        return answer
    print("(lệnh cấu hình; không chờ phản hồi)")
    return None


with serial.Serial(PORT, BAUDRATE, timeout=1, write_timeout=1,
                   xonxoff=False, rtscts=False) as device:
    time.sleep(2)
    device.reset_input_buffer()

    send(device, "*IDN?")
    send(device, "*RST")  # Đưa thiết bị về mặc định; chỉ chạy theo hướng dẫn giảng viên.
    send(device, "CONF:VOLT:DC")
    send(device, "CONF?")
    send(device, "SENS:FUNC?")
    send(device, "SENS:VOLT:DC:RANG?")
    send(device, "SENS:VOLT:DC:RANG 1")
    send(device, "SENS:VOLT:DC:RANG?")
    send(device, "SENS:VOLT:DC:RANG:AUTO?")
    send(device, "SENS:VOLT:DC:NPLC 2")
    send(device, "SENS:VOLT:DC:NPLC?")
    send(device, "READ?")
    send(device, "FETC?")
    send(device, "SYST:ERR?")

    # Đọc hàng đợi lỗi sau chuỗi lệnh. Không giả định mọi thang đo
    # đều không hợp lệ trên thiết bị thật; cần đối chiếu manual trước.
    send(device, "SYST:ERR?")
