def catAndMouse(x, y, z):  # x => cat A, y => cat B, z => mouse C
    a = abs(x - z)
    b = abs(y - z)
    return "Cat A" if a < b else "Cat B" if b < a else "Mouse C"


x = 1
y = 3
z = 2
print(catAndMouse(x, y, z))
