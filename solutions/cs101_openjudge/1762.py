'''
1762:数字三角形
dp, http://cs101.openjudge.cn/practice/1762/
'''
n = int(input())
triangle = []
for fake_i in range(n):
    triangle.append([int(x) for x in input().split()])
#dp for each small triangles maximum
dp = []
for fake_i in range(n-1):
    dp.append([0]*(fake_i+1))
dp.append(triangle[-1])

for i in range(n-2,0-1,-1):
    for j in range(0,i+1):
        max_below = max(dp[i+1][j],dp[i+1][j+1])
        dp[i][j] = triangle[i][j] + max_below

print(dp[0][0])


