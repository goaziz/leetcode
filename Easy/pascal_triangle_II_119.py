from typing import List


class Solution:

    def generate_row(self, prev):
        next_ = [1]

        for i in range(len(prev) - 1):
            next_.append(prev[i] + prev[i + 1])
        next_.append(1)

        return next_

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        row = [1]
        result = [row]

        for i in range(rowIndex):
            row = self.generate_row(row)
            result.append(row)

        return result[rowIndex]

    def getRow2(self, rowIndex: int) -> List[int]:
        element = 1
        ans = [element]

        for i in range(1, rowIndex + 1):
            element = element * (rowIndex - i+1) // i

            ans.append(element)
        return ans


obj = Solution()
rowIndex = 2
print(obj.getRow(rowIndex))
