from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        s = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []
        for key, v in s:
            if len(result) == k:
                return result
            result.append(key)

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, val in freq.items():
            buckets[val].append(key)

        buckets.reverse()
        result = [item for val in buckets for item in val]

        return result[:k]


obj = Solution()
nums = [2, 2, 2, 3, 4, 3, 4, 5, 3, 3]
print(obj.topKFrequent2(nums, 2))
