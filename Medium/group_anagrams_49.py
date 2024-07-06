from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            anagrams[key].append(s)

        return list(anagrams.values())


obj = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(obj.groupAnagrams(strs))
