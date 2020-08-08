def missingNumber(nums):
    index = 0
    for i in range(len(nums)):
        index += (i + 1) - nums[i]
    return index


### Gauss Formula
# def missingNumber(nums):
#     expected_sum = len(nums) * (len(nums) + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum