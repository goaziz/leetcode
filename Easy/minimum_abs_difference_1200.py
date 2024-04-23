from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []

        min_n = float('inf')
        for i in range(len(arr) - 1):
            min_n = min(abs(arr[i] - arr[i + 1]), min_n)

        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i + 1])
            if min_n == diff:
                res.append([arr[i], arr[i + 1]])

        return res

    def minimumAbsDifference2(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff_pair = float('inf')
        res = []

        for i in range(len(arr) - 1):
            curr_pair_diff = arr[i + 1] - arr[i]
            if curr_pair_diff == min_diff_pair:
                res.append([arr[i], arr[i + 1]])
            elif curr_pair_diff < min_diff_pair:
                res = [[arr[i], arr[i + 1]]]
                min_diff_pair = curr_pair_diff

        return res


obj = Solution()
arr = [40, 11, 26, 27, -20]
print(obj.minimumAbsDifference(arr))
