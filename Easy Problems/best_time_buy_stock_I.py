def maxProfit(nums):
    if len(nums) == 0:
        return 0

    minprice = max(nums)
    maxprofit = 0

    for i in range(len(nums)):
        if nums[i] < minprice:
            minprice = nums[i]
        elif nums[i] - minprice > maxprofit:
            maxprofit = nums[i] - minprice
    return maxprofit