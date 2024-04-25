from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        is_true = True

        while True:
            is_true = False

            temp = arr[:]
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    temp[i] += 1

                if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    temp[i] -= 1

                if arr[i] != temp[i]:
                    is_true = True
            arr = temp

            if not is_true:
                break

        return arr


obj = Solution()
arr = [1, 3, 2, 6]
print(obj.transformArray(arr))
