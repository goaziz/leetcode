class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            substring = s[:i]
            if substring * (n // i) == s:
                return True

        return False


obj = Solution()
s = 'abcabcabcabc'
print(obj.repeatedSubstringPattern(s))
