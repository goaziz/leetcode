import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = []
        heap = []
        
        heapq.heappush(heap, 1)
        seen = set()
        seen.add(1)
        
        primes = [2, 3, 5]
        
        for _ in range(n):
            current_ugly = heapq.heappop(heap)
            ugly_numbers.append(current_ugly)
            
            for prime in primes:
                new_ugly = current_ugly * prime
                if new_ugly not in seen:
                    heapq.heappush(heap, new_ugly)
                    seen.add(new_ugly)
        
        return ugly_numbers[n - 1]
        


obj = Solution()
n = 10
print(obj.nthUglyNumber(n))
