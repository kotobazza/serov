import numpy as np
from scipy.optimize import linprog

c = [-1, -1]  # коэффициенты целевой функции для минимизации

A_ub = [[1, 2], [-2, -1], [3, -1]]  # коэффициенты левых частей неравенств (<=)
b_ub = [4*13, -13, -17.5]  # правые части неравенств (<=)

bounds = [(0, 2*13), (0, 1.5*13)]  # границы x и y

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

print(res)