'''
Puzzles: array sorting and comparing
'''
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split(' ')))
array.sort()

least = array[-1] - array[0]
for i in range(m-n+1):
    temp = array[i+n-1] - array[i]
    if temp < least:
        least = temp
print(least)