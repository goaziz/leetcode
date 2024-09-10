from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0

        while tickets[k] != 0:
            for idx, val in enumerate(tickets):
                if val > 0:
                    tickets[idx] = val - 1
                    time_taken += 1

                    if idx == k and tickets[idx] == 0:
                        break

        return time_taken


obj = Solution()
tickets = [5, 1, 1, 1]
k = 0
print(obj.timeRequiredToBuy(tickets, k))
