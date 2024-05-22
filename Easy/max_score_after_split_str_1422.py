class Solution:
    def maxScore(self, s: str) -> int:
        sums = []

        for i in range(1, len(s)):
            zeroes = s[:i].count('0')
            ones = s[i:].count('1')
            sums.append(ones + zeroes)

        return max(sums)


obj = Solution()
s = "00"
print(obj.maxScore2(s))
