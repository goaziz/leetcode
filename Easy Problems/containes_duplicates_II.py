def containsNearbyDuplicate(nums, k):
    dic = {}
    print(dic)
    for i, j in enumerate(nums):
        if j in dic and i - dic[j] <= k:
            return True
        dic[j] = i
        print(dic[j])
    return False


nums = [1, 0, 1, 1]
k = 1
print(containsNearbyDuplicate(nums, k))
