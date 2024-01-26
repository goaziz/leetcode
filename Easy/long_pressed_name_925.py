from collections import Counter


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        t = len(typed)

        if n > t:
            return False

        i, j = 0, 0
        while j < t:
            if i < n and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j - 1] == typed[j]:
                j += 1
            else:
                return False

        return i == n


obj = Solution()
name = "rick"
typed = "kric"
print(obj.isLongPressedName(name, typed))
