'''
18182:打怪兽(sorting,math)
url:http://cs101.openjudge.cn/practice/18182/
'''
n = int(input())

for fake_i in range(n):
    nums, max_per, monstor = list(map(int, input().split(' ')))
    methods = []

    for i in range(nums):
        temp = list(map(int, input().split(' ')))
        methods.append(temp)

    methods.sort(key=(lambda x: (x[0],-x[1])))
    # dump the over kills
    count = 0
    current = 1
    killed_blood = 0
    for kill in methods:
        if current == kill[0]:
            count += 1
        else:
            count = 1
            current = kill[0]

        if count <= max_per:
            killed_blood += kill[1]
        else:
            continue

        # if dead
        if killed_blood >= monstor:
            print(kill[0])
            break
    if killed_blood < monstor:
        print('alive')





