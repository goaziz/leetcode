def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:m + i]) == d:
            count += 1
    return count
