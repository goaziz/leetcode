class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = 'aeiouAEIOU'
        a_vowels = 0
        b_vowels = 0
        i = 0

        while i != (n // 2):
            if s[i] in vowels:
                a_vowels += 1

            if s[n - i - 1] in vowels:
                b_vowels += 1
            i += 1

        return a_vowels == b_vowels


obj = Solution()
s = 'teetbork'
print(obj.halvesAreAlike(s))
