import numpy as np
from scipy.optimize import linprog

def quadratic_minimization(c, Q, x0):
    """
    Минимизация квадратичной функции с использованием алгоритма Франка-Вульфа и линейной оптимизации.

    Аргументы:
    c: numpy.array
        Вектор коэффициентов линейной части целевой функции.
    Q: numpy.array
        Матрица квадратичной части целевой функции.
    x0: numpy.array
        Начальное приближение.

    Возвращает:
    x_opt: numpy.array
        Оптимальная точка.
    f_opt: float
        Значение функции в оптимальной точке.
    """
    # Размерность пространства
    n = len(c)

    # Лямбда-функция для вычисления значения функции в точке
    f = lambda x: 0.5 * np.dot(x, np.dot(Q, x)) + np.dot(c, x)

    # Градиент квадратичной функции
    grad_f = lambda x: np.dot(Q, x) + c

    # Функция линейной оптимизации для шага
    def line_search(alpha, x, grad_f):
        return f(x - alpha * grad_f)

    # Начальная точка
    x = x0

    # Максимальное количество итераций
    max_iter = 100

    # Параметр сходимости
    epsilon = 1e-6

    for i in range(max_iter):
        # Вычисление градиента в текущей точке
        grad = grad_f(x)

        # Поиск оптимального шага с помощью линейной оптимизации
        res = linprog(grad, A_eq=Q, b_eq=-grad, bounds=[(None, None)] * n)
        alpha = res.fun

        # Обновление точки
        x_new = x - alpha * grad

        # Проверка критерия останова
        if np.linalg.norm(x_new - x) < epsilon:
            break

        x = x_new

    return x, f(x)

# Пример использования
c = np.array([1, 2])
Q = np.array([[2, 0.5], [0.5, 1]])
x0 = np.array([0, 0])

x_opt, f_opt = quadratic_minimization(c, Q, x0)
print("Оптимальная точка:", x_opt)
print("Значение функции в оптимальной точке:", f_opt)