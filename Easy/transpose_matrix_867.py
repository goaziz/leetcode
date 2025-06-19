from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []

        for i, arr in enumerate(matrix):
            if i == 0:
                for num in arr:
                    result.append([num])
            else:
                for j, num in enumerate(arr):
                    result[j].append(num)

        return result

    def transpose2(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*matrix)]


obj = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(obj.transpose2(matrix))
