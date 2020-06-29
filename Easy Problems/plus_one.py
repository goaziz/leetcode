def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits

    if digits[0] == 0:
        lis = [1]
        lis.extend(digits)
        return lis


digits = [1, 2]
print(plusOne(digits))