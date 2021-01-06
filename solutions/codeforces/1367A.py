'''
Short Substrings
'''
t = int(input())
for ini in range(t):
    code = input()
    temp = code[1:-1]
    output = code[0]
    for i in range(0, len(temp), 2):
        output += temp[i]
    output += code[-1]
    print(output)