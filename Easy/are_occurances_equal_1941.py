from collections import Counter, defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        
        count = freq[s[0]]
        
        for val in freq.values():
            if val != count:
                return False

        return True

    def areOccurrencesEqual2(self, s: str) -> bool:
        freq = Counter(s)
        counts = set(freq.values())
        
        return len(counts) == 1

obj = Solution()
s = "abacbc"
print(obj.areOccurrencesEqual(s))
