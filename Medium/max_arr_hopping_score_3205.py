from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        max_score = 0
        ans = 0
        
        for i in range(len(nums) - 1, 0, -1):
            max_score = max(max_score, nums[i])
            ans += max_score
        
        return ans

    def maxScore2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        
        for i in range(n):
            for j in range(i + 1, n):
                dp[j] = max(dp[j], dp[i] + (j - i) * nums[j])
        
        return max(dp)

obj = Solution()
nums = [4, 5, 2, 8, 9, 1, 3]
print(obj.maxScore2(nums))
