'''
Police Recruits
'''
n = int(input())
events = list(map(int, input().split(' ')))
forces = 0
untreat = 0
for event in events:
    forces += event
    if forces == -1:
        untreat += 1
        forces = 0
print(untreat)