t = int(input())
results = []
for fake_i in range(t):
    n = int(input())
    courier = list(map(int, input().split(' ')))
    self = list(map(int, input().split(' ')))
    # (self, courier)
    '''
    combined = [[x, y] for x, y in zip(self, courier)]
    combined = sorted(combined, key=(lambda x: x[1]), reverse=True)
    '''
    combined = sorted(list(zip(self, courier)), key=(lambda x: x[1]), reverse=True)

    # greedy start from the lowest one see if satisfied
    # calculate left retrieve time
    sum_self = 0
    for i in range(n):
        sum_self += combined[i][0]
        if sum_self >= combined[i][1]:
            sum_self = max(combined[i][1], sum_self-combined[i][0])
            break
    results.append(sum_self)
print('\n'.join(map(str, results)))
'''
n = int(input())
ans = []
for i in range(n):
    m = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = sorted(list(zip(b,a)), key=(lambda x: x[1]), reverse=True)
    d = 0
    for i in range(m):
        d += c[i][0]
        if d >= c[i][1]:
            d = max(c[i][1],d-c[i][0])
            break
    ans.append(d)
print('\n'.join(map(str, ans)))
'''