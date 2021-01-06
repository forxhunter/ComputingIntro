"""
Boredom
v0.1 错误：直接统计了所有可能的数值a和对应的count，忽视了要求中只影响a-1,a+1两个数，而误认为影响了小于a和大于a的两个数
v1 超时，利用空间复杂度解决时间复杂度问题。重写find counts
v2  a: use iteration instead of recursion, and save each result in a array
    b: pre calc sum in find_counts to avoid multiple calc
"""

'''
基本思路：
1. 函数找到每个值及其对应的sum
2. 找到最大sum 的所对应的num，并和周围相邻num-1,num+1对应的sum和比较。如果大于则。。，小于就删掉
3. 加入result，并删除对应值
'''


def need_eliminate(first, second):
    if abs(first - second) == 1:
        return True
    else:
        return False


def find_sum(lists):
    counts = []
    lists.sort()
    while len(lists) != 0:
        temp = lists[0]
        num = lists.count(temp)
        counts.append([temp, num * temp])
        lists = lists[num:]
    return counts


# read the inputs

if __name__ == '__main__':
    max_len = 10 ** 5
    n = int(input())
    integers = list(map(int, input().split(' ')))
    sums = find_sum(integers)

    n_maxs = [0] * (max_len+1)
    # one
    n_maxs[1] = sums[0][1]
    if len(sums) >= 2:
        # two
        if need_eliminate(sums[0][0], sums[1][0]):
            n_maxs[2] = max(sums[0][1], sums[1][1])
        else:
            n_maxs[2] = sums[0][1] + sums[1][1]


        if len(sums) >= 3:
            # get max_list wit n
            for i in range(3, len(sums) + 1):
                if need_eliminate(sums[i-1][0], sums[i - 2][0]):
                    # if need to do elimination
                    n_maxs[i] = max(n_maxs[i - 1], n_maxs[i - 2] + sums[i - 1][1])
                else:
                    n_maxs[i] = n_maxs[i - 1] + sums[i - 1][1]



    print(n_maxs[len(sums)])
