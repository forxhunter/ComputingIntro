'''
Input

The first line contains one integer n (1≤n≤100) — the quantity of friends Petya invited to the party.
The second line contains n space-separated integers: the i-th number is pi — the number of a friend who gave a
gift to friend number i. It is guaranteed that each friend received exactly one gift. It is possible that some friends
do not share Petya's ideas of giving gifts to somebody else. Those friends gave the gifts to themselves.

Output

Print n space-separated integers: the i-th number should equal the number of the
friend who gave a gift to friend number i.
'''
n = int(input())
trans = list(map(int, input().split(' ')))
received = [0] * n
for i in range(n):
    p = trans[i]
    received[p-1] = i

output = str(received[0]+1)
for ele in received[1:]:
    output += ' ' + str(ele+1)
print(output)
