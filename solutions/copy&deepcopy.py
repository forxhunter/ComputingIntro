import copy
a = [[1, 2], [5, 6]]
b = copy.deepcopy(a)
b[1][1] = -1
print(b)
print(a)
