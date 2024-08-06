class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.flatten(top.getList())
        return False
