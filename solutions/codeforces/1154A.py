'''
Restoring three numbers
solve the equations
2 important facts:
1. the largest number is always a+b+c
2. the rest number can be acquired by minus operation
'''
numbers = list(map(int, input().split(' ')))
numbers.sort()
s = ''
for i in range(3):
    s += str(numbers[-1]-numbers[i])
    if i != 2:
        s+= ' '

print(s)
