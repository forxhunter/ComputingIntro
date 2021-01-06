'''
even odds
'''
n, k =list(map(int, input().split(' ')))
output = 0
half_n = n // 2
if n % 2 == 0:
    if k <= half_n:
        output = 2 * k - 1
    else:
        output = 2 * (k - half_n)
else:
# n%2 ==1
    if k <= half_n + 1:
        output = 2 * k - 1
    else:
        output = 2 * (k - half_n - 1)

print(output)