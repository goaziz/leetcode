class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        groups = [s[i:i + 2 * k] for i in range(0, len(s), 2 * k)]
        result = ''
        for word in groups:
            result += word[:k][::-1] + word[k:]

        return result

    def reverseStr2(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)


obj = Solution()
print(obj.reverseStr(s='abcdefg', k=2))
print(obj.reverseStr(s='abcd', k=2))
