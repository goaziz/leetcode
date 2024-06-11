from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                sub_arr = arr[i: j + 1]
                if len(sub_arr) % 2 != 0:
                    s += sum(sub_arr)

        return s

    def sumOddLengthSubarrays2(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0

        for i in range(n):
            end = i + 1
            start = n - i
            total_subarrays = start * end
            odd_count = (total_subarrays + 1) // 2
            total += arr[i] * odd_count

        return total

    def sumOddLengthSubarrays3(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0

        for left in range(n):
            current_sum = 0
            for right in range(left, n):
                current_sum += arr[right]
                answer += current_sum if (right - left + 1) % 2 == 1 else 0
        return answer


obj = Solution()
arr = [1, 4, 2, 5, 3]
print(obj.sumOddLengthSubarrays3(arr))
