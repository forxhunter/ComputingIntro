'''
B. Light It Up
Facts:
1.亮灯时间和非亮灯时间是相邻的
2.加入一个点，意味着后面的亮灯和非亮灯时间段被反转
3.按照贪心思想，加入的这个点在亮灯区间的话，应该在区间靠后的位置；不亮灯区间的话应该尽量靠前
'''
n, duration = list(map(int, input().split(' ')))
# flips is the point when change the status of light
flips = [0]
flips += list(map(int, input().split(' ')))
flips.append(duration)

# duration between two adjacent points
posi_intervals = []
counter_intervals = [0] * (n+1)
temp_sum = 0
counter_sum = 0
# determine whether last duration is on or off by n
last_on = False
if n % 2 == 0:
    last_on = True

for i in range(1, n+2):
    if i % 2 != 0:
        temp_sum += flips[i] - flips[i-1]
    # posi_part
    posi_intervals.append(temp_sum)
    # counter_part for flip judgement
    j = n+1 - i
    if last_on is False:
        #flipped, now on
        if j % 2 != 0:
            counter_sum += flips[j+1] -flips[j]

        counter_intervals[j] = counter_sum
    if last_on is True:
        #flipped, now false
        if j %2 != 0:
            counter_sum += flips[j+1] - flips[j]
        counter_intervals[j] = counter_sum

# now greedy to find if better way exist!

for i in range(n+1):
    temp = 0
    if i == 0:
        temp = flips[1]-1 + counter_intervals[1]
    elif i < n and flips[i+1] - flips[i] != 1:
        temp = posi_intervals[i-1] + flips[i+1] - flips[i] -1 +counter_intervals[i+1]
    else:
        temp = posi_intervals[i-1] + flips[i+1] - flips[i] -1

    if temp > temp_sum:
        temp_sum = temp

print(temp_sum)






