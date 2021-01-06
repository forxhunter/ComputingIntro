"""
read i words.
follow the rule, abbr word strictly longer than 10 letters
input: i  and words, each sits one line
output: abbr. each in one line
"""

i = int(input())
words = []
abbrs = []
for num in range(i):
    word = input()
    words.append(word)

for word in words:
    if len(word) <= 10 :
        abbrs.append(word)
    else:
        abbr = word[0] + str(len(word)-2) + word[-1]
        abbrs.append(abbr)

for abbr in abbrs:
    print(abbr)