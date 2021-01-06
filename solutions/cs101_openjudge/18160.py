k = int(input())
chess = 'W'
empty = '.'
neighbour = [[0, -1], [0, 1], [1, 0], [-1, 0],[1,-1],[1,1],[-1,-1],[-1,1]]


def dfs(r, c, area, visited):
    mianji = 1
    visited[r][c] = 1
    stack = []
    stack.append([r, c])

    while len(stack) != 0:
        x, y = stack.pop()
        for dx, dy in neighbour:
            temp_x = x + dx
            temp_y = y + dy

            if area[temp_x][temp_y] == chess and visited[temp_x][temp_y] == 0:
                visited[temp_x][temp_y] = 1
                stack.append([temp_x, temp_y])
                mianji += 1
    return mianji
for _ in range(k):

    n, m = list(map(int,input().split()))
    area = []
    visited =[]
    area.append(empty*(m+2))
    visited.append([0] * (m + 2))
    current_max = 0
    for __ in range(n):
        area.append(empty+input()+empty)
        visited.append([0] * (m + 2))
    area.append(empty*(m+2))
    visited.append([0] * (m + 2))

    # search
    for row in range(1,n+1):
        for column in range(1,m+1):
            if area[row][column] != empty and visited[row][column] == 0:

                # dfs
                temp_mianji = dfs(row,column,area=area,visited=visited)
                if temp_mianji > current_max:
                    current_max = temp_mianji

    print(current_max)
