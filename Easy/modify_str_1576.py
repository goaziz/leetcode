import random


class Solution:
    def modifyString(self, s: str) -> str:
        str_list = list(s)
        letters = list('abcdefghijklmnopqrstuvwxyz')

        for i, curr_char in enumerate(str_list):
            if curr_char == '?':
                left = str_list[i - 1] if i > 0 else ''
                right = str_list[i + 1] if i < len(str_list) - 1 else ''
                letter = random.choice(letters)

                while letter == left or letter == right:
                    letter = random.choice(letters)

                str_list[i] = letter

        return ''.join(str_list)

    def modifyString2(self, s: str) -> str:
        s = list('#' + s + '#')

        for i, char in enumerate(s):
            if char == '?':
                for letter in 'abc':
                    if letter != s[i - 1] and letter != s[i + 1]:
                        s[i] = letter
                        break

        return ''.join(s[1:-1])


obj = Solution()
s = "????????????????????????????????"
print(obj.modifyString2(s))
