'''
trivial string problem
'''
codes = input()
valids = ['H', 'Q', '9']
test = 0
for valid in valids:
    if valid in codes:
        print('YES')
        test = 1
        break

if test == 0:
    print('NO')
