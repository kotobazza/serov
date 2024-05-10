import numpy as np
from scipy.optimize import linprog
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
import math



x = np.linspace(1, 10, 100)
y = -5*x + 10

plt.plot(x, y)

x2 = np.linspace(-10, 20, 100)
y2 = 3*x2-10

plt.plot(x2, y2)

plt.xlim(-50, 70)
plt.ylim(-50, 70)

plt.axhline(0, color='black',linewidth=1.5)
plt.axvline(0, color='black',linewidth=1.5)
plt.grid()

plt.show()