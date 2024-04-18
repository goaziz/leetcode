from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a = min(start, destination)
        b = max(start, destination)
        s = distance[a:b]
        return min(s, sum(distance) - s)