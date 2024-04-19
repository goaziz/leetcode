from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        apple_count = 0
        weight_sum = 0

        for w in weight:
            weight_sum += w
            if weight_sum > 5000:
                break
            apple_count += 1

        return apple_count


obj = Solution()
weight = [900, 950, 800, 1000, 700, 800]
print(obj.maxNumberOfApples(weight))
