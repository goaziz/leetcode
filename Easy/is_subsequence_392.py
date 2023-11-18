class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                i += 1

            j += 1

        return i == len(s)


obj = Solution()
s = "acb"
t = "ahbgdc"
print(obj.isSubsequence(s, t))
