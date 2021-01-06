'''
greedy
Input

The first line contains integer n (1≤n≤100) — the number of coins. The second line contains a sequence of n integers
a1, a2, ..., an (1≤ai≤100) — the coins' values. All numbers are separated with spaces.
Output

In the single line print the single number — the minimum needed number of coins.
'''
number = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
amount = 0
rest = 0
taken = 0
rest = sum(coins)
for coin in coins:
    if amount > rest:
        break
    else:
        amount += coin
        rest -= coin
        taken += 1

print(taken)
