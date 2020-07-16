def getTotalX(a, b):
    results = []
    for i in range(1, max(b) + 1):
        if all(i % anum == 0 for anum in a) and all(bnum % i == 0 for bnum in b):
            results.append(i)
            print(results)

    return (len(results))

a = [2, 6]
b = [24, 36]
print(getTotalX(a, b))