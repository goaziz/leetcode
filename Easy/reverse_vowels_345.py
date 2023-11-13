import time


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        hashmap = {}
        for i in range(len(s)):
            if s[i] in vowels:
                hashmap[i] = s[i]
        s = list(s)
        keys = list(hashmap.keys())
        values = list(reversed(list(hashmap.values())))

        for key, value in zip(keys, values):
            s[key] = value

        return "".join(s)

    def reverseVowels2(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1
        s = list(s)
        while (i < j):
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)


obj = Solution()
s = 'hello'
print(obj.reverseVowels2(s))
