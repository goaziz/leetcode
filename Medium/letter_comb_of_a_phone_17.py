from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []

        def backtrack(idx, s):
            if len(s) == len(digits):
                res.append(s)
                return

            for i in letters[digits[idx]]:
                backtrack(idx + 1, s + i)

        if digits:
            backtrack(0, '')

        return res


obj = Solution()
digits = '234'
print(obj.letterCombinations(digits))
