import sys

# We only need to check if n is evenly divisible by numbers ≤√n.
# Take n = 100. It is evenly divisible by: 2, 4, 5, 10, 20, 25, 50
# Note that the largest factor (50) is n/2. All divisors of n are ≤ n/2. This holds for all numbers
# If we test all divisors of 100: 2*50, 4*25, 5*20, 10*10, 20*5, 25*4, 50*2
# Products past 10*10 are duplicates of the previous products (2*50 = 50*2).
# To avoid duplicates, we only need to check until 10*10 (√100).
# All unique divisors of n are less than or equal to √n.
# If we can evenly divide n by an even number so can 2. Therefor we can eliminate all even numbers past 2.
def isPrime(n: int) -> bool:
    # Check even number
    if n % 2 == 0:
        return False
    # Check all numbers below √n
    # Since we have already checked 2 we can start with 3 which is an odd number
    # Suppress even numbers by incrementing by 2
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# All prime numbers above 3 are of the form 6k +- 1.
# Although, not all numbers generated with this formula are primes: 6 * 6 - 1 = 35 (35 % 5 = 0)
def isPrime6k(n: int) -> bool:
    # Check even numbers and multiples of 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Since we've checked 2 and 3 we start with the next odd number: 5
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        # we started with 5 = 3 + 2 so 5 + 4 = 3 + 6
        # i + 4 is always a multiple of 3, so we skip it
        # 1 2 3 4 5 6 7 8 9 10 11 12
        #     |---|---|---|
        # 3:    +2  +4  +6
        #         |---|---|----|
        # 5:        +2  +4  +6
        i += 6
    return True

num = int(sys.argv[1])
print("{}: {}".format(num, isPrime(num)))
print("{}: {}".format(num, isPrime6k(num)))
