import math


def isPowerOfThree(n):
    # if n == 0:
    #     return 0
    # while n != 1:
    #     n /= 3
    #     if n % 3 != 0 and n != 1:
    #         return False
    # return True

    ### without using loop
    return (math.log10(n) / math.log10(3)) % 1 == 0

n = 27
print(isPowerOfThree(n))
