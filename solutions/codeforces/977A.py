'''
Strange substraction
Input

The first line of the input contains two integer numbers 𝑛
and 𝑘 (2≤𝑛≤109, 1≤𝑘≤50) — the number from which Tanya will subtract and the number of subtractions correspondingly.
Output

    Print one integer number — the result of the decreasing 𝑛 by one 𝑘 times.

    It is guaranteed that the result will be positive integer number.
'''
n, k = input().split()
k = int(k)
for i in range(k):
    if n[-1] != '0':
        lastdig = int(n[-1]) -1
        n = n[:-1] + str(lastdig)
    else:
        n = n[:-1]
print(n)