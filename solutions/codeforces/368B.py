'''
368B. Sereja and Suffixes
data structures/dp, 1100, https://codeforces.com/problemset/problem/368/B
'''
n, m = [int(x) for x in input().split()]
array = [0] + [int(x) for x in input().split()]
dp_distinct = [-1] * n + [1]
read_set = {array[-1]}
answers = []
for i in range(n-1, 0, -1):
    if array[i] not in read_set:
        read_set.add(array[i])
        dp_distinct[i] = dp_distinct[i+1]+1
    else:
        dp_distinct[i] = dp_distinct[i+1]

for fake_i in range(m):
    l = int(input())
    answers.append(dp_distinct[l])

print('\n'.join(map(str,answers)))

