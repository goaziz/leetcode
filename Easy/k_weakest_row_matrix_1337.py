from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rs = []

        for i, row in enumerate(mat):
            soldiers = sum(row)
            rs.append((soldiers, i))

        rs.sort()

        return [idx for _, idx in rs[:k]]


obj = Solution()
mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3
print(obj.kWeakestRows(mat, k))
