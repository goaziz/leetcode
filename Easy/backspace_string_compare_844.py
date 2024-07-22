class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        s_stack = []
        t_stack = []
        i = 0
        j = 0

        while s_length > i:
            if s[i] != '#':
                s_stack.append(s[i])
            else:
                if s_stack:
                    s_stack.pop()

            i += 1

        while t_length > j:
            if t[j] != '#':
                t_stack.append(t[j])
            else:
                if t_stack:
                    t_stack.pop()

            j += 1

        return ''.join(s_stack) == ''.join(t_stack)

    def backspaceCompare2(self, s: str, t: str) -> bool:
        def backspace_str(chars):
            stack = []

            for char in chars:
                if char != '#':
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()

            return stack

        return backspace_str(s) == backspace_str(t)


obj = Solution()
s = "y#fo##f"
t = "y#f#o##f"
print(obj.backspaceCompare(s, t))
