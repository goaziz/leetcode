class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_spaces = text.count(' ')
        words = text.split()
        n = len(words)

        if n == 1:
            return words[0] + ' ' * total_spaces

        space_between_words = total_spaces // (n - 1)
        ans = (' ' * space_between_words).join(words)
        ans += ' ' * (total_spaces % (n - 1))

        return ans


obj = Solution()
text = " hello"
print(obj.reorderSpaces(text))
