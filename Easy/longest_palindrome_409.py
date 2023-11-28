from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        sum_val = 0

        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
            if hashmap[i] % 2 == 0:
                sum_val += 2

        if len(s) - sum_val != 0:
            return sum_val + 1
        return sum_val

    def longestPalindrome2(self, s: str) -> int:
        ans = 0
        for v in Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans


obj = Solution()
s = "abccccdd"
print(obj.longestPalindrome(s))
