'''
get all factors for a integer
'''
n = int(input())
factors = []
for i  in range(1,n//2+1):
    if n % i == 0:
        factors.append(i)
        factors.append(n//i)

factors = set(factors)
print(factors)