class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = ""

        for i in range(n):
            substr = ""
            for j in range(i, n):
                substr += s[j]

                if substr == substr[::-1]:
                    result = max([result, substr], key=len)

        return result

    def longestPalindrome2(self, s: str) -> str:

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1: right]

        result = ""
        for i in range(len(s) - 1):
            odd_palindrome = expand(i, i)
            even_palindrome = expand(i, i + 1)

            result = max([result, odd_palindrome, even_palindrome], key=len)

        return result


obj = Solution()
s = "babad"
print(obj.longestPalindrome2(s))
