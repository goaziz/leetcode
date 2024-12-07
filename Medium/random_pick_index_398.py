from collections import defaultdict
from random import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.hashmap = defaultdict(list)
        
        for i, val in enumerate(nums):
            self.hashmap[val].append(i)

    def pick(self, target: int) -> int:
        indexes = self.hashmap[target]
        
        return random.choice(indexes)