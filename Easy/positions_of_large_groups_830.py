from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        start, end = 0, 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                end = i
            else:
                if end - start + 1 >= 3:
                    ans.append([start, end])
                start = i

        if end - start + 1 >= 3:
            ans.append([start, end])

        return ans

    def largeGroupPositions2(self, s: str) -> List[List[int]]:
        ans = []
        start = 0
        n = len(s)

        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if i - start + 1 >= 3:
                    ans.append([start, i])

                start = i + 1

        return ans

    def largeGroupPositions3(self, s: str) -> List[List[int]]:
        n = len(s)
        start, end = 0, 0
        ans = []

        while start < n:
            while end < n and s[start] == s[end]:
                end += 1

            if end - start >= 3:
                ans.append([start, end - 1])

            start = end

        return ans


obj = Solution()
s = "abcdddeeeeaabbbcd"
print(obj.largeGroupPositions2(s))
