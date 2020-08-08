def viralAdvertising(n):
    likes = 0
    shared = 5
    for i in range(1, n + 1):
        likes += (shared // 2)
        shared = (shared // 2) * 3
    return likes

print(viralAdvertising(3))