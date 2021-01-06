'''
706B:Interesting drink
url: https://codeforces.com/problemset/problem/706/B
'''
shops = int(input())
costs = list(map(int, input().split(' ')))
days = int(input())
costs.sort()
# jisuan
min_cost = costs[0]
max_cost = costs[-1]

# shorten the available shops but need to focus whether coin exceeds the max
availabe_shops = [-1] * (max_cost + 1)
for i in range(min_cost):
    availabe_shops[i] = 0
# processed max cost
current_max = min_cost-1

for i in range(days):
    coin = int(input())
    # coins even larger than max price offered!
    if coin > max_cost:
        print(shops)
    # not prepared yet
    else:
        if availabe_shops[coin] == -1:

            for spend in range(current_max+1, coin + 1):
                if spend >= max_cost:
                    availabe_shops[spend] = shops
                    continue
                '''
                for index in range(shops):
                    if costs[index] > spend and costs[index-1] <= spend:
                        availabe_shops[spend] = index
                        break
                '''
                # use binary search instead
                left = 0
                right = shops - 1
                while left != right:
                    mid = (left+right)//2
                    if costs[mid] <= spend:
                        left = mid
                        # only need to find if latter shop is smaller
                        # mind the exceeding problem
                        if mid == shops-1:
                            availabe_shops[spend] = shops
                            break
                        if costs[mid+1] > spend:
                            availabe_shops[spend] = mid + 1
                            break
                    elif costs[mid] > spend:
                        # shops >= spend
                        right = mid

            #update the current max
            current_max = coin
        # get the info, yeah!
        print(availabe_shops[coin])