from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        c = Counter(filter(lambda x: x.isalpha(), licensePlate.lower()))
        hashmap = {}

        for word in range(len(words)):
            flag = True
            for char, count in c.items():
                if words[word].count(char) < count:
                    flag = False
            if flag:
                hashmap[words[word]] = len(words[word])
        return min(hashmap, key=hashmap.get)

    def shortestCompletingWord2(self, licensePlate: str, words: List[str]) -> str:
        c = Counter(filter(lambda x: x.isalpha(), licensePlate.lower()))
        return min([w for w in words if c - Counter(w)], key=len)


obj = Solution()
licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
print(obj.shortestCompletingWord2(licensePlate, words))
