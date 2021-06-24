import math

def primes(number):
    matrix = list(range(2, number + 1))
    blacklist = list()
    primes = list()
    for n in matrix:
        if n not in blacklist:
            primes.append(n)
            for multiple in range(n + n, number + 1, n):
                blacklist.append(multiple)
    return primes

def highestPrimeFactor(number):
    largest = 1
    primes_desc = list(reversed(primes(number)))
    print("found all prime numbers below {}".format(number))
    for n in primes_desc:
        if number % n == 0:
            largest = n
            break
    return largest

def primeFactors(n: int):
    while n % 2 == 0:
        print("2, ")
        n /= 2
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            n /= i
            print("{}, ".format(i))

number = 600851475143
#number = 13195
#print("largest: {}".format(highestPrimeFactor(number)))
primeFactors(number)
