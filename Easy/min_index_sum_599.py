from collections import Counter
from math import inf
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        c1 = Counter(list1)
        c2 = Counter(list2)
        hashmap = c1 + c2
        res = []
        min_sum = len(list1) + len(list2)

        for i, j in hashmap.items():
            if j > 1:
                list1_index = list1.index(i)
                list2_index = list2.index(i)
                s = list1_index + list2_index
                if s < min_sum:
                    min_sum = s
                    res = [i]
                elif s == min_sum:
                    res.append(i)

        return res

    def findRestaurant2(self, list1: List[str], list2: List[str]) -> List[str]:
        c1 = Counter(list1)
        c2 = Counter(list2)
        res = []
        min_sum = inf
        for i in range(len(list1)):
            if list1[i] in c1 and list1[i] in c2:
                list2_index = list2.index(list1[i])
                s = i + list2_index
                if s < min_sum:
                    min_sum = s
                    res = [list1[i]]
                elif s == min_sum:
                    res.append(list1[i])

        return res


obj = Solution()
list1 = ["Shogun", "Piatti", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines",
         "Hungry Hunter Steakhouse", "Shogun"]
print(obj.findRestaurant(list1, list2))
