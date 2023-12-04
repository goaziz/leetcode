class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

    def countSegments2(self, s: str) -> int:
        count = 0

        for i in range(len(s) - 1):
            if s[i] != ' ':
                count += 1

        return count


obj = Solution()
s = "Hello, my name is John"
print(obj.countSegments(s))
