import time
from humanfriendly import format_timespan

start_time = time.time()


def perfectSquare(n):
    i = 1

    while i * i <= n:
        if n % i == 0 and n / i == i:
            return True
        i += 1
    return False


end = time.time() - start_time


# Newton method
# def perfectSquare(n):
#     tmp = n
#     while tmp * tmp > n:
#         tmp = (tmp + n / tmp) // 2
#     return tmp * tmp == n
