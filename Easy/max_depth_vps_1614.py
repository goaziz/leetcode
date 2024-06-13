class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_count = 0

        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            max_count = max(max_count, count)

        return max_count


obj = Solution()
s = "(1+(2*3)+((8)/4))+1"
print(obj.maxDepth(s))
