'''
723A. The New Year: Meeting Friends
implementation, math, sorting, 800, https://codeforces.com/problemset/problem/723/A
The New Year: Meeting Friends
'''
place = list(map(int, input().split(' ')))
place.sort()
move = place[2]-place[0]
print(move)