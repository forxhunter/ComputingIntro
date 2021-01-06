status = [0] * 12
left = ['' for _ in range(3)]
right = ['' for _ in range(3)]
result = ['' for _ in range(3)]


def Balanced():
    for i in range(3):
        leftW = rightW = 0
        for k in range(len(left[i])):
            leftW += status[ord(left[i][k]) - ord('A')]
            rightW += status[ord(right[i][k]) - ord('A')]

        if leftW > rightW and result[i][0] != 'u':
            return False
        if leftW == rightW and result[i][0] != 'e':
            return False
        if leftW < rightW and result[i][0] != 'd':
            return False

    return True


for _ in range(int(input())):
    for i in range(3):
        left[i], right[i], result[i] = input().split()

    for i in range(12):
        status[i] = 0

    i = 0
    for i in range(12):
        status[i] = 1
        if Balanced():
            break

        status[i] = -1
        if Balanced():
            break

        status[i] = 0

    print('{} is the counterfeit coin and it is {}.'.format(chr(i + ord('A')), "heavy" if status[i] > 0 else "light"))