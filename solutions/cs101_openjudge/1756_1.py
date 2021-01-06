'''
1756:八皇后
http://cs101.openjudge.cn/practice/1756
1. a=b1b2...b8，其中bi为相应摆法中第i行皇后所处的列数
2.已经知道8皇后问题一共有92组解（即92个不同的皇后串）
output: 给出一个数b，要求输出第b个串。串的比较是这样的：皇后串x置于皇后串y之前，当且仅当将x视为整数时比y小。
思路：
找到全部92个解，然后排序，然后查表输出
version1
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
        y = row
        x = column
        while table[y][x] != -1:
            if table[y][x] == 1:

                jud = False
                break
            x -= 1
            y -= 1
        y = row
        x = column
        while table[y][x] != -1:
            if table[y][x] == 1:
                jud = False
                break
            x += 1
            y += 1

        # 左下方斜线和 右上方
        y = row
        x = column
        while table[y][x] != -1:
            if table[y][x] == 1:
                jud = False
                break
            x -= 1
            y += 1
        y = row
        x = column
        while table[y][x] != -1:
            if table[y][x] == 1:
                jud = False
                break
            x += 1
            y -= 1

    return jud


# 找到全部可能的序列并存进queens[],从第一行向后排可能性
# row 1
for i1 in range(1, 9):
    table1 = copy.deepcopy(table_blank)
    table1[1][i1] = 1
    # row 2
    for i2 in range(1, 9):
        if check(table1, 2, i2) is True:
            table2 = copy.deepcopy(table1)
            table2[2][i2] = 1
            # row 3
            for i3 in range(1, 9):
                if check(table2, 3, i3) is True:
                    table3 = copy.deepcopy(table2)
                    table3[3][i3] = 1
                    # row 4
                    for i4 in range(1, 9):
                        if check(table3, 4, i4) is True:
                            table4 = copy.deepcopy(table3)
                            table4[4][i4] = 1
                            # row 5
                            for i5 in range(1, 9):
                                if check(table4, 5, i5) is True:
                                    table5 = copy.deepcopy(table4)
                                    table5[5][i5] = 1
                                    # row 6
                                    for i6 in range(1, 9):
                                        if check(table5, 6, i6) is True:
                                            table6 = copy.deepcopy(table5)
                                            table6[6][i6] = 1
                                            # row 7
                                            for i7 in range(1, 9):
                                                if check(table6, 7, i7) is True:
                                                    table7 = copy.deepcopy(table6)
                                                    table7[7][i7] = 1
                                                    # row 8
                                                    for i8 in range(1, 9):
                                                        if check(table7, 8, i8) is True:
                                                            queens.append(
                                                                str(i1) + str(i2) + str(i3) + str(i4) + str(i5) + str(
                                                                    i6) + str(i7) + str(i8))

n = int(input())


for i in range(n):
    num = int(input())
    print(queens[num])

