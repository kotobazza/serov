import matplotlib.pyplot as plt

# Начальная точка вектора
x_start = 0
y_start = 0

# Компоненты вектора
dx = 3  # изменение по x
dy = 2  # изменение по y

# Конечная точка вектора
x_end = x_start + dx
y_end = y_start + dy

# Отрисовка вектора
plt.figure(figsize=(6, 6))
plt.quiver(x_start, y_start, dx, dy, angles='xy', scale_units='xy', scale=1, color='b', label='Вектор (3, 2)')
plt.xlim(-1, 4)
plt.ylim(-1, 3)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.title('Отрисовка вектора')
plt.show()