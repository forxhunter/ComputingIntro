'''
string test
'''
n = int(input())
results = input()
anton = results.count('A')
danik = len(results) - anton
if anton > danik:
    print('Anton')
elif danik > anton:
    print('Danik')
else:
    print('Friendship')