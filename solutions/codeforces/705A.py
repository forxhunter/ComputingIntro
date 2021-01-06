'''
Hulk
'''

n = int(input())

start = 'I'
end = 'it'
result = start
for i in range(n):
    if i % 2 == 0:
        result += ' ' + 'hate'
    else:
        result += ' ' + 'love'

    if n != 1 and i < n-1:
        result += ' ' + 'that' + ' ' + start

result += ' ' + end
print(result)