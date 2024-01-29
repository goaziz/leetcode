from typing import List


class Solution:
    def check_right_part(self, idx, arr):
        # this function needs to check arr if decreasing
        rigth_part = arr[idx:]

        for i in range(len(rigth_part) - 1):
            if rigth_part[i] > rigth_part[i + 1]:
                continue
            else:
                return False

        return True

    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) == 1:
            return True
        elif arr[0] > arr[1]:
            return False

        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                continue
            else:
                return self.check_right_part(i, arr)

        return False

    def validMountainArray2(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0

        # walk up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == n - 1:
            return False

        # walk down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1


obj = Solution()
arr = [2, 1]
print(obj.validMountainArray(arr))
