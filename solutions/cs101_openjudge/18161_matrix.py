
# matrix 1
m1, n1 = [int(x) for x in input().split()]
matrix1 = []
for _ in range(m1):
    matrix1.append([int(x) for x in input().split()])

# matrix 2
m2, n2 = [int(x) for x in input().split()]
matrix2 = []
for _ in range(m2):
    matrix2.append([int(x) for x in input().split()])

# matrix 1
m3, n3 = [int(x) for x in input().split()]
matrix3 = []
for _ in range(m3):
    matrix3.append([int(x) for x in input().split()])
if n1 != m2 or m1 != m3 or n2 != n3:
    print('Error!')
else:
    result = []
    for i in range(m1):
        temp = []
        for j in range(n2):
            ele = 0
            for add in range(m2):
                ele += matrix1[i][add]*matrix2[add][j]

            ele += matrix3[i][j]
            temp.append(ele)
        result.append(temp)

    for i in range(m1):
        print(*result[i], sep=' ')