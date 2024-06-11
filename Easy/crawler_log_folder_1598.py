from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for step in logs:
            if step == '../':
                 # Move up one directory if possible
                if stack:
                    stack.pop()
            elif step != './':
                stack.append(step)

        return len(stack)


obj = Solution()
logs = ["./", "../", "./"]
print(obj.minOperations(logs))
