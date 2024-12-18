from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        hashmap = defaultdict(set)

        for i in range(1, len(rings)):
            if rings[i].isdigit():
                hashmap[rings[i]].add(rings[i - 1])

        count = 0

        for vals in hashmap.values():
            if len(vals) >= 3:
                count += 1

        return count


obj = Solution()
rings = "B0R0G0R9R0B0G0"
print(obj.countPoints(rings))
