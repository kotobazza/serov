import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import math
from sympy import symbols, diff, simplify, solveset




def linprog_maximization(xcoeff, ycoeff):    
    c = np.array([-xcoeff, -ycoeff])    
    
    res = linprog(c, A_ub = linprog_A, b_ub = linprog_B, bounds=x_y_bounds)
    #print(res)
    return res


def linprog_minimization(xcoeff, ycoeff):
    c = np.array([xcoeff, ycoeff])    

    res = linprog(c, A_ub = linprog_A, b_ub = linprog_B, bounds=x_y_bounds)
    #print(res)
    return res


def f(x1, x2):
    return 11*x1**2 - 10*x1*x2 - 168.133*x1 + 11*x2**2 - 140.4*x2  + 8383.15
        

def f_doted(x):
    x1 = x[0]
    x2 = x[1]

    return f(x1, x2)


def grad_f(x1, x2):
    df_dx1 = 22*x1 - 168.133 - 10*x2
    df_dx2 = 22*x2 - 140.4 - 10*x1
    return [df_dx1, df_dx2]


def frank_wolfe(x0, max_iter=10, tol = 1e-5):
    x = np.array(x0)

    F_last = 0
    
    default_points = list()
    gradient_vectors = list()
    grad_optimized_points = list()
    grad_optimized_values = list()
    lambdas = list()
    specified_points = list()
    specified_values = list()
    
    

    for i in range(max_iter):
        print("\nFrank-Wolfe: Iteration", i)
        print("default point: ", x)
        default_points.append(x)
        
        gradient = grad_f(x[0], x[1])
        gradient_vectors.append(gradient)
        print("gradient: ", gradient)
        
        grad_optimization = linprog_minimization(gradient[0], gradient[1])

        if not grad_optimization.success:
            print("Линейная оптимизация не удалась")
            break

        grad_optimized_point = np.array(grad_optimization.x)

        grad_optimized_points.append(grad_optimized_point)
        print("gradient optimized point: ", grad_optimized_point)
        
        grad_optimized_values.append(grad_optimization.fun)  
        print("gradient optimized value: ", grad_optimization.fun)


        lambda_symbol = symbols("lambda")
        x1 = simplify(x[0] + lambda_symbol*(grad_optimized_point[0] - x[0]))
        x2 = simplify(x[1] + lambda_symbol*(grad_optimized_point[1] - x[1]))
        g_x = simplify(11*x1**2 - 10*x1*x2 - 168.133*x1 + 11*x2**2 - 140.4*x2  + 8383.15)

        diff_g_x = diff(g_x)

        lambda_sol = solveset(diff_g_x, lambda_symbol).args[0]
        print("specified lambda:", lambda_sol)
        
        
        lamda = float(lambda_sol)

        x_ = x + lamda*(grad_optimized_point - x)
        specified_value = f_doted(x_)
        
        specified_values.append(specified_value)
        print("specified function value: ", specified_value)
        
        
        
        if abs(abs(specified_value) - F_last) < tol:
            print()
            print("---")
            print("Breaking: abs(function_difference) < tolerance")
            print("\ttolerance: ", tol)
            print("\tlast_function:", F_last)
            print("\tspecified_function:", specified_value)
            print("\tABS(function_difference): ", abs(abs(specified_value) - F_last))
            print("---")
            print()
            break
  
        
        F_last = abs(specified_value)

        
        if np.linalg.norm(x - x_) < tol:
            print()
            print("---")
            print("Breaking: linalg.norm < tolerance")
            print("\ttolerance: ", tol)
            print("\tnorm: ", np.linalg.norm(x - x_))
            print("---")
            print()
            break
        
        x = x_

        specified_points.append(x)
        print("specified point: ", x)


    return default_points, gradient_vectors, grad_optimized_points, grad_optimized_values, lambdas, specified_points, specified_values 


def print_all_results_from_frank_wolfe(x0, max_iter, tol):
    default_points, gradient_vectors, grad_optimized_points, grad_optimized_values, lambdas, specified_points, specified_values = frank_wolfe(x0, max_iter, tol)
    print("\n\n")
    print("--RESULTS--")
    print(f"default points ({len(default_points)} values): ", default_points)
    print(f"gradient vectors ({len(gradient_vectors)} values): ", gradient_vectors)
    print(f"gradient optimized points ({len(grad_optimized_points)} values): ", grad_optimized_points)
    print(f"gradient optimized values ({len(grad_optimized_values)} values): ", grad_optimized_values)
    print(f"lambdas ({len(lambdas)} values): ", lambdas)
    print(f"specified points ({len(specified_points)} values)", specified_points)
    print(f"specified values ({len(specified_values)} values)", specified_values)


def drawing1():
    'Нарисовали область D'

    plt.title("Область D")
    
    x = np.linspace(graphic_borders[0], graphic_borders[1], 400)
   
    y1 = (2*n - x)  # из x + y >= 26
    y2 = (x - n) / 2  # из x - 2y <= 13
    y3 = (3 * x + 2*n) / 2  # из -3x + 2y <= 26

    plt.plot(x, y1, label=f'x + y >= {2*n}', color='green')
    plt.plot(x, y2, label=f'x - 2y <= {n}', color='red')
    plt.plot(x, y3, label=f'-3x + 2y <= {2*n}', color='blue')

    y_uppest = graphic_borders[1]
    y_lowest = graphic_borders[0]

    # Заливаем области, удовлетворяющие неравенствам
    plt.fill_between(x, y1, y_uppest, color='green', alpha=0.1)
    plt.fill_between(x, y2, y_uppest, color='red', alpha=0.1)
    plt.fill_between(x, y_lowest, y3, color='blue', alpha=0.1)


    plt.axvline(x=4*n, color="black", linestyle="-.", label=f"0<x<{4*n}")
    plt.axhline(y = 3*n, color="black", linestyle='-.', label=f"0<y<{3*n}")

    plt.fill_between(x, 3*n, y_lowest, color='gray', alpha=0.2)
    plt.fill_between(x, y_uppest, y_lowest, where=(x<=4*n), color='gray', alpha=0.2)


def drawing2():
    '''
    Нарисовать максимизированные критерии на нарисованной области
    '''
    
    drawing1()

    plt.title("Максимизированные критерии")

    x = np.linspace(graphic_borders[0], graphic_borders[1], 400)

    maximized1 = linprog_maximization(1, 1)
    maximized2 = linprog_maximization(-3, 1)
    maximized3 = linprog_maximization(1, -3)

    point1 = maximized1.x
    point2 = maximized2.x
    point3 = maximized3.x

    res1 = -(maximized1.fun)
    res2 = -(maximized2.fun)
    res3 = -(maximized3.fun)

    
    f1 = res1-x  
    f2 = res2+3*x 
    f3 = (x-res3)/3

    plt.plot(x, f1, label=f'f1(x)=x + y = {round(res1, 4)}', color='yellow')
    plt.scatter(point1[0], point1[1], label=f"F*_1[{point1}]", color='yellow', s=60)
    plt.plot(x, f2, label=f'f2(x)=-3x+y = {round(res2, 4)}', color='orange')
    plt.scatter(point2[0], point2[1], label=f"F*_2[{point2}]", color='orange', s=60)
    plt.plot(x, f3, label=f'f3(x)=x -3y = {round(res3, 4)}', color='purple')
    plt.scatter(point3[0], point3[1], label=f"F*_3[{point3}]", color='purple', s=60)



def drawing3(iterations = 1000):
    '''
    Нарисует результаты большого количества итераций Франк-Вульфа
    '''
    x0 = [26, 13]
    tolerance = 1e-5

    
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'yellow', 'pink']
    c_len = len(colors)
    
    plt.figure(figsize=(20, 12))
    drawing1()
    plt.title(f"Алгоритм Франк-Вульфа на большом количестве итераций ({iterations})")

    default_points, gradient_vectors, grad_optimized_points, grad_optimized_values, lambdas, specified_points, specified_values = frank_wolfe(x0, max_iter=iterations, tol=tolerance)

    x = np.linspace(graphic_borders[0], graphic_borders[1], 400)

    '''
        for i in range(1, 10):
            default_point = default_points[i]
            plt.scatter(x=default_point[0], y=default_point[1], label=f'X_{i}[{round(default_point[0], 6)}, {round(default_point[1], 6)}], P(X_{i}) = {round(f_doted(default_point), 6)}', color=colors[i%c_len])

        for i in range(len(default_points)-100, len(default_points)):
            default_point = default_points[i]
            plt.scatter(x=default_point[0], y=default_point[1], label=f'X_{i}[{round(default_point[0], 6)}, {round(default_point[1], 6)}], P(X_{i}) = {round(f_doted(default_point), 6)}', color=colors[i%c_len])
    '''
    for i in range(1, 10):
        default_point = default_points[i]
        plt.scatter(x=default_point[0], y=default_point[1], label=f'X_{i}[{round(default_point[0], 6)}, {round(default_point[1], 6)}], P(X_{i}) = {round(f_doted(default_point), 6)}', color=colors[i%c_len])
    
    for i in range(len(default_points)-7, len(default_points)):
        default_point = default_points[i]
        plt.scatter(x=default_point[0], y=default_point[1], label=f'X_{i}[{round(default_point[0], 6)}, {round(default_point[1], 6)}], P(X_{i}) = {round(f_doted(default_point), 6)}', color=colors[i%c_len])



    

def cyclic_drawing_frank_wolfe(x0, iterations, tolerance):
    iterations = iterations+1
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'yellow', 'pink']
    c_len = len(colors)
    for j in range(1, iterations):
        print("Drawing Frank-Wolfe: Iteration ", j)
        plt.figure(figsize=(20, 12))
        
        drawing1()

        plt.title(f"Алгоритм Франк-Вульфа, итерация {j}")


        default_points, gradient_vectors, grad_optimized_points, grad_optimized_values, lambdas, specified_points, specified_values = frank_wolfe(x0, max_iter=j, tol=tolerance)

        x = np.linspace(graphic_borders[0], graphic_borders[1], 400)

        
        for i in range(len(default_points)):
            default_point = default_points[i]
            gradient = gradient_vectors[i]
            
            gradient_optimized_point = grad_optimized_points[i%2]
            
            specified_point = specified_points[i]
            specified_value = specified_values[i]

            next_gradient = grad_f(specified_point[0], specified_point[1])
            
            plt.scatter(x=default_point[0], y=default_point[1], label=f'X_{i}[{round(default_point[0], 3)}, {round(default_point[1], 3)}], P(X_{i}) = {round(f_doted(default_point), 3)}', color=colors[i%c_len])

            
            if i == len(default_points)-1:
                plt.scatter(x=specified_point[0], y=specified_point[1], label=f"X_{i+1}[{round(specified_point[0], 3)}, {round(specified_point[1], 3)}], P(X_{i+1}) = {round(specified_value, 4)}", color=colors[(i+1)%c_len])
                
                plt.scatter(x = gradient_optimized_point[0], y = gradient_optimized_point[1], label = f"grad_optimized_point[{i}]", alpha=0.3, s=70, color=colors[i%c_len])

                y = -next_gradient[0]*(x-specified_point[0])/next_gradient[1] + specified_point[1]
                y1 = next_gradient[1]*(x-default_point[0])/next_gradient[0] + default_point[1]
                
                plt.plot(x, y, alpha=0.3, color=colors[i%c_len], label=f'line[{i}]')
                plt.plot(x, y1, alpha=0.6, color="gray", label=f'grad_optimization_line[{i}]')


                plt.plot([default_point[0], specified_point[0]], [default_point[1], specified_point[1]], linestyle='--', color=colors[i%c_len])

                plt.quiver(default_point[0], default_point[1], -gradient[0]/graphic_borders[1], -gradient[1]/graphic_borders[1], alpha=0.6, color='gray', label=f'grad(P(X_{i}))[{round(-gradient[0], 3)}, {round(-gradient[1])}]')
        
        plt.legend(loc = 'upper right', fontsize='small')
        plt.xlim(graphic_borders[0], graphic_borders[1])
        plt.ylim(graphic_borders[0], graphic_borders[1])
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.axhline(0, color='black',linewidth=1.5)
        plt.axvline(0, color='black',linewidth=1.5)
        
        plt.grid()
        plt.show()






def generate_graphics(drawer, iterations=1000):
    drawer(iterations)

    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend(loc = 'lower right', fontsize='small')
    
    plt.axhline(0, color='black',linewidth=1.5)
    plt.axvline(0, color='black',linewidth=1.5)
    
    plt.xlim(*graphic_borders)
    plt.ylim(*graphic_borders)

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    n = 13

    #linprog_values
    linprog_A = [[-1, -1], [1, -2], [-3, 2]] # не редактировать
    linprog_B = [-2*n, n, 2*n] # не редактировать
    x_y_bounds = [(0, 4*n), (0, 3*n)] # не редактировать

    graphic_borders = [-n, 6*n] # не редактировать

    minimal_lambda = 0.01 #чем меньше, тем больше итераций нужно для остановки по function difference
    iterations = 1000
    
    

    # принимает только функции drawing(1-3)
    generate_graphics(drawing3, iterations)

    
    #cyclic_drawing_frank_wolfe([26, 13], 5, 1e-5)



    


