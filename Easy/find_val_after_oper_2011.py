from typing import List


class Solution:

    def find_operation(self, ident: str):
        if ident[0] == '-' or ident[1] == '-':
            return '-'
        return '+'

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        a = 0

        for o in operations:
            op = self.find_operation(o)

            if op == '+':
                a += 1
            else:
                a -= 1

        return a

    def finalValueAfterOperations2(self, operations: List[str]) -> int:
        return sum(1 if op[1] == '+' else -1 for op in operations)