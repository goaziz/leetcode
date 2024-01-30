from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        count = 0
        n = len(s)
        res = []

        for i in s:
            if i == 'I':
                res.append(count)
                count += 1
            else:
                res.append(n)
                n -= 1

        return res + [count]
