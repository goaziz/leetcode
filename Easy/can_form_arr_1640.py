from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        res = []

        for i in range(len(arr)):
            for j in range(len(pieces)):
                if arr[i] in pieces[j] and pieces[j] not in res:
                    res.append(pieces[j])

        res = [sublist for item in res for sublist in item]

        return res == arr

    def canFormArray2(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        p_len = len(pieces)
        pieces.sort()

        i = 0
        while i < n:
            left = 0
            right = p_len - 1
            found = -1
            # use binary search to find target piece:
            while left <= right:
                mid = (left + right) // 2
                if pieces[mid][0] == arr[i]:
                    found = mid
                    break
                elif pieces[mid][0] > arr[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            if found == -1:
                return False
            # check target piece
            target_piece = pieces[found]
            for x in target_piece:
                if x != arr[i]:
                    return False
                i += 1

        return True

    def canFormArray3(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        # initialize hashmap
        mapping = {p[0]: p for p in pieces}

        i = 0
        while i < n:
            # find target piece
            if arr[i] not in mapping:
                return False
            # check target piece
            target_piece = mapping[arr[i]]
            for x in target_piece:
                if x != arr[i]:
                    return False
                i += 1

        return True


obj = Solution()
arr = [91, 4, 64, 78]
pieces = [[78], [4, 64], [91]]
print(obj.canFormArray3(arr, pieces))
