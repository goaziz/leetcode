from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

    def arrayStringsAreEqual2(self, word1: List[str], word2: List[str]) -> bool:
        i = j = k = l = 0
        while i < len(word1) and k < len(word2):
            if word1[i][j] != word2[k][l]:
                return False

            j += 1
            l += 1

            if j == len(word1[i]):
                i += 1
                j = 0

            if l == len(word2[k]):
                k += 1
                l = 0

        return i == len(word1) and k == len(word2)


obj = Solution()
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(obj.arrayStringsAreEqual2(word1, word2))
