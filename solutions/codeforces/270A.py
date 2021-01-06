'''
Fancy Fence
geometry implementation
Fact: for regular polygon with n layers, the inner angle is (n-2)/n *180
x = 180 - 360/n
require x is integer, which means n can only be 360's factor
360 = 2^3 * 5 * 3^2
'''
n = int(input())
# possible results of 360's factors and also the range    0 < x < 360
# so factor can't be larger than or equal 180
possibles = {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120}
results = []
for ele in possibles:
    results.append(180-ele)

i = 7
for i in range(n):
    angle = int(input())
    if angle in results:
        print('YES')
    else:
        print('NO')
