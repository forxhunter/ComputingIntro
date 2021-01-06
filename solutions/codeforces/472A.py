'''
Design Tutorial: Learn from Math
12 10^6
'''
import math
n = int(input())
if n % 2 == 0:
    a = 4
    b = n - a
    print(str(a)+' '+str(b))
else:
    initial = n - 4
    jud = False
    a = 0
    for odd in range(9, initial+1, 2):
        for j in range(2, int(math.sqrt(odd))+1):
            if odd % j == 0:
                jud = True
                break
        if jud == True:
            a = odd
            break
    print(str(a)+' '+str(n-a))