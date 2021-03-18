import sys
num = int(sys.argv[1])

def primes(number):
    matrix = list(range(2, number + 1))
    blacklist = list()
    primes = list()

    for n in matrix:
        if n not in blacklist:
            primes.append(n)
            for multiple in range(n + n, number + 1, n):
                print("new non-prime found: {}".format(multiple))
                blacklist.append(multiple)
    return primes

print(primes(num))
