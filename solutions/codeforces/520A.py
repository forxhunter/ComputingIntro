'''
Pangram
'''
n = int(input())
word = input()
letters = set(word.lower())
if len(letters) == 26:
    print('YES')
else:
    print('NO')