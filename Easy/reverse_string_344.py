from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s) - 1):
            char = s.pop()
            s.insert(i, char)

        print(s)

    def reverseString2(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        print(s)

    def reverseString3(self, s: List[str]) -> None:
        s[:] == s[::-1]


obj = Solution()
s = ["h", "e", "l", "l", "o"]
print(obj.reverseString2(s))
