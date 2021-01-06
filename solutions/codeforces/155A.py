'''
 I_love_%username%
 requirements:
 First, it is amazing if during the contest the coder earns strictly more points that he earned on each past contest.
 Second, it is amazing if during the contest the coder earns strictly less points that he earned on each past contest.
 Third, A coder's first contest isn't considered amazing.
 Output:
 Amazing number
'''
n = int(input())
scores = list(map(int,input().split(' ')))
amazings = 0
for i in range(1, n):

    max_score = max(scores[:i])
    min_score = min(scores[:i])
    if scores[i] > max_score or scores[i] < min_score:
        amazings += 1

print(amazings)
