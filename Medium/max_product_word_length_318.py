from collections import defaultdict
from typing import List


class Solution:
    def check_words(self, s1, s2):
        a = set(s1)
        b = set(s2)

        if a & b:
            return 0
        return len(s1) * len(s2)

    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        max_val = 0

        for i in range(n):
            for j in range(i + 1, n):
                product = self.check_words(words[i], words[j])
                max_val = max(max_val, product)

        return max_val


obj = Solution()
words = ["a", "aa", "aaa", "aaaa"]
print(obj.maxProduct(words))
