from collections import Counter


class Solution:
    def greatestLetter(self, s: str) -> str:
        c = Counter(s)
        result = ""

        for char in s:
            if char.islower() and char.upper() in c:
                result = max(result, char.upper())

        return result
