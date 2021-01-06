'''
Danger or not:If there are at least 7 players of some team standing one after another,
then the situation is considered dangerous. For example, the situation 00100110111111101
is dangerous and 11110111011101 is not. You are given the current situation. Determine whether it is dangerous or not.
Input

    The first input line contains a non-empty string consisting of characters "0" and "1", which represents players.
    The length of the string does not exceed 100 characters. There's at least one player from each team present on the field.
Output

    Print "YES" if the situation is dangerous. Otherwise, print "NO".
'''
position = input()
if '1111111' in position or '0000000' in position:
    print('YES')
else:
    print('NO')
