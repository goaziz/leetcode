class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()

        for i in range(len(l)):
            l[i] = l[i][::-1]

        return ' '.join(l)

    def reverseWords2(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])


obj = Solution()
print(obj.reverseWords(s="Mr Ding"))
print(obj.reverseWords(s="Let's take LeetCode contest"))
