# Newton's method

def solve(function = "x**3-5*x**2+10*x-80", a=4.0):

    # a = float(input())

    def f(x):
        return eval(function)

    def df(x, dx):
        return (f(x + dx) - f(x)) / dx

    while abs(f(a)) > 1e-10:
        if df(a, 1e-10) == 0:
            a -= 1e-10
        else:
            a = a - f(a) / df(a, 1e-10)
    return a


ans = solve()
print("{:.9f}".format(ans))