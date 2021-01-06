'''
non decreasing length of a sequence a
'''

n = int(input())
array = list(map(int, input().split(' ')))
max_length = 1
length = 1
last = array[0]
for i in range(1, n):
    if array[i] >= last:
        length += 1

    else:
        if length > max_length:
            max_length = length
        length = 1

    last = array[i]

if length > max_length:
    max_length = length
print(max_length)