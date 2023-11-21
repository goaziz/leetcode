from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1 = wordsDict.index(word1)
        idx2 = wordsDict.index(word2)
        min_distance = abs(idx1 - idx2)
        
        for i, j in enumerate(wordsDict):
            if j == word1:
                idx1 = i

            elif j == word2:
                idx2 = i

            if idx1 != idx2:
                difference = abs(idx1 - idx2)
                min_distance = min(difference, min_distance)

        return min_distance


obj = Solution()
wordsDict = ["this", "is", "a", "long", "sentence", "is", "fun", "day", "today", "sunny",
             "weather", "is", "a", "day", "tuesday", "this", "sentence", "run", "running", "rainy"]
word1 = "weather"
word2 = "long"
print(obj.shortestDistance(wordsDict, word1, word2))
