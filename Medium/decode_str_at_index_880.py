class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0

        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1

        for char in reversed(s):
            k %= size

            if k == 0 and char.isalpha():
                return char

            if char.isdigit():
                size //= int(char)
            else:
                size -= 1


obj = Solution()
s = "a2345678999999999999999"
k = 1
print(obj.decodeAtIndex(s, k))
