'''
12560:生存游戏(matrix)
url:http://cs101.openjudge.cn/practice/12560/
'''
n, m = list(map(int, input().split(' ')))
matrix = []
for fake_i in range(n):
    line = list(map(int, input().split(' ')))
    matrix.append(line)

# define neighbours
neighbours = ((1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1) )
new_m = []

for i in range(n):
    temp = []
    for j in range(m):
        count = 0
        for neighbour in neighbours:
            dx, dy = neighbour
            x = i + dx
            y = j + dy
            if count <= 3:
                if x>=0 and x< n and y >=0 and y < m:
                    if matrix[x][y] == 1:
                        count += 1
            else:
                #more than 3, have to die
                break
        # judge the state of ele in next state
        if matrix[i][j]==1 and (count == 2 or count == 3):
            temp.append(1)
        elif matrix[i][j]==0 and count == 3:
            temp.append(1)
        else:
            temp.append(0)
     # all line updated, add to the new matrix
    new_m.append(temp)
# give the output
for i in range(n):
    print(*new_m[i], sep=' ')
