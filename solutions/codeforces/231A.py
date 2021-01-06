'''
Team decision making
input: n problem numbers, n lines each line three numbers(0/1)
if the number of 1 >=2 , it means the problem solved with certainty

'''

n = int(input())
result = 0 # problem solved
for i in range(n):
    outcomes = input() #string type
    count = outcomes.count('1')

    if count >= 2:
        result += 1
print(result)
