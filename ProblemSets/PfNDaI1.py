import sympy
from formulas import *

sympy.init_printing(use_unicode=True, wrap_line=False, no_global=True)

x,y,z = sympy.symbols('x y z')

def f(x):
    return x**2*sympy.cos(x)

d = sympy.diff(f(x),x)

print(d)