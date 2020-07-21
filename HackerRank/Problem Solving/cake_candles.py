def birthdayCakeCandles(ar):
    max_x = max(ar)
    count = 0
    for i in range(len(ar)):
        if max_x == ar[i - 1]:
            count += 1

    return count