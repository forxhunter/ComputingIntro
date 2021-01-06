'''
Buy a Shovel
'''
k, r = list(map(int, input().split(' ')))
tens = 10
min_count = 0
threshold = 10

for i in range(threshold):
    costs_by_count = (i+1) * k
    if (costs_by_count-r) % 10 == 0 or costs_by_count % 10 == 0:
        print(i+1)
        break

else:
    print(threshold)
