'''
make the addition only equation. and the number must be in non decreasing order

Input:

The first line contains a non-empty string s — the sum Xenia needs to count. String s contains no spaces.
It only contains digits and characters "+". Besides, string s is a correct sum of numbers 1, 2 and 3.
String s is at most 100 characters long.

Output:

    Print the new sum that Xenia can count.
'''
equation = input().split('+')
# counting 1 2 3
counts = [0, 0, 0]
i = 1

while i <= 3:

    counts[i - 1] = equation.count(str(i))
    i += 1

#build the output equation
output = ''
for j in range(3):
    for k in range(counts[j]):
        output += str(j+1) + '+'

print(output[:-1])
