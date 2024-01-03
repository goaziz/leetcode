from typing import List


class Solution:

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def calPoints(self, operations: List[str]) -> int:
        records = []

        for opt in operations:
            if self.is_number(opt):
                records.append(int(opt))
            elif opt == 'C':
                records.pop()
            elif opt == 'D':
                doubled = 2 * records[-1]
                records.append(doubled)
            elif opt == '+':
                d = records[-1] + records[-2]
                records.append(d)

        return sum(records)

    def calPoints2(self, operations: List[str]) -> int:
        stack = []
        for opt in operations:
            if opt == '+':
                stack.append(stack[-1] + stack[-2])
            elif opt == 'C':
                stack.pop()
            elif opt == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(opt))

        return sum(stack)


obj = Solution()
ops = ["5", "2", "C", "D", "+"]
print(obj.calPoints(operations=ops))
