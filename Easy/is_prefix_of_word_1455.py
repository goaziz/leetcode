class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentences = sentence.split()
        n = len(searchWord)

        for idx, word in enumerate(sentences, start=1):
            if word[:n] == searchWord:
                return idx
        return -1

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentences = sentence.split()

        for idx, word in enumerate(sentences, start=1):
            if word.startswith(searchWord):
                return idx
        return -1


obj = Solution()
sentence = "this problem is an easy problem"
searchWord = "pro"
print(obj.isPrefixOfWord(sentence, searchWord))
