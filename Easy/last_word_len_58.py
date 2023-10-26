class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip().split(' ')[-1]

        return len(last_word)

    def lengthOfLastWord2(self, s: str) -> int:
        length = 0
        s = s.strip()

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
            else:
                break

        return length


obj = Solution()
s = "luffy is still joyboy "
print(obj.lengthOfLastWord2(s))
