'''
4 Values whose Sum is 0，
binary search, http://cs101.openjudge.cn/practice/2442
'''
n = int(input())
a = [0] *(n+1)
b = [0] *(n+1)
c = [0] *(n+1)
d = [0] *(n+1)
combined_ab = {}
for i in range(1,n+1):
    a[i], b[i], c[i], d[i] = [int(x) for x in input().split()]

for i in range(1, n+1):
    for j in range(1, n+1):
        if a[i] + b[j] not in combined_ab.keys():
            combined_ab[a[i]+b[j]] = 1
        else:
            combined_ab[a[i] + b[j]] += 1
count = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if -(c[i]+d[j]) in combined_ab.keys():
            count += combined_ab[-(c[i]+d[j])]
print(count)

