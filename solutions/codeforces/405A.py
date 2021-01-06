'''
gravity flips
'''
n = int(input())
columns = list(map(int, input().split(' ')))
columns.sort()
output = str(columns[0])
for ele in columns[1:]:
    output += ' ' + str(ele)
print(output)