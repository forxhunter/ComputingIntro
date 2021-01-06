'''
calculate how many participants will advance
n participants k advance number
input:
1  n  k
2 scores with ith participants get the scores
output:
the number of participants
# Note
if get zero, can't advance
if last one has someone with equal score participants, all of them will advance

'''

n, k = input().split(' ')
n = int(n)
k = int(k)
scores = []
scores = input().split(' ')
scores = list(map(int, scores))  # string to int

advances = k

# if has the same score
last = scores[advances-1]
while last == 0:
    if advances == 0:
        break

    advances -= 1
    last = scores[advances-1]
if advances == 0:
    print('0')
else:
    for i in range(k, n):
        if scores[i] == last:
            advances += 1
        else:
            break
    print(advances)



