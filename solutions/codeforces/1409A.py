'''
Yet Another Two Integers Problem
'''
t = int(input())
for ini in range(t):
    a, b = list(map(int, input().split(' ')))
    delta = abs(a-b)
    moves = 0
    if delta == 0:
        moves = 0
    elif delta <= 10:
        moves = 1
    else:
        moves = delta // 10
        if delta % 10 != 0:
            moves += 1
    print(moves)