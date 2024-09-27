from typing import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        freq = Counter(num)

        for idx, val in enumerate(num):
            if freq[str(idx)] != int(val):
                return False

        return True


obj = Solution()
num = "030"
print(obj.digitCount(num))
