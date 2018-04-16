from math import *

def ffdd(f, x, h):
    return (f(x+h)-f(x))/h


def bfdd(f, x, h):
    return (f(x)-f(x-h))/h


def cfdd(f, x, h):
    return (f(x+h)-f(x-h))/(h*2)


def absolute_error(tval, eval):
    return abs((tval-eval)/tval)*100


def relative_error(pval, cval):
    return abs((cval-pval)/cval)*100


def second_derivative(f, x ,h):
    return (f(x+h)-2*f(x)+f(x-h))/h**2


def rche(f, x, h):
    return cfdd(f,x,h/2)+(cfdd(f,x,h/2)-(cfdd(f,x,h)))/3


def trapz(f,x,b,a):
    return (b-a)*((f(a)/2)+(f(b)/2))


def maptz(f,a,b,n):
    h = (b-a)/n
    x = a
    sum = f(x)
    for i in range(1,n-1,1):
        x += h
        sum += 2*(f(x))
    sum += f(b)
    return (b-a)*sum/(2*n)

def smp13(f,x,b,a):
    return (((b-a)/2)/3)*(f(a)+4*f(x)+f(b))


def map13(f,a,b,n):
    h = (b-a)/n
    ret = h/3;
    o = 0
    for i in range(1,n-1,2):
        o += f((b-a)/n)
    e = 0
    for i in range(2,n-2,2):
        e += f((b-a)/n)
    I = a + (4*o)+(2*e)+b


if __name__ == '__main__':

    a=0
    b=0.8
    n=10

    def f1(x):
        return 0.2 + 25*x - 200*x**4 + 400*x**5

    def f(x):
        return 0.2*x + 12.5*x**2 - 40*x**5 + 66*x**6

    print(maptz(f1,a,b,n),f(.8))