from collections import defaultdict


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s) - 2):
            a = s[i]
            b = s[i + 1]
            c = s[i + 2]

            if a != b and a != c and b != c:
                count += 1

        return count


obj = Solution()
s = "aababcabc"
print(obj.countGoodSubstrings(s))
