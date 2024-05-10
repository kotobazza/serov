import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt


def calc_linprog(n):
    
    A_default = [[-1, -1], [1, -2], [-3, 2]]
    B_default = [-n*2, n, 2*n]
    

    A_appended_var2 = [[-1, -1], [-1, 3]]
    B_appended_var2 = [-5*n, 6*n]
    
    c_var2 = np.array([3, -1])



    A = np.array(A_default + A_appended_var2)
    B = np.array(B_default + B_appended_var2)
    c = c_var2 
    
    x_y_bounds = [(1, 4*n), (1, 3*n)]

    res = linprog(c, A_ub = A, b_ub = B, bounds=x_y_bounds)
    print(res)
    return res

def create_graphics(n):

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    plot1, plot2 = axs

    create_plot1(plot1, n)
    create_plot2(plot2, n)

    for ax in axs:
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(False)
        ax.set_xlim(left=0, right=7*n)
        ax.set_ylim(bottom=0, top=4*n)
        
        ax.legend(loc='lower right')

    axs[0].set_title("Область D")
    axs[1].set_title("Область D с волной")

    plt.tight_layout()
    plt.show()

def create_plot2(plot, n):

    res = calc_linprog(n)
    
    result_point = res.x
    optimized_function = res.fun


    
    x = np.linspace(0, 7*n, 400)
    
    y1 = (2*n - x) 
    y2 = (x - n) / 2 
    y3 = (3*x + 2*n) / 2 

    gamma1 = 5*n
    gamma2 = -6*n

    
    f1 = gamma1 - x # x + y >= 5n
    f2 = -optimized_function + 3*x
    f3 = (x - gamma2) / 3 # x - 3y >= -6n

    f2_ = -39 + 3*x
    f2__ = -65 + 3*x
    f2___ = -13*9 + 3*x
    f2____ = -13*10.5 + 3*x

    


    plot.axhline(y = 3*n, color = 'red', linestyle='-.', label=f'0<x<{3*n}')
    plot.axvline(x = 4*n, color = 'red', linestyle='--', label=f'0<y<{4*n}')

    
    
    
    plot.plot(x, f1, label=f'(f1) x + y >= {gamma1}')
    
    plot.plot(x, f3, label=f'(f3) x - 3y >= {gamma2}')
    plot.plot(x, f2, label=f'(f2) -3x + y = {-optimized_function}')
    # plot.plot(x, f2_, label=f'(f2) -3x + y = {-39}')
    # plot.plot(x, f2__, label=f'(f2) -3x + y = {-65}')
    # plot.plot(x, f2___, label=f'(f2) -3x + y = {-(13*9)}')
    # plot.plot(x, f2____, label=f'(f2) -3x + y = {-(13*10.5)}')
    

    

    
    y_values = [y1, y2, y3, f1, f3]

    y_lower = 0
    y_upper = 4*n

    plot.scatter(x = result_point[0], y = result_point[1], label=f'P ({result_point[0]}:{result_point[1]})', color='red', s=50, marker='o')

    plot.fill_between(x, f1, y_upper, color='green', alpha=0.2)
    #plot.fill_between(x, f2, y_upper, color='green', alpha=0.2)
    plot.fill_between(x, f3, y_lower, color='green', alpha=0.2)

    x_c = np.linspace(0, 4*n, 400)
    y_c = np.linspace(0, 3*n, 400)
    X, Y = np.meshgrid(x_c, y_c)

    # неравенства для отображения областей
    ineq1 = X + Y >= 2*n
    ineq2 = X - 2*Y <= n
    ineq3 = -3*X + 2*Y <= 2*n

    ineqf1 = X + Y >= gamma1
    #ineqf2 = -3*X + Y >= 
    ineqf3 = X - 3*Y >= gamma2

    
    # область D
    combined_inequality1 = ineq1 & ineq2 & ineq3
    plot.imshow(combined_inequality1, extent=(0, 4*n, 0, 3*n), origin='lower', cmap='Oranges', alpha=0.5)
    
    # область D с волной
    combined_inequality2 = ineq1 & ineq2 & ineq3 & ineqf1 & ineqf3 # & ineqf2
    plot.imshow(combined_inequality2, extent=(0, 4*n, 0, 3*n), origin='lower', cmap='Greens', alpha=0.5)
    
def create_plot1(plot, n):

    x = np.linspace(0, 7*n, 400)

    y1 = (2*n - x)
    y2 = (x - n) / 2
    y3 = (3*x + 2*n) / 2


    plot.axhline(y = 3*n, color = 'red', linestyle='-.', label=f'0<x<{3*n}')
    plot.axvline(x = 4*n, color = 'red', linestyle='--', label=f'0<y<{4*n}')


    plot.plot(x, y1, label=f'x + x >= {2*n}')
    plot.plot(x, y2, label=f'x - 2y <= {n}')
    plot.plot(x, y3, label=f'-3x + 2y <= {2*n}')


    y_values = [y1, y2, y3]

    y_lower = 0

    y_upper = 4*n

    plot.fill_between(x, y1, y_upper, color='yellow', alpha=0.1)
    plot.fill_between(x, y2, y_upper, color='yellow', alpha=0.1)
    plot.fill_between(x, y3, y_lower, color='yellow', alpha=0.1)
    plot.fill_between(x, 4*n, 0, color='red', alpha=0.1)
    plot.fill_between(x, 0, y_upper, color='red', alpha=0.1)


    x_c = np.linspace(0, 4*n, 400)
    y_c = np.linspace(0, 3*n, 400)
    X, Y = np.meshgrid(x_c, y_c)

    # неравенства для отображения области
    ineq1 = X + Y >= 2*n
    ineq2 = X - 2*Y <= n
    ineq3 = -3*X + 2*Y <= 2*n

    combined_inequality = ineq1 & ineq2 & ineq3
    plot.imshow(combined_inequality, extent=(0, 4*n, 0, 3*n), origin='lower', cmap='Oranges', alpha=0.5)




if __name__ == '__main__':
    n=13
    create_graphics(n)


