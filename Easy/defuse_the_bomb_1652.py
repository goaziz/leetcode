from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        n = len(code)
        arr = code + code

        for i in range(n):
            if k > 0:
                # Sum next k elements
                code[i] = sum(arr[i + 1: i + 1 + k])
            else:
                # Sum previous k elements
                code[i] = sum(arr[i + n + k: i + n])

        return code


obj = Solution()
code = [2, 4, 9, 3]
k = -2
print(obj.decrypt(code, k))
