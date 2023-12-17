class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word.istitle():
            return True
        return False


obj = Solution()
print(obj.detectCapitalUse('USA'))
print(obj.detectCapitalUse('FlaG'))
print(obj.detectCapitalUse('leetcoe'))
