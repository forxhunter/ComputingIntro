n = int(input())
while n != 0:
    tians = [int(x) for x in input().split()]
    kings = [int(x) for x in input().split()]
    tians.sort(reverse=True)
    kings.sort(reverse=True)


    win = 0
    lose = 0
    while len(tians) != 0:
        if tians[-1] > kings[-1]:
            win += 1
            del tians[-1]
            del kings[-1]
        else:
            if tians[0] > kings[0]:
                win += 1
                del tians[0]
                del kings[0]
            else:
                if tians[-1] < kings[0]:
                    lose += 1
                elif tians[-1] > kings[0]:
                    win += 1

                del tians[-1]
                del kings[0]



    money = 200 *(win-lose)
    print(money)
    # next test
    n = int(input())
