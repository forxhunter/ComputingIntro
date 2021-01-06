'''
Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.
Input

A single line contains a non-empty word. This word consists of lowercase and uppercase English letters.
The length of the word will not exceed 103.
Output
a
Output the given word after capitalization.
'''
string = input()

first = string[0]
if first.isupper():
    print(string)
else:
    new_string = chr(ord(first) - 32) + string[1:]
    print(new_string)