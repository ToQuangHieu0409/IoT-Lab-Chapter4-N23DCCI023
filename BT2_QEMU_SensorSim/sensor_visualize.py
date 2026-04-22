import matplotlib
import matplotlib.pyplot as plt
# Bắt buộc sử dụng Agg backend cho môi trường không có GUI như QEMU headless
matplotlib.use('Agg')
from sensor_sim import SimUltrasonic, SimPotentiometer
from time import sleep

# Bước 5: Khởi tạo cảm biến và thu thập dữ liệu
us = SimUltrasonic(echo=24, trigger=23, base_distance=50.0)
pot = SimPotentiometer(initial_value=0.4)  # Ví dụ: 0.4 tương ứng ngưỡng 40cm
span = pot.value * 100  # Chuyển đổi giá trị biến trở sang cm

# Thu thập 50 mẫu dữ liệu
distances = []
print("--- Đang thu thập dữ liệu cảm biến ---")
for i in range(50):
    d = us.distance
    distances.append(d)
    print(f"  Mẫu {i+1}/50: {d:.1f} cm")
    sleep(0.1)  # Khoảng nghỉ giữa các lần đọc

print(f"\nThu thập xong {len(distances)} mẫu.")

# Bước 6: Vẽ đồ thị và lưu thành file ảnh
fig, ax = plt.subplots(figsize=(10, 5))
x = range(len(distances))

# Vẽ đường biểu diễn khoảng cách (màu xanh)
ax.plot(x, distances, 'b-', linewidth=1.5, label='Khoảng cách (cm)')

# Vẽ đường ngưỡng span (màu đỏ, nét đứt)
ax.axhline(y=span, color='r', linestyle='--', linewidth=2, label=f'Span = {span:.0f} cm')

# Tô vùng phía dưới ngưỡng Span (vùng cảnh báo)
ax.fill_between(x, 0, [min(d, span) for d in distances],
alpha=0.2, color='red', label='Vùng Span!')

# Cấu hình nhãn trục, tiêu đề và lưới
ax.set_title('Ultrasonic Sensor Simulation — Span Detection')
ax.set_xlabel('Sample')
ax.set_ylabel('Distance (cm)')
ax.set_ylim(0, max(distances) + 10)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# Tối ưu hóa bố cục và lưu file
plt.tight_layout()
plt.savefig('sensor_chart.png', dpi=150)
print('Đã lưu đồ thị: sensor_chart.png')