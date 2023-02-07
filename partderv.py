import numpy as py
import matplotlib.pyplot as plt
import sympy as sy
from sympy.tensor.array import derive_by_array

x,y = sy.symbols('x y')
f = 3*x + 4*y


# dx = sy.diff(f,x)
# dy = sy.diff(f,y)

gradient = derive_by_array(f, (x, y))

print(f)
# print('Partial derivative x = ', dx)
# print('Partial derivative y = ', dy)
print('Gradient [x,y] = ', gradient)


