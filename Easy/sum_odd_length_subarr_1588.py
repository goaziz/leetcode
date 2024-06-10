from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                sub_arr = arr[i: j + 1]
                if len(sub_arr) % 2 != 0:
                    s += sum(sub_arr)

        return s


obj = Solution()
arr = [10, 11, 12]
print(obj.sumOddLengthSubarrays(arr))
