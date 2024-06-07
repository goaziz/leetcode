class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        stack = []

        while i < len(s):
            current_char = s[i]

            if len(stack) != 0:
                prev_char = stack[-1]

                if (current_char.islower() and prev_char.isupper()) or (current_char.isupper() and prev_char.islower()):
                    if prev_char.lower() == current_char.lower():
                        stack.pop()
                    else:
                        stack.append(current_char)
                else:
                    stack.append(current_char)
            else:
                stack.append(current_char)

            i += 1

        return ''.join(stack)

    def makeGood2(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


obj = Solution()
s = "leEeetcode"
print(obj.makeGood(s))
