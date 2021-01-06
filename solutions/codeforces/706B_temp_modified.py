'''
template dp
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
availabe_shops = [0] * (max_cost + 1)
# the final dp pointer
current_maxc = 0
# first give each shop's price an +1
for cost in costs:
    # '+=' instead of '+' in case more than two shops have the same price
    availabe_shops[cost] += 1


# start to do the program
for fake_i in range(days):
    money = int(input())
    # if exceed list_max
    if money >= max_cost:
        print(shops)
    else:
        # if need dynamic programming
        if money > current_maxc:
            # start the dynamic programming
            for i in range(current_maxc+1, money+1):
                availabe_shops[i] += availabe_shops[i-1]
            current_maxc = money

        print(availabe_shops[money])
