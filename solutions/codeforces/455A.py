"""
Boredom
v0.1 错误：直接统计了所有可能的数值a和对应的count，忽视了要求中只影响a-1,a+1两个数，而误认为影响了小于a和大于a的两个数
"""

'''
基本思路：
1. 函数找到每个值及其对应的sum
2. 找到最大sum 的所对应的num，并和周围相邻num-1,num+1对应的sum和比较。如果大于则。。，小于就删掉
3. 加入result，并删除对应值
'''



def find_counts(lists):
    counts = []
    # 排序后方便对元素个数进行计数
    lists.sort(reverse=True)
    while len(lists) != 0:
        temp = lists[0]
        num = lists.count(temp)
        counts.append([temp, num])
        lists = lists[num:]
    return counts

'''
def if_need_eliminate(m, n):
    if abs(m - n) == 1:
        return True
    elif abs(m - n) == 0:
        return -1
    else:
        return False
'''

def recursive_maximization(total_num, counts):
    if total_num == 0:
        return 0
    elif total_num == 1:
        return counts[0][0] * counts[0][1]
    else:
        #total_num >= 2:
        largest_sum = counts[0][0] * counts[0][1]
        if abs(counts[0][0]-counts[1][0]) == 1:
            # need elimination
            a = recursive_maximization(total_num-1, counts[1:])
            b = recursive_maximization(total_num-2, counts[2:]) + largest_sum
            return max(a, b)
        else:
            return recursive_maximization(total_num-1, counts[1:]) + largest_sum
# read the inputs
n = int(input())
integers = list(map(int, input().split(' ')))
counts = find_counts(integers)
result = recursive_maximization(len(counts), counts)
print(result)
