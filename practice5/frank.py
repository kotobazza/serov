import numpy as np
from scipy.optimize import linprog

def f(x, y):
    return 11*x**2 + 166.133*x + 11*y**2 + 140.4*y - 10*x*y + 8383.15

def grad_f(x, y):
    df_dx = 22*x + 166.133 - 10*y
    df_dy = 22*y + 140.4 - 10*x
    return np.array([df_dx, df_dy])

# Определение ограничений в формате linprog
def constraints():
    # x + y >= 26
    # x - 2y <= 13
    # -3x + 2y <= 26
    # 0 < x < 52
    # 0 < y < 39
    A = np.array([
        [-1, -1], # -x - y <= -26
        [1, -2],  # x - 2y <= 13
        [-3, 2],  # -3x + 2y <= 26
    ])
    b = np.array([
        -26,
        13,
        26
    ])
    bounds = [(0, 52), (0, 39)]
    return A, b, bounds

def frank_wolfe(x0, max_iter=10, tol=1e-5):
    x = np.array(x0)
    A, b, bounds = constraints()

    gradients = []

    for i in range(max_iter):
        g = grad_f(x[0], x[1])
        gradients.append(g)
        # Решение линейной аппроксимации функции
        res = linprog(g, A_ub=A, b_ub=b, bounds=bounds, method='highs')

        if res.success:
            s = res.x
            # Проверка условия сходимости
            if np.linalg.norm(s - x) < tol:
                break
            
            
            # Вычисление шага гамма
            lamda = 2 / (i + 2)

            # Обновление точки x
            x = x + lamda * (s - x)
        else:
            print("Линейная оптимизация не удалась")
            break
        print(f"--{i}--")
        print(f"linprog_res = {res.fun}")
        print(f"F(X) = {f(x[0], x[1])}")
        print(f"X = {x}")
    print('------')
    return gradients, x

# Начальная точка
x0 = (26, 13)

# Выполнение алгоритма Франка-Вульфа
_, result = frank_wolfe(x0, max_iter=10)
print("Результат минимизации:", result)
print("Значение функции в минимуме:", f(result[0], result[1]))


print(f(5.2, 20.8))