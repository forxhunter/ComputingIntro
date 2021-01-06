'''
as little as possible letters should be changed
same length to lower case
'''

word = input()
count_low = 0
count_hig = 0
for letter in word:
    if letter.islower() == True:
        count_low += 1
count_hig = len(word) - count_low

if count_hig <= count_low:
    print(word.lower())
else:
    print(word.upper())
