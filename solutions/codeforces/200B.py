'''
Drinks
'''
n = int(input())

arrays = list(map(int, input().split(' ')))
result = sum(arrays)

print('{:.12f}'.format(result/n))