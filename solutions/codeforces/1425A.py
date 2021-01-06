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
# to save answer together
ans = []
def optimum(left):

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
        if left ==4:
            greedy_first += 3
            greedy_second += 1
            left = 0

        elif (left //2) & 1:
            greedy_first += left // 2
            greedy_second += 1
            left = (left//2) - 1
        else:
            greedy_first += 1
            greedy_second += 1
            left -= 2

    ans.append([greedy_second+1,greedy_first][fs])
    #return [greedy_second+1,greedy_first][fs]
# find the answer


for gold in golds:
    if gold == 1:
        ans.append(1)
    else:
        optimum(gold)
print('\n'.join(map(str, ans)))