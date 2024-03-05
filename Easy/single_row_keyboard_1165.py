from collections import Counter


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = {}
        for idx, val in enumerate(keyboard):
            hashmap[val] = idx

        time = 0
        prev_index = 0
        for char in word:
            idx = hashmap.get(char)
            time += abs(prev_index - idx)
            prev_index = idx

        return time

    def calculateTime2(self, keyboard: str, word: str) -> int:
        time = 0
        prev_index = 0

        for char in word:
            idx = keyboard.find(char)
            time += abs(prev_index - idx)
            prev_index = idx

        return time


obj = Solution()
keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"
print(obj.calculateTime2(keyboard, word))
