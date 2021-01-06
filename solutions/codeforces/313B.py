'''
313B. Ilya and Queries
dp, 1300, https://codeforces.com/contest/313/problem/B
'''
sequence = input()
length = len(sequence)
m = int(input())


dp = [0] * length
if sequence[0] == sequence[1]:
    dp[1] = 1

for i in range(1, length-1):
    if sequence[i] == sequence[i+1]:
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = dp[i]
# print(dp)
ans = []
for fake_i in range(m):
    l, r = [int(x) for x in input().split()]

    ans.append(dp[r-1]-dp[l-1])
print('\n'.join(map(str,ans)))