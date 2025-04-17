from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0

        for i in range(len(fruits)):
            placed = False
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    baskets[j] = 0
                    placed = True
                    break

            if not placed:
                count += 1

        return count


obj = Solution()
fruits = [4, 2, 5]
baskets = [3, 5, 4]
print(obj.numOfUnplacedFruits(fruits, baskets))
