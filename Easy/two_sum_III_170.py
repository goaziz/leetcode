class TwoSum:

    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        hashmap = {}

        for i, j in enumerate(self.nums):
            diff = value - j
            if diff in hashmap:
                return True
            hashmap[j] = i
        
        return False


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(1)
obj.add(2)
obj.add(3)
param_2 = obj.find(6)
print(param_2)
