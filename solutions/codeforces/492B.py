'''
Vanya and lanterns
Vanya wonders: what is the minimum light radius d should the lanterns have to light the whole street?
it can be proved that the answer must the max of three number:
1. the length from leftest light to 0
2. the length from rightest light to l
3. the half  max distance between two adjacent lights
'''
n, l = list(map(int, input().split(' ')))
posis = list(map(int, input().split(' ')))

posis = list(set(posis))
posis.sort()

to_left = posis[0] - 0
to_right = l - posis[-1]
# in between
delta = 0
for i in range(1, len(posis)):
    if delta < posis[i] - posis[i-1]:
        delta = posis[i] - posis[i-1]
delta /= 2

result = max(to_left, to_right)
result = max(result, delta)
print(result)


