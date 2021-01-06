'''
Divisibility Problem
'''
t = int(input())

for i in range(t):
    a, b = list(map(int, input().split(' ')))
    integer = a // b
    left = a % b
    if left == 0:
        print(0)
    else:
        result = b - left
        print(result)
