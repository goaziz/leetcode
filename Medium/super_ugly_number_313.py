import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_numbers = []
        heap = []

        heapq.heappush(heap, 1)
        seen = set()
        seen.add(1)

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
n = 12
primes = [2, 7, 13, 19]
print(obj.nthSuperUglyNumber(n, primes))
