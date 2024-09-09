from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

    def is_greater_or_equal_to_size(self):
        while len(self.queue) > self.size:
            self.queue.popleft()

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.is_greater_or_equal_to_size()

        return sum(self.queue) / len(self.queue)


class MovingAverage2:
    def __init__(self, size: int) -> None:
        self.size = size
        self.queue = deque()
        self.count = 0
        self.sum = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        self.sum = self.sum - tail + val

        return self.sum / min(self.size, self.count)


obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))
