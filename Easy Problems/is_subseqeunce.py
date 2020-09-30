def isSubsequence(s: str, t: str):
    m = len(s)
    n = len(t)

    j = 0
    i = 0
    while j < m and i < n:
        if s[j] == t[i]:
            j += 1
        i += 1
    return j == s