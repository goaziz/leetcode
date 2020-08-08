def utopianTree(n):
    # return ~(~1 << (n >> 1)) << (n & 1)

    # i = 1
    # height = 1
    # while i <= n:
    #     if i % 2 == 0:
    #         height += 1
    #     else:
    #         height *= 2
    #     i += 1
    # return height
    sum = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum += 1
        else:
            sum *= 2
    return sum

n = 5
print(utopianTree(n))
