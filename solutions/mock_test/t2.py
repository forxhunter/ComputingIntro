m = int(input())
for _ in range(m):
    x1, x2, x3, x4 = list(map(int, input().split()))

    if abs((x1 + x2 + x3 + x4)) == 24:
        print('YES')
        continue
    elif abs(x1 + x2 + x3 - x4) == 24:
        print('YES')
        continue
    elif abs(x1 + x2 - x3 + x4) == 24:
        print('YES')
        continue
    elif abs(x1 + x2 - x3 - x4) == 24:
        print('YES')
        continue
    elif abs(x1 - x2 + x3 + x4) == 24:
        print('YES')
        continue
    elif abs(x1 - x2 + x3 - x4) == 24:
        print('YES')
        continue
    elif abs(x1 - x2 - x3 + x4) == 24:
        print('YES')
        continue
    elif abs(x1 - x2 - x3 - x4) == 24:
        print('YES')
        continue
    else:
        print('NO')
