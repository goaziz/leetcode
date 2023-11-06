from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        sc = Counter(s)
        tc = Counter(t)

        return tc == sc

    def isAnagram3(self, s: str, t: str) -> bool:
        """without built-in functions"""

        hashmap_s = {}
        hashmap_t = {}

        for i in s:
            hashmap_s[i] = hashmap_s.get(i, 0) + 1

        for i in t:
            hashmap_t[i] = hashmap_t.get(i, 0) + 1

        return hashmap_s == hashmap_t


obj = Solution()
s = "cat"
t = "rat"
print(obj.isAnagram3(s, t))
