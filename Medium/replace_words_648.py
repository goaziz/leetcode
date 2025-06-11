from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()

        for word in dictionary:
            for i, strt in enumerate(sentence):
                if word == strt[:len(word)]:
                    sentence[i] = word

        return ' '.join(sentence)


obj = Solution()
dictionary = ["a", "b", "c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(obj.replaceWords(dictionary, sentence))
