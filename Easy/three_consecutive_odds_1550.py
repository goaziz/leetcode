from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        for i in range(len(arr) - 2):
            x = arr[i]
            y = arr[i + 1]
            z = arr[i + 2]

            if all(num % 2 != 0 for num in [x, y, z]):
                return True

        return False


obj = Solution()
arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
print(obj.threeConsecutiveOdds(arr))
