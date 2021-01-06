'''
Remove Smallest

'''
t = int(input())
for ll in range(t):
    n = int(input())
    integers = set(map(int, input().split(' ')))
    integers = list(integers)
    integers.sort()
    for i in range(1,len(integers)):
        if abs(integers[i]-integers[i-1]) > 1:
            print('NO')
            break
    else:
        print('YES')