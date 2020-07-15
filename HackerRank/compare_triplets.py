def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0
    for i in range(3):
        if a[i] > b[i]:
            alice_points += 1
        elif a[i] < b[i]:
            bob_points += 1
    return [alice_points, bob_points]


a = [1, 2, 3]
b = [3, 2, 1]
print(compareTriplets(a, b))
