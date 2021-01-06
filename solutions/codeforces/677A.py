'''
Input

The first line of the input contains two integers n and h (1≤n≤1000, 1≤h≤1000) — the number of friends and the height of the fence, respectively.

The second line contains n integers ai (1≤ai≤2h), the i-th of them is equal to the height of the i-th person.
Output

Print a single integer — the minimum possible valid width of the road.
'''
n, h = list(map(int, input().split(' ')))
heights = list(map(int, input().split(' ')))
width = 0
for person in heights:
    if person <= h:
        width += 1
    else:
        width += 2
print(width)
