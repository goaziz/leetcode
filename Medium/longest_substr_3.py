class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashset = set()
        i, j = 0, 0
        lonegst_length = 0

        while i < n:
            if s[i] not in hashset:
                hashset.add(s[i])
                i += 1
                lonegst_length = max(lonegst_length, i - j)
            else:
                hashset.remove(s[j])
                j += 1

        return lonegst_length


obj = Solution()
s = "pwwkew"
print(obj.lengthOfLongestSubstring(s))
