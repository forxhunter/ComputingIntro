'''
flagstonea*a, square n*m, least number needed to cover the square. cant break the flagstones.
input: n m a
output: the number needed
'''
m, n, a = input().split()
m = int(m)
n = int(n)
a = int(a)
countn = n // a
countm = m // a
if n % a != 0:
    countn += 1
if m % a != 0:
    countm += 1

print(countm * countn)