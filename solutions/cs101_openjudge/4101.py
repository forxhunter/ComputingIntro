k = int(input())
black = 'b'
red = 'r'
empty = '#'
neighbour = [[0, -1], [0, 1], [1, 0], [-1, 0]]


def dfs(r, c, area, visited, color):
    visited[r][c] = 1
    stack = []
    stack.append([r, c])
    while len(stack) != 0:
        x, y = stack.pop()
        for dx, dy in neighbour:
            temp_x = x + dx
            temp_y = y + dy

            if area[temp_x][temp_y] == color and visited[temp_x][temp_y] == 0:
                visited[temp_x][temp_y] = 1
                stack.append([temp_x, temp_y])
    return
for _ in range(k):
    c_black = 0
    c_red = 0
    n = int(input())
    area = []
    visited =[]
    area.append(empty*(n+2))
    visited.append([0] * (n + 2))

    for __ in range(n):
        area.append(empty+input()+empty)
        visited.append([0] * (n + 2))
    area.append(empty*(n+2))
    visited.append([0] * (n + 2))

    # search
    for row in range(1,n+1):
        for column in range(1,n+1):
            if area[row][column] != empty and visited[row][column] == 0:
                color = black
                if area[row][column] == black:
                    c_black += 1
                else:
                    color = red
                    c_red += 1
                # dfs
                dfs(row,column,area=area,visited=visited,color=color)


    print(c_red,c_black,sep=' ')
