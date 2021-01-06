'''
16528:充实的寒假生活（cs10117 Final Exam）
请用dp实现, http://cs101.openjudge.cn/practice/16528/
'''

n = int(input())
activities = [-1] * 61
for i in range(n):
    s, e = map(int, input().split())
    if activities[s] == -1:
        activities[s] = e
    else:
        activities[s] = min(activities[s], e)

dp_maxact = [0] * 61
for i in range(61):
    if activities[i] != -1:
        dp_maxact[activities[i]] = max(dp_maxact[activities[i]], dp_maxact[i-1]+1)
    dp_maxact[i] = max(dp_maxact[i], dp_maxact[i-1])

print(dp_maxact[-1])
