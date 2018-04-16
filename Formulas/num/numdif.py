import numpy


def ffdd(f, x, h):
    return (f(x + h) - f(x)) / h


def bfdd(f, x, h):
    return (f(x) - f(x + h)) / h


def cfdd(f, x, h):
    return (f(x + h) - f(x - h)) / 2 * h


def richardson(f, x, n, h):
    d = numpy.array([[0] * (n + 1)] * (n + 1), float)
    for i in range(n + 1):
        d[i, 0] = cfdd(f, x, h)
        powOf4 = 1
        for j in range(1, i+1):
            powOf4 = 4 * powOf4
            d[i, j] = d[i, j-1] + (d[i, j-1]-d[i-1, j-1]) / (powOf4-1)
        h = 0.5 * h
    return d
