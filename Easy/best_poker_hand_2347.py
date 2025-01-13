from collections import Counter
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rank_map = Counter(ranks)
        suit_map = Counter(suits)

        if len(suit_map) == 1:
            return 'Flush'
        elif any(count >= 3 for count in rank_map.values()):
            return 'Three of a Kind'
        elif any(count == 2 for count in rank_map.values()):
            return 'Pair'
        else:
            return 'High Card'
