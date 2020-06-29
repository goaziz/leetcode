def isPowerOfTwo(n):
    if n == 0:
        return 0
    while n != 1:
        n /= 2
        if n % 2 != 0 and n != 1:
            return False
    return True