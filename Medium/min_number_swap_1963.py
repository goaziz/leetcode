class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []

        for b in s:
            if stack and b == ']':
                stack.pop()
            else:
                stack.append(b)

        return (len(stack) + 1) // 2

    def minSwaps2(self, s: str) -> int:
        open_bracket_needed = 0

        for b in s:
            if open_bracket_needed > 0 and b == ']':
                open_bracket_needed -= 1
            elif b == '[':
                open_bracket_needed += 1

        return (open_bracket_needed + 1) // 2


obj = Solution()
s = "][]["
print(obj.minSwaps2(s))
