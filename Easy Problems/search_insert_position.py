

# def searchInsert(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target or nums[i] > target:
#             return i
#         else:
#             return -1
#     # return -1

def get_index(array, target):
    first = 0
    length_arr = len(array) - 1

    while first <= length_arr:
        d = (first + length_arr) // 2
        if array[d] == target:
            return d
        else:
            if array[d] > target:
                length_arr = d - 1
            else:
                first = d + 1
    return -1

array = [0, 1, 2, 33, 45, 45, 61, 71, 72, 73]
target = 45

print(get_index(array, target))