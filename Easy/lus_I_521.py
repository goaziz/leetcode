class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        a_length = len(a)
        b_length = len(b)

        if a == b:
            return -1
        else:
            return max(a_length, b_length)


obj = Solution()
a = "aaa"
b = "bbb"
print(obj.findLUSlength(a, b))
