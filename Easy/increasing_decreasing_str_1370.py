from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        alphabet = [chr(i) for i in range(97, 123)]
        c = Counter(s)
        res = ''

        while len(res) < len(s):
            for char in alphabet:
                if c[char] > 0:
                    res += char
                    c[char] -= 1

            for char in reversed(alphabet):
                if c[char] > 0:
                    res += char
                    c[char] -= 1

        return res

    def sortString2(self, s: str) -> str:
        alphabet = [chr(i) for i in range(97, 123)]
        c = Counter(s)
        res = ''

        while len(res) < len(s):
            for char in alphabet:
                if c[char] > 0:
                    res += char
                    c[char] -= 1

            alphabet = alphabet[::-1]
        
        return res


obj = Solution()
s = "rat"
print(obj.sortString2(s))
