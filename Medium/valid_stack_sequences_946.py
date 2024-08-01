from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0

        for num in pushed:
            stack.append(num)

            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return len(stack) == 0


obj = Solution()
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(obj.validateStackSequences(pushed, popped))
