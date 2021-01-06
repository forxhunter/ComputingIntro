'''
19942:二维矩阵上的卷积运算v0.2 (matrix)
http://cs101.openjudge.cn/practice/19942/
'''
m, n, p, q = [int(x) for x in input().split()]
# initialize and read the number
matrix = []
core = []
for _ in range(m):
    matrix.append([int(x) for x in input().split()])
for _ in range(p):
    core.append([int(x) for x in input().split()])


# convolution function
def convolution(x,y):
    ci = cj = 0
    result = 0
    for i in range(p):
        for j in range(q):
            result += matrix[x][y] * core[i][j]
            y += 1
        x += 1
        y -= q
    return result
# calculate
for i in range(m+1-p):
    temp_line = []
    for j in range(n+1-q):
        result = convolution(i, j)
        temp_line.append(result)
    print(*temp_line, sep=' ')


