'''
Anton and Letters
'''
origin = input()
origin = origin[1:-1]

letters = origin.split(', ')

sets = set(letters)

n = len(sets)
if '' in sets:
    n -= 1
print(n)
