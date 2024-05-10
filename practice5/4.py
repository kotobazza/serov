import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np

# Центр эллипса (примерный, следует уточнить аналитически или численно)
x0, y0 = -7, 6  # Предполагаемые значения, полученные численно или экспертно
width, height = 20, 10  # Также предполагаемые размеры полуосей
angle = 45  # Угол поворота в градусах, оцененный по коэффициенту -10xy

# Создание фигуры и осей
fig, ax = plt.subplots()

# Создание эллипса
ellipse = patches.Ellipse((x0, y0), width, height, angle=angle, edgecolor='r', facecolor='none')
ax.add_patch(ellipse)

# Настройка отображения графика
ax.set_xlim(x0 - width, x0 + width)
ax.set_ylim(y0 - height, y0 + height)
ax.set_aspect('equal')
plt.grid(True)
plt.show()
