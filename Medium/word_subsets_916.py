from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char in word_count:
                max_freq[char] = max(max_freq[char], word_count[char])

        result = []

        for word in words1:
            word_count = Counter(word)

            is_universal = True
            for char in max_freq:
                if word_count[char] < max_freq[char]:
                    is_universal = False
                    break

            if is_universal:
                result.append(word)

        return result


obj = Solution()
words1 = ["acaac", "cccbb", "aacbb", "caacc", "bcbbb"]
words2 = ["c", "cc", "b"]
print(obj.wordSubsets(words1, words2))
