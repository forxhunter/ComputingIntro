'''
implementation
校门外的树， http://cs101.openjudge.cn/practice/1810
'''
length, sectors = [int(x) for x in input().split()]
tress = [1] * (length+1)
for _ in range(sectors):
    start, end = [int(x) for x in input().split()]
    for i in range(start, end+1):
        tress[i] = 0
print(tress.count(1))