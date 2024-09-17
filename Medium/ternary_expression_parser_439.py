class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []

        # Reverse the expression to process it from right to left
        for exp in reversed(expression):
            if stack and stack[-1] == '?':
                # Remove '?' from stack
                stack.pop()
                # Get the two options from the stack
                true_exp = stack.pop()
                stack.pop()  # This is the ':'
                false_exp = stack.pop()

                if exp == 'T':
                    stack.append(true_exp)
                else:
                    stack.append(false_exp)
            else:
                stack.append(exp)

        return stack.pop()


obj = Solution()
expression = "F?T:F?T?1:2:F?3:4"
print(obj.parseTernary(expression))
