'''
Input

The first line contains integer n (1≤n≤50) — the number of stones on the table.

The next line contains string s, which represents the colors of the stones.
We'll consider the stones in the row numbered from 1 to n from left to right.
Then the i-th character s equals "R", if the i-th stone is red, "G", if it's green and "B", if it's blue.
Output

Print a single integer — the answer to the problem.
'''
n = int(input())
colors = input()
taken = 0
previous = '0'
for stone in colors:
    if stone == previous:
        taken += 1
    else:
        previous = stone

if previous == '0':
    print(0)
else:
    print(taken)