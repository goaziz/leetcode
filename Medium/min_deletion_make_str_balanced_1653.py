class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        delete_count = 0

        for char in s:
            if stack and stack[-1] == 'b' and char == 'a':
                stack.pop()
                delete_count += 1
            else:
                stack.append(char)

        return delete_count


obj = Solution()
s = "aababbab"
print(obj.minimumDeletions(s))
