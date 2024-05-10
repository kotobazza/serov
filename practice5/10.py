import numpy as np

def f1(x, y):
    return x+y

def f2(x, y):
    return -3*x+y

def f3(x, y):
    return x-3*y


a = np.array([13.471, 12.603])

print(f1(a[0], a[1]))
print(f2(a[0], a[1]))
print(f3(a[0], a[1]))