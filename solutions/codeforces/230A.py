'''
Dragons
'''
s, n = list(map(int, input().split(' ')))
dragons = []
for i in range(n):
    one = list(map(int, input().split(' ')))
    dragons.append(one)
#print(dragons)
dragons = sorted(dragons, key=lambda x: x[0])
#print(dragons)
jud = True
for dragon in dragons:
    if s <= dragon[0]:
        print('NO')
        jud = False
        break
    else:
        s+= dragon[1]


if jud is True:
    print('YES')
