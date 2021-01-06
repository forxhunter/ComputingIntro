'''
New Year and Hurry
interpretation:
partial sum of the array
'''





n, k = list(map(int, input().split(' ')))

total_min = 240 - k
answer = 0
used = 0
l = 0
while used < total_min and l < n:
    l += 1
    used += 5 * l

if used <= total_min:
    answer = l
elif used > total_min:
    answer = l -1

print(answer)

