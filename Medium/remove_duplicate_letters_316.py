class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = {}
        stack = []
        seen = set()

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in s:
            if char not in seen:
                while stack and stack[-1] > char and freq[stack[-1]] > 0:
                    seen.discard(stack.pop())

                stack.append(char)
                seen.add(char)

            freq[char] -= 1

        return ''.join(stack)


obj = Solution()
s = "cbacdcbc"
print(obj.removeDuplicateLetters(s))
