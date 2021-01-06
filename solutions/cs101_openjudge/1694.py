'''
brute force 枚举 仅24种可能
假币问题， http://cs101.openjudge.cn/practice/1694
'''
n = int(input())
coins = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
# 'heavy'==1,'light'==-1
status = [-1, 1]
found = False
for _ in range(n):
    lefts = []
    rights = []
    results = []
    for fake_i in range(3):
        left, right, result = input().split()
        lefts.append(left)
        rights.append(right)
        results.append(result)
    # greedy search
    for stat in status:
        for coin in coins:
            if_match = [False, False, False]
            # find if match continuously
            for i in range(3):
                left_weight = 0
                right_weight = 0

                # add special coin's weight
                if coin in lefts[i]:
                    left_weight += stat
                if coin in rights[i]:
                    right_weight += stat
                # give test result
                temp_result = ''
                if left_weight < right_weight:
                    temp_result = 'down'
                elif left_weight > right_weight:
                    temp_result = 'up'
                else:
                    temp_result = 'even'
                # if not match
                if temp_result != results[i]:
                    break
                # if match
                else:
                    if_match[i] = True

            if if_match.count(False) == 0:
                weigh = ''
                if stat == -1:
                    weigh = 'light'
                else:
                    weigh = 'heavy'

                print(coin + ' is the counterfeit coin and it is '+ weigh+'.')
                found = True
                break


