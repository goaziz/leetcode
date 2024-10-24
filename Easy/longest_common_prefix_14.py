from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = strs[0]

        for word in strs:
            if len(word) < len(shortest_word):
                shortest_word = word

        prefix = ""
        for i in range(len(shortest_word)):
            letter = shortest_word[i]

            for word in strs:
                if word[i] != letter:
                    return prefix

            prefix += letter

        return prefix
