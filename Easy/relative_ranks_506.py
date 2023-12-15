import heapq
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        duplicate_score = score.copy()
        heapq.heapify(duplicate_score)
        hashmap = {}
        n = len(score)

        while len(duplicate_score) > 0:
            item = heapq.heappop(duplicate_score)
            hashmap[item] = n
            n -= 1

        answer = []
        for i, j in enumerate(score):
            rank = hashmap[score[i]]
            if rank == 1:
                answer.append('Gold Medal')
            elif rank == 2:
                answer.append('Silver Medal')
            elif rank == 3:
                answer.append('Bronze Medal')
            else:
                answer.append(str(hashmap[score[i]]))

        return answer

    def findRelativeRanks2(self, score: List[int]) -> List[str]:
        sorted_score_copy = sorted(score, reverse=True)
        hashmap = {}
        answer = []

        for i in range(len(sorted_score_copy)):
            if i == 0:
                hashmap[sorted_score_copy[i]] = "Gold Medal"
            elif i == 1:
                hashmap[sorted_score_copy[i]] = 'Silver Medal'
            elif i == 2:
                hashmap[sorted_score_copy[i]] = 'Bronze Medal'
            else:
                hashmap[sorted_score_copy[i]] = str(i + 1)

        for i in score:
            answer.append(hashmap[i])

        return answer


obj = Solution()
score = [10, 3, 8, 9, 4]
print(obj.findRelativeRanks2(score))
