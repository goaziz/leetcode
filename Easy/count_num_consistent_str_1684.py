from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words:
            if all(char in allowed for char in word):
                count += 1

        return count

    def countConsistentStrings2(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed_set = set(allowed)

        for word in words:
            if set(word).issubset(allowed_set):
                count += 1

        return count


obj = Solution()
allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
print(obj.countConsistentStrings2(allowed, words))
