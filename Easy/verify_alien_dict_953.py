from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for idx, val in enumerate(order):
            hashmap[val] = idx

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if hashmap[words[i][j]] > hashmap[words[i + 1][j]]:
                        return False

        return True


obj = Solution()
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(obj.isAlienSorted(words, order))
