

def singleNumber(nums):
    # return [i for i in nums if nums.count(i) % 2 != 0][0]
    for i in nums:
        if nums.count(i) % 2 != 0:
            return i

d = [4,1,2,1,2]
print(singleNumber(d))