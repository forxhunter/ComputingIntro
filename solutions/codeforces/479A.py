'''
expression
Brutal force
'''
numbers = []
adding = 0
multiply = 1
result = 0
for i in range(3):
    temp = int(input())
    adding += temp
    multiply *= temp
    numbers.append(temp)

if adding > multiply:
    result = adding
else:
    result = multiply

result1 = (numbers[0] + numbers[1]) * numbers[2]
result2 = numbers[0] * (numbers[1] + numbers[2])
if result1 > result:
    result = result1
if result2 > result:
    result = result2


print(result)
