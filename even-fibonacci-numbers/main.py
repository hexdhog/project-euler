x, y = 1, 2
total = 0
while True:
    sum = x + y
    print(x)
    x = y
    y = sum
    if x > 4000000:
        break
    if x % 2 == 0:
        total += x
print("total: {}".format(total))
