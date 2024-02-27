class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']

        res = ""
        for char in s:
            if char not in vowels:
                res += char

        return res


obj = Solution()
s = "leetcodeisacommunityforcoders"
print(obj.removeVowels(s))
