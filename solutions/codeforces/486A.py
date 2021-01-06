'''
Calculating Function
'''
n = int(input())
result = 0
if n % 2 == 0:
    result = n // 2
else:
    result = n // 2 - n
print(result)