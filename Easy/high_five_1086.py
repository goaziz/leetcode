from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(reverse=True)
        count = 0
        hashmap = {}

        for i in range(len(items)):
            if items[i][0] in hashmap:
                if count != 5:
                    hashmap[items[i][0]] = hashmap.get(
                        items[i][0], 0) + items[i][1]
                    count += 1
            else:
                count = 0
                hashmap[items[i][0]] = hashmap.get(
                    items[i][0], 0) + items[i][1]
                count += 1

        result = []
        for key, val in hashmap.items():
            result.append([key, val // 5])

        return result[::-1]


obj = Solution()
items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [
    2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(obj.highFive(items))
