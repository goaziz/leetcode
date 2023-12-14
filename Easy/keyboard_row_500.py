from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')
        result = []

        for word in words:
            w = set(word.lower())
            if w <= first_row or w <= second_row or w <= third_row:
                result.append(word)

        return result

    def findWords2(self, words: List[str]) -> List[str]:
        first_row = 'qwertyuiop'
        second_row = 'asdfghjkl'
        third_row = 'zxcvbnm'

        result = []
        l1, l2, l3 = 0, 0, 0

        for word in words:
            n = len(word)
            for w in word.lower():
                if w in first_row:
                    l1 += 1
                elif w in second_row:
                    l2 += 1
                elif w in third_row:
                    l3 += 1

            if n == l1 or n == l2 or n == l3:
                result.append(word)

            l1, l2, l3 = 0, 0, 0

        return result


obj = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(obj.findWords2(words))
