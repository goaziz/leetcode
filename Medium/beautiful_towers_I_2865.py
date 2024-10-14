from typing import List


class Solution:

    def partition(self, peak, nums, index):
        heights = nums[:]
        result = []

        # Traverse right side of the peak
        for i in range(index, len(heights) - 1):
            heights[i + 1] = min(heights[i], heights[i + 1])
            result.append(heights[i + 1])

        # Traverse left side of the peak
        for i in range(index - 1, -1, -1):
            heights[i] = min(heights[i], heights[i + 1])
            result.append(heights[i])

        # Add the peak value
        return sum(result) + peak

    def maximumSumOfHeights(self, heights: List[int]) -> int:
        max_sum = 0

        for i in range(len(heights)):
            s = self.partition(heights[i], heights, i)
            max_sum = max(s, max_sum)

        return max_sum

    def maximumSumOfHeights2(self, heights: List[int]) -> int:
        n = len(heights)
        max_sum = 0

        for i, val in enumerate(heights):
            peak = val
            left = val
            for j in range(i - 1, -1, -1):
                if heights[j] < left:
                    left = heights[j]
                peak += left

            right = val
            for j in range(i + 1, n):
                if heights[j] < right:
                    right = heights[j]
                peak += right

            max_sum = max(peak, max_sum)

        return max_sum


obj = Solution()
heights = [3, 2, 5, 5, 2, 3]
print(obj.maximumSumOfHeights2(heights))
