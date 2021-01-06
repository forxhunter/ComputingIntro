'''
Amusing Joke
Judge creteria
whether it is possible to restore the names of the host and his guests from the letters lying at the door?
That is, we need to verify that there are no extra letters, and that nobody will need to cut more letters.

Input
The input file consists of three lines:
the first line contains the guest's name,
the second line contains the name of the residence host
and the third line contains letters in a pile that were found at the door in the morning.
All lines are not empty and contain only uppercase Latin letters. The length of each line does not exceed 100.

Output
YES/NO
'''
guest = input()
host = input()
messing = input()
# find if numbers match
mymess = guest + host
jud = True
if len(mymess) != len(messing):
    print('NO')
else:
    # find if there are wrong letters
    for i in range(ord('A'),ord('Z')+1):
        if mymess.count(chr(i)) != messing.count((chr(i))):
            print('NO')
            jud = False
            break
    if jud is True:
        print('YES')