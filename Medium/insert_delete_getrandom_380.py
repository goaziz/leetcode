import random


class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False

        self.data[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False

        idx = self.data[val]
        last_val = self.l[-1]
        self.l[idx] = last_val
        self.data[last_val] = idx

        self.l.pop()
        del self.data[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.l)


obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(2))
print(obj.insert(3))
print(obj.insert(4))
print(obj.insert(5))
print(obj.insert(6))
print(obj.remove(3))
