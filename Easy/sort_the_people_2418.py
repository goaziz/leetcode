from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}

        for name, height in zip(names, heights):
            hashmap[height] = name

        sorted_people = sorted(hashmap.items(), reverse=True)
        ans = []

        for key in sorted_people:
            ans.append(key[1])

        return ans


obj = Solution()
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
print(obj.sortPeople(names, heights))
