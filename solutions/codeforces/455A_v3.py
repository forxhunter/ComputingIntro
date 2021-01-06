"""
Boredom
v0.1 错误：直接统计了所有可能的数值a和对应的count，忽视了要求中只影响a-1,a+1两个数，而误认为影响了小于a和大于a的两个数
v1 超时，利用空间复杂度解决时间复杂度问题。重写find counts
v2  a: use iteration instead of recursion, and save each result in a array
    b: pre calc sum in find_counts to avoid multiple calc
    仍然超时，采用动态规划的方法
v3 DP solved
"""
MAXN = 100001
n = int(input())
nums = [int(x) for x in input().split()]
cnt = [0] * MAXN
for x in nums:
    cnt[x] += 1
dp = [0] * MAXN
dp[1] = cnt[1]
ans = 0
for i in range(2, MAXN):
    dp[i] = max(dp[i - 1], dp[i - 2] + cnt[i] * i)
    ans = max(dp[i], ans)
print(ans)