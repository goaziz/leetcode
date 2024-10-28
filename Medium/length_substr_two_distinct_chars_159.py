from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)

        if n < 3:
            return n

        left = 0
        hashset = {}
        longest_len = 0

        for right in range(n):
            char = s[right]
            hashset[char] = hashset.get(char, 0) + 1

            while len(hashset) > 2:
                left_char = s[left]
                hashset[left_char] -= 1
                if hashset[left_char] == 0:
                    hashset.pop(left_char)

                left += 1

            longest_len = max(longest_len, right - left + 1)

        return longest_len

    def lengthOfLongestSubstringTwoDistinct2(self, s: str) -> int:
        n = len(s)

        if n < 3:
            return n

        left = 0
        right = 0
        hashset = defaultdict()
        longest_len = 0

        while right < n:
            hashset[s[right]] = right
            right += 1

            if len(hashset) == 3:
                min_idx = min(hashset.values())
                hashset.pop(s[min_idx])
                left = min_idx + 1

            longest_len = max(longest_len, right - left)

        return longest_len


obj = Solution()
s = "eceba"
print(obj.lengthOfLongestSubstringTwoDistinct2(s))
