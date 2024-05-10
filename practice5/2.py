import numpy as np
from scipy.optimize import linprog

def quadratic_function(x, a, b, c, d, e, f):
    return a * x[0]**2 + b * x[0] + c * x[1]**2 + d * x[1] + e * x[0] * x[1] + f

def frank_wolfe_quadratic(a, b, c, d, e, f, initial_point, max_iter=100, tol=1e-6):
    x = np.array(initial_point)
    for i in range(max_iter):
        gradient = np.array([2*a*x[0] + b + e*x[1], 2*c*x[1] + d + e*x[0]])
        linear_prog_result = linprog(gradient, bounds=[(-np.inf, np.inf), (-np.inf, np.inf)])
        if linear_prog_result.success:
            direction = linear_prog_result.x - x
            step_size = 2.0 / (i + 2)
            x += step_size * direction
            if np.linalg.norm(step_size * direction) < tol:
                break
        else:
            print("Linear programming failed.")
            break
    return x

# Пример использования:
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
initial_point = [0, 0]

result = frank_wolfe_quadratic(a, b, c, d, e, f, initial_point)
print("Минимум функции:", result)
print("Значение функции в минимуме:", quadratic_function(result, a, b, c, d, e, f))