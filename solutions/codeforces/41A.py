'''
boring translation
'''

t = input()
s = input()
check_s = ''
for letter in t:
    check_s = letter + check_s

if check_s == s:
    print('YES')
else:
    print('NO')