import numpy as np
import matplotlib.pyplot as plt

print("Hello")
def define_colors(classes):
    t = ['g', 'y', 'r']
    return [t[i] for i in classes]

def plotter(limiter, dots_x, dots_y, classes):
    # Генерируем значения x и y
    x = np.linspace(0, limiter*2, 400)
    y = np.linspace(0, limiter*2, 400)
    X, Y = np.meshgrid(x, y)

    # Условие для круга
    circle = (X-limiter)**2 + (Y-limiter)**2 - limiter**2 <= 0

    # Условие для прямой
    line = -X + Y - limiter <= 0

    # Условие для полуплоскости
    half_plane = X + Y - limiter*2 >= 0

    # Закрасим пересечение всех условий
    intersection = circle & line & half_plane


    dots_colors = define_colors(classes)

    



    # Строим график

    plt.title('Распределение решений на кластеры')

    #plt.title('Возможные решения')

    plt.contourf(X, Y, intersection, alpha=0.5, cmap='Paired')
    plt.plot(x, limiter + np.sqrt(limiter**2 - (x-limiter)**2), 'r-', label=f'(x-{limiter})**2 + (y-{limiter})**2 <= {limiter}**2')
    plt.plot(x, (limiter - np.sqrt(limiter**2 - (x-limiter)**2)), 'r-')
    plt.plot(x, x+limiter, 'g-', label=f'-x+y <= {limiter}')
    plt.plot(x, limiter*2-x, 'b-', label=f'x+y >= 2*{limiter}')
    plt.xlim(0, limiter*2)
    plt.ylim(0, limiter*2)
    plt.xlabel('x')
    plt.ylabel('y')

    t = []

    for i in range(len(dots_colors)):
        if dots_colors[i] not in t:
            t.append(dots_colors[i])
            plt.scatter(dots_x[i], dots_y[i], c=dots_colors[i], label=f"K{classes[i]+1}")
        else:
            plt.scatter(dots_x[i], dots_y[i], c=dots_colors[i])
        

    plt.legend(loc = 'lower left')
    plt.show()

    

