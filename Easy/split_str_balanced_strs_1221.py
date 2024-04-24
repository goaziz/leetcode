class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_l = 0
        count_r = 0
        ans = 0

        for letter in s:
            if letter == 'R':
                count_r += 1
            else:
                count_l += 1

            if count_l == count_r:
                count_l = 0
                count_r = 0
                ans += 1

        return ans


obj = Solution()
s = 'RRLL'
print(obj.balancedStringSplit(s))
