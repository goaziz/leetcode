class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                while stack and stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        ans = ''
        for st in stack:
            char, count = st[0], st[1]
            ans += char * count

        return ans


obj = Solution()
s = "abcd"
k = 2
print(obj.removeDuplicates(s, k))
