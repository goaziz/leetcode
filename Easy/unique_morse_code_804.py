from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
            'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
            's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..'
        }

        codes = {}
        for word in words:
            s = ''
            for char in word:
                s += morse_code.get(char)
            codes[s] = codes.get(s, 0) + 1
            s = ''

        return len(codes)

    def uniqueMorseRepresentations2(self, words):
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}
        print(seen)
        return len(seen)


obj = Solution()
words = ["gin", "zen", "gig", "msg"]
print(obj.uniqueMorseRepresentations2(words))
