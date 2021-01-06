'''
insomnia cure
'''
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
number = 0

number = (d // k) + (d // l) + (d // m) + (d // n)
# 最小公倍数

def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm
# minus two factors
two = []
two.append(lcm(k, l))
two.append(lcm(k, m))
two.append(lcm(k, n))
two.append(lcm(l, m))
two.append(lcm(l, n))
two.append(lcm(m, n))


three = []
three.append(lcm(two[0], m))
three.append(lcm(two[0], n))
three.append(lcm(two[1], n))
three.append(lcm(two[3], n))

four = lcm(three[0], n)

for factor in two:
    number -= (d // factor)
for factor in three:
    number += (d // factor)
number -= (d // four)
print(number)
