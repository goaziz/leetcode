from collections import Counter
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def matches(word, pattern):
            p_map = {}
            w_map = {}

            for w_char, p_char in zip(word, pattern):
                if w_char not in p_map:
                    p_map[w_char] = p_char

                if p_char not in w_map:
                    w_map[p_char] = w_char

                if p_map[w_char] != p_char or w_map[p_char] != w_char:
                    return False

            return True

        return [word for word in words if matches(word, pattern)]


obj = Solution()
words = ["badc", "abab", "dddd", "dede", "yyxx"]
pattern = "baba"
print(obj.findAndReplacePattern(words, pattern))
