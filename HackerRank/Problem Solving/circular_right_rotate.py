from collections import deque


def circularArrayRotation(a, k, queries):
    arr = deque(a)
    arr.rotate(k)
    return [arr[i] for i in queries]

a = [3, 4, 5]
k = 2
q = [0, 1, 2]
print(circularArrayRotation(a, k, q))
