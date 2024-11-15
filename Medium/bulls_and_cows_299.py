from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        s_counter = Counter(secret)
        g_counter = Counter(guess)
        cows = sum((s_counter & g_counter).values()) - bulls

        return f'{bulls}A{cows}B'


obj = Solution()
secret = "1123"
guess = "0111"
print(obj.getHint(secret, guess))
