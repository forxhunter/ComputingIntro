'''
I wanna be the guy
'''
n = int(input())
line1 = input()[2:]
line2 = input()[2:]
line = line1 + ' ' + line2
result = True
for i in range(n):
    if str(i+1) not in line:
        result = False
        break

if result == True:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')