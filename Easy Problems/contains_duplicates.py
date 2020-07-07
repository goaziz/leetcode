def containsDUplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

t = [1, 2, 3, 1]
print(containsDUplicate(t))
