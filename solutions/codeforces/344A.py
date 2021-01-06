'''
trvial magnets
'''
n = int(input())
groups = 0
last = ''
for i in range(n):
    present = input()
    if last != present:
        groups += 1
        last = present
print(groups)