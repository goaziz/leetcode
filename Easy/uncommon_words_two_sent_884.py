from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        s1_table = Counter(s1)
        s2_table = Counter(s2)

        ans = []

        for word in s1:
            if word not in s2_table and s1_table.get(word, 0) == 1:
                ans.append(word)

        for word in s2:
            if word not in s1_table and s2_table.get(word, 0) == 1:
                ans.append(word)

        return ans

    def uncommonFromSentences2(self, s1: str, s2: str) -> List[str]:
        count = {}

        for word in s1.split():
            count[word] = count.get(word, 0) + 1

        for word in s2.split():
            count[word] = count.get(word, 0) + 1

        # Alternatively:
        # count = collections.Counter(A.split())
        # count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]


obj = Solution()
s1 = "apple apple"
s2 = "banana"
print(obj.uncommonFromSentences(s1, s2))
