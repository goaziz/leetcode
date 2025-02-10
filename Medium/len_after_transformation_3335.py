from collections import Counter


class Solution:
    letter_mapping = {
        'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g',
        'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm',
        'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's',
        's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y',
        'y': 'z', 'z': 'ab'
    }

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = Counter(s)

        for _ in range(t):
            new_freq = Counter()
            for char, count in freq.items():
                mapped_char = self.letter_mapping[char]
                for new_char in mapped_char:
                    new_freq[new_char] += count
            
            freq = new_freq
            
        result = sum(freq.values()) 
        return result % (10 ** 9 + 7)


obj = Solution()
s = "abcyy"
t = 2
print(obj.lengthAfterTransformations(s, t))
