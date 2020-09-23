from collections import Counter

class Solution:
    def firstUniqChar(self, s: str):
        hash_map = Counter(s)
        for i, j in enumerate(s):
            if hash_map[j] == 1:
                return i
        return -1