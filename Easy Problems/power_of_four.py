import math

def isPowerOfFour(num):
    if num < 0 or num == 0:
        return False
    return (math.log10(num) / math.log10(4)) % 1 == 0
