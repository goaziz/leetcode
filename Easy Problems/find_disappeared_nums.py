def findDisappearedNumbers(nums):
    res = []
    n = len(nums)
    for i in range(n):
        nums[(nums[i] - 1) % n] += n

    for i in range(n):
        if nums[i] <= n:
            res.append(i + 1)
    return res