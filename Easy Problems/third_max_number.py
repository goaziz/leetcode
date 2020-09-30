def thirdMax(nums):
    nums = list(set(nums))
    nums.sort()
    if len(nums) <= 2:
        return nums[-1]
    return nums[-3]
