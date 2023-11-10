class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        hashmap = {}
        hashmap2 = {}

        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                hashmap[pattern[i]] = words[i]
            else:
                if hashmap[pattern[i]] != words[i]:
                    return False

            if words[i] not in hashmap2:
                hashmap2[words[i]] = pattern[i]
            else:
                if hashmap2[words[i]] != pattern[i]:
                    return False

        return True

    def wordPattern2(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False

        if len(set(s)) != len(set(pattern)):
            return False

        hashmap = {}
        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                hashmap[pattern[i]] = s[i]
            elif hashmap[pattern[i]] == s[i]:
                continue
            else:
                return False

        return True


obj = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(obj.wordPattern2(pattern, s))
