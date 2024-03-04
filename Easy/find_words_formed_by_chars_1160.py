from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = 0

        for word in words:
            n = len(word)
            for char in word:
                word_char_count = word.count(char)
                chars_char_count = chars.count(char)
                if word_char_count <= chars_char_count:
                    n -= 1

            if n == 0:
                s += len(word)

        return s

    def countCharacters2(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        s = 0
        for word in words:
            word_count = Counter(word)
            n = len(word)
            for key, val in word_count.items():
                if chars_count[key] >= val:
                    n -= val
            
            if n == 0:
                s += len(word)
        
        return s


obj = Solution()
words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"
print(obj.countCharacters2(words, chars))
