"""Liệt kê cổng COM đang có trên máy."""
from serial.tools import list_ports

ports = list(list_ports.comports())
if not ports:
    print("Không tìm thấy cổng serial. Kiểm tra cáp dữ liệu, driver và Device Manager.")
else:
    for port in ports:
        print(f"{port.device:8} {port.description}")
