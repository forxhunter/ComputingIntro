'''
The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically.
The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter.
Help Petya perform the comparison.
Input:

    Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive.
    It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.
Output:

    If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1".
    If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.
'''
string1 = input()
string2 = input()
string1 = string1.lower()
string2 = string2.lower()

if string1 == string2:
    print('0')
elif string1 < string2:
    print('-1')
else:
    print('1')

