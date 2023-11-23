class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashmap = {}

        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1

        odd = 0
        for i in hashmap.values():
            if i % 2 != 0:
                odd += 1

        return odd <= 1


    def canPermutePalindrome2(self, s: str) -> bool:
        chars = set()
        
        for i in s:
            if i not in chars:
                chars.add(i)
            else:
                chars.remove(i)
        
        return len(chars) <= 1

obj = Solution()
s = 'aa'
print(obj.canPermutePalindrome2(s))
