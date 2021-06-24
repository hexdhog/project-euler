def isPalindrome(number: int) -> bool:
    nstr = str(number)
    half = int(len(nstr) / 2)
    if nstr[:half] == nstr[-half:][::-1]:
        return True
    return False

def findProducts(number: int, start: int, end: int) -> (int, int):
    diff = end - start
    step = 1
    if diff < 0:
        step = -1
    for i in range(start, end + 1, step):
        if number % i == 0:
            return int(i), int(number / i)
    return None, None

for n in range(999 * 999, 100 * 100, -1):
    if (isPalindrome(n)):
        p1, p2 = findProducts(n, 999, 100)
        if p1 != None and p2 != None:
            if len(str(p1)) == 3 and len(str(p2)) == 3:
                print("{} = {} * {}".format(n, p1, p2))
