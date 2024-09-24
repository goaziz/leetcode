from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def balance(self):
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        elif len(self.back) > len(self.front):
            self.front.append(self.back.popleft())

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)
        self.balance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.front and self.back:
            return -1

        if self.front:
            val = self.front.popleft()
        else:
            val = self.back.popleft()
        self.balance()
        return val

    def popMiddle(self) -> int:
        if not self.back and not self.front:
            return -1

        val = self.front.pop()
        self.balance()
        return val

    def popBack(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.back:
            val = self.back.pop()
        else:
            val = self.front.pop()
        return val


obj = FrontMiddleBackQueue()
# print(obj.pushFront(1))
# print(obj.pushBack(2))
# print(obj.pushMiddle(1))
# print(obj.pushMiddle(2))
# print(obj.pushMiddle(3))
# print(obj.popFront())
print(obj.popMiddle())
print(obj.popMiddle())
print(obj.pushMiddle(8))
print(obj.popBack())
print(obj.popFront())
print(obj.popMiddle())
