class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                encoded_str = ""

                while stack and stack[-1] != '[':
                    encoded_str = stack.pop() + encoded_str

                # Pop the '['
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                k = int(k)
                stack.append(k * encoded_str)
            else:
                stack.append(char)

        return ''.join(stack)


obj = Solution()
s = "2[abc]3[cd]ef"
print(obj.decodeString(s))
