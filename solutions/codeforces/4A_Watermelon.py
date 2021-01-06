'''
input w , decide whether w can be divided into two even number.
'''
w = int(input())
if w ==2:
    print("NO")
elif w % 2 == 0:
    print("YES")
else:
    print("NO")