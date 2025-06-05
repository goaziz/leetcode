from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set('aeiou')

        def devowel(word):
            return ''.join('*' if c in vowels else c for c in word.lower())

        words_set = set(wordlist)
        case_map = {}
        devowel_map = {}

        for word in wordlist:
            lower = word.lower()
            devow = devowel(word)
            if lower not in case_map:
                case_map[lower] = word
            if devow not in devowel_map:
                devowel_map[devow] = word

        result = []
        for q in queries:
            if q in words_set:
                result.append(q)
            elif q.lower() in case_map:
                result.append(case_map[q.lower()])
            elif devowel(q) in devowel_map:
                result.append(devowel_map[devowel(q)])
            else:
                result.append("")
        return result


obj = Solution()
wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite", "KiTe", "Hare", "HARE",
           "Hear", "hear", "keti", "keet", "keto"]
print(obj.spellchecker(wordlist, queries))
