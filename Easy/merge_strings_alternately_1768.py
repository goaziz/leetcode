from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''

        for x, y in zip_longest(word1, word2):
            result += x if x else ''
            result += y if y else ''

        return result
