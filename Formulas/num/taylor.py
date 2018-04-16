

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)


# taylor(f,x,h,e): double
# f: Function to utilise
# x,y: variables
# e: Acceptable error %


def taylor(f, x, h, e):
    return f, x, h, e
