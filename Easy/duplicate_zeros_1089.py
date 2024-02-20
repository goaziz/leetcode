from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0

        while i < n:
            if arr[i] == 0:
                arr.pop()
                arr.insert(i, 0)
                i += 2
            else:
                i += 1


obj = Solution()
arr = [1, 0, 2, 3, 0, 4, 5, 0]
# arr = [1, 2, 3]
print(obj.duplicateZeros(arr))
