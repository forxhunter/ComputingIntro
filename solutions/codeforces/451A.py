'''
Game With sticks
Akshat move first, Malvika moves next

idea: treat it as a matrx m*n
Akshat lose if odd round left 0*0 matrix
Malvika lose if even round left 0*0 matrix
each round minus 1 for both m and n
'''
n, m = list(map(int, input().split(' ')))
number = min(n, m)

if number % 2 == 0:
    print('Malvika')
else:
    print('Akshat')
