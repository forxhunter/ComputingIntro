'''
C. Number of Ways
binary search/brute force/data structures/dp/two pointers, 1700,
https://codeforces.com/problemset/problem/466/C
'''

n = int(input())
integers = list(map(int, input().split(' ')))

total = 0
suml = sum(integers)
# can be equally divided
if suml % 3 == 0 and n >= 3:
    onethird = suml // 3
    twothird = onethird * 2
    sums = 0
    count1 = 0
    count2 = 0
    for i in range(n-1):
        sums += integers[i]
        if sums == twothird:
            total += count1
        if sums == onethird:
            count1 += 1
print(total)

