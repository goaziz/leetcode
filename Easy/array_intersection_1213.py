from collections import Counter
from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        hashmap = Counter(arr1 + arr2 + arr3)
        result = []

        for num in hashmap:
            if hashmap[num] == 3:
                result.append(num)

        return result

    def arraysIntersection2(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        p1, p2, p3 = 0, 0, 0

        result = []

        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                result.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if arr1[p1] > arr2[p2]:
                    p2 += 1
                elif arr2[p2] > arr3[p3]:
                    p3 += 1
                else:
                    p1 += 1

        return result


obj = Solution()
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
print(obj.arraysIntersection2(arr1, arr2, arr3))
