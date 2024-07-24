class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def length(self) -> int:
        return len(self.stack)

    def push(self, x: int) -> None:
        if self.maxSize > self.length():
            self.stack.append(x)

    def pop(self) -> int:
        if self.is_empty() is False:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if self.length() > i:
                self.stack[i] += val


obj = CustomStack(3)
obj.push(1)
obj.push(2)
obj.pop()
obj.push(2)
obj.push(3)
obj.push(4)
obj.increment(5, 100)
obj.increment(2, 100)
obj.pop()
obj.pop()
obj.pop()
print(obj.list_s())
