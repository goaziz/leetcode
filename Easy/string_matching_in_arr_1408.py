from typing import List


class Solution:

    def find_str(self, sub, words):
        temp = words.copy()
        temp.remove(sub)

        for word in temp:
            idx = word.find(sub)

            if idx != -1:
                return idx
        return -1

    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []

        for word in words:
            idx = self.find_str(word, words)

            if idx != -1:
                ans.append(word)

        return ans

    def stringMatching2(self, words: List[str]) -> List[str]:
        ans = []

        for sub in words:
            for word in words:
                if sub in word and word != sub:
                    ans.append(sub)
                    break

        return ans


obj = Solution()
words = ["mass", "as", "hero", "superhero"]
print(obj.stringMatching2(words))
