from collections import defaultdict
import heapq
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(reverse=True)
        count = 0
        hashmap = {}

        for i in range(len(items)):
            score_id = items[i][0]
            score = items[i][1]
            if score_id in hashmap:
                if count != 5:
                    hashmap[score_id] = hashmap.get(score_id, 0) + score
                    count += 1
            else:
                count = 0
                hashmap[score_id] = hashmap.get(score_id, 0) + score
                count += 1

        result = []
        for key, val in hashmap.items():
            result.append([key, val // 5])

        return result[::-1]

    def highFive2(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for _id, score in items:
            heapq.heappush(scores[_id], score)
            if len(scores[_id]) > 5:
                heapq.heappop(scores[_id])
        result = []
        for _id, heap in scores.items():
            result.append([_id, sum(heap) // 5])
        return sorted(result)


obj = Solution()
items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [
    2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(obj.highFive(items))
