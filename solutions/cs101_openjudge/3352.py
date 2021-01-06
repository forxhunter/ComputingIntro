'''
3532: 最大上升子序列和
请用dp实现, http://cs101.openjudge.cn/practice/3532/
'''
n = int(input())
numbers = [int(x) for x in input().split()]
# dp state array minimum length for given n first numbers

sum_result = numbers[:]
for i in range(n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            sum_result[i] = max(sum_result[j]+numbers[i], sum_result[i])
print(max(sum_result))


