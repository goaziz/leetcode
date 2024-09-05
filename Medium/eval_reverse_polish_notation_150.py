from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char in '+-/*':
                a = stack.pop()
                b = stack.pop()

                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(b - a)
                elif char == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))
            else:
                stack.append(int(char))

        return stack.pop()


obj = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(obj.evalRPN(tokens))
