'''
greedy algorithm
An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.
Input

The first line of the input contains an integer x (1≤x≤1000000) — The coordinate of the friend's house.
Output

Print the minimum number of steps that elephant needs to make to get from point 0 to point x.
'''
x = int(input())
possible_moves = [5, 4, 3, 2, 1]
count = 0
for move in possible_moves:
    if x < move:
        continue
    count += (x//move)
    x = x % move
    if x == 0:
        break
print(count)
