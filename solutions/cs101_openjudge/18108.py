'''
18108:池塘数目（cs101-2016 期末机考备选）
matrix,dfs, http://cs101.openjudge.cn/practice/18108/
'''

water = 'W'
direct = [[1,0],[1,1],[1,-1],[0,1],[0,-1],[-1,-1],[-1,0],[-1,1]]
group = int(input())
for fake_i in range(group):
    n, m = [int(x) for x in input().split()]
    land = []
    land_status = []
    land.append('-'*(m+2))
    land_status.append([-1] * (m + 2))
    for fake_j in range(n):
        land.append('-'+input()+'-')
        land_status.append([-1]+[0]*m+[-1])

    land.append('-'*(m+2))
    land_status.append([-1] * (m + 2))
    # count
    ponds = 0
    stack = []

    for i in range(1,n+1):
        for j in range(1,m+1):
            if land[i][j] == water and land_status[i][j] == 0:
                ponds += 1
                stack.append([i, j])
                land_status[i][j] = 1
                while len(stack) != 0:
                    y, x = stack.pop()
                    for dy, dx in direct:
                        if land[y+dy][x+dx] == water and land_status[y+dy][x+dx] == 0:
                            stack.append([y+dy, x+dx])
                            land_status[y+dy][x+dx] = 1


    print(ponds)