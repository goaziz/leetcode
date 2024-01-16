class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = sentence.split()
        ans = []
        for idx, word in enumerate(s, start=1):
            multiple_a = idx * 'a'
            if word[0] in vowels:
                s = word + 'ma' + multiple_a
            else:
                s = 'a' + word[1:] + word[0]
                s += 'ma' + multiple_a

            ans.append(s)

        return ''.join(ans)


obj = Solution()
sentence = "I speak Goat Latin"
print(obj.toGoatLatin(sentence))
