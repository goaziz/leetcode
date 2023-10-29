class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''

        for char in s:
            if char.isalnum():
                clean_str += char.lower()

        return clean_str == clean_str[::-1]


obj = Solution()
s = " "
print(obj.isPalindrome(s))
