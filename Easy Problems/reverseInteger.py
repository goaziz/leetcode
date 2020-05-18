def reverse(x):
    str_x = str(abs(x))

    if x < 0:
        res = -1 * int(str_x[::-1])
    else:
        res = int(str_x[::-1])

    if res not in range(-2147483648, 2147483648):
        return 0
    return res

print(reverse(-120))