'''
16528充实的寒假生活
寒假马上就要到了，龙傲天同学获得了从第0天开始到第60天结束为期61天超长寒假，他想要尽可能丰富自己的寒假生活。
现提供若干个活动的起止时间，请计算龙同学这个寒假至多可以参加多少个活动？注意所参加的活动不能有任何时间上的重叠，
在第x天结束的活动和在第x天开始的活动不可同时选择。
输入：
第一行为整数n，代表接下来输入的活动个数(n < 10000)
紧接着的n行，每一行都有两个整数，第一个整数代表活动的开始时间，第二个整数代表全结束时间
'''
n = int(input())
activities = []
count = 0
for i in range(n):
    temp = list(map(int, input().split()))
    activities.append(temp)
activities = sorted(activities, key=lambda x: x[1])
last = -1
for activity in activities:
    if activity[0] > last:
        count += 1
        last = activity[1]

print(count)


