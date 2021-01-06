'''
Dubstep
'''
import re
string = input()
pattern = r'(WUB)+'
string = re.sub(pattern, ' ', string)
string = string.strip()
print(string)