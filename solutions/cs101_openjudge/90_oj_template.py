n, m = map(int, input().split())
land = []
land_status = []
land.append([-1]*(m+2))
land_status.append([-1]*(m+2))
for fake_i in range(n):

    land.append([-1]+[int(x) for x in input().split()]+[-1])
    land_status.append([-1]+[0]*m+[-1])
land.append([-1]*(m+2))
land_status.append([-1]*(m+2))
max_length = 0
direct = [[0,1],[0,-1],[1,0],[-1,0]]


def dfs(i,j):
    if land_status[i][j]>0:
        return land_status[i][j]
    for dy, dx in direct:

        if land[i+dy][j+dx] != -1 and land[i+dy][j+dx] < land[i][j]:
            land_status[i][j] = max( land_status[i][j], dfs(i+dy, j+dx)+1 )
    return land_status[i][j]

for i in range(1, n+1):
    for j in range(1, m+1):
        max_length = max( max_length, dfs(i,j) )
print(max_length+1)