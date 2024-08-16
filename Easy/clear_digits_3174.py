class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1].isalpha() and char.isdigit():
                stack.pop()
            elif char.isalpha():
                stack.append(char)
        
        return ''.join(stack)

obj = Solution()
s = 'cb34'
print(obj.clearDigits(s))