class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        n = len(s)
        count = 1

        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1

        groups.append(count)

        answer = 0
        for i in range(1, len(groups)):
            answer += min(groups[i], groups[i - 1])

        return answer

    def countBinarySubstrings2(self, s: str) -> int:
        prev = 0
        current = 1
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                result += min(current, prev)
                prev = current
                current = 1

        return result + min(current, prev)


obj = Solution()
s = "00110011"
print(obj.countBinarySubstrings2(s))
