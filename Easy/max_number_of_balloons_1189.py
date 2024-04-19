class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for char in text:
            if char in chars:
                chars[char] = chars.get(char, 0) + 1
        
        for char, count in chars.items():
            if char == 'l':
                count //= 2
            if char == 'o':
                count //= 2
            chars[char] = count
        
        return min(chars.values())


obj = Solution()
text = "loonbalxballpoon"
print(obj.maxNumberOfBalloons(text))
