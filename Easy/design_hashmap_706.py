class MyHashMap:

    def __init__(self):
        self.MAX = 10
        self.map = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        idx = self.get_hash(key)

        for i, (k, v) in enumerate(self.map[idx]):
            if key == k:
                self.map[idx][i] = (key, value)
                return

        self.map[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self.get_hash(key)

        for k, v in self.map[idx]:
            if key == k:
                return v

        return -1

    def remove(self, key: int) -> None:
        idx = self.get_hash(key)

        for i, (k, v) in enumerate(self.map[idx]):
            if k == key:
                print(i, k, v)
                del self.map[idx][i]
                return


obj = MyHashMap()
print(obj.put(1, 1))
print(obj.put(2, 2))
print(obj.put(2, 1))
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(2))
print(obj.remove(2))
print(obj.map)
# print(obj.get(2))
