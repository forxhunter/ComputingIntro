'''
round numbers
'''
n = int(input())
for i in range(n):
    integer = int(input())
    zeros = 0
    while integer % 10 == 0:
        integer //= 10
        zeros += 1

    primes = []
    # add the numbers
    minus = 0
    while integer != 0:
        result = integer % 10
        integer //= 10
        if result != 0:
            primes.append(result*10**minus)
        minus += 1
    primes = [prime * (10**zeros) for prime in primes]
    k = len(primes)
    print(k)
    s = str(primes[0])
    for x in primes[1:]:
        s += ' ' + str(x)
    print(s)

