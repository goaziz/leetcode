import math
from collections import deque


class ProductOfNumbers:

    def __init__(self):
        self.queue = deque()

    def add(self, num: int) -> None:
        self.queue.appendleft(num)

    def getProduct(self, k: int) -> int:
        l = list(self.queue)
        return math.prod(l[:k])


class ProductOfNumbers2:

    def __init__(self):
        self.nums = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [1]
        else:
            self.nums.append(self.nums[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.nums):
            return 0

        return self.nums[-1] // self.nums[-1-k]


obj = ProductOfNumbers2()
print(obj.add(1))
print(obj.add(2))
print(obj.add(3))
print(obj.add(4))
print(obj.add(5))
print(obj.add(6))
print(obj.getProduct(2))
