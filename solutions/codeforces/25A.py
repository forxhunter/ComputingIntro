'''
IQ test
'''
n = int(input())
numbers = list(map(int, input().split(' ')))
even = 0
odd = 0
first_eve = -1
first_odd = -1
for i in range(n):
    if numbers[i] % 2 == 0:
        even += 1
        if first_eve == -1:
            first_eve = i
    else:
        odd += 1
        if first_odd == -1:
            first_odd = i
    if even >= 2 and first_odd != -1:
        print(first_odd+1)
        break
    if odd >= 2 and first_eve != -1:
        print(first_eve+1)
        break