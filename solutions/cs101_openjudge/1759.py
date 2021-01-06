'''
1759: 最长上升子序列
dp, http://cs101.openjudge.cn/practice/1759
'''
n = int(input())
array = [int(x) for x in input().split()]
dp = [1] * n
for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))