class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_count = -1
        hashmap = {}

        for i, char in enumerate(s):
            if char in hashmap:
                difference = i - hashmap[char] - 1
                max_count = max(max_count, difference)
            else:
                hashmap[char] = i

        return max_count


obj = Solution()
s = "scayofdzca"
print(obj.maxLengthBetweenEqualCharacters(s))
