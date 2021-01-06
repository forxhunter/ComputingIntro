'''
Balanced Array
logic:
1. n=2, definitely can not
2. (n-1) %2 == 0, means if you substract 1 from each elements and
can not make the last one a odd number
3. (n-1) % 2 == 1, plausible, give the sequence
'''
t = int(input())
for ini in range(t):
    n = int(input())
    if n == 2:
        print('NO')
    elif (n//2-1) %2 == 0:
        print('NO')
    else:
        print('YES')
        for i in range(n//2):
            print((i+1)*2, end=' ')
        for i in range(n//2-1):
            print((i+1)*2-1, end=' ')
        print(n//2-1+1 +(n-1))
