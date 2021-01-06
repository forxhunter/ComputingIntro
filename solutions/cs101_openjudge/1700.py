'''
1756:八皇后
http://cs101.openjudge.cn/practice/1756
1. a=b1b2...b8，其中bi为相应摆法中第i行皇后所处的列数
2.已经知道8皇后问题一共有92组解（即92个不同的皇后串）
output: 给出一个数b，要求输出第b个串。串的比较是这样的：皇后串x置于皇后串y之前，当且仅当将x视为整数时比y小。
思路：
找到全部92个解，然后排序，然后查表输出
version2: 合并了一些重复的部分
'''
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
# 计数，第几个棋盘
count = 0
# 栈，用于存放之前层的数字
temp_queen = ''


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


# 输出结果的函数
def output(queen_str):
    table_output = []
    for i in range(8):
        table_output.append([0] * 8)
    for i in range(8):
        j = int(queen_str[i])-1
        table_output[j][i] = 1
    print('No. '+str(count))
    for i in range(8):
        print(*table_output[i], sep=' ')


# 每层的方法
def layer(c_col, last_table):
    global temp_queen
    global count
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
                count += 1
                output(temp_queen+str(i))


# 找到全部可能的序列并存进queens[],从第一行向后排可能性
# row 1

for i1 in range(1, 9):
    table1 = copy.deepcopy(table_blank)
    table1[1][i1] = 1
    temp_queen += str(i1)
    # row 2
    layer(2, table1)
    temp_queen = temp_queen[:-1]


