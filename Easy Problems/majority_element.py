def majorityElement(nums):
    nums.sort()
    print(len(nums))
    return nums[len(nums) // 2]


t = [1, 1, 1, 2, 2]

print(majorityElement(t))