class Solution:
    def isFascinating(self, n: int) -> bool:
        s = f'{n}{2 * n}{3 * n}'
        return sorted(s) == [str(i + 1) for i in range(9)]