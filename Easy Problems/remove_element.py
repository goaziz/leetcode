# def validateSubsequence(array, sequence):
#     index = 0
#     for i in array:
#         if index < len(sequence) and i == sequence[index]:
#             index += 1
#     return index == len(sequence)
#
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [4, 5, 1, 22, 25, 6, -1, 8, 10]
#
# print(validateSubsequence(array, sequence))

# def removeElement(nums, val):
#     mod = [i for i in nums if i != val]
#     return mod
#
# nums = [3, 2, 2, 3]
# val = 3
#
# print(removeElement(nums, val))

def removeElement(nums, val):
    i = 0
    n = len(nums)

    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return n

nums = [3, 2, 2, 3]
val = 3

print(removeElement(nums, val))