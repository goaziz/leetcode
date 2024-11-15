from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        hashset = defaultdict(int)
        longest_len = 0

        for right in range(n):
            hashset[s[right]] += 1

            while len(hashset) > k:
                left_char = s[left]
                hashset[left_char] -= 1
                if hashset[left_char] == 0:
                    hashset.pop(left_char)

                left += 1

            longest_len = max(longest_len, right - left + 1)

        return longest_len


obj = Solution()
s = "eceba"
k = 2
print(obj.lengthOfLongestSubstringKDistinct(s, k))
