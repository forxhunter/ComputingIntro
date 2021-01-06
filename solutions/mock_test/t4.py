

land = 1
empty = 0
neighbour = [[0, -1], [0, 1], [1, 0], [-1, 0]]


count = 0
n, m = list(map(int, input().split()))
area = []

area.append([empty]*(m+2))


for __ in range(n):
    temp = [empty]
    temp.extend(([int(x) for x in input().split()]))
    temp.append(empty)
    area.append(temp)
area.append([empty]*(m+2))

# search
for row in range(1,n+1):
    for column in range(1,m+1):
        if area[row][column] != empty:
            arount_w = 0
            for dx, dy in neighbour:
                temp_x = row + dx
                temp_y = column + dy

                if area[temp_x][temp_y] == empty:
                    arount_w += 1
            count += arount_w

print(count)
