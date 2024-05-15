from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0

        for i in arr1:
            is_greater = True
            for j in arr2:
                if abs(i - j) <= d:
                    is_greater = False
                    break

            if is_greater is True:
                count += 1

        return count

    def findTheDistanceValue2(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        arr2.sort()

        for i in range(len(arr1)):
            left, right = 0, len(arr2) - 1
            while left <= right:
                mid = (left + right) // 2
                if abs(arr1[i] - arr2[mid]) <= d:
                    count += 1
                    break
                elif arr1[i] < arr2[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return len(arr1) - count


obj = Solution()
arr1 = [2, 1, 100, 3]
arr2 = [-5, -2, 10, -3, 7]
d = 6
print(obj.findTheDistanceValue2(arr1, arr2, d))
