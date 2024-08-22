from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        seen = set()

        for char in s:
            freq[char] -= 1
            if char in seen:
                continue

            while stack and stack[-1] > char and freq[stack[-1]] > 0:
                removed_char = stack.pop()
                seen.remove(removed_char)

            stack.append(char)
            seen.add(char)

        return ''.join(stack)


obj = Solution()
s = "cbacdcbc"
print(obj.smallestSubsequence(s))
