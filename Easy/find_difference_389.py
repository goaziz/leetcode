from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c_s = Counter(s)
        c_t = Counter(t)

        for i in t:
            s_val = c_s.get(i, 0)
            t_val = c_t.get(i)

            if s_val != t_val:
                return i

    def findTheDifference2(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                return t[j]

            i += 1
            j += 1

        return t[-1]

    def findTheDifference3(self, s: str, t: str) -> str:
        hashmap = {}

        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1

        for i in t:
            if i not in hashmap or hashmap[i] == 0:
                return i
            else:
                hashmap[i] -= 1


obj = Solution()
s = "a"
t = "aa"
print(obj.findTheDifference3(s, t))
