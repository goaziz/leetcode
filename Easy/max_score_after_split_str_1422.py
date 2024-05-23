class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0

        for i in range(1, len(s)):
            zeroes = s[:i].count('0')
            ones = s[i:].count('1')
            max_score = max(max_score, zeroes + ones)

        return max_score

    def maxScore2(self, s: str) -> int:
        ones = 0
        zeros = 0
        best = float('-inf')

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1

            best = max(best, zeros - ones)

        if s[-1] == "1":
            ones += 1

        return best + ones


obj = Solution()
s = "011101"
print(obj.maxScore2(s))
