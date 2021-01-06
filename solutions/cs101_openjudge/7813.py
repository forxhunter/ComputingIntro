'''
greedy
圣诞老人的礼物-Santa Clau’s Gifts， http://cs101.openjudge.cn/practice/7813
'''
n, w = list(map(int, input().split()))
boxes = []
for i in range(n):
    value, weight = list(map(int, input().split()))
    value_per = value/weight
    boxes.append([value_per, value, weight])
boxes.sort(reverse=True)
left_w = w
i = 0
total_value = 0

while i < n and left_w >= boxes[i][2]:

    total_value += boxes[i][1]
    left_w -= boxes[i][2]
    i += 1

if i <= n-1:
    total_value += left_w * boxes[i][0]

print('%.1f'%total_value)