class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []

        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)

        ans = ""
        if abs(len(letters) - len(digits)) > 1:
            return ans

        if len(letters) > len(digits):
            longer, shorter = letters, digits
        else:
            longer, shorter = digits, letters

        for i in range(len(s)):
            if i % 2 == 0:
                ans += longer[i // 2]
            else:
                ans += shorter[i // 2]

        return ans


obj = Solution()
s = "covid2019"
print(obj.reformat(s))
