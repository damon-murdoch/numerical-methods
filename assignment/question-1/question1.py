import math.h


def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.15*x + 1.2


def opt_h(e, M):
    return 3 * math.sqrt((3*e)/M)


def central_difference(f):
    def df(x, h=0.1e-5):
        return (f(x+h/2)-f(x-h/2))/h
    return df

