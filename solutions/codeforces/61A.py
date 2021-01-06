'''
Ultra-Fast Mathematician
'''
string1 = input()
string2 = input()
string3 = ''
for ele1, ele2 in zip(string1,string2):
    if ele1 == ele2:
        string3 += '0'
    else:
        string3 += '1'
print(string3)