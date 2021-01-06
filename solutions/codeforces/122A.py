'''
judge if a number contains only 4 and 7
or can be evenly divided by 4 or 7
Input

The single line contains an integer n (1≤n≤1000) — the number that needs to be checked.
Output

In the only line print "YES" (without the quotes), if number n is almost lucky. Otherwise, print "NO" (without the quotes).
'''

lucknums = [4, 7, 44, 77, 47, 74, 444, 447, 474, 477, 744, 747, 774, 777]
number = int(input())
if number in lucknums:
    print('YES')
else:
    for lucknum in lucknums:
        if lucknum < number:
            if number % lucknum == 0:
                print('YES')
                break
            elif number % lucknum != 0 and lucknum == lucknums[-1]:
                print('NO')

        else:
            print('NO')
            break


