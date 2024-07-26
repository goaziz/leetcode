class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for char in s:
            if char == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)

        return len(stack)

    def minAddToMakeValid2(self, s: str) -> int:
        count = 0
        min_difference = 0

        for char in s:
            if char == '(':
                count += 1
            else:
                count -= 1

            if count == -1:
                count += 1
                min_difference += 1

        return count + min_difference


obj = Solution()
s = "())"
print(obj.minAddToMakeValid(s))
