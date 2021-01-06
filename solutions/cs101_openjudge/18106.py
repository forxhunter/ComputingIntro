'''
matrices
螺旋矩阵，http://cs101.openjudge.cn/practice/18106/
'''
n = int(input())
#原始为(n,m)的矩阵
board = []
wall = -1
#最上面多加一层
board.append([wall for x in range(n+2)])
for y in range(n):
    board.append([wall]+[ 0 for x in range(n)]+[wall])
#最后面多加一层
board.append([wall for x in range(n+2)])

k = 1
x = 1
y = 1
direction = [[0, 1], [1, 0],[0,-1],[-1,0]]
index_d = 0
sume = n**2
while k != sume+1:

    if board[x][y] == 0:
        board[x][y] = k
        k += 1

    else:
        x -= direction[index_d][0]
        y -= direction[index_d][1]
        index_d = (index_d + 1) % 4
    # move
    x += direction[index_d][0]
    y += direction[index_d][1]

for i in range(1,n+1):
    board[i] = board[i][1:-1]
    print(*board[i], sep=' ')