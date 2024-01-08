from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        hashset = set()
        for w1, w2 in similarPairs:
            hashset.add((w1, w2))
            hashset.add((w2, w1))

        for s1, s2 in zip(sentence1, sentence2):
            if s1 != s2:
                if (s1, s2) not in hashset:
                    return False

        return True


obj = Solution()
sentence1 = ["great", "acting", "skills"]
sentence2 = ["fine", "drama", "talent"]
similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
print(obj.areSentencesSimilar(sentence1, sentence2, similarPairs))
