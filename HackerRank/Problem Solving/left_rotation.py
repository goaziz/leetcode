a = [1, 2, 3, 4, 5]
d = 4
t = a[:] + a[:d]
print(t)
d = t[d:]
print(' '.join(map(str, d)))
