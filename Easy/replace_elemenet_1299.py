from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        max_n = arr[n]
        arr[n] = -1
        
        for i in range(n - 1, -1, -1):
            temp = max_n
            if max_n < arr[i]:
                max_n = arr[i]
            
            arr[i] = temp
        
        return arr

obj = Solution()
arr = [17, 18, 5, 4, 6, 1]
print(obj.replaceElements(arr))
