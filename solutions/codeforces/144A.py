'''
Arrival of the General
'''
n = int(input())
soldiers = list(map(int, input().split(' ')))
maxs = max(soldiers)
mins = min(soldiers)
posi_max = soldiers.index(maxs)
soldiers.reverse()
posi_min = n-1 - soldiers.index(mins)

if posi_max > posi_min:

    swap = (posi_max - 0) + (n - 1 - (posi_min + 1))
else:
    swap = (posi_max - 0) + (n - 1 - posi_min)
print(swap)