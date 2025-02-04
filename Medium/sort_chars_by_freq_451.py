from typing import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sorted_freq = {k: v for k, v in sorted(
            freq.items(), key=lambda x: x[1], reverse=True)}
        result = []

        for k, v in sorted_freq.items():
            result.append(k * v)

        return ''.join(result)

    def frequencySort2(self, s: str) -> str:
        freq = Counter(s)
        result = [k * v for k,
                  v in sorted(freq.items(), key=lambda x: x[1], reverse=True)]
        return ''.join(result)


obj = Solution()
s = "tree"
print(obj.frequencySort2(s))
