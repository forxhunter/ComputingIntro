'''
Vasya the Hipster
red blue socks
simple one
'''
socks = list(map(int, input().split(' ')))
socks.sort()
diff = socks[0]
left = socks[1]-socks[0]
same = left//2
#output format
s = str(diff) + ' ' + str(same)
print(s)
