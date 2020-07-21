def migratoryBirds(arr):
    a = arr.count(1)
    b = arr.count(2)
    c = arr.count(3)
    d = arr.count(4)
    e = arr.count(5)
    ar = [a, b, c, d, e]
    print(ar)
    print(1 + ar.index(max(ar)))


migratoryBirds([1, 4, 4, 4, 5, 3])
