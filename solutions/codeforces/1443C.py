'''
print('\n'.join(map(str, ans)))
'''
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
    max_time = combined[0][1]
    # greedy start from the lowest one see if satisfied
    # calculate left retrieve time
    sum_self = 0
    for i in range(n):
        sum_self += combined[i][0]
        if i < n - 1 and combined[i][1] == combined[i + 1][1]:
            continue
        else:
            time_courier = 0
            if i < n - 1:
                time_courier = combined[i + 1][1]

            result = max(sum_self, time_courier)
            if result < max_time:
                max_time = result

    results.append(max_time)
print('\n'.join(map(str, results)))
