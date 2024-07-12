class MyHashSet:

    def __init__(self):
        self.hashset = {}

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset[key] = key

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.pop(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset


class MyHashSet2:

    def __init__(self):
        self.key_range = 796
        self.bucket_array = [Bucket() for _ in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].insert(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucket_array[bucket_index].delete(key)

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        return self.bucket_array[bucket_index].exists(key)


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Bucket:
    def __init__(self) -> None:
        self.head = Node(0)

    def insert(self, val):
        if not self.exists(val):
            new_node = Node(val, self.head.next)
            self.head.next = new_node

    def delete(self, val):
        previous = self.head
        current = self.head.next

        while current is not None:
            if current.val == val:
                previous.next = current.next

            previous = current
            current = current.next

    def exists(self, val):
        current = self.head

        while current is not None:
            if current.val == val:
                return True
            current = current.next

        return False


obj = MyHashSet2()
print(obj.add(1))
print(obj.add(2))
print(obj.contains(1))
print(obj.contains(3))
print(obj.add(2))
print(obj.contains(2))
print(obj.remove(2))
print(obj.contains(2))
