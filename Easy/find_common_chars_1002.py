from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words or len(words) < 2:
            return []

        common_chars_counter = Counter(words[0])

        for word in words[1:]:
            common_chars_counter &= Counter(word)

        return list(common_chars_counter.elements())


obj = Solution()
words = ["bella", "label", "roller"]
print(obj.commonChars(words))
