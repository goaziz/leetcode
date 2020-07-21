import collections


def sockMerchant(n, ar):
    count = 0
    for i in collections.Counter(ar).values():
        count += i // 2
    return count
