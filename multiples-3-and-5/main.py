#!/usr/bin/python3
sum = 0
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        print(n)
        sum += n
print(sum)
