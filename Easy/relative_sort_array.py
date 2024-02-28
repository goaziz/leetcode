from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = Counter(arr1)
        res = []
        not_existed = []

        for num in arr2:
            if num in hashmap:
                res += [num] * hashmap.get(num)
                hashmap.pop(num)

        for key, value in hashmap.items():
            not_existed += [key] * value

        return res + sorted(not_existed)


obj = Solution()
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(obj.relativeSortArray(arr1, arr2))
