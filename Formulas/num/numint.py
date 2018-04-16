def trapz(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2


def multi_app_trapz(f, a, b, n):
    ret = (b - a) / (2 * n)
    x = f(a)
    for i in range(1, n - 1, 1):
        x += f(((b - a) / (2 * n)) * i)
    x += f(b)
    return ret * x


def simp_13(f, a, b):
    return (b - a) * (f(a) + 4 * f((b + a) / 2) + f(b)) / 6


def multi_app_simp_13(f, a, b, n):
    ret = (b - a) / (3 * n)
    x = f(a)
    for i in range(1, n - 1, 2):
        x += 4 * f(((b - a) / (2 * n)))
    for i in range(2, n - 2, 2):
        x += 2 * f(((b - a) / (2 * n)))
    x += f(b)
    return ret * x

def simp_38(f,a,b):
    x1 = ((b-a)/b)*2
    x2 = ((b-a)/b)*3
    return (b-a)*((f(a)+3*f(x1)+3*f(x2)+f(b))/8)

