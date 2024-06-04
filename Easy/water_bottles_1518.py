class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles

        while True:
            remainder = numBottles - numExchange
            if remainder >= 0:
                count += 1
                numBottles -= numExchange
                numBottles += 1
            else:
                break

        return count

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles

        while empty >= numExchange:
            numBottles += empty // numExchange
            empty = empty % numExchange + empty // numExchange

        return numBottles


obj = Solution()
numBottles = 9
numExchange = 3
print(obj.numWaterBottles(numBottles, numExchange))
