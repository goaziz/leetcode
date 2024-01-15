from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."

        for symbol in symbols:
            paragraph = paragraph.replace(symbol, ' ')

        words = paragraph.lower().split()
        c = Counter(words)
        count = 0
        frequent_word = ''
        for key, val in c.items():
            if key not in banned and val > count:
                count = val
                frequent_word = key

        return frequent_word


obj = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(obj.mostCommonWord(paragraph, banned))
