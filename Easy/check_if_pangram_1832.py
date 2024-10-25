import string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set(string.ascii_lowercase)
        sentence = set(sentence)
        diff = letters - sentence

        return len(diff) == 0

    def checkIfPangram2(self, sentence: str) -> bool:
        seen = set(sentence)

        return len(seen) == 26


obj = Solution()
print(obj.checkIfPangram('wddd'))
