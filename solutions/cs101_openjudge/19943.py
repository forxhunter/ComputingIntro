'''
19943:图的拉普拉斯矩阵(matrix)
http://cs101.openjudge.cn/practice/19943/

'''
node, edge = [int(i) for i in input().split()]
matrix = []
for i in range(node):
    matrix.append([0] * node)
for fake_i in range(edge):
    i, j = [int(i) for i in input().split()]
    matrix[i][i] += 1
    matrix[j][j] += 1
    matrix[i][j] = -1
    matrix[j][i] = -1

for i in range(node):
    print(*matrix[i], sep=' ')