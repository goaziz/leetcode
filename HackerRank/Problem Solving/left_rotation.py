a = [1, 2, 3]
d = 2
t = a[:] + a[:d]
d = t[d:]
print(d)
print(' '.join(map(str, d)))
