from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False

        hashmap = Counter(s1)

        count = 0

        for idx, val in enumerate(s2):

            if val not in hashmap:
                return False

            if hashmap[val] <= 0:
                return False

            hashmap[val] -= 1

            if s1[idx] != val:
                count += 1

        return count <= 2

    def areAlmostEqual2(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False

        mismatches = [(a, b) for a, b in zip(s1, s2) if a != b]

        n = len(mismatches)
        if n == 0:
            return True

        return n == 2 and mismatches[0] == mismatches[1][::-1]


obj = Solution()
s1 = "yf"
s2 = "yy"
print(obj.areAlmostEqual(s1, s2))
