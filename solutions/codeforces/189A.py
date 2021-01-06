'''
cut ribbon
After the cutting each ribbon piece should have length a, b or c.
After the cutting the number of ribbon pieces should be maximum.
!!!solve the optimization problem
ax+by+cz = n
max. x+y+z
c·max= n +(c-a)x+(c-b)y
#Note:
PyPi accepted
'''
n, a, b, c = list(map(int, input().split(' ')))
count = 0

xmax = n // a
ymax = n // b


for x in range(xmax+1):

    for y in range(ymax+1):
        z = (n-a*x-b*y)/c
        if z < 0:
            break
        result = x + y + z
        if result > count and result % 1 == 0:
            count = result



print(int(count))