class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = haystack.find(needle)

        return idx

    def strStr2(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1


obj = Solution()
haystack = "sadbutsad"
needle = "sad"
print(obj.strStr(haystack, needle))
