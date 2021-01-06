'''
Games
input:
    number of the teams: n
    home uni and guest uni color
    ...
'''

n = int(input())
home_unis = []
guest_unis = []
result = 0
for i in range(n):
    home, guest = list(map(int, input().split(' ')))
    home_unis.append(home)
    guest_unis.append(guest)

for i in range(n):
    host_color = home_unis[i]
    tests = guest_unis[0:i]
    if i != n:
        tests.extend(guest_unis[i+1:])
    result += tests.count(host_color)
print(result)