'''
check
'''
groups = [0, 0, 0, 0]
n = int(input())
data = input()
carsnum = 0
for i in range(4):
    groups[i] = data.count(str(i+1))

# deal with 4 people group
carsnum += groups[3]
groups[3] = 0
# deal with 2 people group
carsnum += groups[1] // 2
groups[1] %= 2

# deal with 1 and 3 people group
if groups[0] <= groups[2]:
    carsnum += groups[0]

    groups[2] -= groups[0]
    groups[0] = 0

    # deal with the 3 people group left
    carsnum += groups[2]
    if groups[1] != 0:
        carsnum += 1
else:
    carsnum += groups[2]
    groups[0] -= groups[2]
    groups[2] = 0

    # deal with the 1 people group left
    carsnum += groups[0] // 4
    groups[0] %= 4
    if groups[1] == 0:
        if groups[0] != 0:
            carsnum += 1
    else:
        # 2 people group has 1 group
        if groups[0] == 3:
            carsnum += 2
        else:
            carsnum += 1
print(carsnum)