'''
580C. Kefa and Park
dfs and similar, graphs, trees, 1500
http://codeforces.com/problemset/problem/580/C
'''
n, m = map(int, input().split())
cat = 1
empty = 0
status = [-1] + list(map(int, input().split()))
tree = {}

for _ in range(n-1):
    s, e = map(int, input().split())
    if s not in tree:
        tree[s] = [e]
    else:
        tree[s].append(e)
    if e not in tree:
        tree[e] = [s]
    else:
        tree[e].append(s)

count = 0

# graph: dict type, s: start node code
def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s[0])

    result = 0
    while (len(queue) > 0):
        vertex, current_c = queue.pop(0)
        if current_c <= m:
            nodes = graph[vertex]
            # if is the restaurant(leaves)
            if vertex != s[0] and len(nodes) == 1:
                result += 1
            else:
            # if not leaves, add the children
                for w in nodes:
                    if w not in seen:
                        # if not exceed max cat met

                        if status[w] == empty:
                            queue.append([w, 0])
                        elif current_c+status[w] <= m:
                            queue.append([w, current_c+status[w]])

                        seen.add(w)


    return result


count = BFS(tree, [1, status[1]])
print(count)