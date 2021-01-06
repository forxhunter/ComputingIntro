import copy

queens = []
# 开头加入-1，使得下标与后续输入值对齐
queens.append(-1)

# 建立一个搜索棋盘8*8,有保护圈
table_blank = []
table_blank.append([-1] * 10)
for fake_i in range(8):
    table_blank.append([-1] + [0] * 8 + [-1])
table_blank.append([-1] * 10)

# 判断函数
# 四个斜方向的判断矩阵
direct = [[1, 1], [-1, -1], [1, -1], [-1, 1]]


def check(table, row, column):
    jud = True
    if table[row].count(1) != 0:
        jud = False
    else:
        for i in range(1, 9):
            if table[i][column] == 1:
                jud = False
                break

        # 左上方斜线和右下方
        for dx, dy in direct:
            y = row
            x = column
            while table[y][x] != -1:
                if table[y][x] == 1:
                    jud = False
                    return jud
                x += dx
                y += dy
    return jud

# 栈，用于存放之前层的数字
temp_queen = ''

# 每层的方法
def layer(c_col, last_table):
    #当前行数c_col，上一行的table
    global temp_queen
    if c_col != 8:
        for i in range(1, 9):
            if check(last_table, c_col, i) is True:
                table = copy.deepcopy(last_table)
                table[c_col][i] = 1
                temp_queen += str(i)
                layer(c_col+1,table)
                temp_queen = temp_queen[:-1]
    else:
        for i in range(1, 9):
            if check(last_table, 8, i) is True:
                queens.append(temp_queen+str(i))

# 找到全部可能的序列并存进queens[],从第一行向后排可能性
# row 1
for i1 in range(1, 9):
    table1 = copy.deepcopy(table_blank)
    table1[1][i1] = 1
    temp_queen += str(i1)
    # row 2
    layer(2, table1)
    temp_queen = temp_queen[:-1]
'''
for q in queens:
    print(q)
'''
# 读取数据并开始输出
n = int(input())

for i in range(n):
    num = int(input())
    print(queens[num])
