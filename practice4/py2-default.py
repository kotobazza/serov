import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt



def solve1(n):
    c = [3, -1]  
    A = [[1, 2], [-2, -1]] 
    b = [4*n, -n] 
    bounds = [(0, 2*n), (0, 1.5*n)] 


    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    #print(res)
    return res

def solve2(n, fun):
    c = [-1, -1]  

    A_ub = [[1, 2], [-2, -1], [3, -1]] 
    b_ub = [4*n, -n, -fun]  

    bounds = [(0, 2*n), (0, 1.5*n)] 

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    #print(res)
    return res

def solve3(n, fun1, fun2):
    c = [-1, 3]  

    A_ub = [[1, 2], [-2, -1], [3, -1], [-1, -1]]  
    b_ub = [4*n, -n, -fun1, fun2]  

    bounds = [(0, 2*n), (0, 1.5*n)] 

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    #print(res)
    return res



def create_graphics0(n):
    '''Рисует область D'''

    x = np.linspace(-0.25*n, 3*n, 1000)
    x_linspace = y_linspace = np.array([-0.25*n, 2.5*n])

    d_bound1 = (4*n - x) / 2
    d_bound2 = n - 2*x

    x_bounds = np.array([0, 2.5*n])
    y_bounds = np.array([0, 2.5*n])

    plt.plot(x, d_bound1, label=f'x1 + 2x2 <= {4*n}')
    plt.plot(x, d_bound2, label=f'2x1 + x2 >= {n}')

    y_lowest = -0.25*n
    y_uppest = 3*n

    # Заполним области неравенств
    plt.fill_between(x, d_bound1, y_lowest, where=(x + 2*d_bound1 <= 4*n), color='yellow', alpha=0.1)
    
    plt.fill_between(x, d_bound2, y_uppest, where=(2*x + d_bound2 >= n), color='yellow', alpha=0.1)

    plt.fill_between(x, 0, 1.5*n, where = (x>=0) & (x <= 2*n), color ='red', alpha=0.4)
    
    
    
    plt.fill_between(x, d_bound1, y_lowest, color='yellow', alpha=0.2)
    plt.fill_between(x, d_bound2, y_uppest, color='yellow', alpha=0.2)

    plt.axhline(y = 1.5*n, color = 'red', linestyle='-.', label=f'0<=x1<={1.5*n}')
    plt.axvline(x = 2*n, color = 'red', linestyle='--', label=f'0<=x2<={2*n}')

    # Границы x и y
    plt.xlim(x_linspace)
    plt.ylim(y_linspace)


def create_graphics1(n):
    '''Рисует решение 1 подзадачи на области D'''

    x = np.linspace(-0.25*n, 3*n, 1000)
    x_linspace = y_linspace = np.array([-0.25*n, 2.5*n])

    d_bound1 = (4*n - x) / 2
    d_bound2 = n - 2*x

    x_bounds = np.array([0, 2.5*n])
    y_bounds = np.array([0, 2.5*n])

    plt.plot(x, d_bound1, label=f'x1 + 2x2 <= {4*n}')
    plt.plot(x, d_bound2, label=f'2x1 + x2 >= {n}')

    y_lowest = -0.25*n
    y_uppest = 3*n

    # Заполним области неравенств
    plt.fill_between(x, d_bound1, y_lowest, where=(x + 2*d_bound1 <= 4*n), color='yellow', alpha=0.1)
    
    plt.fill_between(x, d_bound2, y_uppest, where=(2*x + d_bound2 >= n), color='yellow', alpha=0.1)

    plt.fill_between(x, 0, 1.5*n, where = (x>=0) & (x <= 2*n), color ='red', alpha=0.2)
    
    plt.fill_between(x, d_bound1, y_lowest, color='yellow', alpha=0.2)
    plt.fill_between(x, d_bound2, y_uppest, color='yellow', alpha=0.2)

    plt.axhline(y = 1.5*n, color = 'red', linestyle='-.', label=f'0<=x1<={1.5*n}')
    plt.axvline(x = 2*n, color = 'red', linestyle='--', label=f'0<=x2<={2*n}')

    
    #Решение задачи 1
    res1 = solve1(n)
    x_res, y_res = res1.x
    fun1 = -res1.fun


    y1 = fun1 + 3*x
    plt.plot(x, y1, label=f'-3x1+x2 = {fun1}', color='green')

    plt.scatter(x = x_res, y=y_res, label = f'P2 ({x_res}, {y_res})', color='red', s=50, marker='o')

    plt.quiver(0, 0, -3, 1, angles='xy', scale_units='xy', scale=1, color='green', label='G2 (-3, 1)')
    
    # Границы x и y
    plt.xlim(x_linspace)
    plt.ylim(y_linspace)


def create_graphics2(n):
    '''Рисует область D1'''
    x = np.linspace(-0.25*n, 3*n, 1000)
    x_linspace = y_linspace = np.array([-0.25*n, 2.5*n])

    d_bound1 = (4*n - x) / 2
    d_bound2 = n - 2*x

    x_bounds = np.array([0, 2.5*n])
    y_bounds = np.array([0, 2.5*n])

    plt.plot(x, d_bound1, label=f'x1 + 2x2 <= {4*n}')
    plt.plot(x, d_bound2, label=f'2x1 + x2 >= {n}')

    y_lowest = -0.25*n
    y_uppest = 3*n

    # Заполним области неравенств
    plt.fill_between(x, d_bound1, y_lowest, where=(x + 2*d_bound1 <= 4*n), color='yellow', alpha=0.1)
    
    plt.fill_between(x, d_bound2, y_uppest, where=(2*x + d_bound2 >= n), color='yellow', alpha=0.1)

    plt.fill_between(x, 0, 1.5*n, where = (x>=0) & (x <= 2*n), color ='yellow', alpha=0.1)
    
    plt.fill_between(x, d_bound1, y_lowest, color='yellow', alpha=0.2)
    plt.fill_between(x, d_bound2, y_uppest, color='yellow', alpha=0.2)

    plt.axhline(y = 1.5*n, color = 'red', linestyle='-.', label=f'0<=x1<={1.5*n}')
    plt.axvline(x = 2*n, color = 'red', linestyle='--', label=f'0<=x2<={2*n}')

    
    #Решение задачи 1
    delta_f2 = 2
    res1 = solve1(n)
    x_res, y_res = res1.x
    fun1 = -res1.fun - delta_f2
    y1 = fun1 + 3*x

    # Представление области D1
    plt.plot(x, y1, label=f'-3x1+x2 >= {fun1}', color='green')
    plt.fill_between(x, y1, 1.5*n, where = (x >= 0) & (x <= delta_f2/3), color='red', alpha=0.5)
    plt.fill_between(x, y1, y_uppest, where = (y_uppest > y1), color='orange', alpha=0.2)



    plt.quiver(0, 0, -3, 1, angles='xy', scale_units='xy', scale=1, color='green', label='G2 (-3, 1)')
    
    # Границы x и y
    plt.xlim(x_linspace)
    plt.ylim(y_linspace)


def create_graphics3(n):
    '''Рисует решение 2 подзадачи на области D1'''
    x = np.linspace(-0.25*n, 3*n, 1000)
    x_linspace = y_linspace = np.array([-0.25*n, 2.5*n])

    d_bound1 = (4*n - x) / 2
    d_bound2 = n - 2*x

    x_bounds = np.array([0, 2.5*n])
    y_bounds = np.array([0, 2.5*n])

    plt.plot(x, d_bound1, label=f'x1 + 2x2 <= {4*n}')
    plt.plot(x, d_bound2, label=f'2x1 + x2 >= {n}')

    y_lowest = -0.25*n
    y_uppest = 3*n

    # Заполним области неравенств
    plt.fill_between(x, d_bound1, y_lowest, where=(x + 2*d_bound1 <= 4*n), color='yellow', alpha=0.1)
    
    plt.fill_between(x, d_bound2, y_uppest, where=(2*x + d_bound2 >= n), color='yellow', alpha=0.1)

    plt.fill_between(x, 0, 1.5*n, where = (x>=0) & (x <= 2*n), color ='yellow', alpha=0.1)
    
    plt.fill_between(x, d_bound1, y_lowest, color='yellow', alpha=0.2)
    plt.fill_between(x, d_bound2, y_uppest, color='yellow', alpha=0.2)

    plt.axhline(y = 1.5*n, color = 'red', linestyle='-.', label=f'0<=x1<={1.5*n}')
    plt.axvline(x = 2*n, color = 'red', linestyle='--', label=f'0<=x2<={2*n}')

    
    #Решение задачи 1
    delta_f2 = 2
    res1 = solve1(n)
    x_res, y_res = res1.x
    fun1 = -res1.fun - delta_f2
    y1 = fun1 + 3*x

    # Представление области D1
    plt.plot(x, y1, label=f'-3x1+x2 >= {fun1}', color='green')
    plt.fill_between(x, y1, 1.5*n, where = (x >= 0) & (x <= delta_f2/3), color='red', alpha=0.5)

    #Решение задачи 2
    res2 = solve2(n, fun1)
    x_res2, y_res2 = res2.x
    fun2 = -res2.fun
    y2 = fun2 - x

    plt.plot(x, y2, label = f'x1+x2 = {fun2}', color='red')
    plt.scatter(x = x_res2, y = y_res2, label = f'P1 ({x_res2}, {y_res2})', color='red', s=50, marker='o')

    plt.quiver(0, 0, -3, 1, angles='xy', scale_units='xy', scale=1, label='G2 (-3, 1)', color='green') #f2
    plt.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1, label='G1 (1, 1)', color='red') #f1
    # Границы x и y
    plt.xlim(x_linspace)
    plt.ylim(y_linspace)


def create_graphics4(n):
    '''Рисует область D2'''
    x = np.linspace(-0.25*n, 3*n, 1000)
    x_linspace = y_linspace = np.array([-0.25*n, 2.5*n])

    d_bound1 = (4*n - x) / 2
    d_bound2 = n - 2*x

    x_bounds = np.array([0, 2.5*n])
    y_bounds = np.array([0, 2.5*n])

    plt.plot(x, d_bound1, label=f'x1 + 2x2 <= {4*n}')
    plt.plot(x, d_bound2, label=f'2x1 + x2 >= {n}')

    y_lowest = -0.25*n
    y_uppest = 3*n

    # Заполним области неравенств
    plt.fill_between(x, d_bound1, y_lowest, where=(x + 2*d_bound1 <= 4*n), color='yellow', alpha=0.1)
    
    plt.fill_between(x, d_bound2, y_uppest, where=(2*x + d_bound2 >= n), color='yellow', alpha=0.1)

    plt.fill_between(x, 0, 1.5*n, where = (x>=0) & (x <= 2*n), color ='yellow', alpha=0.1)
    
    plt.fill_between(x, d_bound1, y_lowest, color='yellow', alpha=0.2)
    plt.fill_between(x, d_bound2, y_uppest, color='yellow', alpha=0.2)

    plt.axhline(y = 1.5*n, color = 'red', linestyle='-.', label=f'0<=x1<={1.5*n}')
    plt.axvline(x = 2*n, color = 'red', linestyle='--', label=f'0<=x2<={2*n}')

    
    #Решение задачи 1
    delta_f2 = 2
    res1 = solve1(n)
    x_res, y_res = res1.x
    fun1 = -res1.fun - delta_f2
    y1 = fun1 + 3*x

    # Представление области D1
    plt.plot(x, y1, label=f'-3x1+x2 >= {fun1}', color='green')
    plt.fill_between(x, y1, 1.5*n, where = (x >= 0) & (x <= delta_f2/3), color='red', alpha=0.5)

    #Решение задачи 2
    delta_f1 = 3
    res2 = solve2(n, fun1)
    x_res2, y_res2 = res2.x
    fun2 = 17.5
    y2 = fun2 - x

    # Представление области D2

    plt.plot(x, y2, label = f'x1+x2 >= {fun2}', color='red')
    plt.fill_between(x, y2, y_uppest, where = (x+ y2 >= fun2), color='orange', alpha=0.2)
    
    
    plt.quiver(0, 0, -3, 1, angles='xy', scale_units='xy', scale=1, label='G2 (-3, 1)', color='green')
    plt.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1, label='G1 (1, 1)', color='red') #f1
    # Границы x и y
    plt.xlim(x_linspace)
    plt.ylim(y_linspace)


def create_graphics5(n):
    '''Рисурет решение 3 подзадачи на области D2'''
    x = np.linspace(-0.25*n, 3*n, 1000)
    x_linspace = y_linspace = np.array([-0.25*n, 2.5*n])

    d_bound1 = (4*n - x) / 2
    d_bound2 = n - 2*x

    x_bounds = np.array([0, 2.5*n])
    y_bounds = np.array([0, 2.5*n])

    plt.plot(x, d_bound1, label=f'x1 + 2x2 <= {4*n}')
    plt.plot(x, d_bound2, label=f'2x1 + x2 >= {n}')

    y_lowest = -0.25*n
    y_uppest = 3*n

    # Заполним области неравенств
    plt.fill_between(x, d_bound1, y_lowest, where=(x + 2*d_bound1 <= 4*n), color='yellow', alpha=0.1)
    
    plt.fill_between(x, d_bound2, y_uppest, where=(2*x + d_bound2 >= n), color='yellow', alpha=0.1)

    plt.fill_between(x, 0, 1.5*n, where = (x>=0) & (x <= 2*n), color ='yellow', alpha=0.1)
    
    plt.fill_between(x, d_bound1, y_lowest, color='yellow', alpha=0.2)
    plt.fill_between(x, d_bound2, y_uppest, color='yellow', alpha=0.2)

    plt.axhline(y = 1.5*n, color = 'red', linestyle='-.', label=f'0<=x1<={1.5*n}')
    plt.axvline(x = 2*n, color = 'red', linestyle='--', label=f'0<=x2<={2*n}')

    
    #Решение задачи 1
    delta_f2 = 2
    res1 = solve1(n)
    x_res, y_res = res1.x
    fun1 = -res1.fun - delta_f2
    y1 = fun1 + 3*x

    # Представление области D1
    plt.plot(x, y1, label=f'-3x1+x2 >= {fun1}', color='green')
    plt.fill_between(x, y1, 1.5*n, where = (x >= 0) & (x <= delta_f2/3), color='red', alpha=0.5)

    #Решение задачи 2
    delta_f1 = 3
    res2 = solve2(n, fun1)
    x_res2, y_res2 = res2.x
    fun2 = 17.5
    y2 = fun2 - x

    # Представление области D2

    plt.plot(x, y2, label = f'x1+x2 >= {fun2}', color='red')
    plt.fill_between(x, y2, y_uppest, where = (x+ y2 >= fun2), color='yellow', alpha=0.2)

    # Решение задачи 3

    res3 = solve3(n, fun1, fun2)
    x_res3, y_res3 = res3.x
    fun3 = -res3.fun
    y3 = (fun3 - x)/(-3)

    plt.plot(x, y3, label=f'x1-3x2 = {fun3}', color='blue')
    plt.scatter(x = x_res3, y = y_res3, label = f'P3 ({x_res3}, {y_res3})', color='red', s=60, marker='o')
 


    plt.quiver(0, 0, -3, 1, angles='xy', scale_units='xy', scale=1, label='G2 (-3, 1)', color='green')
    plt.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1, label='G1 (1, 1)', color='red') #f1
    plt.quiver(0, 0, 1, -3, angles='xy', scale_units='xy', scale=1, label='G3 (1, -3)', color='blue') #f3
    # Границы x и y
    plt.xlim(x_linspace)
    plt.ylim(y_linspace)

if __name__ == "__main__":
    create_graphics0(13)
        
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend(loc = 'upper right')
    plt.title("Решение подзадачи 3")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)

    plt.grid(True)
    plt.show()