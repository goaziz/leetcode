from collections import Counter, defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = []
        hashmap = Counter(s)

        for char in order:
            for _ in range(hashmap[char]):
                result.append(char)
                hashmap[char] -= 1

        for k, v in hashmap.items():
            for _ in range(v):
                result.append(k)

        return ''.join(result)

    def customSortString2(self, order: str, s: str) -> str:
        result = []
        hashmap = Counter(s)

        for char in order:
            if char in hashmap:
                result.append(char * hashmap[char])
                del hashmap[char]

        for k, v in hashmap.items():
            result.append(k * v)

        return ''.join(result)


obj = Solution()
order = "hucw"
s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
print(obj.customSortString(order, s))
