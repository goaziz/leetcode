class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left].isalpha():
                right -= 1
            elif s[right].isalpha():
                left += 1
            else:
                left += 1
                right -= 1

        return ''.join(s)

    def reverseOnlyLetters2(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        ans = []

        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)

        return ''.join(ans)


obj = Solution()
s = "Test1ng-Leet=code-Q!"
print(obj.reverseOnlyLetters(s))
