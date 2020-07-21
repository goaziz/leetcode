def pickingNumbers(a):
    m = 0
    n = 1
    for i in a:
        n1 = a.count(i)
        n2 = a.count(i - n)
        m = max(m, n1 + n2)
    return m


a = [4, 6, 5, 3, 3, 1]
print(pickingNumbers(a))
