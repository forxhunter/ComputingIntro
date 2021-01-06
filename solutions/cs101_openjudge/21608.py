
n = int(input())
## create graph
graph = {}
ids = set()

for _ in range(n):
    ln = input().split(' : ')
    u = int(ln[0])
    # u = int(ln[0].rstrip()) delte the right side empty space
    ids.add(u)
    if u not in graph:
        neighbours = [int(_) for _ in ln[1].split()]
        graph[u] = neighbours
'''
{53: [-1], 118: [119, 136, 137], 92: [107, 93, 102, 91], 102: [-1], 130: [66, 132, 135, 103]}
'''


def dfs_Non_recursion(graph, initial):
    # 字典结构的图graph
    # initial指的是初始id
    visited = [initial]
    stack = [initial]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.append(node)

        if node not in graph:
            stack.pop()
            continue

        remove_from_stack = True
        for nei in graph[node]:  # neighbour
            #mei you fang wen guo
            if nei not in visited:
                stack.append(nei)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited

## dfs_Non_recursion travel
maxp = []
for i in ids:
    dfs_path = dfs_Non_recursion(graph, i)
    if -1 in dfs_path:
        dfs_path.remove(-1)

    maxp.append(len(dfs_path))
    #print(len(bfs_path), bfs_path)
print(max(maxp))