from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                num = matrix[row][column]
                if num == min(matrix[row]) and num == max(matrix[i][column] for i in range(len(matrix))):
                    res.append(num)

        return res

    def luckyNumbers2(self, matrix: List[List[int]]) -> List[int]:
        def find_min_row(row, matrix):
            min_n = matrix[row][0]
            for i in range(1, len(matrix[row])):
                if min_n > matrix[row][i]:
                    min_n = matrix[row][i]

            return min_n

        def find_max_col(col, matrix):
            max_n = matrix[0][col]
            for i in range(len(matrix)):
                if max_n < matrix[i][col]:
                    max_n = matrix[i][col]

            return max_n

        res = []
        mins = []
        for i in range(len(matrix)):
            mins.append(find_min_row(i, matrix))

        maxes = matrix[0]
        for i in range(len(matrix[0])):
            maxes[i] = find_max_col(i, matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if mins[i] == matrix[i][j] and maxes[j] == matrix[i][j]:
                    res.append(matrix[i][j])

        return res


obj = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(obj.luckyNumbers2(matrix))
