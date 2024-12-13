class MapSum:

    def __init__(self):
        self.hashmap = {}

    def insert(self, key: str, val: int) -> None:
        self.hashmap[key] = val

    def sum(self, prefix: str) -> int:
        s = 0

        for key, val in self.hashmap.items():
            if key.startswith(prefix):
                s += val

        return s


obj = MapSum()
print(obj.insert("apple", 3))
print(obj.sum("ap"))
print(obj.insert("app", 2))
print(obj.sum("app"))
