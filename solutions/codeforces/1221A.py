'''
2048 Game
accpted when:
1.2048 in it
if not :
2. delete all elments larger than 1024, and find sum is not less than 2048
'''
q = int(input())
# read the following lines

for i in range(q):
    '''
    n: number of integers 
    numbers: list of integers in each game
    '''
    n = int(input())
    numbers = list(map(int, input().split(' ')))

    # have 2048, directly out
    if 2048 in numbers:
        print('YES')
    else:
        # wipe out numbers larger than 2048
        numbers.sort()
        if max(numbers) > 1024:
            for j in range(len(numbers)):
                if numbers[j] > 1024:
                    numbers = numbers[:j]
                    break


        # find if possible
        results = sum(numbers)
        if results >= 2048:
            print('YES')
        else:
            print('NO')







