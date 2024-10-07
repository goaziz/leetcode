from typing import List


class Solution:

    def generate_row(self, prev_row):
        next_row = [1]

        for i in range(len(prev_row) -  1):
            next_row.append(prev_row[i] + prev_row[i + 1])

        next_row.append(1)
        return next_row

    def generate(self, numRows: int) -> List[List[int]]:
        prev_row = [1]
        result = [prev_row]

        for _ in range(numRows - 1):
            prev_row = self.generate_row(prev_row)
            result.append(prev_row)

        return result


obj = Solution()
n = 5
print(obj.generate(n))
