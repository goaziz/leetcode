from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s = set(letters)
        s.add(target)
        l = list(s)
        l.sort()
        for letter in range(len(l) - 1):
            if l[letter] == target:
                return l[letter + 1]
        return l[0]

    def nextGreatestLetter2(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

    def nextGreatestLetter3(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if left == len(letters):
            return letters[0]
        else:
            return letters[left]


obj = Solution()
letters = ["c", "f", "j"]
target = "d"
print(obj.nextGreatestLetter(letters, target))
