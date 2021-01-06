'''
T-primes
find how many divisors a integers have.
Oouput:
    3 divisors return yes else no
3 important facts:
 first it must be equally divided integer = x*x
 second no other divisors besides 1 and itself
 third: it is T-prime as long as it's sqrt is a prime number except 4
'''
import math


# find all prime no larger than 10^6
def find_all_primes(limit=1000000):
    primes = [True] * (limit + 1)
    primes[0] = False
    primes[1] = False

    for i in range(2, limit + 1):
        if primes[i] == True:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes


def check_t_prime(number):
    jud = False
    if number == 4:
        jud = True
    elif number < 4 or number % 2 == 0:
        jud = False
    sqrt = int(math.sqrt(number))
    if sqrt ** 2 == number and prime_nums[int(math.sqrt(number))] == True:
        jud = True
    return jud


prime_nums = find_all_primes()
n = int(input())
integers = list(map(int, input().split(' ')))

for integer in integers:
    if check_t_prime(integer) is True:
        print('YES')
    else:
        print('NO')
