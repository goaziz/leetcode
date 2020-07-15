

def miniMaxSum(arr):
    sum_min = sum(arr) - min(arr)
    sum_max = sum(arr) - max(arr)

    print(sum_min, ' ', sum_max)

arr = [1, 3, 5, 7, 9]
print(miniMaxSum(arr))