from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False

        division = sum(arr) // 3
        s = parts = 0
        add = division
        for i in arr:
            s += i
            if division == s:
                parts += 1
                division += add

        return s == sum(arr) and parts >= 3


obj = Solution()
arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
print(obj.canThreePartsEqualSum(arr))
