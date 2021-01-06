'''
熄灯问题，
brute force, http://cs101.openjudge.cn/practice/1813
'''
import copy
n = 5
m = 6
off = 0
on = 1
change = [[0, -1], [0, 1], [1, 0], [-1, 0], [0, 0]]
#原始为(n,m)的矩阵
lights = []
#最上面多加一层
lights.append([-1 for x in range(m+2)])
for y in range(n):
    lights.append([-1]+[int(x) for x in input().split()]+[-1])
#最后面多加一层
lights.append([-1 for x in range(m+2)])


# several functions
def flip(ele):
    if ele == 1:
        return 0
    elif ele == 0:
        return 1
    else:
        return ele
#iterator for first line operator list
class Operator1:
    def __init__(self, start, stop):  # 迭代起始、终止位
        self.value = start
        self.stop = stop

    def __iter__(self):     # 返回自身的迭代器
        return self

    def __next__(self):     # 返回下一个元素
        if self.value > self.stop:   # 结尾时抛出异常
            raise (StopIteration)
        item = '{0:b}'.format(self.value)

        item = (6-len(item))*'0' + item
        result = [int(x) for x in item]
        self.value += 1
        return result
# brutal
eles = [0, 1]

for operate1 in Operator1(0, 63):
    operate1 = [-1] + operate1 + [-1]
    #initiate operator matrix
    operates = []
    operates.append([-1] * (m + 2))
    operates.append(operate1)

    for _ in range(n-1):
        operates.append([-1]+[0]*m+[-1])
    operates.append([-1]*(m+2))

    # get a deep copy to avoid outer change
    matrix = copy.deepcopy(lights)
    # first line
    for j in range(1, m + 1):
        if operates[1][j] == 1:
            for dx,dy in change:
                matrix[1+dx][j+dy] = flip(matrix[1+dx][j+dy])
    # if satisfy
    for i in range(2, n+1):
        for j in range(1, m+1):
            if matrix[i-1][j] == on:
                operates[i][j] = 1
                for dx, dy in change:
                    matrix[i + dx][j + dy] = flip(matrix[i + dx][j + dy])
    on_light = 0
    for i in range(i, n+1):
        on_light += matrix[i].count(on)
    if on_light == 0:
        for i in range(1, n + 1):
            operates[i] = operates[i][1:-1]
            print(*operates[i], sep=' ')
        break