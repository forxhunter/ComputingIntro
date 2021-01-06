'''
Xenia and Ringroad
can only move clockwise
one house one unit of time
'''
n, m = list(map(int, input().split(' ')))
tasks = list(map(int,input().split(' ')))
steps = 0
current_po = 1
for task in tasks:
    if task >= current_po:
        steps += (task-current_po)

    else:
        steps += (task + n - current_po)
    current_po = task
print(steps)