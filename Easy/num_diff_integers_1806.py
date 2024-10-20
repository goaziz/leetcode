class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        hash_set = set()
        digit = ''

        for char in word:
            if char.isdigit():
                digit += char
            elif digit != '':
                hash_set.add(int(digit))
                digit = ''

        if digit != '':
            hash_set.add(int(digit))

        return len(hash_set)


obj = Solution()
word = "a1b01c001"
print(obj.numDifferentIntegers(word))
