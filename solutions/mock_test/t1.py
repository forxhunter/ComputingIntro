a = int(input())
if a % 2 != 0:
    print('0 0')
else:
    max_a = a//2
    min_a = a//4+(a%4)//2
    print(min_a,max_a,sep=' ')