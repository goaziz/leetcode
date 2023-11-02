class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}
        mapped_set = set()

        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapped_set:
                    return False

                hashmap[s[i]] = t[i]
                mapped_set.add(t[i])

        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        hashmap = {}
        mapped_chars = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapped_chars:
                    return False
                hashmap[s[i]] = t[i]
                mapped_chars[t[i]] = i

        return True

    def isIsomorphic3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in hashmap.values():
                    return False
                hashmap[s[i]] = t[i]
            elif hashmap[s[i]] != t[i]:
                return False

        return True


obj = Solution()
s = "egg"
t = "add"
print(obj.isIsomorphic3(s, t))
