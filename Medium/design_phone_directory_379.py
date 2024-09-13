class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.hashmap = {}

        for i in range(maxNumbers):
            self.hashmap[i] = True

    def get(self) -> int:
        for key, val in self.hashmap.items():
            if val is True:
                self.hashmap[key] = False
                return key

        return -1

    def check(self, number: int) -> bool:
        return self.hashmap.get(number, False)

    def release(self, number: int) -> None:
        self.hashmap[number] = True


class PhoneDirectory2:
    def __init__(self, maxNumbers: int):
        self.slots_available = set(range(maxNumbers))

    def get(self) -> int:
        if not self.slots_available:
            return -1
        return self.slots_available.pop()

    def check(self, number: int) -> bool:
        return number in self.slots_available

    def release(self, number: int) -> None:
        self.slots_available.add(number)


obj = PhoneDirectory(3)
print(obj.get())
print(obj.get())
print(obj.check(2))
print(obj.get())
print(obj.check(2))
print(obj.release(2))
print(obj.check(2))
