from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum_so_far = 0
        higest_alt = 0

        for i in range(len(gain)):
            sum_so_far += gain[i]
            higest_alt = max(higest_alt, sum_so_far)

        return higest_alt


obj = Solution()
gain = [-4, -3, -2, -1, 4, 3, 2]
print(obj.largestAltitude(gain))
