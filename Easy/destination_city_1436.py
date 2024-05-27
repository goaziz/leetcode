from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash_set = set()

        for path in paths:
            hash_set.add(path[0])

        for path in paths:
            if path[1] not in hash_set:
                return path[1]


obj = Solution()
paths = [["B", "C"], ["D", "B"], ["C", "A"]]
print(obj.destCity(paths))
