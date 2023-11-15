from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)

        for key, value in c.items():
            if value == 1:
                return s.index(key)

        return -1

    def firstUniqChar2(self, s: str) -> int:

        for i in s:
            if s.count(i) == 1:
                return s.index(i)

        return -1

    def firstUniqChar3(self, s: str) -> int:
        hashmap = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1

        for i, j in enumerate(s):
            if hashmap[j] == 1:
                return i
        return -1


obj = Solution()
s = "lleettcode"
print(obj.firstUniqChar(s))
