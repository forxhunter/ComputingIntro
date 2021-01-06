'''
1425A. Arena of Greed
games, greedy, 1400
https://codeforces.com/problemset/problem/1425/A
'''
# get the input at once
t = int(input())

golds = []
for _ in range(t):
    golds.append(int(input()))
# save the solved puzzle
dp = {}
# save the special case when n == 4
dp[4] = [3, 1]
def optimum(n):
    left = n
    greedy_first = 0
    greedy_second = 0
    # if Chanek is first
    fs = True

    if left & 1 == 1:
        left -= 1
        fs = False

    while left:
        # for first man
        # dp
        if left in dp:
            greedy_first += dp[left][0]
            greedy_second += dp[left][1]
            left -= (dp[left][0]+dp[left][0])
            break
        else:
            if (left //2) & 1:
                greedy_first += left // 2
                greedy_second += 1
                left = (left//2) - 1
            else:
                greedy_first += 1
                greedy_second += 1
                left -= 2

    dp[n] = [greedy_first, greedy_second]
    return [greedy_second+1,greedy_first][fs]
# find the answer
ans = []

for gold in golds:
    if gold == 1:
        ans.append(1)
    else:
        ans.append(optimum(gold))

print(*ans,sep='\n')