from collections import Counter


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        count = 0
        n = len(word)

        for i in range(n):
            if word[i] not in vowels:
                continue
            seen = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    count += 1
        return count


obj = Solution()
word = "cuaieuouac"
print(obj.countVowelSubstrings(word))
