
def moveZeroes(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    return nums


n = [0, 1, 0, 3, 12]
print(moveZeroes(n))
