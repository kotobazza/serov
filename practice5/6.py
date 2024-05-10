from scipy.optimize import minimize_scalar

def objective_function(lambda_value):
    # Вычисляем значение F(X1) для данного lambda_value
    X1 = X0 + lambda_value * (X1_ - X0)
    return F(X1)

# Находим оптимальное значение lambda, минимизирующее F(X1)
result = minimize_scalar(objective_function, bounds=(0, 1), method='bounded')
optimal_lambda = result.x