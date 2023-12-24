from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, count = 0, 0

        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
                i += 1  # Skip the next plot, since it can't have a flower
            i += 1

        return count >= n

    def canPlaceFlowers2(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) -
                                   1) or (flowerbed[i + 1] == 0)

                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n


obj = Solution()
flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2
print(obj.canPlaceFlowers(flowerbed, n))
