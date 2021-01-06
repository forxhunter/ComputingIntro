'''
Bulbs
Vasya wants to turn on Christmas lights consisting of m bulbs.
Initially, all bulbs are turned off.
There are n buttons, each of them is connected to some set of bulbs.
Vasya can press any of these buttons. When the button is pressed, it turns on all the bulbs it's connected to.
Can Vasya light up all the bulbs?

If Vasya presses the button such that some bulbs connected to it are already turned on, they do not change their state, i.e. remain turned on.
'''
buttons, bulbs = list(map(int, input().split(' ')))
status = [0]*(bulbs+1)
status[0] = 1
for ll in range(buttons):
    numbers = list(map(int, input().split(' ')))
    for number in numbers[1:]:
        status[number] = 1


if status.count(0) == 0:
    print('YES')
else:
    print('NO')

