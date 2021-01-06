'''
C Woodcutters
dp greedy
'''
n = int(input())
trees = []

falled = [0] * n
# 0 not fall, 1 for left, 2 for right
for i in range(n):
    # add the tree
    temp_tree = list(map(int, input().split()))
    trees.append(temp_tree)
    if i == 0:
        # the zeroth tree
        falled[0] = 1
    elif i == n-1:
        falled[i] = 2
        if falled[i-1] == 0 and trees[i-1][1] < temp_tree[0]-trees[i-1][0]:
            falled[i-1] = 2
    else:
        # 1->n-1
        sep = temp_tree[0] - trees[i-1][0]
        height = temp_tree[1]
        pre_height = trees[i-1][1]
        if falled[i-1] == 0 and pre_height + height < sep:
            falled[i-1] = 2
            falled[i] = 1
        elif falled[i-1] == 0 and pre_height < sep:
            falled[i-1] = 2
        elif height < sep:
            falled[i] = 1

count = n - falled.count(0)
print(count)


