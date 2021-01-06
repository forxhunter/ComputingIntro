'''
 He gave the lazy student a seemingly easy task: You are given an idle body in space and the forces that affect it. The body can be considered as a material point with coordinates (0; 0; 0). Vasya had only to answer whether it is in equilibrium. "Piece of cake" — thought Vasya, we need only to check if the sum of all vectors is equal to 0. So, Vasya began to solve the problem. But later it turned out that there can be lots and lots of these forces, and Vasya can not cope without your help. Help him. Write a program that determines whether a body is idle or is moving by the given vectors of forces.
Input:

    The first line contains a positive integer n (1≤n≤100),
    then follow n lines containing three integers each:
        the xi coordinate, the yi coordinate and the zi coordinate of the force vector, applied to the body
        (-100≤xi,yi,zi≤100).
Output:

    Print the word "YES" if the body is in equilibrium, or the word "NO" if it is not.

'''
n = int(input())
force_s = [0, 0, 0]
for i in range(n):
    coordinates = list(map(int, input().split(' ')))
    force_s[0] += coordinates[0]
    force_s[1] += coordinates[1]
    force_s[2] += coordinates[2]
if force_s[0] == 0 and force_s[1] == 0 and force_s[2] == 0:
    print('YES')
else:
    print('NO')

