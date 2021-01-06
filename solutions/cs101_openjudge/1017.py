'''
1017装箱问题
greedy
'''

while True:
    counts = list(map(int, input().split()))
    if counts.count(0) == 6:
        break
    else:

        packages_num = 0
        # for 6*6
        packages_num += counts[5]
        counts[5] = 0

        # for 5*5 with 1*1
        packages_num += counts[4]
        counts[0] -= counts[4] * 11
        # for 4*4 with 2*2
        packages_num += counts[3]
        counts[1] -= counts[3] * 5

        # for 3*3 with 2*2 and 1*1
        packages_num += counts[2]//4
        counts[2] %= 4
        if counts[2] != 0:
            packages_num += 1

            if counts[2] == 1:
                counts[1] -= 5
                counts[0] -= 7
            elif counts[2] == 2:
                counts[1] -= 3
                counts[0] -= 6
            elif counts[2] == 3:
                counts[1] -= 1
                counts[0] -= 5

        # find how to place the left
        # 2*2 left
        if counts[1] > 0:
            packages_num += counts[1] // 9
            counts[1] %= 9
            # if still have 2*2
            if counts[1] != 0:
                packages_num += 1
                counts[0] -= (9-counts[1]) * 4

        # 1*1 left
        # first fill the negative 2*2 place with 4 1*1
        if counts[1] < 0:
            counts[0] -= abs(counts[1]) * 4
        # 1*1 left
        if counts[0] > 0:
            packages_num += counts[0]//36
            if counts[0] % 36 != 0:
                packages_num += 1
        print(packages_num)