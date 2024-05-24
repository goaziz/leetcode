from typing import List


class Solution:
    def stringShift2(self, s: str, shift: List[List[int]]) -> str:
        l = list(s)

        for arr in shift:
            direction = arr[0]
            amount = arr[1]
            for i in range(1, amount + 1):
                if direction == 0:
                    val = l.pop(0)
                    l.append(val)
                else:
                    val = l.pop()
                    l.insert(0, val)

        return ''.join(l)

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_shifts = 0
        for direction, amount in shift:
            if direction == 1:
                amount = -amount
            left_shifts += amount
            
        left_shifts %= len(s)
        s = s[left_shifts:] + s[:left_shifts]
        return s


obj = Solution()
s = "abc"
shift = [[0, 1], [1, 2]]
print(obj.stringShift(s, shift))
