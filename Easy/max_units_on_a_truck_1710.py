from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        max_units = 0

        for box, unit in boxTypes:
            if truckSize >= box:
                max_units += (box * unit)
                truckSize -= box
            else:
                max_units += truckSize * unit
                break

        return max_units

    def maximumUnits2(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        max_units = 0

        for box, unit in boxTypes:
            if truckSize <= 0:
                return max_units

            max_units += min(truckSize, box) * unit
            truckSize -= box

        return max_units


obj = Solution()
boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10
print(obj.maximumUnits2(boxTypes, truckSize))
