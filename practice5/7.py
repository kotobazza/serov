from scipy.optimize import minimize_scalar


def f(x, y):
    return 4*x + 8*y -x**2 -y**2

f1 = lambda lamda: -f(0, 3*lamda)

res = minimize_scalar(f1, bounds=(0, 1), method='bounded')
print("Min value for functin:", -round(res.fun, 4))
print("X for minimal value: ", round(res.x, 4))


def grad_f(x, y):
    df_dx = -2*x+4
    df_dy = -2*y + 8
    return [df_dx, df_dy]


print(grad_f(0, 0))
