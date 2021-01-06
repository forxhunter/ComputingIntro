'''
Greedy Algorithm
You are given a rectangular board of M×N squares. Also you are given an unlimited number of standard domino pieces of 2×1 squares. You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:

1. Each domino completely covers two squares.

2. No two dominoes overlap.

3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions.
input: m n
output: max number of domino
'''
# read and convert to integer
m, n = list(map(int, input().split(' ')))

length = m
width = n
number = 0
if length < width:
    length = n
    width = m

while length != 1 or width != 1:
    if length < width:
        mid = width
        width = length
        length = mid

    if length >= 2:
        number += width * (length // 2)
        length = length % 2
        if length == 0:
            break

print(number)