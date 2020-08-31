
def moveZeroes(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    return nums


arr = ['a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, False, 0, 0, 0, 0, 0, 0, 0]
print(moveZeroes(arr))
