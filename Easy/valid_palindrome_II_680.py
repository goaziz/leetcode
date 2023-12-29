class Solution:
    def isValid(self, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.isValid(left + 1, right) or self.isValid(left, right - 1)

            left += 1
            right -= 1

        return True


obj = Solution()
s = 'abca'
print(obj.validPalindrome(s))
