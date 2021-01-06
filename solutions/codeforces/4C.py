'''
Registration system
'''
database = {}
n = int(input())
for i in range(n):
    username = input()
    if username not in database.keys():
        database[username] = 0
        print('OK')
    else:
        database[username] += 1
        print(username + str(database[username]))
