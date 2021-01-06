
def func(x):
    function = x ** 3- 5*x**2+10*x-80
    return function


left = 0
right = 10

delta = func(right) -func(left)
mid = (left + right) / 2
while delta > 10**(-10):

    if func(mid) < 0:
        left = mid
    elif func(mid) > 0:
        right = mid
    else:
        break
    delta = func(right) - func(left)
    mid = (left + right) / 2
print('%.9f' % mid)