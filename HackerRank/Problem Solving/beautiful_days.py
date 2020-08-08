def beautifulDays(i, j, k):
    count = 0
    for c in range(i, j + 1):
        t = str(abs(c))
        if ((c - int(t[::-1])) % k) == 0:
            count += 1
    return count

# one line solution beautifulDays = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0] print(sum(beautifulDays))
